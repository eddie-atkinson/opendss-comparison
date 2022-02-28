import pandapower as pp
from pandapower.timeseries import DFData
from pandapower.timeseries import OutputWriter
from pandapower.timeseries.run_time_series import run_timeseries
from pandapower.control import ConstControl
from line_codes import (
    linecode_2c_data,
    linecode_4_xc_data,
    linecode_5c_01,
    linecode_5c_04,
    linecode_5c_06,
)
import pandas as pd
from pathlib import Path
from lines import create_lines

# For network 5 feeder 1 there are 130 buses
N_BUSES = 130

# Run simulation for one day at 5 min resolution
TIME_STEPS = 288

OUT_PATH = Path("./simulation_res")

net = pp.create_empty_network()
bus_external_grid = pp.create_bus(net, vn_kv=11, name="Ext. Grid")
bus_trafo_lv_side = pp.create_bus(net, vn_kv=0.416, name="bus 0")

""" The following parameters have been left the same as they appear in the pandapower example here: https://github.com/e2nIEE/pandapower/blob/develop/tutorials/three_phase_loadflow_tutorial_simple.ipynb
* `s_sc_max_mva`: maximal short circuit apparent power to calculate internal impedance of ext_grid for short circuit calculations
* `rx_max`: maximal R/X-ratio to calculate internal impedance of ext_grid for short circuit calculations
* `r0x0_max`: minimal R/X-ratio to calculate internal impedance of ext_grid for short circuit calculations
* `x0x_max`: maximal X0/X-ratio to calculate Zero sequence internal impedance of ext_grid

I would be lying if I said I totally understood them
However, the documentation says they are used for short-circuit calculations, which we are not doing.
¯\_(ツ)_/¯
"""
pp.create_ext_grid(
    net,
    bus=bus_external_grid,
    vm_pu=1.0,
    name="Grid connection",
    s_sc_max_mva=5000,
    rx_max=0.1,
    r0x0_max=0.1,
    x0x_max=1.0,
)


# Create 416V 3Ph buses
# We already have bus 0 which is on the LV side of the transformer, create n_buses - 1 buses
buses = [bus_trafo_lv_side]
for i in range(N_BUSES - 1):
    buses.append(pp.create_bus(net, vn_kv=0.416, name=f"bus {i + 1}"))

# Create the line codes
pp.create_std_type(net, linecode_2c_data, "2c_.0145", element="line")
pp.create_std_type(net, linecode_4_xc_data, "4_XC", element="line")
pp.create_std_type(net, linecode_5c_04, "5c_.04", element="line")
pp.create_std_type(net, linecode_5c_06, "5c_.06", element="line")
pp.create_std_type(net, linecode_5c_01, "5c_.01", element="line")


# Create the lines
create_lines(net, buses)


# Create the transformer, default params taken the the pandapower example
# Some of the settings have been changed to match the OpenDSS declaration below:
# New Transformer.TR1 Buses=[SourceBus.1.2.3 1.1.2.3.4] Conns=[Delta Wye] kVs=[11 0.416] kVAs=[800 800] XHL=1 phases=3
pp.create_transformer_from_parameters(
    net,
    hv_bus=bus_external_grid,
    lv_bus=bus_trafo_lv_side,
    sn_mva=0.8,
    vn_hv_kv=11,
    vn_lv_kv=0.416,
    vk_percent=6,
    vkr_percent=0.78125,
    pfe_kw=2.7,
    i0_percent=0.16875,
    # Required params for running 3ph power flow
    si0_hv_partial=0.9,
    vector_group="Dyn",
    mag0_rx=0.0,
    mag0_percent=100,
    vkr0_percent=0.78125,
    vk0_percent=6,
)

# Read the load data for all the loads from CSV

all_load_data_df = pd.read_csv("combined_loads.csv")

load_profiles_df = pd.DataFrame()
load_profiles_df["load1_p"] = all_load_data_df["load1_mw"]
load_profiles_df["load2_p"] = all_load_data_df["load2_mw"]
load_profiles_df["load3_p"] = all_load_data_df["load3_mw"]
load_profiles_df["load4_p"] = all_load_data_df["load4_mw"]


# Create the loads on the appropriate buses.
load1 = pp.create_asymmetric_load(net, buses[54], p_a_mw=0.02, p_b_mw=0, p_c_mw=0)
load2 = pp.create_asymmetric_load(net, buses[86], p_a_mw=0.02, p_b_mw=0, p_c_mw=0)
load3 = pp.create_asymmetric_load(net, buses[98], p_a_mw=0, p_b_mw=0, p_c_mw=0.02)
load4 = pp.create_asymmetric_load(net, buses[129], p_a_mw=0, p_b_mw=0, p_c_mw=0.02)


# Create data source for controllers
ds = DFData(load_profiles_df)

# Create the controllers for the loads
controller1 = ConstControl(
    net,
    element="asymmetric_load",
    variable="p_a_mw",
    element_index=[load1, load2],
    data_source=ds,
    profile_name=["load1_p", "load2_p"],
)

controller2 = ConstControl(
    net,
    element="asymmetric_load",
    variable="p_c_mw",
    element_index=[load3, load4],
    data_source=ds,
    profile_name=["load3_p", "load4_p"],
)

# Create the output writer
ow = OutputWriter(
    net,
    TIME_STEPS,
    output_path=Path(OUT_PATH),
    output_file_type=".csv",
)

p_a_mw_df = pd.DataFrame(columns=net.asymmetric_load.index)
p_b_mw_df = pd.DataFrame(columns=net.asymmetric_load.index)
p_c_mw_df = pd.DataFrame(columns=net.asymmetric_load.index)


vm_a_pu_df = pd.DataFrame(columns=net.bus.index)
vm_b_pu_df = pd.DataFrame(columns=net.bus.index)
vm_c_pu_df = pd.DataFrame(columns=net.bus.index)

pp.add_zero_impedance_parameters(net)


"""
Forgive me for I have sinned. The time series module didn't work for 3ph for me.

It seemed like less effort to just roll my own. It is not a better implementation, was just faster to
write than it was to grok
"""


def append_data_to_df(df, data_to_append, index):
    columns = range(len(data_to_append))
    # Should only be a single row of data at a time
    temp_df = pd.DataFrame([], columns=columns, index=[index])
    temp_df.loc[index] = data_to_append
    return pd.concat([df, temp_df]).reset_index(drop=True)


pp.runpp_3ph(net)
breakpoint()
for i in range(TIME_STEPS):
    controller1.time_step(net, i)
    controller2.time_step(net, i)
    pp.runpp_3ph(net)
    p_a_mw_df = append_data_to_df(p_a_mw_df, net.res_asymmetric_load_3ph["p_a_mw"], i)
    p_b_mw_df = append_data_to_df(p_b_mw_df, net.res_asymmetric_load_3ph["p_b_mw"], i)
    p_c_mw_df = append_data_to_df(p_c_mw_df, net.res_asymmetric_load_3ph["p_c_mw"], i)

    vm_a_pu_df = append_data_to_df(vm_a_pu_df, net.res_bus_3ph["vm_a_pu"], i)
    vm_b_pu_df = append_data_to_df(vm_b_pu_df, net.res_bus_3ph["vm_b_pu"], i)
    vm_c_pu_df = append_data_to_df(vm_c_pu_df, net.res_bus_3ph["vm_c_pu"], i)


OUT_PATH.mkdir(exist_ok=True)

p_a_mw_df.to_csv(OUT_PATH / "p_a_mw.csv")
p_b_mw_df.to_csv(OUT_PATH / "p_b_mw.csv")
p_c_mw_df.to_csv(OUT_PATH / "p_c_mw.csv")

vm_a_pu_df.to_csv(OUT_PATH / "vm_a_pu.csv")
vm_b_pu_df.to_csv(OUT_PATH / "vm_b_pu.csv")
vm_c_pu_df.to_csv(OUT_PATH / "vm_c_pu.csv")
