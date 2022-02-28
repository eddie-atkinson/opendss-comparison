import opendssdirect as dss
from pathlib import Path
import pandas as pd
import re
import os

# 416V 3ph / sqrt(3) = 240
BASE_VOLTAGE = 240
OUTPUT_PATH = Path("./output")
PROCESS_OUTPUT_PATH = Path("./processed_output")

"""
Just some helpers for dealing with OpenDSS's 'interesting' API
"""


def get_linenames():
    return dss.Lines.AllNames()


def set_data_path(path: Path):
    dss.run_command(f"""Set Datapath = {path.resolve()}""")


def get_loads():
    return dss.Loads.AllNames()


def export_line_monitors():
    for linename in get_linenames():
        dss.run_command(
            f"""
        Export Monitor {linename}_PQ_vs_Time
        Export Monitor {linename}_VI_vs_Time
        """
        )


def set_data_path(path: Path):
    dss.run_command(f"""Set Datapath = {path.resolve()}""")


dss.run_command("Redirect ./Feeder_1/Master.dss")

set_data_path(OUTPUT_PATH)

export_line_monitors()

# Just need to process the line voltages to a dataframe that's useful for comparisons
df_a = pd.DataFrame()
df_b = pd.DataFrame()
df_c = pd.DataFrame()

# Confused as to why we're now in the ./output dir? So am I...
# OpenDSS has its own rules..

for file_path in Path(".").iterdir():
    file_name = file_path.name
    match = re.search(r"line\d*_vi_vs_time.csv", file_name)
    if not match:
        continue
    load_number = re.search(r"line\d*", file_name).group().strip("line")
    file_data = pd.read_csv(file_path)
    file_data = file_data.rename(
        mapper={" V1": "vm_a_pu", " V2": "vm_b_pu", " V3": "vm_c_pu"}, axis=1
    )

    file_data = file_data.filter(["vm_a_pu", "vm_b_pu", "vm_c_pu"])

    file_data["vm_a_pu"] /= BASE_VOLTAGE
    file_data["vm_b_pu"] /= BASE_VOLTAGE
    file_data["vm_c_pu"] /= BASE_VOLTAGE

    # This generates a performance warning, it doesn't bother me
    df_a[load_number] = file_data["vm_a_pu"].values
    df_b[load_number] = file_data["vm_b_pu"].values
    df_c[load_number] = file_data["vm_c_pu"].values


PROCESS_OUTPUT_PATH.mkdir(exist_ok=True)

df_a.to_csv(f"{PROCESS_OUTPUT_PATH.resolve()}/vm_a_pu.csv")
df_b.to_csv(f"{PROCESS_OUTPUT_PATH.resolve()}/vm_b_pu.csv")
df_c.to_csv(f"{PROCESS_OUTPUT_PATH.resolve()}/vm_c_pu.csv")
