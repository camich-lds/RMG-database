#!/usr/bin/env python
# encoding: utf-8

name = "Tran_DEE_submech"
shortDesc = ""
longDesc = """
Luc-Sy Tran, Olivier Herbinet, Yuyang Li, Julia Wullenkord, Meirong Zeng, Eike Bräuer, Fei Qi, Katharina Kohse-Höinghaus, Frédérique Battin-Leclerc,
Low-temperature gas-phase oxidation of diethyl ether: Fuel reactivity and fuel-specific products,
Proceedings of the Combustion Institute,
Volume 37, Issue 1,
2019,
Pages 511-519,
ISSN 1540-7489,
https://doi.org/10.1016/j.proci.2018.05.135
"""
entry(
    index = 0,
    label = "DEE",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.04483,0.0183196,3.55081e-05,-5.02668e-08,1.89014e-11,-33834.2,-5.84275], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.78564,0.0425982,-2.18045e-05,5.47179e-09,-5.46342e-13,-33655.2,7.33101], Tmin=(1000,'K'), Tmax=(2500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2500,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1,
    label = "C2H5OC2H4-B",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {2,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.85195,0.0229054,2.36937e-05,-4.13043e-08,1.65961e-11,-7880.22,2.70002], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.96848,0.0376126,-1.91373e-05,4.76861e-09,-4.72236e-13,-8177.92,4.42055], Tmin=(1000,'K'), Tmax=(2500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2500,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2,
    label = "C2H5OC2H4-A",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {3,S} {5,S} {14,S}
5  O u0 p2 c0 {1,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53522,0.0354038,-2.27974e-07,-2.17372e-08,1.07186e-11,-11343.7,12.3808], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.43904,0.0364642,-1.82512e-05,4.47334e-09,-4.35637e-13,-12091.7,1.23263], Tmin=(1000,'K'), Tmax=(2500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2500,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 3,
    label = "C2OC2H4OO-B",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {3,S} {16,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.83039,0.0140264,7.29693e-05,-1.01492e-07,4.01882e-11,-26134.3,-6.80851], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.9873,0.0324217,-1.31532e-05,2.4348e-09,-1.68723e-13,-28691.8,-35.4109], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

# entry(
    # index = 3,
    # label = "C2OC2H4OO-B",
    # molecule = 
# """
# multiplicity 2
# 1  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
# 2  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
# 3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
# 4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
# 5  O u0 p2 c0 {1,S} {2,S}
# 6  O u0 p2 c0 {3,S} {16,S}
# 7  H u0 p0 c0 {2,S}
# 8  H u0 p0 c0 {2,S}
# 9  H u0 p0 c0 {1,S}
# 10 H u0 p0 c0 {1,S}
# 11 H u0 p0 c0 {3,S}
# 12 H u0 p0 c0 {3,S}
# 13 H u0 p0 c0 {4,S}
# 14 H u0 p0 c0 {4,S}
# 15 H u0 p0 c0 {4,S}
# 16 O u1 p2 c0 {6,S}
# """,
    # thermo = NASA(
        # polynomials = [
            # NASAPolynomial(coeffs=[6.69000000E+00, 3.85000000E-02,-9.51120000E-06, 1.50000000E-11,-2.50000000E-12,-2.57520000E+04, 1.66200000E+00], Tmin=(200,'K'), Tmax=(1000,'K')),
            # NASAPolynomial(coeffs=[1.68000000E+01, 2.33000000E-02,-7.35000000E-06, 7.40000000E-10, 2.00000000E-14,-2.98900000E+04,-5.52000000E+01], Tmin=(1000,'K'), Tmax=(5000,'K')),
        # ],
        # Tmin = (200,'K'),
        # Tmax = (5000,'K'),
    # ),
    # shortDesc = """Duan et al. 2022""",
    # longDesc = 
# """

# """,
# )

entry(
    index = 4,
    label = "C2OC2H4OO-A",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.48553,0.030558,3.99702e-05,-7.44018e-08,3.21226e-11,-31293.5,1.19693], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.9406,0.0312309,-1.25998e-05,2.32341e-09,-1.60566e-13,-34286.3,-42.1928], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

# entry(
    # index = 4,
    # label = "C2OC2H4OO-A",
    # molecule = 
# """
# multiplicity 2
# 1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
# 2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
# 3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
# 4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
# 5  O u0 p2 c0 {1,S} {2,S}
# 6  O u0 p2 c0 {1,S} {16,S}
# 7  H u0 p0 c0 {1,S}
# 8  H u0 p0 c0 {2,S}
# 9  H u0 p0 c0 {2,S}
# 10 H u0 p0 c0 {4,S}
# 11 H u0 p0 c0 {4,S}
# 12 H u0 p0 c0 {4,S}
# 13 H u0 p0 c0 {3,S}
# 14 H u0 p0 c0 {3,S}
# 15 H u0 p0 c0 {3,S}
# 16 O u1 p2 c0 {6,S}
# """,
    # thermo = NASA(
        # polynomials = [
            # NASAPolynomial(coeffs=[6.65000000E+00, 3.86800000E-02,-9.52000000E-06, 1.20000000E-10,-2.25000000E-12,-3.07610000E+04,-1.05000000E-01], Tmin=(200,'K'), Tmax=(1000,'K')),
            # NASAPolynomial(coeffs=[ 1.69000000E+01, 2.30000000E-02,-7.35900000E-06, 7.41000000E-10, 2.70000000E-14,-3.41870000E+04,-5.67300000E+01], Tmin=(1000,'K'), Tmax=(5000,'K')),
        # ],
        # Tmin = (200,'K'),
        # Tmax = (5000,'K'),
    # ),
    # shortDesc = """Duan et al. 2022""",
    # longDesc = 
# """

# """,
# )

entry(
    index = 5,
    label = "C2OC2-BO2H-A",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {2,S} {5,S} {15,S}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.55168,0.00817878,9.41414e-05,-1.30857e-07,5.32457e-11,-21801.1,-8.14319], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.993,0.0303366,-1.21431e-05,2.22714e-09,-1.53329e-13,-24484.4,-38.8503], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 6,
    label = "C2OC2-BO2H-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {3,S} {5,S} {15,S}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.04809,0.04262,1.04522e-05,-4.61843e-08,2.24966e-11,-21296.7,8.46202], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.385,0.0300271,-1.20373e-05,2.20997e-09,-1.52257e-13,-24409.5,-42.6669], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 7,
    label = "C2OC2-BO2H-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
4  C u1 p0 c0 {3,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.010321,0.0917558,-0.000125356,1.02484e-07,-3.44036e-11,-17601.1,28.2168], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.6004,0.0297905,-1.19431e-05,2.19373e-09,-1.51227e-13,-20790.8,-42.4421], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 8,
    label = "C2OC2-AO2H-B",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.07146,0.0225468,6.24342e-05,-1.02295e-07,4.38645e-11,-22846.7,-4.07451], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.2643,0.0289179,-1.15225e-05,2.10669e-09,-1.44717e-13,-25871.5,-46.9522], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 9,
    label = "C2OC2-AO2H-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {3,S} {5,S} {15,S}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.48782,0.0428071,1.5018e-05,-5.64236e-08,2.78373e-11,-26761.5,5.7937], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.8131,0.0281952,-1.11786e-05,2.03656e-09,-1.3954e-13,-30068.3,-50.3132], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 10,
    label = "C2OC2-AO2H-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {2,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.34829,0.0261285,5.7471e-05,-9.99728e-08,4.37153e-11,-23278.9,-1.11852], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.5362,0.0285959,-1.13771e-05,2.07791e-09,-1.42631e-13,-26492.2,-48.7742], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 11,
    label = "C2OC2OA-B",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {1,S} {2,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.6943,0.0114861,8.47912e-05,-1.2285e-07,5.08234e-11,-33861.3,3.62949], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.3106,0.0280029,-1.13118e-05,2.08757e-09,-1.44344e-13,-36742.6,-32.5361], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 12,
    label = "C2OC2OA-2",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {3,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.62498,0.00198465,0.00011672,-1.57453e-07,6.35801e-11,-44846.3,9.01294], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.46818,0.0301415,-1.22716e-05,2.2771e-09,-1.58062e-13,-47955.5,-25.4125], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 13,
    label = "C2OC2OB-2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {6,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {3,S}
6  O u0 p2 c0 {1,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79147,-0.000646443,0.000134558,-1.79443e-07,7.18015e-11,-40729.7,10.2151], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.573,0.0295618,-1.21994e-05,2.28659e-09,-1.59911e-13,-44736.2,-36.0458], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 14,
    label = "C2OC2OA-1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {2,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.5789,0.00551377,0.000100432,-1.37485e-07,5.56257e-11,-41116.6,2.87831], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.2427,0.0292496,-1.18728e-05,2.19853e-09,-1.52383e-13,-43978.6,-29.538], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

#Old RMG-GA
# entry(
#     index = 15,
#     label = "C2H5OCH2CHO",
#     molecule = 
# """
# 1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
# 2  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
# 3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
# 4  C u0 p0 c0 {2,S} {13,D} {14,S}
# 5  O u0 p2 c0 {1,S} {2,S}
# 6  H u0 p0 c0 {1,S}
# 7  H u0 p0 c0 {1,S}
# 8  H u0 p0 c0 {3,S}
# 9  H u0 p0 c0 {3,S}
# 10 H u0 p0 c0 {3,S}
# 11 H u0 p0 c0 {2,S}
# 12 H u0 p0 c0 {2,S}
# 13 O u0 p2 c0 {4,D}
# 14 H u0 p0 c0 {4,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[3.91034,0.0366171,-2.90959e-06,-1.48433e-08,6.13435e-12,-41079.1,11.723], Tmin=(100,'K'), Tmax=(1174.32,'K')),
#             NASAPolynomial(coeffs=[12.6767,0.0243583,-9.73375e-06,1.79431e-09,-1.24795e-13,-44351.6,-37.1455], Tmin=(1174.32,'K'), Tmax=(5000,'K')),
#         ],
#         Tmin = (100,'K'),
#         Tmax = (5000,'K'),
#     ),
#     shortDesc = """""",
#     longDesc = 
# """

# """,
# )

entry(
    index = 16,
    label = "C2H5OC2H4O-B",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {10,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u1 p2 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.7984,0.00553203,0.000100984,-1.35633e-07,5.41637e-11,-25412.1,1.09427], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.6929,0.0318907,-1.29789e-05,2.4074e-09,-1.67048e-13,-28142.4,-27.6162], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 17,
    label = "C2H5OC2H4O-A",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {5,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u1 p2 c0 {2,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.96877,0.0119442,8.74784e-05,-1.24184e-07,5.06611e-11,-31267.6,4.22311], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.0828,0.031269,-1.26619e-05,2.34057e-09,-1.62022e-13,-34130.5,-29.8272], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 18,
    label = "C2OC2H4OOH-B",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {3,S} {7,S}
7  O u0 p2 c0 {6,S} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.22533,0.00692048,0.000112642,-1.52857e-07,6.14027e-11,-43402.7,-3.83001], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.966,0.0351009,-1.41649e-05,2.61282e-09,-1.80618e-13,-46515.1,-37.7812], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 19,
    label = "C2OC2H4OOH-A",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.83588,0.0192614,8.24257e-05,-1.22925e-07,5.07812e-11,-49663.6,0.284877], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.3862,0.034473,-1.38521e-05,2.54764e-09,-1.7575e-13,-52903.9,-41.1211], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 20,
    label = "EVE",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {12,S} {13,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.34503,0.0616421,-6.2749e-05,3.72898e-08,-9.39786e-12,-19160.5,25.4219], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.32417,0.0333592,-1.71546e-05,4.35285e-09,-4.4195e-13,-20443.3,-6.42158], Tmin=(1000,'K'), Tmax=(2500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2500,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

#Old RMG-GA
# entry(
#     index = 21,
#     label = "C2H5OC2H4OH-B",
#     molecule = 
# """
# 1  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
# 2  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
# 3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
# 4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
# 5  O u0 p2 c0 {1,S} {2,S}
# 6  O u0 p2 c0 {3,S} {16,S}
# 7  H u0 p0 c0 {2,S}
# 8  H u0 p0 c0 {2,S}
# 9  H u0 p0 c0 {1,S}
# 10 H u0 p0 c0 {1,S}
# 11 H u0 p0 c0 {3,S}
# 12 H u0 p0 c0 {3,S}
# 13 H u0 p0 c0 {4,S}
# 14 H u0 p0 c0 {4,S}
# 15 H u0 p0 c0 {4,S}
# 16 H u0 p0 c0 {6,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[3.27004,0.0514805,-3.08522e-05,9.37184e-09,-1.14667e-12,-52242.8,14.8238], Tmin=(100,'K'), Tmax=(1891.02,'K')),
#             NASAPolynomial(coeffs=[16.8187,0.0228216,-8.11927e-06,1.35748e-09,-8.71362e-14,-57366.9,-59.1726], Tmin=(1891.02,'K'), Tmax=(5000,'K')),
#         ],
#         Tmin = (100,'K'),
#         Tmax = (5000,'K'),
#     ),
#     shortDesc = """""",
#     longDesc = 
# """

# """,
# )

#Old RMG-GA
# entry(
#     index = 22,
#     label = "C2H5OC2H4OH-A",
#     molecule = 
# """
# 1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
# 2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
# 3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
# 4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
# 5  O u0 p2 c0 {1,S} {2,S}
# 6  O u0 p2 c0 {1,S} {16,S}
# 7  H u0 p0 c0 {1,S}
# 8  H u0 p0 c0 {2,S}
# 9  H u0 p0 c0 {2,S}
# 10 H u0 p0 c0 {4,S}
# 11 H u0 p0 c0 {4,S}
# 12 H u0 p0 c0 {4,S}
# 13 H u0 p0 c0 {3,S}
# 14 H u0 p0 c0 {3,S}
# 15 H u0 p0 c0 {3,S}
# 16 H u0 p0 c0 {6,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[2.77665,0.0515702,-2.69972e-05,4.48983e-09,4.32213e-13,-57058.5,16.5507], Tmin=(100,'K'), Tmax=(1360.59,'K')),
#             NASAPolynomial(coeffs=[15.4913,0.0249052,-9.41274e-06,1.66185e-09,-1.11698e-13,-61510.1,-52.3499], Tmin=(1360.59,'K'), Tmax=(5000,'K')),
#         ],
#         Tmin = (100,'K'),
#         Tmax = (5000,'K'),
#     ),
#     shortDesc = """""",
#     longDesc = 
# """

# """,
# )

#O2QOOH species used manipulated Sakai Thermo - Remove from future RMG runs
entry(
    index = 23,
    label = "C4O-BO2H-AO2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {7,S} {9,S}
2  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {3,S} {8,S}
7  O u0 p2 c0 {1,S} {17,S}
8  O u0 p2 c0 {6,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u1 p2 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.60686,0.0462131,3.88122e-05,-9.22327e-08,4.26409e-11,-41806.5,6.92991], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[19.512,0.0326316,-1.34424e-05,2.51466e-09,-1.75558e-13,-46626.2,-70.2929], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 24,
    label = "C4O-BO2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {7,S} {9,S}
2  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {3,S} {8,S}
7  O u0 p2 c0 {1,S} {17,S}
8  O u0 p2 c0 {6,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u1 p2 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.35671,0.0376816,5.64308e-05,-1.08943e-07,4.85443e-11,-41696.8,2.12264], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[19.76,0.0322665,-1.32606e-05,2.47669e-09,-1.72714e-13,-46273.7,-68.2566], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 25,
    label = "C4O-BO2H-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {3,S} {5,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {6,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {3,S} {8,S}
7  O u0 p2 c0 {4,S} {17,S}
8  O u0 p2 c0 {6,S} {18,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 O u1 p2 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.24569,0.0262982,8.77646e-05,-1.42313e-07,6.10012e-11,-36200.3,-0.71626], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[19.3668,0.0327871,-1.35085e-05,2.5272e-09,-1.76437e-13,-40782.8,-66.3764], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 26,
    label = "C4O-AO2H-BO2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {9,S}
2  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {3,S} {17,S}
8  O u0 p2 c0 {6,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u1 p2 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.38092,0.0416166,5.0337e-05,-1.04764e-07,4.74932e-11,-42002.5,5.29364], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[19.7073,0.0323435,-1.32989e-05,2.48468e-09,-1.73311e-13,-46759.4,-69.5038], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 27,
    label = "C4O-AO2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {3,S} {5,S} {7,S} {9,S}
3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {2,S} {17,S}
8  O u0 p2 c0 {6,S} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u1 p2 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.73623,0.0515034,2.22133e-05,-7.43584e-08,3.60402e-11,-47359.9,6.25911], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[20.0891,0.0318377,-1.3058e-05,2.4356e-09,-1.69694e-13,-52079.4,-72.131], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 28,
    label = "C4O-AO2H-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {9,S}
2  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {3,S} {17,S}
8  O u0 p2 c0 {6,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u1 p2 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.66662,0.0401623,5.3389e-05,-1.0768e-07,4.85266e-11,-42003.9,4.4505], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[19.7395,0.0322907,-1.32715e-05,2.47886e-09,-1.7287e-13,-46720.6,-69.1968], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 29,
    label = "C4O-BO2H-AO2H-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
4  C u1 p0 c0 {3,S} {5,S} {16,S}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {1,S} {9,S}
7  O u0 p2 c0 {2,S} {8,S}
8  O u0 p2 c0 {7,S} {17,S}
9  O u0 p2 c0 {6,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.26771,0.0530676,1.68256e-05,-6.94479e-08,3.45647e-11,-36140.4,4.51679], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[20.8629,0.0308099,-1.25687e-05,2.33598e-09,-1.62353e-13,-40809.2,-74.5946], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 30,
    label = "C4O-BO2H-1O2H-A",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {7,S} {14,S} {15,S}
4  C u1 p0 c0 {3,S} {5,S} {16,S}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {3,S} {9,S}
8  O u0 p2 c0 {6,S} {17,S}
9  O u0 p2 c0 {7,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.35131,0.0649143,-1.03039e-05,-4.26967e-08,2.49748e-11,-36025.7,10.9431], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[20.786,0.0308629,-1.25849e-05,2.33839e-09,-1.62496e-13,-40905.6,-76.1188], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 31,
    label = "C4O-BO2H-2O2H-A",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {7,S} {14,S} {15,S}
4  C u1 p0 c0 {3,S} {5,S} {16,S}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {2,S} {9,S}
7  O u0 p2 c0 {3,S} {8,S}
8  O u0 p2 c0 {7,S} {17,S}
9  O u0 p2 c0 {6,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.62549,0.0430943,4.03965e-05,-9.293e-08,4.30187e-11,-30728,1.50351], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[20.6948,0.0309446,-1.2615e-05,2.34346e-09,-1.62817e-13,-35234,-71.0831], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

#Old RMG-GA
# entry(
#     index = 32,
#     label = "C4O-AO2H-1O2H-B",
#     molecule = 
# """
# multiplicity 2
# 1  C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
# 2  C u0 p0 c0 {4,S} {5,S} {7,S} {11,S}
# 3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
# 4  C u1 p0 c0 {2,S} {15,S} {16,S}
# 5  O u0 p2 c0 {1,S} {2,S}
# 6  O u0 p2 c0 {1,S} {9,S}
# 7  O u0 p2 c0 {2,S} {8,S}
# 8  O u0 p2 c0 {7,S} {17,S}
# 9  O u0 p2 c0 {6,S} {18,S}
# 10 H u0 p0 c0 {1,S}
# 11 H u0 p0 c0 {2,S}
# 12 H u0 p0 c0 {3,S}
# 13 H u0 p0 c0 {3,S}
# 14 H u0 p0 c0 {3,S}
# 15 H u0 p0 c0 {4,S}
# 16 H u0 p0 c0 {4,S}
# 17 H u0 p0 c0 {8,S}
# 18 H u0 p0 c0 {9,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[-1.14932,0.112188,-0.000142436,9.97061e-08,-2.85315e-11,-37889.6,38.3126], Tmin=(100,'K'), Tmax=(964.57,'K')),
#             NASAPolynomial(coeffs=[10.8289,0.0496129,-2.50624e-05,4.71543e-09,-3.17358e-13,-39600.2,-15.9323], Tmin=(964.57,'K'), Tmax=(5000,'K')),
#         ],
#         Tmin = (100,'K'),
#         Tmax = (5000,'K'),
#     ),
#     shortDesc = """""",
#     longDesc = 
# """

# """,
# )

#Old RMG-GA
# entry(
#     index = 33,
#     label = "C2OC2KETB-A",
#     molecule = 
# """
# 1  C u0 p0 c0 {4,S} {5,S} {6,S} {10,S}
# 2  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
# 3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
# 4  C u0 p0 c0 {1,S} {14,D} {15,S}
# 5  O u0 p2 c0 {1,S} {2,S}
# 6  O u0 p2 c0 {1,S} {7,S}
# 7  O u0 p2 c0 {6,S} {16,S}
# 8  H u0 p0 c0 {2,S}
# 9  H u0 p0 c0 {2,S}
# 10 H u0 p0 c0 {1,S}
# 11 H u0 p0 c0 {3,S}
# 12 H u0 p0 c0 {3,S}
# 13 H u0 p0 c0 {3,S}
# 14 O u0 p2 c0 {4,D}
# 15 H u0 p0 c0 {4,S}
# 16 H u0 p0 c0 {7,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[2.58933,0.0647787,-4.79635e-05,1.7614e-08,-2.59245e-12,-58188.3,21.023], Tmin=(100,'K'), Tmax=(1586.06,'K')),
#             NASAPolynomial(coeffs=[18.0514,0.0257839,-1.10847e-05,2.11284e-09,-1.49101e-13,-63093.1,-60.7045], Tmin=(1586.06,'K'), Tmax=(5000,'K')),
#         ],
#         Tmin = (100,'K'),
#         Tmax = (5000,'K'),
#     ),
#     shortDesc = """""",
#     longDesc = 
# """

# """,
# )

entry(
    index = 34,
    label = "C2OC2KETB-1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {14,D} {15,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.53234,0.0348352,4.24095e-05,-8.59167e-08,3.84094e-11,-56245.2,3.40117], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.2032,0.0288905,-1.18924e-05,2.22361e-09,-1.55185e-13,-60165.2,-56.9538], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 35,
    label = "C2OC2KETB-2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {14,D} {15,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.50509,0.023924,7.14008e-05,-1.1617e-07,4.95482e-11,-51572.1,0.502916], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.8382,0.0293892,-1.21332e-05,2.27304e-09,-1.58847e-13,-55462.5,-54.7205], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

#Old RMG-GA
# entry(
#     index = 36,
#     label = "C2OC2KETA-B",
#     molecule = 
# """
# 1  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
# 2  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
# 3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
# 4  C u0 p0 c0 {2,S} {5,S} {15,D}
# 5  O u0 p2 c0 {1,S} {4,S}
# 6  O u0 p2 c0 {2,S} {7,S}
# 7  O u0 p2 c0 {6,S} {16,S}
# 8  H u0 p0 c0 {1,S}
# 9  H u0 p0 c0 {1,S}
# 10 H u0 p0 c0 {3,S}
# 11 H u0 p0 c0 {3,S}
# 12 H u0 p0 c0 {3,S}
# 13 H u0 p0 c0 {2,S}
# 14 H u0 p0 c0 {2,S}
# 15 O u0 p2 c0 {4,D}
# 16 H u0 p0 c0 {7,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[3.89023,0.053048,-2.07615e-05,-5.02853e-09,3.86356e-12,-64875.2,14.5472], Tmin=(100,'K'), Tmax=(1220.26,'K')),
#             NASAPolynomial(coeffs=[17.779,0.0261727,-1.06529e-05,1.97496e-09,-1.37546e-13,-69653.4,-60.9131], Tmin=(1220.26,'K'), Tmax=(5000,'K')),
#         ],
#         Tmin = (100,'K'),
#         Tmax = (5000,'K'),
#     ),
#     shortDesc = """""",
#     longDesc = 
# """

# """,
# )

entry(
    index = 37,
    label = "C2OC2KETA-1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {5,S} {15,D}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {4,D}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.56527,0.0429614,2.20429e-05,-6.55083e-08,3.11366e-11,-69275,6.03494], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.283,0.0285983,-1.17146e-05,2.18316e-09,-1.52013e-13,-73223.8,-58.4079], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 38,
    label = "C2OC2KETA-2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {5,S} {15,D}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {4,D}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.6088,0.0317614,5.19147e-05,-9.70357e-08,4.28705e-11,-65909.8,3.92953], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.965,0.0289795,-1.18879e-05,2.21751e-09,-1.54503e-13,-69815.9,-55.2535], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

#Old RMG-GA
# entry(
#     index = 39,
#     label = "C2OC2KETB-1R",
#     molecule = 
# """
# multiplicity 2
# 1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
# 2  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
# 3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
# 4  C u0 p0 c0 {2,S} {13,D} {14,S}
# 5  O u0 p2 c0 {1,S} {2,S}
# 6  O u1 p2 c0 {1,S}
# 7  H u0 p0 c0 {1,S}
# 8  H u0 p0 c0 {3,S}
# 9  H u0 p0 c0 {3,S}
# 10 H u0 p0 c0 {3,S}
# 11 H u0 p0 c0 {2,S}
# 12 H u0 p0 c0 {2,S}
# 13 O u0 p2 c0 {4,D}
# 14 H u0 p0 c0 {4,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[8.69292,0.0131521,4.43705e-05,-5.50585e-08,1.82899e-11,-38551.7,-5.37235], Tmin=(100,'K'), Tmax=(1097.09,'K')),
#             NASAPolynomial(coeffs=[13.541,0.0242261,-1.00791e-05,1.91544e-09,-1.36248e-13,-41345.7,-37.0962], Tmin=(1097.09,'K'), Tmax=(5000,'K')),
#         ],
#         Tmin = (100,'K'),
#         Tmax = (5000,'K'),
#     ),
#     shortDesc = """""",
#     longDesc = 
# """

# """,
# )

#Old RMG-GA
# entry(
#     index = 40,
#     label = "C2OC2KETA-1R",
#     molecule = 
# """
# multiplicity 2
# 1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
# 2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
# 3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
# 4  C u0 p0 c0 {3,S} {5,S} {14,D}
# 5  O u0 p2 c0 {1,S} {4,S}
# 6  O u1 p2 c0 {1,S}
# 7  H u0 p0 c0 {1,S}
# 8  H u0 p0 c0 {2,S}
# 9  H u0 p0 c0 {2,S}
# 10 H u0 p0 c0 {2,S}
# 11 H u0 p0 c0 {3,S}
# 12 H u0 p0 c0 {3,S}
# 13 H u0 p0 c0 {3,S}
# 14 O u0 p2 c0 {4,D}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[3.81652,0.0357054,-2.89799e-06,-1.09006e-08,3.84125e-12,-52833.4,16.4162], Tmin=(100,'K'), Tmax=(1392.71,'K')),
#             NASAPolynomial(coeffs=[14.2046,0.0240447,-9.91407e-06,1.82815e-09,-1.2565e-13,-57489.5,-43.4696], Tmin=(1392.71,'K'), Tmax=(5000,'K')),
#         ],
#         Tmin = (100,'K'),
#         Tmax = (5000,'K'),
#     ),
#     shortDesc = """""",
#     longDesc = 
# """

# """,
# )

#Old RMG-GA
# entry(
#     index = 41,
#     label = "AA",
#     molecule = 
# """
# 1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
# 2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
# 3  C u0 p0 c0 {1,S} {5,S} {12,D}
# 4  C u0 p0 c0 {2,S} {5,S} {13,D}
# 5  O u0 p2 c0 {3,S} {4,S}
# 6  H u0 p0 c0 {1,S}
# 7  H u0 p0 c0 {1,S}
# 8  H u0 p0 c0 {1,S}
# 9  H u0 p0 c0 {2,S}
# 10 H u0 p0 c0 {2,S}
# 11 H u0 p0 c0 {2,S}
# 12 O u0 p2 c0 {3,D}
# 13 O u0 p2 c0 {4,D}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[4.57833,0.029723,2.25034e-06,-1.63648e-08,6.19028e-12,-71975.5,12.9657], Tmin=(100,'K'), Tmax=(1179.35,'K')),
#             NASAPolynomial(coeffs=[11.673,0.0220124,-8.74116e-06,1.60567e-09,-1.11407e-13,-74786.1,-27.2538], Tmin=(1179.35,'K'), Tmax=(5000,'K')),
#         ],
#         Tmin = (100,'K'),
#         Tmax = (5000,'K'),
#     ),
#     shortDesc = """""",
#     longDesc = 
# """

# """,
# )

#Old RMG-GA
# entry(
#     index = 42,
#     label = "CC(O)OCCO",
#     molecule = 
# """
# 1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
# 2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
# 3  C u0 p0 c0 {2,S} {5,S} {11,D}
# 4  C u0 p0 c0 {1,S} {12,D} {13,S}
# 5  O u0 p2 c0 {1,S} {3,S}
# 6  H u0 p0 c0 {1,S}
# 7  H u0 p0 c0 {1,S}
# 8  H u0 p0 c0 {2,S}
# 9  H u0 p0 c0 {2,S}
# 10 H u0 p0 c0 {2,S}
# 11 O u0 p2 c0 {3,D}
# 12 O u0 p2 c0 {4,D}
# 13 H u0 p0 c0 {4,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[4.61312,0.023701,3.06576e-05,-4.91084e-08,1.79958e-11,-63984.1,11.9027], Tmin=(100,'K'), Tmax=(1046.33,'K')),
#             NASAPolynomial(coeffs=[11.2213,0.02554,-1.08304e-05,2.07974e-09,-1.49089e-13,-66850.5,-27.3664], Tmin=(1046.33,'K'), Tmax=(5000,'K')),
#         ],
#         Tmin = (100,'K'),
#         Tmax = (5000,'K'),
#     ),
#     shortDesc = """""",
#     longDesc = 
# """

# """,
# )

# #DFT_QCI_thermo
# # entry(
# #     index = 43,
# #     label = "HOCH2CHO",
# #     molecule = 
# # """
# # 1 O u0 p2 c0 {3,S} {8,S}
# # 2 O u0 p2 c0 {4,D}
# # 3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
# # 4 C u0 p0 c0 {2,D} {3,S} {7,S}
# # 5 H u0 p0 c0 {3,S}
# # 6 H u0 p0 c0 {3,S}
# # 7 H u0 p0 c0 {4,S}
# # 8 H u0 p0 c0 {1,S}
# # """,
# #     thermo = NASA(
# #         polynomials = [
# #             NASAPolynomial(coeffs=[2.73814,0.0141773,3.76402e-05,-6.47357e-08,2.7252e-11,-39927.4,13.6156], Tmin=(100,'K'), Tmax=(935.24,'K')),
# #             NASAPolynomial(coeffs=[12.0848,0.00651697,-1.90276e-06,3.96704e-10,-3.42954e-14,-43089,-38.4068], Tmin=(935.24,'K'), Tmax=(5000,'K')),
# #         ],
# #         Tmin = (100,'K'),
# #         Tmax = (5000,'K'),
# #     ),
# #     shortDesc = """""",
# #     longDesc = 
# # """

# # """,
# # )

#Old GA thermo
# entry(
#     index = 44,
#     label = "C4O-BO2H-AO2H1O2",
#     molecule = 
# """
# multiplicity 2
# 1  C u0 p0 c0 {3,S} {5,S} {6,S} {12,S}
# 2  C u0 p0 c0 {4,S} {5,S} {8,S} {11,S}
# 3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
# 4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
# 5  O u0 p2 c0 {1,S} {2,S}
# 6  O u0 p2 c0 {1,S} {10,S}
# 7  O u0 p2 c0 {3,S} {9,S}
# 8  O u0 p2 c0 {2,S} {18,S}
# 9  O u0 p2 c0 {7,S} {19,S}
# 10 O u0 p2 c0 {6,S} {20,S}
# 11 H u0 p0 c0 {2,S}
# 12 H u0 p0 c0 {1,S}
# 13 H u0 p0 c0 {3,S}
# 14 H u0 p0 c0 {3,S}
# 15 H u0 p0 c0 {4,S}
# 16 H u0 p0 c0 {4,S}
# 17 H u0 p0 c0 {4,S}
# 18 O u1 p2 c0 {8,S}
# 19 H u0 p0 c0 {9,S}
# 20 H u0 p0 c0 {10,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[-2.10974,0.142417,-0.00021231,1.72887e-07,-5.61494e-11,-55951.4,43.8371], Tmin=(100,'K'), Tmax=(869.24,'K')),
#             NASAPolynomial(coeffs=[12.2942,0.0560763,-2.87035e-05,5.52341e-09,-3.79385e-13,-57697.7,-19.2762], Tmin=(869.24,'K'), Tmax=(5000,'K')),
#         ],
#         Tmin = (100,'K'),
#         Tmax = (5000,'K'),
#     ),
#     shortDesc = """""",
#     longDesc = 
# """

# """,
# )

# entry(
#     index = 45,
#     label = "C4O-BO2H-1O2HAO2",
#     molecule = 
# """
# multiplicity 2
# 1  C u0 p0 c0 {4,S} {5,S} {6,S} {11,S}
# 2  C u0 p0 c0 {3,S} {5,S} {8,S} {12,S}
# 3  C u0 p0 c0 {2,S} {7,S} {13,S} {14,S}
# 4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
# 5  O u0 p2 c0 {1,S} {2,S}
# 6  O u0 p2 c0 {1,S} {9,S}
# 7  O u0 p2 c0 {3,S} {10,S}
# 8  O u0 p2 c0 {2,S} {18,S}
# 9  O u0 p2 c0 {6,S} {19,S}
# 10 O u0 p2 c0 {7,S} {20,S}
# 11 H u0 p0 c0 {1,S}
# 12 H u0 p0 c0 {2,S}
# 13 H u0 p0 c0 {3,S}
# 14 H u0 p0 c0 {3,S}
# 15 H u0 p0 c0 {4,S}
# 16 H u0 p0 c0 {4,S}
# 17 H u0 p0 c0 {4,S}
# 18 O u1 p2 c0 {8,S}
# 19 H u0 p0 c0 {9,S}
# 20 H u0 p0 c0 {10,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[-2.10974,0.142417,-0.00021231,1.72887e-07,-5.61494e-11,-55951.4,43.8371], Tmin=(100,'K'), Tmax=(869.24,'K')),
#             NASAPolynomial(coeffs=[12.2942,0.0560763,-2.87035e-05,5.52341e-09,-3.79385e-13,-57697.7,-19.2762], Tmin=(869.24,'K'), Tmax=(5000,'K')),
#         ],
#         Tmin = (100,'K'),
#         Tmax = (5000,'K'),
#     ),
#     shortDesc = """""",
#     longDesc = 
# """

# """,
# )

# entry(
#     index = 46,
#     label = "C4O-BO2H-2O2HAO2",
#     molecule = 
# """
# multiplicity 2
# 1  C u0 p0 c0 {3,S} {5,S} {8,S} {11,S}
# 2  C u0 p0 c0 {4,S} {5,S} {14,S} {15,S}
# 3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
# 4  C u0 p0 c0 {2,S} {7,S} {16,S} {17,S}
# 5  O u0 p2 c0 {1,S} {2,S}
# 6  O u0 p2 c0 {3,S} {9,S}
# 7  O u0 p2 c0 {4,S} {10,S}
# 8  O u0 p2 c0 {1,S} {18,S}
# 9  O u0 p2 c0 {6,S} {19,S}
# 10 O u0 p2 c0 {7,S} {20,S}
# 11 H u0 p0 c0 {1,S}
# 12 H u0 p0 c0 {3,S}
# 13 H u0 p0 c0 {3,S}
# 14 H u0 p0 c0 {2,S}
# 15 H u0 p0 c0 {2,S}
# 16 H u0 p0 c0 {4,S}
# 17 H u0 p0 c0 {4,S}
# 18 O u1 p2 c0 {8,S}
# 19 H u0 p0 c0 {9,S}
# 20 H u0 p0 c0 {10,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[-1.34537,0.144273,-0.000231557,2.06441e-07,-7.4026e-11,-51215.9,40.4493], Tmin=(100,'K'), Tmax=(683.34,'K')),
#             NASAPolynomial(coeffs=[14.7162,0.0502582,-2.5192e-05,5.11842e-09,-3.74636e-13,-53411.1,-30.9236], Tmin=(683.34,'K'), Tmax=(5000,'K')),
#         ],
#         Tmin = (100,'K'),
#         Tmax = (5000,'K'),
#     ),
#     shortDesc = """""",
#     longDesc = 
# """

# """,
# )

# entry(
#     index = 47,
#     label = "C4O-AO2H-1O2HBO2",
#     molecule = 
# """
# multiplicity 2
# 1  C u0 p0 c0 {3,S} {5,S} {7,S} {12,S}
# 2  C u0 p0 c0 {4,S} {5,S} {6,S} {11,S}
# 3  C u0 p0 c0 {1,S} {8,S} {13,S} {14,S}
# 4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
# 5  O u0 p2 c0 {1,S} {2,S}
# 6  O u0 p2 c0 {2,S} {9,S}
# 7  O u0 p2 c0 {1,S} {10,S}
# 8  O u0 p2 c0 {3,S} {18,S}
# 9  O u0 p2 c0 {6,S} {19,S}
# 10 O u0 p2 c0 {7,S} {20,S}
# 11 H u0 p0 c0 {2,S}
# 12 H u0 p0 c0 {1,S}
# 13 H u0 p0 c0 {3,S}
# 14 H u0 p0 c0 {3,S}
# 15 H u0 p0 c0 {4,S}
# 16 H u0 p0 c0 {4,S}
# 17 H u0 p0 c0 {4,S}
# 18 O u1 p2 c0 {8,S}
# 19 H u0 p0 c0 {9,S}
# 20 H u0 p0 c0 {10,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[-2.10974,0.142417,-0.00021231,1.72887e-07,-5.61494e-11,-55951.4,43.8371], Tmin=(100,'K'), Tmax=(869.24,'K')),
#             NASAPolynomial(coeffs=[12.2942,0.0560763,-2.87035e-05,5.52341e-09,-3.79385e-13,-57697.7,-19.2762], Tmin=(869.24,'K'), Tmax=(5000,'K')),
#         ],
#         Tmin = (100,'K'),
#         Tmax = (5000,'K'),
#     ),
#     shortDesc = """""",
#     longDesc = 
# """

# """,
# )

# entry(
#     index = 48,
#     label = "C2OC2KETA-B-1",
#     molecule = 
# """
# 1  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
# 2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
# 3  C u0 p0 c0 {4,S} {7,S} {14,S} {15,S}
# 4  C u0 p0 c0 {3,S} {5,S} {16,D}
# 5  O u0 p2 c0 {1,S} {4,S}
# 6  O u0 p2 c0 {1,S} {8,S}
# 7  O u0 p2 c0 {3,S} {9,S}
# 8  O u0 p2 c0 {6,S} {17,S}
# 9  O u0 p2 c0 {7,S} {18,S}
# 10 H u0 p0 c0 {1,S}
# 11 H u0 p0 c0 {2,S}
# 12 H u0 p0 c0 {2,S}
# 13 H u0 p0 c0 {2,S}
# 14 H u0 p0 c0 {3,S}
# 15 H u0 p0 c0 {3,S}
# 16 O u0 p2 c0 {4,D}
# 17 H u0 p0 c0 {8,S}
# 18 H u0 p0 c0 {9,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[0.640001,0.0927448,-8.4892e-05,3.98268e-08,-7.6439e-12,-80032.5,31.4089], Tmin=(100,'K'), Tmax=(1222.95,'K')),
#             NASAPolynomial(coeffs=[17.1189,0.0388461,-1.87833e-05,3.78915e-09,-2.76983e-13,-84063.1,-51.4091], Tmin=(1222.95,'K'), Tmax=(5000,'K')),
#         ],
#         Tmin = (100,'K'),
#         Tmax = (5000,'K'),
#     ),
#     shortDesc = """""",
#     longDesc = 
# """

# """,
# )

# entry(
#     index = 49,
#     label = "C2OC2KET1-A-B",
#     molecule = 
# """
# 1  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
# 2  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
# 3  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
# 4  C u0 p0 c0 {3,S} {5,S} {16,D}
# 5  O u0 p2 c0 {1,S} {4,S}
# 6  O u0 p2 c0 {1,S} {9,S}
# 7  O u0 p2 c0 {2,S} {8,S}
# 8  O u0 p2 c0 {7,S} {17,S}
# 9  O u0 p2 c0 {6,S} {18,S}
# 10 H u0 p0 c0 {1,S}
# 11 H u0 p0 c0 {2,S}
# 12 H u0 p0 c0 {2,S}
# 13 H u0 p0 c0 {3,S}
# 14 H u0 p0 c0 {3,S}
# 15 H u0 p0 c0 {3,S}
# 16 O u0 p2 c0 {4,D}
# 17 H u0 p0 c0 {8,S}
# 18 H u0 p0 c0 {9,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[0.116497,0.0970374,-0.000101211,5.90396e-08,-1.46457e-11,-81728.6,34.4021], Tmin=(100,'K'), Tmax=(947.43,'K')),
#             NASAPolynomial(coeffs=[11.6328,0.0484167,-2.42344e-05,4.87458e-09,-3.53256e-13,-83910.7,-20.5355], Tmin=(947.43,'K'), Tmax=(5000,'K')),
#         ],
#         Tmin = (100,'K'),
#         Tmax = (5000,'K'),
#     ),
#     shortDesc = """""",
#     longDesc = 
# """

# """,
# )

# entry(
#     index = 50,
#     label = "C2OC2KET2-A-B",
#     molecule = 
# """
# 1  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
# 2  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
# 3  C u0 p0 c0 {4,S} {5,S} {13,S} {14,S}
# 4  C u0 p0 c0 {3,S} {15,D} {16,S}
# 5  O u0 p2 c0 {1,S} {3,S}
# 6  O u0 p2 c0 {1,S} {9,S}
# 7  O u0 p2 c0 {2,S} {8,S}
# 8  O u0 p2 c0 {7,S} {17,S}
# 9  O u0 p2 c0 {6,S} {18,S}
# 10 H u0 p0 c0 {1,S}
# 11 H u0 p0 c0 {2,S}
# 12 H u0 p0 c0 {2,S}
# 13 H u0 p0 c0 {3,S}
# 14 H u0 p0 c0 {3,S}
# 15 O u0 p2 c0 {4,D}
# 16 H u0 p0 c0 {4,S}
# 17 H u0 p0 c0 {8,S}
# 18 H u0 p0 c0 {9,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[2.77308,0.0881617,-8.2014e-05,3.85243e-08,-7.24714e-12,-67188.4,22.2358], Tmin=(100,'K'), Tmax=(1266.5,'K')),
#             NASAPolynomial(coeffs=[20.8677,0.0310132,-1.43292e-05,2.89603e-09,-2.14327e-13,-71771.8,-69.3354], Tmin=(1266.5,'K'), Tmax=(5000,'K')),
#         ],
#         Tmin = (100,'K'),
#         Tmax = (5000,'K'),
#     ),
#     shortDesc = """""",
#     longDesc = 
# """

# """,
# )

# entry(
#     index = 51,
#     label = "R52C3H7OE",
#     molecule = 
# """
# multiplicity 2
# 1  O u0 p2 c0 {2,S} {4,S}
# 2  C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
# 3  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
# 4  C u1 p0 c0 {1,S} {10,S} {11,S}
# 5  H u0 p0 c0 {2,S}
# 6  H u0 p0 c0 {2,S}
# 7  H u0 p0 c0 {3,S}
# 8  H u0 p0 c0 {3,S}
# 9  H u0 p0 c0 {3,S}
# 10 H u0 p0 c0 {4,S}
# 11 H u0 p0 c0 {4,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[0.0382329,0.047239,-4.3643e-05,2.46455e-08,-6.21955e-12,-5764.4,25.6299], Tmin=(298,'K'), Tmax=(1000,'K')),
#             NASAPolynomial(coeffs=[12.2369,0.0126899,-3.27163e-06,4.28168e-10,-2.30448e-14,-9330.54,-37.7485], Tmin=(1000,'K'), Tmax=(5000,'K')),
#         ],
#         Tmin = (298,'K'),
#         Tmax = (5000,'K'),
#     ),
#     shortDesc = """""",
#     longDesc = 
# """

# """,
# )

# entry(
#     index = 52,
#     label = "R51C4H7OEZ",
#     molecule = 
# """
# multiplicity 2
# 1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
# 2  C u0 p0 c0 {4,D} {5,S} {10,S}
# 3  C u1 p0 c0 {1,S} {8,S} {9,S}
# 4  C u0 p0 c0 {2,D} {11,S} {12,S}
# 5  O u0 p2 c0 {1,S} {2,S}
# 6  H u0 p0 c0 {1,S}
# 7  H u0 p0 c0 {1,S}
# 8  H u0 p0 c0 {3,S}
# 9  H u0 p0 c0 {3,S}
# 10 H u0 p0 c0 {2,S}
# 11 H u0 p0 c0 {4,S}
# 12 H u0 p0 c0 {4,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[1.44055,0.0515995,-4.85361e-05,2.60794e-08,-5.95189e-12,6617.96,19.8896], Tmin=(298,'K'), Tmax=(1000,'K')),
#             NASAPolynomial(coeffs=[12.0364,0.0181214,-6.54034e-06,1.08215e-09,-6.80587e-14,3835.19,-33.9618], Tmin=(1000,'K'), Tmax=(5000,'K')),
#         ],
#         Tmin = (298,'K'),
#         Tmax = (5000,'K'),
#     ),
#     shortDesc = """""",
#     longDesc = 
# """

# """,
# )

# entry(
#     index = 53,
#     label = "R56C4H7OEV",
#     molecule = 
# """
# multiplicity 2
# 1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
# 2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
# 3  C u0 p0 c0 {5,D} {11,S} {12,S}
# 4  O u0 p2 c0 {1,S} {5,S}
# 5  C u1 p0 c0 {3,D} {4,S}
# 6  H u0 p0 c0 {1,S}
# 7  H u0 p0 c0 {1,S}
# 8  H u0 p0 c0 {2,S}
# 9  H u0 p0 c0 {2,S}
# 10 H u0 p0 c0 {2,S}
# 11 H u0 p0 c0 {3,S}
# 12 H u0 p0 c0 {3,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[3.31922,0.0279385,1.53516e-06,-1.62886e-08,7.04884e-12,9176.63,15.9778], Tmin=(298,'K'), Tmax=(1000,'K')),
#             NASAPolynomial(coeffs=[11.4901,0.0157807,-4.26332e-06,5.77408e-10,-3.18182e-14,6217.1,-29.2593], Tmin=(1000,'K'), Tmax=(5000,'K')),
#         ],
#         Tmin = (298,'K'),
#         Tmax = (5000,'K'),
#     ),
#     shortDesc = """""",
#     longDesc = 
# """

# """,
# )

# entry(
#     index = 54,
#     label = "R57C4H7OEV",
#     molecule = 
# """
# multiplicity 2
# 1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
# 2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
# 3  C u0 p0 c0 {4,S} {5,D} {11,S}
# 4  O u0 p2 c0 {1,S} {3,S}
# 5  C u1 p0 c0 {3,D} {12,S}
# 6  H u0 p0 c0 {1,S}
# 7  H u0 p0 c0 {1,S}
# 8  H u0 p0 c0 {2,S}
# 9  H u0 p0 c0 {2,S}
# 10 H u0 p0 c0 {2,S}
# 11 H u0 p0 c0 {3,S}
# 12 H u0 p0 c0 {5,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[2.5366,0.0332151,-7.47016e-06,-9.52643e-09,5.05819e-12,10349.7,18.7652], Tmin=(298,'K'), Tmax=(1000,'K')),
#             NASAPolynomial(coeffs=[12.1479,0.0152258,-4.07863e-06,5.48253e-10,-3.00157e-14,7101.49,-33.4201], Tmin=(1000,'K'), Tmax=(5000,'K')),
#         ],
#         Tmin = (298,'K'),
#         Tmax = (5000,'K'),
#     ),
#     shortDesc = """""",
#     longDesc = 
# """

# """,
# )

# entry(
#     index = 55,
#     label = "R61C4H7OEZ",
#     molecule = 
# """
# multiplicity 2
# 1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
# 2  C u1 p0 c0 {1,S} {5,S} {9,S}
# 3  C u0 p0 c0 {4,D} {5,S} {10,S}
# 4  C u0 p0 c0 {3,D} {11,S} {12,S}
# 5  O u0 p2 c0 {2,S} {3,S}
# 6  H u0 p0 c0 {1,S}
# 7  H u0 p0 c0 {1,S}
# 8  H u0 p0 c0 {1,S}
# 9  H u0 p0 c0 {2,S}
# 10 H u0 p0 c0 {3,S}
# 11 H u0 p0 c0 {4,S}
# 12 H u0 p0 c0 {4,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[1.59022,0.0426493,-3.40927e-05,1.98071e-08,-6.2399e-12,2494.53,22.8731], Tmin=(298,'K'), Tmax=(1000,'K')),
#             NASAPolynomial(coeffs=[20.3573,0.00374311,-4.13115e-07,2.76985e-11,-9.46798e-16,-4348.91,-79.6654], Tmin=(1000,'K'), Tmax=(5000,'K')),
#         ],
#         Tmin = (298,'K'),
#         Tmax = (5000,'K'),
#     ),
#     shortDesc = """""",
#     longDesc = 
# """

# """,
# )

# entry(
#     index = 56,
#     label = "R62C3H5OEZ",
#     molecule = 
# """
# multiplicity 2
# 1 O u0 p2 c0 {2,S} {4,S}
# 2 C u0 p0 c0 {1,S} {3,D} {5,S}
# 3 C u0 p0 c0 {2,D} {6,S} {7,S}
# 4 C u1 p0 c0 {1,S} {8,S} {9,S}
# 5 H u0 p0 c0 {2,S}
# 6 H u0 p0 c0 {3,S}
# 7 H u0 p0 c0 {3,S}
# 8 H u0 p0 c0 {4,S}
# 9 H u0 p0 c0 {4,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[2.88859,0.0263851,-1.77342e-05,8.99495e-09,-2.72453e-12,7332.93,14.371], Tmin=(298,'K'), Tmax=(1000,'K')),
#             NASAPolynomial(coeffs=[10.632,0.00907738,-2.15301e-06,2.67527e-10,-1.40384e-14,4689.39,-27.37], Tmin=(1000,'K'), Tmax=(5000,'K')),
#         ],
#         Tmin = (298,'K'),
#         Tmax = (5000,'K'),
#     ),
#     shortDesc = """""",
#     longDesc = 
# """

# """,
# )

# entry(
#     index = 57,
#     label = "HO2CH2CHO",
#     molecule = 
# """
# 1 O u0 p2 c0 {2,S} {4,S}
# 2 O u0 p2 c0 {1,S} {9,S}
# 3 O u0 p2 c0 {5,D}
# 4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
# 5 C u0 p0 c0 {3,D} {4,S} {8,S}
# 6 H u0 p0 c0 {4,S}
# 7 H u0 p0 c0 {4,S}
# 8 H u0 p0 c0 {5,S}
# 9 H u0 p0 c0 {2,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[4.98086,0.0217447,-8.71608e-06,2.8968e-10,3.89597e-13,-32033.1,7.08712], Tmin=(298,'K'), Tmax=(1363,'K')),
#             NASAPolynomial(coeffs=[12.0205,0.0101453,-3.59186e-06,5.70656e-10,-3.36439e-14,-35022.9,-32.5428], Tmin=(1363,'K'), Tmax=(5000,'K')),
#         ],
#         Tmin = (298,'K'),
#         Tmax = (5000,'K'),
#     ),
#     shortDesc = """""",
#     longDesc = 
# """

# """,
# )

