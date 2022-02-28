"""
Line code definitions for simulation.

For each line code type the original OpenDSS definition is copied above for comparison with the Pandapower equivalent.

TODO: The values for the following required parameters are unclear:
* `max_i_ka` (float): maximum thermal current in kilo Ampere
* `type` ("ol" -> overhead line, "cs" -> cabling system): type of line

In both cases the default value from the pandapower asymmetric loads example has been used. 

In the case of the maximum thermal current I don't think the value matters too much as we are not going to simulate fault conditions
"""


# New LineCode.2c_.0145 nphases=3 R1=1.903 X1=0.09 R0=1.903 X0=0.09 C1=0 C0=0 Units=km

linecode_2c_data = line_data = {
    "c_nf_per_km": 0,
    "c0_nf_per_km": 0,
    "r_ohm_per_km": 1.903,
    "r0_ohm_per_km": 1.903,
    "x_ohm_per_km": 0.09,
    "x0_ohm_per_km": 0.09,
    # Taken directly from the Pandapower example, it is unclear from the source data what this is?
    "max_i_ka": 0.142,
    # Unclear whether the line is underground or overhead, for now let's assume underground
    "type": "cs",
}

# New LineCode.4_XC nphases=3 R1=4.61 X1=0.091 R0=4.8 X0=0.091 C1=0 C0=0 Units=km
linecode_4_xc_data = {
    "c_nf_per_km": 0,
    "c0_nf_per_km": 0,
    "r_ohm_per_km": 4.61,
    "r0_ohm_per_km": 4.8,
    "x_ohm_per_km": 0.091,
    "x0_ohm_per_km": 0.091,
    # Taken directly from the Pandapower example, it is unclear from the source data what this is?
    "max_i_ka": 0.142,
    # Unclear whether the line is underground or overhead, for now let's assume underground
    "type": "cs",
}


# New LineCode.5c_.04 nphases=3 R1=0.708 X1=0.079 R0=2.32 X0=0.093 C1=0 C0=0 Units=km
linecode_5c_04 = {
    "c_nf_per_km": 0,
    "c0_nf_per_km": 0,
    "r_ohm_per_km": 0.708,
    "r0_ohm_per_km": 2.32,
    "x_ohm_per_km": 0.079,
    "x0_ohm_per_km": 0.093,
    # Taken directly from the Pandapower example, it is unclear from the source data what this is?
    "max_i_ka": 0.142,
    # Unclear whether the line is underground or overhead, for now let's assume underground
    "type": "cs",
}


# New LineCode.5c_.06 nphases=3 R1=0.469 X1=0.075 R0=1.581 X0=0.091 C1=0 C0=0 Units=km
linecode_5c_06 = {
    "c_nf_per_km": 0,
    "c0_nf_per_km": 0,
    "r_ohm_per_km": 0.469,
    "r0_ohm_per_km": 1.581,
    "x_ohm_per_km": 0.075,
    "x0_ohm_per_km": 0.091,
    # Taken directly from the Pandapower example, it is unclear from the source data what this is?
    "max_i_ka": 0.142,
    # Unclear whether the line is underground or overhead, for now let's assume underground
    "type": "cs",
}


# New LineCode.5c_.1 nphases=3 R1=0.274 X1=0.073 R0=0.959 X0=0.079 C1=0 C0=0 Units=km
linecode_5c_01 = {
    "c_nf_per_km": 0,
    "c0_nf_per_km": 0,
    "r_ohm_per_km": 0.274,
    "r0_ohm_per_km": 0.959,
    "x_ohm_per_km": 0.073,
    "x0_ohm_per_km": 0.079,
    # Taken directly from the Pandapower example, it is unclear from the source data what this is?
    "max_i_ka": 0.142,
    # Unclear whether the line is underground or overhead, for now let's assume underground
    "type": "cs",
}
