#!/usr/bin/env python
# encoding: utf-8

name = "Zhang_EtOH_submech"
shortDesc = ""
longDesc = """
Yingjia Zhang, Hilal El-Merhubi, Benoîte Lefort, Luis Le Moyne, Henry J. Curran, Alan Kéromnès,
Probing the low-temperature chemistry of ethanol via the addition of dimethyl ether,
Combustion and Flame,
Volume 190,
2018,
Pages 74-86,
https://doi.org/10.1016/j.combustflame.2017.11.011.
"""
autoGenerated=False
entry(
    index = 0,
    label = "C2H5OH <=> C2H5O + H",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([1,2,10,100],'atm'), arrhenius=[Arrhenius(A=(8.41e+49,'s^-1'), n=-10.08, Ea=(116207,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.6e+45,'s^-1'), n=-8.71, Ea=(114324,'cal/mol'), T0=(1,'K')), Arrhenius(A=(3.03e+35,'s^-1'), n=-5.7, Ea=(110085,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.44e+24,'s^-1'), n=-2.27, Ea=(105127,'cal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1,
    label = "C2H5OH <=> CH3CHOH + H",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([1,2,10,100],'atm'), arrhenius=[Arrhenius(A=(3.47e+56,'s^-1'), n=-12.2, Ea=(111333,'cal/mol'), T0=(1,'K')), Arrhenius(A=(3.17e+51,'s^-1'), n=-10.67, Ea=(109213,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.36e+40,'s^-1'), n=-7.23, Ea=(104310,'cal/mol'), T0=(1,'K')), Arrhenius(A=(3.2e+26,'s^-1'), n=-3.13, Ea=(98273,'cal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2,
    label = "C2H5OH <=> CH2CH2OH + H",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([1,2,10,100],'atm'), arrhenius=[Arrhenius(A=(9.56e+60,'s^-1'), n=-13.32, Ea=(114498,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.67e+56,'s^-1'), n=-11.86, Ea=(118705,'cal/mol'), T0=(1,'K')), Arrhenius(A=(8.84e+44,'s^-1'), n=-8.44, Ea=(113928,'cal/mol'), T0=(1,'K')), Arrhenius(A=(5.19e+30,'s^-1'), n=-4.15, Ea=(107710,'cal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 3,
    label = "C2H5OH <=> C2H4 + H2O",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(3.41e+59,'s^-1'), n=-14.2, Ea=(83672.6,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.62e+57,'s^-1'), n=-13.3, Ea=(85262.2,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.65e+52,'s^-1'), n=-11.5, Ea=(84745.6,'cal/mol'), T0=(1,'K')), Arrhenius(A=(5.23e+43,'s^-1'), n=-8.9, Ea=(81506.7,'cal/mol'), T0=(1,'K')), Arrhenius(A=(4.59e+32,'s^-1'), n=-5.6, Ea=(76062.4,'cal/mol'), T0=(1,'K')), Arrhenius(A=(3.84e+20,'s^-1'), n=-2.06, Ea=(69465.5,'cal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 4,
    label = "C2H5OH <=> CH3 + CH2OH",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(1.2e+54,'s^-1'), n=-12.9, Ea=(100006,'cal/mol'), T0=(1,'K')), Arrhenius(A=(5.18e+59,'s^-1'), n=-14, Ea=(99906.4,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.62e+66,'s^-1'), n=-15.3, Ea=(105390,'cal/mol'), T0=(1,'K')), Arrhenius(A=(5.55e+64,'s^-1'), n=-14.5, Ea=(106183,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.55e+58,'s^-1'), n=-12.3, Ea=(105768,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.78e+47,'s^-1'), n=-8.96, Ea=(101059,'cal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 5,
    label = "C2H5OH <=> C2H5 + OH",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(8.1e+46,'s^-1'), n=-11.3, Ea=(111053,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.86e+56,'s^-1'), n=-13.5, Ea=(107238,'cal/mol'), T0=(1,'K')), Arrhenius(A=(4.65e+63,'s^-1'), n=-15, Ea=(109623,'cal/mol'), T0=(1,'K')), Arrhenius(A=(4.46e+65,'s^-1'), n=-14.9, Ea=(112345,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.79e+61,'s^-1'), n=-13.4, Ea=(113080,'cal/mol'), T0=(1,'K')), Arrhenius(A=(6.17e+51,'s^-1'), n=-10.3, Ea=(109941,'cal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 6,
    label = "C2H5 + OH <=> C2H4 + H2O",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(1.2926e+19,'cm^3/(mol*s)'), n=-1.96, Ea=(272.7,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.2184e+19,'cm^3/(mol*s)'), n=-1.9533, Ea=(238.8,'cal/mol'), T0=(1,'K')), Arrhenius(A=(4.1052e+19,'cm^3/(mol*s)'), n=-2.1007, Ea=(625.4,'cal/mol'), T0=(1,'K')), Arrhenius(A=(7.9406e+22,'cm^3/(mol*s)'), n=-2.9892, Ea=(3862.6,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.7926e+24,'cm^3/(mol*s)'), n=-3.3287, Ea=(7748.8,'cal/mol'), T0=(1,'K')), Arrhenius(A=(4.6961e+18,'cm^3/(mol*s)'), n=-1.5805, Ea=(7999.2,'cal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 7,
    label = "C2H5 + OH <=> CH3 + CH2OH",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(9.2017e+17,'cm^3/(mol*s)'), n=-1.2994, Ea=(2504.6,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.0981e+18,'cm^3/(mol*s)'), n=-1.3206, Ea=(2569.4,'cal/mol'), T0=(1,'K')), Arrhenius(A=(5.7367e+18,'cm^3/(mol*s)'), n=-1.5182, Ea=(3184.8,'cal/mol'), T0=(1,'K')), Arrhenius(A=(6.5278e+21,'cm^3/(mol*s)'), n=-2.3515, Ea=(6022.7,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.8799e+25,'cm^3/(mol*s)'), n=-3.2495, Ea=(10576.2,'cal/mol'), T0=(1,'K')), Arrhenius(A=(6.5044e+22,'cm^3/(mol*s)'), n=-2.4427, Ea=(12646.6,'cal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 8,
    label = "CH3 + CH2OH <=> C2H4 + H2O",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(6.3236e+24,'cm^3/(mol*s)'), n=-3.7134, Ea=(2798.4,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.1607e+25,'cm^3/(mol*s)'), n=-3.7867, Ea=(3001.3,'cal/mol'), T0=(1,'K')), Arrhenius(A=(3.2261e+27,'cm^3/(mol*s)'), n=-4.45, Ea=(5345.2,'cal/mol'), T0=(1,'K')), Arrhenius(A=(7.2451e+29,'cm^3/(mol*s)'), n=-5.0344, Ea=(9245.4,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.711e+27,'cm^3/(mol*s)'), n=-4.1839, Ea=(11151.8,'cal/mol'), T0=(1,'K')), Arrhenius(A=(3.9278e+17,'cm^3/(mol*s)'), n=-1.3688, Ea=(8977.6,'cal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 9,
    label = "CH3CHOH + H <=> C2H4 + H2O",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(1.2326e+17,'cm^3/(mol*s)'), n=-1.166, Ea=(283.6,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.1913e+17,'cm^3/(mol*s)'), n=-1.162, Ea=(266.4,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.8452e+17,'cm^3/(mol*s)'), n=-1.216, Ea=(386.2,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.5864e+20,'cm^3/(mol*s)'), n=-2.079, Ea=(3147.8,'cal/mol'), T0=(1,'K')), Arrhenius(A=(9.2995e+23,'cm^3/(mol*s)'), n=-2.996, Ea=(7953.6,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.6473e+20,'cm^3/(mol*s)'), n=-1.812, Ea=(9447.7,'cal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 10,
    label = "CH3CHOH + H <=> CH3 + CH2OH",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(1.3812e+17,'cm^3/(mol*s)'), n=-0.912, Ea=(3081,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.5182e+17,'cm^3/(mol*s)'), n=-0.923, Ea=(3116.4,'cal/mol'), T0=(1,'K')), Arrhenius(A=(4.4703e+17,'cm^3/(mol*s)'), n=-1.052, Ea=(3508.8,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.2689e+20,'cm^3/(mol*s)'), n=-1.795, Ea=(5893.1,'cal/mol'), T0=(1,'K')), Arrhenius(A=(4.9841e+24,'cm^3/(mol*s)'), n=-2.949, Ea=(10754.3,'cal/mol'), T0=(1,'K')), Arrhenius(A=(4.0326e+23,'cm^3/(mol*s)'), n=-2.527, Ea=(13636.5,'cal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 11,
    label = "CH3CHOH + H <=> C2H5 + OH",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(4.0386e+13,'cm^3/(mol*s)'), n=0.021, Ea=(4441.5,'cal/mol'), T0=(1,'K')), Arrhenius(A=(4.4427e+13,'cm^3/(mol*s)'), n=0.01, Ea=(4476.2,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.0601e+14,'cm^3/(mol*s)'), n=-0.095, Ea=(4790.3,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.6457e+16,'cm^3/(mol*s)'), n=-0.697, Ea=(6677.3,'cal/mol'), T0=(1,'K')), Arrhenius(A=(6.8049e+20,'cm^3/(mol*s)'), n=-1.943, Ea=(11331.3,'cal/mol'), T0=(1,'K')), Arrhenius(A=(6.2689e+21,'cm^3/(mol*s)'), n=-2.106, Ea=(15269.3,'cal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 12,
    label = "CH2CH2OH + H <=> C2H4 + H2O",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(1.6675e+17,'cm^3/(mol*s)'), n=-1.184, Ea=(334.5,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.5593e+17,'cm^3/(mol*s)'), n=-1.176, Ea=(299.3,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.6597e+18,'cm^3/(mol*s)'), n=-1.461, Ea=(1107.4,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.6473e+22,'cm^3/(mol*s)'), n=-2.599, Ea=(5235.2,'cal/mol'), T0=(1,'K')), Arrhenius(A=(6.4993e+23,'cm^3/(mol*s)'), n=-2.883, Ea=(9307.2,'cal/mol'), T0=(1,'K')), Arrhenius(A=(3.6403e+16,'cm^3/(mol*s)'), n=-0.716, Ea=(8766.9,'cal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 13,
    label = "CH2CH2OH + H <=> CH3 + CH2OH",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(1.4865e+17,'cm^3/(mol*s)'), n=-0.903, Ea=(3023.5,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.9331e+17,'cm^3/(mol*s)'), n=-0.935, Ea=(3119.8,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.5358e+18,'cm^3/(mol*s)'), n=-1.243, Ea=(4061.8,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.9282e+22,'cm^3/(mol*s)'), n=-2.3, Ea=(7692.7,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.7876e+25,'cm^3/(mol*s)'), n=-3.1, Ea=(12454.4,'cal/mol'), T0=(1,'K')), Arrhenius(A=(7.4673e+20,'cm^3/(mol*s)'), n=-1.693, Ea=(13429.3,'cal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 14,
    label = "CH2CH2OH + H <=> C2H5 + OH",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(3.60192e+13,'cm^3/(mol*s)'), n=0.05139, Ea=(4301.82,'cal/mol'), T0=(1,'K')), Arrhenius(A=(4.63879e+13,'cm^3/(mol*s)'), n=0.02101, Ea=(4392.21,'cal/mol'), T0=(1,'K')), Arrhenius(A=(3.37344e+14,'cm^3/(mol*s)'), n=-0.21686, Ea=(5113.19,'cal/mol'), T0=(1,'K')), Arrhenius(A=(9.20824e+17,'cm^3/(mol*s)'), n=-1.15762, Ea=(8192.54,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.58439e+22,'cm^3/(mol*s)'), n=-2.27331, Ea=(13260.7,'cal/mol'), T0=(1,'K')), Arrhenius(A=(8.07038e+19,'cm^3/(mol*s)'), n=-1.50969, Ea=(15533.9,'cal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 15,
    label = "CH3CHOH + CH3 <=> C3H6 + H2O",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.05,0.1,0.25,0.5,0.75,1,10,100],'atm'), arrhenius=[Arrhenius(A=(2.8456e+39,'cm^3/(mol*s)'), n=-8.0719, Ea=(13734.2,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.2196e+40,'cm^3/(mol*s)'), n=-8.217, Ea=(15035.5,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.3322e+40,'cm^3/(mol*s)'), n=-8.2466, Ea=(16516.9,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.1936e+40,'cm^3/(mol*s)'), n=-8.1228, Ea=(17411.7,'cal/mol'), T0=(1,'K')), Arrhenius(A=(4.7982e+39,'cm^3/(mol*s)'), n=-7.9853, Ea=(17827.7,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.9463e+39,'cm^3/(mol*s)'), n=-7.8558, Ea=(18067,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.6186e+32,'cm^3/(mol*s)'), n=-5.7536, Ea=(18000.1,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.1307e+19,'cm^3/(mol*s)'), n=-1.8284, Ea=(14114.3,'cal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 16,
    label = "C2H5 + HCO <=> CH3 + CH2CHO",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(9.2017e+17,'cm^3/(mol*s)'), n=-1.2994, Ea=(2504.6,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.0981e+18,'cm^3/(mol*s)'), n=-1.3206, Ea=(2569.4,'cal/mol'), T0=(1,'K')), Arrhenius(A=(5.7367e+18,'cm^3/(mol*s)'), n=-1.5182, Ea=(3184.8,'cal/mol'), T0=(1,'K')), Arrhenius(A=(6.5278e+21,'cm^3/(mol*s)'), n=-2.3515, Ea=(6022.7,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.8799e+25,'cm^3/(mol*s)'), n=-3.2495, Ea=(10576.2,'cal/mol'), T0=(1,'K')), Arrhenius(A=(6.5044e+22,'cm^3/(mol*s)'), n=-2.4427, Ea=(12646.6,'cal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 17,
    label = "C2H5OH + O <=> CH3CHOH + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(145000,'cm^3/(mol*s)'), n=2.47, Ea=(876,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 18,
    label = "C2H5OH + O <=> CH2CH2OH + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(969,'cm^3/(mol*s)'), n=3.23, Ea=(4658,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 19,
    label = "C2H5OH + O <=> C2H5O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00146,'cm^3/(mol*s)'), n=4.73, Ea=(1727,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 20,
    label = "C2H5OH + H <=> CH3CHOH + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(87900,'cm^3/(mol*s)'), n=2.68, Ea=(2910,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 21,
    label = "C2H5OH + H <=> CH2CH2OH + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(53100,'cm^3/(mol*s)'), n=2.81, Ea=(7495.7,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 22,
    label = "C2H5OH + H <=> C2H5O + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(945,'cm^3/(mol*s)'), n=3.14, Ea=(8701.1,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 23,
    label = "C2H5OH + OH <=> CH3CHOH + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(75200,'cm^3/(mol*s)'), n=2.49, Ea=(-1474.1,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 24,
    label = "C2H5OH + OH <=> CH2CH2OH + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3760,'cm^3/(mol*s)'), n=2.78, Ea=(-1810.2,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 25,
    label = "C2H5OH + OH <=> C2H5O + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00581,'cm^3/(mol*s)'), n=4.28, Ea=(-3560,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 26,
    label = "C2H5OH + O2 <=> CH3CHOH + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+13,'cm^3/(mol*s)'), n=0, Ea=(50150,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 27,
    label = "C2H5OH + O2 <=> CH2CH2OH + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(52800,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 28,
    label = "C2H5OH + HO2 <=> CH3CHOH + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.1e-05,'cm^3/(mol*s)'), n=5.26, Ea=(6500,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 29,
    label = "C2H5OH + HO2 <=> CH2CH2OH + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.03986,'cm^3/(mol*s)'), n=4.3, Ea=(15333,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 30,
    label = "C2H5OH + HO2 <=> C2H5O + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.47e-07,'cm^3/(mol*s)'), n=5.3, Ea=(10533.1,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 31,
    label = "C2H5OH + CH3 <=> CH3CHOH + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(19.93,'cm^3/(mol*s)'), n=3.37, Ea=(7634,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 32,
    label = "C2H5OH + CH3 <=> CH2CH2OH + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(330,'cm^3/(mol*s)'), n=3.3, Ea=(12290.8,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 33,
    label = "C2H5OH + CH3 <=> C2H5O + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.035,'cm^3/(mol*s)'), n=3.57, Ea=(7722.3,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 34,
    label = "C2H5OH + CH3O2 <=> CH3CHOH + CH3O2H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.225e-05,'cm^3/(mol*s)'), n=5.26, Ea=(7475.1,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 35,
    label = "C2H5OH + CH3O2 <=> CH2CH2OH + CH3O2H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.01995,'cm^3/(mol*s)'), n=4.3, Ea=(15333,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 36,
    label = "C2H5OH + CH3O2 <=> C2H5O + CH3O2H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2359e-07,'cm^3/(mol*s)'), n=5.3, Ea=(10533.1,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 37,
    label = "C2H5OH + C2H5 <=> CH3CHOH + C2H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+10,'cm^3/(mol*s)'), n=0, Ea=(10400,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 38,
    label = "C2H5OH + C2H5 <=> CH2CH2OH + C2H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.9e+10,'cm^3/(mol*s)'), n=0, Ea=(12300,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 39,
    label = "CH3CHOH <=> CH3CHO + H",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(3.085e+09,'s^-1'), n=1.31, Ea=(33778.4,'cal/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(8.85e+15,'cm^3/(mol*s)'), n=0, Ea=(20782.1,'cal/mol'), T0=(1,'K')), alpha=0.187, T3=(65.2,'K'), T1=(2568,'K'), T2=(41226,'K'), efficiencies={}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 40,
    label = "CH3CHOH <=> C2H3OH + H",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(3.18e+09,'s^-1'), n=1.33, Ea=(35974.3,'cal/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(3.09e+14,'cm^3/(mol*s)'), n=0, Ea=(21517.4,'cal/mol'), T0=(1,'K')), alpha=0.473, T3=(10,'K'), T1=(2218,'K'), T2=(2615,'K'), efficiencies={}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 41,
    label = "CH3CHOH <=> C2H5O",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(4.83e+23,'s^-1'), n=-3.29, Ea=(59993.6,'cal/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(1.435e+43,'cm^3/(mol*s)'), n=-8.12, Ea=(52203.7,'cal/mol'), T0=(1,'K')), alpha=0.5, T3=(863,'K'), T1=(320,'K'), T2=(100000,'K'), efficiencies={}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 42,
    label = "CH3CHOH <=> CH3 + CH2O",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(1.11e+09,'s^-1'), n=1.18, Ea=(33987.1,'cal/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(2.93e+15,'cm^3/(mol*s)'), n=0, Ea=(21332.6,'cal/mol'), T0=(1,'K')), alpha=0.124, T3=(1,'K'), T1=(1729,'K'), T2=(50000,'K'), efficiencies={}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 43,
    label = "C2H5O <=> CH3 + CH2O",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(3.155e+10,'s^-1'), n=0.93, Ea=(17099.9,'cal/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(2.35e+25,'cm^3/(mol*s)'), n=-3, Ea=(16533.5,'cal/mol'), T0=(1,'K')), alpha=0.426, T3=(0.3,'K'), T1=(2278,'K'), T2=(100000,'K'), efficiencies={}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 44,
    label = "C2H5O + O2 <=> CH3CHO + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.28e+10,'cm^3/(mol*s)'), n=0, Ea=(1097,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 45,
    label = "CH2CH2OH + O2 <=> CH2CH2OH-2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.6e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 46,
    label = "CH2CH2OH-2O2 <=> CH2CH2O-2OOH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.91e+12,'s^-1'), n=-0.226, Ea=(22300,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 47,
    label = "CH2CH2O-2OOH <=> OH + CH2O + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.072e+13,'s^-1'), n=-0.08, Ea=(10790,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 48,
    label = "CH2CH2OH-2O2 <=> CH2CHOH-2OOH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.97e+12,'s^-1'), n=-0.27, Ea=(28020,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 49,
    label = "CH2CHOH-2OOH <=> C2H3OH + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.71e+09,'s^-1'), n=0.499, Ea=(11790,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 50,
    label = "CH2CHOH-2OOH <=> CY(CCO)OH + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.19e+09,'s^-1'), n=0.634, Ea=(5.38,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 51,
    label = "CH2CH2OH-2O2 <=> C2H3OH + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.44e+13,'s^-1'), n=-0.253, Ea=(32590,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 52,
    label = "CY(CCO)OH + OH <=> CH2CO + H2O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2260,'cm^3/(mol*s)'), n=2.73, Ea=(-4688,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 53,
    label = "CY(CCO)OH + HO2 <=> CH2CO + H2O2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.6,'cm^3/(mol*s)'), n=3.46, Ea=(9732.33,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 54,
    label = "CH3CHOH + O2 <=> CH3CHOH-1O2",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(672000,'cm^3/(mol*s)'), n=0.18, Ea=(-5550,'cal/mol'), T0=(1,'K')), Arrhenius(A=(6.77e+06,'cm^3/(mol*s)'), n=0.17, Ea=(-5540,'cal/mol'), T0=(1,'K')), Arrhenius(A=(7.3e+07,'cm^3/(mol*s)'), n=0.17, Ea=(-5520,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.5e+09,'cm^3/(mol*s)'), n=0.08, Ea=(-5300,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.93e+12,'cm^3/(mol*s)'), n=-0.53, Ea=(-3780,'cal/mol'), T0=(1,'K')), Arrhenius(A=(5.16e+16,'cm^3/(mol*s)'), n=-1.51, Ea=(-507,'cal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 55,
    label = "CH3CHOH-1O2 <=> CH3COHOOH",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(1.88e+43,'s^-1'), n=-11.7, Ea=(16500,'cal/mol'), T0=(1,'K')), Arrhenius(A=(4.54e+45,'s^-1'), n=-12.1, Ea=(17500,'cal/mol'), T0=(1,'K')), Arrhenius(A=(6.32e+48,'s^-1'), n=-12.8, Ea=(19500,'cal/mol'), T0=(1,'K')), Arrhenius(A=(6.64e+42,'s^-1'), n=-10.7, Ea=(18100,'cal/mol'), T0=(1,'K')), Arrhenius(A=(8.08e+21,'s^-1'), n=-4.06, Ea=(10700,'cal/mol'), T0=(1,'K')), Arrhenius(A=(7.32e+08,'s^-1'), n=0.29, Ea=(7300,'cal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 56,
    label = "CH3COHOOH <=> CH3CHO + HO2",
    degeneracy = 1.0,
    kinetics = MultiPDepArrhenius(arrhenius=[PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(14400,'s^-1'), n=0.25, Ea=(28300,'cal/mol'), T0=(1,'K')), Arrhenius(A=(145000,'s^-1'), n=0.24, Ea=(28300,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.6e+06,'s^-1'), n=0.23, Ea=(28400,'cal/mol'), T0=(1,'K')), Arrhenius(A=(4.04e+07,'s^-1'), n=0.12, Ea=(28600,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.09e+11,'s^-1'), n=-0.58, Ea=(30500,'cal/mol'), T0=(1,'K')), Arrhenius(A=(3.28e+14,'s^-1'), n=-1.32, Ea=(33600,'cal/mol'), T0=(1,'K'))]), PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(1030,'s^-1'), n=1.04, Ea=(849,'cal/mol'), T0=(1,'K')), Arrhenius(A=(10400,'s^-1'), n=1.04, Ea=(853,'cal/mol'), T0=(1,'K')), Arrhenius(A=(109000,'s^-1'), n=1.04, Ea=(876,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.56e+06,'s^-1'), n=0.99, Ea=(1020,'cal/mol'), T0=(1,'K')), Arrhenius(A=(6.2e+07,'s^-1'), n=0.83, Ea=(1530,'cal/mol'), T0=(1,'K')), Arrhenius(A=(6.23e+09,'s^-1'), n=0.55, Ea=(2470,'cal/mol'), T0=(1,'K'))])]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 57,
    label = "CH3CHOH-1O2 <=> CH3CHO + HO2",
    degeneracy = 1.0,
    kinetics = MultiPDepArrhenius(arrhenius=[PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(9.52e+13,'s^-1'), n=-1.98, Ea=(32300,'cal/mol'), T0=(1,'K')), Arrhenius(A=(9.61e+14,'s^-1'), n=-1.98, Ea=(32300,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.06e+16,'s^-1'), n=-2, Ea=(32400,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.71e+17,'s^-1'), n=-2.11, Ea=(32700,'cal/mol'), T0=(1,'K')), Arrhenius(A=(7.88e+20,'s^-1'), n=-2.82, Ea=(34500,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.07e+24,'s^-1'), n=-3.55, Ea=(37600,'cal/mol'), T0=(1,'K'))]), PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(7.91e+11,'s^-1'), n=-1.57, Ea=(7570,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.63e+13,'s^-1'), n=-1.66, Ea=(7800,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.29e+16,'s^-1'), n=-2.19, Ea=(9230,'cal/mol'), T0=(1,'K')), Arrhenius(A=(3.86e+20,'s^-1'), n=-3.14, Ea=(12600,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.5e+21,'s^-1'), n=-3.01, Ea=(15100,'cal/mol'), T0=(1,'K')), Arrhenius(A=(5.8e+17,'s^-1'), n=-1.7, Ea=(15100,'cal/mol'), T0=(1,'K'))])]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 58,
    label = "CH3CHOH + O2 <=> CH3CHO + HO2",
    degeneracy = 1.0,
    kinetics = MultiPDepArrhenius(arrhenius=[PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(3.18e+12,'cm^3/(mol*s)'), n=-0.5, Ea=(3130,'cal/mol'), T0=(1,'K')), Arrhenius(A=(3.2e+12,'cm^3/(mol*s)'), n=-0.5, Ea=(3130,'cal/mol'), T0=(1,'K')), Arrhenius(A=(3.39e+12,'cm^3/(mol*s)'), n=-0.51, Ea=(3150,'cal/mol'), T0=(1,'K')), Arrhenius(A=(5.87e+12,'cm^3/(mol*s)'), n=-0.57, Ea=(3320,'cal/mol'), T0=(1,'K')), Arrhenius(A=(3.13e+14,'cm^3/(mol*s)'), n=-1.07, Ea=(4570,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.87e+18,'cm^3/(mol*s)'), n=-2.14, Ea=(8130,'cal/mol'), T0=(1,'K'))]), PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(3.15e+19,'cm^3/(mol*s)'), n=-2.21, Ea=(1500,'cal/mol'), T0=(1,'K')), Arrhenius(A=(3.18e+19,'cm^3/(mol*s)'), n=-2.21, Ea=(1500,'cal/mol'), T0=(1,'K')), Arrhenius(A=(3.42e+19,'cm^3/(mol*s)'), n=-2.22, Ea=(1520,'cal/mol'), T0=(1,'K')), Arrhenius(A=(6.91e+19,'cm^3/(mol*s)'), n=-2.31, Ea=(1740,'cal/mol'), T0=(1,'K')), Arrhenius(A=(8.4e+21,'cm^3/(mol*s)'), n=-2.9, Ea=(3230,'cal/mol'), T0=(1,'K')), Arrhenius(A=(4.11e+25,'cm^3/(mol*s)'), n=-3.95, Ea=(6630,'cal/mol'), T0=(1,'K'))])]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 59,
    label = "CH3CHOH-1O2 <=> C2H4O-1OOH",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(1700,'s^-1'), n=-0.82, Ea=(16000,'cal/mol'), T0=(1,'K')), Arrhenius(A=(181000,'s^-1'), n=-0.82, Ea=(16000,'cal/mol'), T0=(1,'K')), Arrhenius(A=(3.34e+07,'s^-1'), n=-0.9, Ea=(16200,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.55e+11,'s^-1'), n=-1.43, Ea=(17700,'cal/mol'), T0=(1,'K')), Arrhenius(A=(3.42e+17,'s^-1'), n=-2.58, Ea=(21900,'cal/mol'), T0=(1,'K')), Arrhenius(A=(4.08e+18,'s^-1'), n=-2.37, Ea=(24500,'cal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 60,
    label = "C2H4O-1OOH <=> CH3CHO + HO2",
    degeneracy = 1.0,
    kinetics = MultiPDepArrhenius(arrhenius=[PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(2.09e+55,'s^-1'), n=-15.3, Ea=(27900,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.09e+56,'s^-1'), n=-15.3, Ea=(27900,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.12e+57,'s^-1'), n=-15.3, Ea=(27900,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.36e+58,'s^-1'), n=-15.3, Ea=(27900,'cal/mol'), T0=(1,'K')), Arrhenius(A=(5.93e+59,'s^-1'), n=-15.5, Ea=(28000,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.09e+62,'s^-1'), n=-16, Ea=(28500,'cal/mol'), T0=(1,'K'))]), PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(3.27e+40,'s^-1'), n=-10.5, Ea=(14200,'cal/mol'), T0=(1,'K')), Arrhenius(A=(3.5e+41,'s^-1'), n=-10.5, Ea=(14200,'cal/mol'), T0=(1,'K')), Arrhenius(A=(6.72e+42,'s^-1'), n=-10.6, Ea=(14400,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.04e+46,'s^-1'), n=-11.3, Ea=(15800,'cal/mol'), T0=(1,'K')), Arrhenius(A=(3.5e+54,'s^-1'), n=-13.5, Ea=(20800,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.55e+64,'s^-1'), n=-16.3, Ea=(26700,'cal/mol'), T0=(1,'K'))])]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 61,
    label = "CH2CHOH-1OOH <=> CH3CHOH-1O2",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(4.92e+32,'s^-1'), n=-10.7, Ea=(16700,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.26e+40,'s^-1'), n=-12.3, Ea=(20500,'cal/mol'), T0=(1,'K')), Arrhenius(A=(4.25e+45,'s^-1'), n=-13.5, Ea=(23400,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.12e+48,'s^-1'), n=-13.9, Ea=(24300,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.75e+52,'s^-1'), n=-14.8, Ea=(26300,'cal/mol'), T0=(1,'K')), Arrhenius(A=(7.12e+45,'s^-1'), n=-12.7, Ea=(22500,'cal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 62,
    label = "CH2CHOH-1OOH <=> C2H3OH + HO2",
    degeneracy = 1.0,
    kinetics = MultiPDepArrhenius(arrhenius=[PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(9.24e+44,'s^-1'), n=-14, Ea=(24600,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.16e+51,'s^-1'), n=-15.6, Ea=(28300,'cal/mol'), T0=(1,'K')), Arrhenius(A=(8.93e+55,'s^-1'), n=-16.8, Ea=(31300,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.6e+57,'s^-1'), n=-17.2, Ea=(32200,'cal/mol'), T0=(1,'K')), Arrhenius(A=(8.12e+60,'s^-1'), n=-18.2, Ea=(34400,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.29e+58,'s^-1'), n=-17.6, Ea=(33400,'cal/mol'), T0=(1,'K'))]), PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(1.22e+51,'s^-1'), n=-13.7, Ea=(25000,'cal/mol'), T0=(1,'K')), Arrhenius(A=(4.35e+56,'s^-1'), n=-15.1, Ea=(28600,'cal/mol'), T0=(1,'K')), Arrhenius(A=(8.38e+59,'s^-1'), n=-15.9, Ea=(30800,'cal/mol'), T0=(1,'K')), Arrhenius(A=(3.78e+60,'s^-1'), n=-16.1, Ea=(31300,'cal/mol'), T0=(1,'K')), Arrhenius(A=(4.47e+60,'s^-1'), n=-16.1, Ea=(31300,'cal/mol'), T0=(1,'K')), Arrhenius(A=(4.55e+60,'s^-1'), n=-16.1, Ea=(31300,'cal/mol'), T0=(1,'K'))])]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 63,
    label = "CH3CHOH-1O2 <=> C2H3OH + HO2",
    degeneracy = 1.0,
    kinetics = MultiPDepArrhenius(arrhenius=[PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(465,'s^-1'), n=1.31, Ea=(25500,'cal/mol'), T0=(1,'K')), Arrhenius(A=(4720,'s^-1'), n=1.31, Ea=(25500,'cal/mol'), T0=(1,'K')), Arrhenius(A=(54600,'s^-1'), n=1.29, Ea=(25600,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.07e+06,'s^-1'), n=1.13, Ea=(26000,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.3e+10,'s^-1'), n=0.26, Ea=(28200,'cal/mol'), T0=(1,'K')), Arrhenius(A=(5.29e+13,'s^-1'), n=-0.42, Ea=(31200,'cal/mol'), T0=(1,'K'))]), PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(12700,'s^-1'), n=0.58, Ea=(31800,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.71e+07,'s^-1'), n=-0.03, Ea=(33200,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.98e+13,'s^-1'), n=-1.51, Ea=(36800,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.01e+21,'s^-1'), n=-3.33, Ea=(42300,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.74e+23,'s^-1'), n=-3.58, Ea=(46200,'cal/mol'), T0=(1,'K')), Arrhenius(A=(3.42e+20,'s^-1'), n=-2.49, Ea=(48200,'cal/mol'), T0=(1,'K'))])]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 64,
    label = "CH3CHOH + O2 <=> CH2CHOH-1OOH",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(0.000734,'cm^3/(mol*s)'), n=2.06, Ea=(-6890,'cal/mol'), T0=(1,'K')), Arrhenius(A=(0.0889,'cm^3/(mol*s)'), n=1.75, Ea=(-6200,'cal/mol'), T0=(1,'K')), Arrhenius(A=(7290,'cm^3/(mol*s)'), n=0.63, Ea=(-3610,'cal/mol'), T0=(1,'K')), Arrhenius(A=(4.94e+11,'cm^3/(mol*s)'), n=-1.29, Ea=(1520,'cal/mol'), T0=(1,'K')), Arrhenius(A=(3.03e+16,'cm^3/(mol*s)'), n=-2.29, Ea=(6400,'cal/mol'), T0=(1,'K')), Arrhenius(A=(5.06e+15,'cm^3/(mol*s)'), n=-1.73, Ea=(9250,'cal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 65,
    label = "CH3CHOH + O2 <=> C2H3OH + HO2",
    degeneracy = 1.0,
    kinetics = MultiPDepArrhenius(arrhenius=[PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(106000,'cm^3/(mol*s)'), n=1.85, Ea=(951,'cal/mol'), T0=(1,'K')), Arrhenius(A=(106000,'cm^3/(mol*s)'), n=1.85, Ea=(953,'cal/mol'), T0=(1,'K')), Arrhenius(A=(113000,'cm^3/(mol*s)'), n=1.85, Ea=(972,'cal/mol'), T0=(1,'K')), Arrhenius(A=(206000,'cm^3/(mol*s)'), n=1.77, Ea=(1150,'cal/mol'), T0=(1,'K')), Arrhenius(A=(1.59e+07,'cm^3/(mol*s)'), n=1.23, Ea=(2470,'cal/mol'), T0=(1,'K')), Arrhenius(A=(3.85e+11,'cm^3/(mol*s)'), n=-0.01, Ea=(6110,'cal/mol'), T0=(1,'K'))]), PDepArrhenius(pressures=([0.001,0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(1020,'cm^3/(mol*s)'), n=2.09, Ea=(2350,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2270,'cm^3/(mol*s)'), n=1.99, Ea=(2570,'cal/mol'), T0=(1,'K')), Arrhenius(A=(260000,'cm^3/(mol*s)'), n=1.4, Ea=(3890,'cal/mol'), T0=(1,'K')), Arrhenius(A=(4.01e+11,'cm^3/(mol*s)'), n=-0.36, Ea=(8130,'cal/mol'), T0=(1,'K')), Arrhenius(A=(2.44e+18,'cm^3/(mol*s)'), n=-2.23, Ea=(14100,'cal/mol'), T0=(1,'K')), Arrhenius(A=(7.81e+18,'cm^3/(mol*s)'), n=-2.3, Ea=(18100,'cal/mol'), T0=(1,'K'))])]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 66,
    label = "CH2CH2OH + HO2 => CH2OH + CH2O + OH",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12,'cm^3/(mol*s)'), n=0, Ea=(-1000,'cal/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

