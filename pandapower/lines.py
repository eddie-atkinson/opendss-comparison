import pandapower as pp

def create_lines(net, buses):
    pp.create_line(
        net, from_bus=buses[0], to_bus=buses[1], std_type="5c_.06", length_km=0.00025109
    )

    pp.create_line(
        net, from_bus=buses[1], to_bus=buses[2], std_type="5c_.06", length_km=4.8466e-05
    )
    pp.create_line(
        net, from_bus=buses[2], to_bus=buses[3], std_type="5c_.06", length_km=5.4999e-05
    )
    pp.create_line(
        net, from_bus=buses[3], to_bus=buses[4], std_type="5c_.06", length_km=4.8167e-05
    )
    pp.create_line(
        net,
        from_bus=buses[4],
        to_bus=buses[5],
        std_type="5c_.06",
        length_km=4.6141000000000004e-05,
    )
    pp.create_line(
        net, from_bus=buses[5], to_bus=buses[6], std_type="5c_.06", length_km=4.3463e-05
    )
    pp.create_line(
        net, from_bus=buses[6], to_bus=buses[7], std_type="5c_.06", length_km=6.1659e-05
    )
    pp.create_line(
        net,
        from_bus=buses[7],
        to_bus=buses[8],
        std_type="5c_.06",
        length_km=3.0016999999999997e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[8],
        to_bus=buses[9],
        std_type="5c_.06",
        length_km=3.6222999999999995e-05,
    )
    pp.create_line(
        net, from_bus=buses[9], to_bus=buses[10], std_type="5c_.06", length_km=0.0033729
    )
    pp.create_line(
        net,
        from_bus=buses[10],
        to_bus=buses[11],
        std_type="5c_.06",
        length_km=9.0378e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[11],
        to_bus=buses[12],
        std_type="5c_.06",
        length_km=8.071e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[12],
        to_bus=buses[13],
        std_type="5c_.06",
        length_km=8.2806e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[13],
        to_bus=buses[14],
        std_type="5c_.06",
        length_km=0.00049759,
    )
    pp.create_line(
        net,
        from_bus=buses[14],
        to_bus=buses[15],
        std_type="5c_.06",
        length_km=0.0027717,
    )
    pp.create_line(
        net,
        from_bus=buses[15],
        to_bus=buses[16],
        std_type="5c_.06",
        length_km=0.0022246,
    )
    pp.create_line(
        net,
        from_bus=buses[16],
        to_bus=buses[17],
        std_type="5c_.06",
        length_km=0.0025079,
    )
    pp.create_line(
        net,
        from_bus=buses[17],
        to_bus=buses[18],
        std_type="5c_.06",
        length_km=0.0011208,
    )
    pp.create_line(
        net,
        from_bus=buses[18],
        to_bus=buses[19],
        std_type="5c_.06",
        length_km=0.0099483,
    )
    pp.create_line(
        net,
        from_bus=buses[19],
        to_bus=buses[20],
        std_type="5c_.06",
        length_km=0.0006068099999999999,
    )
    pp.create_line(
        net,
        from_bus=buses[20],
        to_bus=buses[21],
        std_type="5c_.06",
        length_km=0.00037184,
    )
    pp.create_line(
        net,
        from_bus=buses[21],
        to_bus=buses[22],
        std_type="5c_.06",
        length_km=0.00052667,
    )
    pp.create_line(
        net,
        from_bus=buses[22],
        to_bus=buses[23],
        std_type="5c_.06",
        length_km=7.7877e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[23],
        to_bus=buses[24],
        std_type="5c_.06",
        length_km=0.0001005,
    )
    pp.create_line(
        net,
        from_bus=buses[24],
        to_bus=buses[25],
        std_type="5c_.06",
        length_km=0.00013665,
    )
    pp.create_line(
        net,
        from_bus=buses[25],
        to_bus=buses[26],
        std_type="5c_.06",
        length_km=0.00017021,
    )
    pp.create_line(
        net,
        from_bus=buses[26],
        to_bus=buses[27],
        std_type="5c_.06",
        length_km=9.586000000000001e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[27],
        to_bus=buses[28],
        std_type="5c_.06",
        length_km=7.3825e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[28],
        to_bus=buses[29],
        std_type="5c_.06",
        length_km=0.00011507000000000001,
    )
    pp.create_line(
        net,
        from_bus=buses[29],
        to_bus=buses[30],
        std_type="5c_.06",
        length_km=0.00028185,
    )
    pp.create_line(
        net,
        from_bus=buses[30],
        to_bus=buses[31],
        std_type="5c_.06",
        length_km=0.0005909600000000001,
    )
    pp.create_line(
        net,
        from_bus=buses[31],
        to_bus=buses[32],
        std_type="5c_.06",
        length_km=0.00040048,
    )
    pp.create_line(
        net, from_bus=buses[32], to_bus=buses[33], std_type="5c_.01", length_km=0.003069
    )
    pp.create_line(
        net,
        from_bus=buses[33],
        to_bus=buses[34],
        std_type="2c_.0145",
        length_km=0.00038009,
    )
    pp.create_line(
        net,
        from_bus=buses[33],
        to_bus=buses[35],
        std_type="5c_.01",
        length_km=0.0133501,
    )
    pp.create_line(
        net,
        from_bus=buses[34],
        to_bus=buses[36],
        std_type="2c_.0145",
        length_km=0.00017214,
    )
    pp.create_line(
        net,
        from_bus=buses[35],
        to_bus=buses[37],
        std_type="5c_.04",
        length_km=0.00028954,
    )
    pp.create_line(
        net,
        from_bus=buses[35],
        to_bus=buses[38],
        std_type="5c_.01",
        length_km=0.0010184,
    )
    pp.create_line(
        net,
        from_bus=buses[36],
        to_bus=buses[39],
        std_type="2c_.0145",
        length_km=0.0001228,
    )
    pp.create_line(
        net,
        from_bus=buses[37],
        to_bus=buses[40],
        std_type="5c_.04",
        length_km=0.00023424,
    )
    pp.create_line(
        net,
        from_bus=buses[38],
        to_bus=buses[41],
        std_type="5c_.01",
        length_km=0.00023902,
    )
    pp.create_line(
        net,
        from_bus=buses[39],
        to_bus=buses[42],
        std_type="2c_.0145",
        length_km=9.7417e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[40],
        to_bus=buses[43],
        std_type="5c_.04",
        length_km=0.00035396,
    )
    pp.create_line(
        net,
        from_bus=buses[41],
        to_bus=buses[44],
        std_type="5c_.01",
        length_km=0.00015403,
    )
    pp.create_line(
        net,
        from_bus=buses[42],
        to_bus=buses[45],
        std_type="2c_.0145",
        length_km=0.00010521,
    )
    pp.create_line(
        net,
        from_bus=buses[43],
        to_bus=buses[46],
        std_type="5c_.04",
        length_km=0.00025602000000000003,
    )
    pp.create_line(
        net,
        from_bus=buses[44],
        to_bus=buses[47],
        std_type="5c_.01",
        length_km=0.00010402,
    )
    pp.create_line(
        net,
        from_bus=buses[45],
        to_bus=buses[48],
        std_type="2c_.0145",
        length_km=0.0072866,
    )
    pp.create_line(
        net,
        from_bus=buses[46],
        to_bus=buses[49],
        std_type="5c_.04",
        length_km=0.00055258,
    )
    pp.create_line(
        net,
        from_bus=buses[47],
        to_bus=buses[50],
        std_type="5c_.01",
        length_km=0.00013330000000000001,
    )
    pp.create_line(
        net,
        from_bus=buses[48],
        to_bus=buses[51],
        std_type="2c_.0145",
        length_km=0.0062443,
    )
    pp.create_line(
        net,
        from_bus=buses[49],
        to_bus=buses[52],
        std_type="5c_.04",
        length_km=0.0005228,
    )
    pp.create_line(
        net,
        from_bus=buses[50],
        to_bus=buses[53],
        std_type="5c_.01",
        length_km=0.00019167,
    )
    pp.create_line(
        net,
        from_bus=buses[51],
        to_bus=buses[54],
        std_type="2c_.0145",
        length_km=0.0038601,
    )
    pp.create_line(
        net,
        from_bus=buses[51],
        to_bus=buses[55],
        std_type="2c_.0145",
        length_km=0.00043269999999999995,
    )
    pp.create_line(
        net,
        from_bus=buses[52],
        to_bus=buses[56],
        std_type="5c_.04",
        length_km=0.00024286,
    )
    pp.create_line(
        net,
        from_bus=buses[53],
        to_bus=buses[57],
        std_type="5c_.01",
        length_km=0.0002103,
    )
    pp.create_line(
        net,
        from_bus=buses[55],
        to_bus=buses[58],
        std_type="2c_.0145",
        length_km=6.989399999999999e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[56],
        to_bus=buses[59],
        std_type="5c_.04",
        length_km=0.00017203999999999999,
    )
    pp.create_line(
        net,
        from_bus=buses[57],
        to_bus=buses[60],
        std_type="5c_.01",
        length_km=0.00028006,
    )
    pp.create_line(
        net,
        from_bus=buses[58],
        to_bus=buses[61],
        std_type="2c_.0145",
        length_km=5.8e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[59],
        to_bus=buses[62],
        std_type="5c_.04",
        length_km=0.00038773999999999997,
    )
    pp.create_line(
        net,
        from_bus=buses[60],
        to_bus=buses[63],
        std_type="5c_.01",
        length_km=0.00010630000000000001,
    )
    pp.create_line(
        net,
        from_bus=buses[61],
        to_bus=buses[64],
        std_type="2c_.0145",
        length_km=4.1e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[62],
        to_bus=buses[65],
        std_type="5c_.04",
        length_km=0.00037352999999999996,
    )
    pp.create_line(
        net,
        from_bus=buses[63],
        to_bus=buses[66],
        std_type="5c_.01",
        length_km=0.00010791,
    )
    pp.create_line(
        net,
        from_bus=buses[64],
        to_bus=buses[67],
        std_type="2c_.0145",
        length_km=0.00014831,
    )
    pp.create_line(
        net,
        from_bus=buses[65],
        to_bus=buses[68],
        std_type="5c_.04",
        length_km=0.00064039,
    )
    pp.create_line(
        net,
        from_bus=buses[66],
        to_bus=buses[69],
        std_type="5c_.01",
        length_km=0.0056452,
    )
    pp.create_line(
        net,
        from_bus=buses[67],
        to_bus=buses[70],
        std_type="2c_.0145",
        length_km=0.0046564,
    )
    pp.create_line(
        net,
        from_bus=buses[68],
        to_bus=buses[71],
        std_type="5c_.04",
        length_km=0.0016055,
    )
    pp.create_line(
        net,
        from_bus=buses[69],
        to_bus=buses[72],
        std_type="5c_.01",
        length_km=0.0031265999999999998,
    )
    pp.create_line(
        net,
        from_bus=buses[70],
        to_bus=buses[73],
        std_type="2c_.0145",
        length_km=0.00012932,
    )
    pp.create_line(
        net,
        from_bus=buses[71],
        to_bus=buses[74],
        std_type="5c_.04",
        length_km=0.0048539,
    )
    pp.create_line(
        net,
        from_bus=buses[73],
        to_bus=buses[75],
        std_type="2c_.0145",
        length_km=9.868e-05,
    )
    pp.create_line(
        net, from_bus=buses[74], to_bus=buses[76], std_type="5c_.04", length_km=0.002477
    )
    pp.create_line(
        net,
        from_bus=buses[75],
        to_bus=buses[77],
        std_type="2c_.0145",
        length_km=0.00011727,
    )
    pp.create_line(
        net, from_bus=buses[76], to_bus=buses[78], std_type="4_XC", length_km=0.0020079
    )
    pp.create_line(
        net,
        from_bus=buses[76],
        to_bus=buses[79],
        std_type="5c_.04",
        length_km=0.00092265,
    )
    pp.create_line(
        net,
        from_bus=buses[77],
        to_bus=buses[80],
        std_type="2c_.0145",
        length_km=0.00019276999999999999,
    )
    pp.create_line(
        net, from_bus=buses[78], to_bus=buses[81], std_type="4_XC", length_km=0.00018357
    )
    pp.create_line(
        net,
        from_bus=buses[79],
        to_bus=buses[82],
        std_type="5c_.04",
        length_km=0.0030745,
    )
    pp.create_line(
        net,
        from_bus=buses[80],
        to_bus=buses[83],
        std_type="2c_.0145",
        length_km=0.00015312,
    )
    pp.create_line(
        net, from_bus=buses[81], to_bus=buses[84], std_type="4_XC", length_km=0.00016926
    )
    pp.create_line(
        net,
        from_bus=buses[82],
        to_bus=buses[85],
        std_type="5c_.04",
        length_km=0.0058297999999999996,
    )
    pp.create_line(
        net,
        from_bus=buses[83],
        to_bus=buses[86],
        std_type="2c_.0145",
        length_km=0.0053411,
    )
    pp.create_line(
        net, from_bus=buses[84], to_bus=buses[87], std_type="4_XC", length_km=0.00012822
    )
    pp.create_line(
        net,
        from_bus=buses[85],
        to_bus=buses[88],
        std_type="5c_.04",
        length_km=0.0036272,
    )
    pp.create_line(
        net, from_bus=buses[87], to_bus=buses[89], std_type="4_XC", length_km=0.00019516
    )
    pp.create_line(
        net,
        from_bus=buses[88],
        to_bus=buses[90],
        std_type="5c_.04",
        length_km=8.124900000000001e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[88],
        to_bus=buses[91],
        std_type="5c_.04",
        length_km=0.00044002,
    )
    pp.create_line(
        net,
        from_bus=buses[90],
        to_bus=buses[92],
        std_type="5c_.04",
        length_km=8.5843e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[91],
        to_bus=buses[93],
        std_type="5c_.04",
        length_km=0.0053325,
    )
    pp.create_line(
        net,
        from_bus=buses[92],
        to_bus=buses[94],
        std_type="5c_.04",
        length_km=8.599999999999999e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[93],
        to_bus=buses[95],
        std_type="2c_.0145",
        length_km=0.0068778,
    )
    pp.create_line(
        net,
        from_bus=buses[93],
        to_bus=buses[96],
        std_type="5c_.04",
        length_km=0.0053315,
    )
    pp.create_line(
        net,
        from_bus=buses[94],
        to_bus=buses[97],
        std_type="5c_.04",
        length_km=8.6313e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[95],
        to_bus=buses[98],
        std_type="2c_.0145",
        length_km=0.0053558,
    )
    pp.create_line(
        net,
        from_bus=buses[95],
        to_bus=buses[99],
        std_type="2c_.0145",
        length_km=0.00050818,
    )
    pp.create_line(
        net,
        from_bus=buses[96],
        to_bus=buses[100],
        std_type="5c_.04",
        length_km=0.0050837,
    )
    pp.create_line(
        net,
        from_bus=buses[97],
        to_bus=buses[101],
        std_type="5c_.04",
        length_km=8.5704e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[99],
        to_bus=buses[102],
        std_type="2c_.0145",
        length_km=0.00014723,
    )
    pp.create_line(
        net,
        from_bus=buses[100],
        to_bus=buses[103],
        std_type="4_XC",
        length_km=6.746499999999999e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[100],
        to_bus=buses[104],
        std_type="5c_.04",
        length_km=0.0021036,
    )
    pp.create_line(
        net,
        from_bus=buses[101],
        to_bus=buses[105],
        std_type="5c_.04",
        length_km=8.6354e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[102],
        to_bus=buses[106],
        std_type="2c_.0145",
        length_km=0.00010046,
    )
    pp.create_line(
        net,
        from_bus=buses[103],
        to_bus=buses[107],
        std_type="4_XC",
        length_km=6.736499999999999e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[104],
        to_bus=buses[108],
        std_type="5c_.04",
        length_km=0.0055094,
    )
    pp.create_line(
        net,
        from_bus=buses[106],
        to_bus=buses[109],
        std_type="2c_.0145",
        length_km=8.005600000000001e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[107],
        to_bus=buses[110],
        std_type="4_XC",
        length_km=6.619e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[108],
        to_bus=buses[111],
        std_type="5c_.04",
        length_km=0.00024035000000000001,
    )
    pp.create_line(
        net,
        from_bus=buses[109],
        to_bus=buses[112],
        std_type="2c_.0145",
        length_km=7.2561e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[110],
        to_bus=buses[113],
        std_type="4_XC",
        length_km=6.790999999999999e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[111],
        to_bus=buses[114],
        std_type="5c_.04",
        length_km=0.0013626,
    )
    pp.create_line(
        net,
        from_bus=buses[112],
        to_bus=buses[115],
        std_type="2c_.0145",
        length_km=0.00012145999999999999,
    )
    pp.create_line(
        net,
        from_bus=buses[113],
        to_bus=buses[116],
        std_type="4_XC",
        length_km=6.621100000000001e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[115],
        to_bus=buses[117],
        std_type="2c_.0145",
        length_km=0.0043578,
    )
    pp.create_line(
        net,
        from_bus=buses[116],
        to_bus=buses[118],
        std_type="4_XC",
        length_km=6.7425e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[117],
        to_bus=buses[119],
        std_type="2c_.0145",
        length_km=0.0001419,
    )
    pp.create_line(
        net,
        from_bus=buses[118],
        to_bus=buses[120],
        std_type="4_XC",
        length_km=6.7178e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[119],
        to_bus=buses[121],
        std_type="2c_.0145",
        length_km=0.00015284,
    )
    pp.create_line(
        net,
        from_bus=buses[120],
        to_bus=buses[122],
        std_type="4_XC",
        length_km=6.685199999999999e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[121],
        to_bus=buses[123],
        std_type="2c_.0145",
        length_km=0.000132,
    )
    pp.create_line(
        net,
        from_bus=buses[122],
        to_bus=buses[124],
        std_type="4_XC",
        length_km=6.7623e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[123],
        to_bus=buses[125],
        std_type="2c_.0145",
        length_km=0.00017612,
    )
    pp.create_line(
        net,
        from_bus=buses[124],
        to_bus=buses[126],
        std_type="4_XC",
        length_km=6.694e-05,
    )
    pp.create_line(
        net,
        from_bus=buses[125],
        to_bus=buses[127],
        std_type="2c_.0145",
        length_km=0.00022769,
    )
    pp.create_line(
        net,
        from_bus=buses[127],
        to_bus=buses[128],
        std_type="2c_.0145",
        length_km=0.00028679,
    )
    pp.create_line(
        net,
        from_bus=buses[128],
        to_bus=buses[129],
        std_type="2c_.0145",
        length_km=0.004835,
    )