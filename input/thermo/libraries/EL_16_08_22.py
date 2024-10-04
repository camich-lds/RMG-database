#!/usr/bin/env python
# encoding: utf-8

name = "EL_16_08_22"
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
    label = "N2",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53604,-0.000158271,-4.26984e-07,2.37543e-09,-1.39708e-12,-1047.5,2.94604], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.93803,0.00141838,-5.03281e-07,8.07555e-11,-4.76064e-15,-917.181,5.95522], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1,
    label = "Ar",
    molecule = 
"""
1 Ar u0 p4 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.49989,2.13038e-07,8.97321e-10,-2.31396e-12,1.30201e-15,-745.354,4.38024], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.49989,1.56135e-07,-7.76109e-11,1.52928e-14,-1.05304e-18,-745.328,4.3803], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2,
    label = "He",
    molecule = 
"""
1 He u0 p1 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.49976,1.01013e-06,-8.24578e-10,-6.85983e-13,7.24752e-16,-745.341,0.9298], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.49986,2.19365e-07,-1.07525e-10,2.07198e-14,-1.39359e-18,-745.309,0.929535], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 3,
    label = "Ne",
    molecule = 
"""
1 Ne u0 p4 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,3.35532], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,3.35532], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 4,
    label = "EL",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {1,S} {5,S} {21,D}
7  C u0 p0 c0 {2,S} {8,S} {22,D}
8  O u0 p2 c0 {3,S} {7,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.53081,0.105509,-8.6119e-05,3.63624e-08,-6.21948e-12,-77731,52.259], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[26.0991,0.0299571,-1.09381e-05,1.86434e-09,-1.16732e-13,-87370.1,-104.598], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 5,
    label = "O2",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78498,-0.00302002,9.92029e-06,-9.7784e-09,3.28878e-12,-1064.14,3.64781], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.6598,0.000659877,-1.44158e-07,2.14656e-11,-1.36504e-15,-1216.03,3.42074], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 6,
    label = "OH",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97585,-0.00228555,4.33443e-06,-3.59927e-09,1.26707e-12,3393.41,-0.0355397], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.84582,0.00109724,-2.89121e-07,4.091e-11,-2.31382e-15,3717.07,5.8034], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 7,
    label = "O",
    molecule = 
"""
multiplicity 3
1 O u2 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.15907,-0.0032151,6.49256e-06,-5.98755e-09,2.06876e-12,29129.8,2.09078], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5516,-3.83085e-05,8.43197e-10,4.01267e-12,-4.17477e-16,29228.8,4.87617], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 8,
    label = "H",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.49976,6.73824e-07,1.11807e-09,-3.70192e-12,2.14234e-15,25473.8,-0.445574], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.49985,2.34583e-07,-1.16172e-10,2.25708e-14,-1.52992e-18,25473.8,-0.445865], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 9,
    label = "H2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.37694,0.00773917,-1.88735e-05,1.95517e-08,-7.17096e-12,-921.173,0.547185], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.90208,0.000868993,-1.65864e-07,1.90852e-11,-9.31122e-16,-797.949,-0.845591], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 10,
    label = "HO2",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.26251,-0.00445642,2.05165e-05,-2.35794e-08,9.05614e-12,262.442,3.88224], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.10564,0.00204047,-3.65878e-07,1.85973e-11,4.98818e-16,43.2899,3.30808], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 11,
    label = "H2O2",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.23854,-0.000249611,1.59858e-05,-2.0692e-08,8.29766e-12,-17648.6,3.5885], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.54017,0.00415971,-1.30877e-06,2.00824e-10,-1.15509e-14,-17951.4,0.855882], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 12,
    label = "CH3",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61264,0.00309209,9.25475e-07,-1.65777e-09,6.07244e-13,16385,1.79995], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.92198,0.00537479,-1.99748e-06,2.97585e-10,-1.7186e-14,16544.7,5.25397], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 13,
    label = "CH3O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71623,-0.00283501,3.77227e-05,-4.73648e-08,1.86739e-11,1358.74,6.55373], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.75205,0.00744944,-2.70076e-06,4.38793e-10,-2.64006e-14,444.371,-1.93362], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 14,
    label = "CH3O2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.93065,0.00868504,8.80315e-06,-1.39561e-08,5.0294e-12,227.483,12.8755], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.88425,0.0140068,-6.88364e-06,1.6379e-09,-1.53129e-13,-20.0433,11.8153], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 15,
    label = "C2H5O2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 O u0 p2 c0 {1,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 O u1 p2 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.50099,0.00687965,4.74144e-05,-6.92287e-08,2.87395e-11,-5395.48,7.9149], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.88872,0.0135833,-4.91117e-06,7.92343e-10,-4.73526e-14,-7441.07,-19.079], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 16,
    label = "C2H5",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.11105,-0.00263844,4.60475e-05,-5.64273e-08,2.19028e-11,13001.4,4.99418], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.41717,0.0122704,-4.34558e-06,6.94963e-10,-4.13531e-14,12146.8,-0.387435], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 17,
    label = "C2H3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u1 p0 c0 {1,D} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.12502,0.00235137,2.36803e-05,-3.35092e-08,1.39444e-11,34524.3,8.81538], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.37211,0.00746869,-2.64716e-06,4.22753e-10,-2.44958e-14,33805.2,0.428772], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 18,
    label = "CH3CO3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,D}
3 O u0 p2 c0 {2,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 O u1 p2 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.12838,0.0294919,-2.00221e-05,5.32494e-09,3.03452e-14,-21203.4,18.0452], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.76604,0.0188598,-9.95181e-06,2.52994e-09,-2.50541e-13,-22126.8,-0.48408], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 19,
    label = "O2CHO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
5 O u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1187,0.0145188,-1.85498e-07,-1.2253e-08,6.08124e-12,-14223.7,11.3178], Tmin=(100,'K'), Tmax=(990.68,'K')),
            NASAPolynomial(coeffs=[8.5215,0.00409726,-1.65616e-06,3.44817e-10,-2.71425e-14,-15853.2,-17.5187], Tmin=(990.68,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 20,
    label = "C2H5O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 O u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.26906,0.00933563,2.96317e-05,-4.53411e-08,1.88796e-11,-2950.23,10.4201], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.55054,0.0132526,-4.74726e-06,7.64699e-10,-4.57008e-14,-4471.92,-9.61231], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 21,
    label = "EL1J",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {7,S} {18,D}
6  C u0 p0 c0 {2,S} {8,S} {19,D}
7  C u1 p0 c0 {5,S} {20,S} {21,S}
8  O u0 p2 c0 {3,S} {6,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {6,D}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.10711,0.104659,-8.88695e-05,3.84436e-08,-6.68274e-12,-56712.1,51.6978], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[25.6125,0.029058,-1.14163e-05,2.05368e-09,-1.3277e-13,-65771.3,-99.4226], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 22,
    label = "EL3J",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {7,S} {11,S} {12,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
5  C u1 p0 c0 {1,S} {6,S} {20,S}
6  C u0 p0 c0 {4,S} {5,S} {19,D}
7  C u0 p0 c0 {1,S} {8,S} {21,D}
8  O u0 p2 c0 {2,S} {7,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {6,D}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.53376,0.102198,-8.45358e-05,3.59899e-08,-6.18961e-12,-58471.9,51.6205], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[25.0156,0.0286974,-1.07282e-05,1.86415e-09,-1.18162e-13,-67676.2,-99.2456], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 23,
    label = "EL4J",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {11,S} {12,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {4,S} {19,D}
6  C u1 p0 c0 {1,S} {7,S} {20,S}
7  C u0 p0 c0 {6,S} {8,S} {21,D}
8  O u0 p2 c0 {2,S} {7,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {5,D}
20 H u0 p0 c0 {6,S}
21 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.57328,0.106131,-8.97042e-05,3.87046e-08,-6.71428e-12,-57336.2,52.3946], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[26.3217,0.0282819,-1.07074e-05,1.86592e-09,-1.18112e-13,-66867.9,-105.239], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 24,
    label = "EL6J",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
4  C u0 p0 c0 {7,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {3,S} {19,D}
6  C u0 p0 c0 {2,S} {8,S} {20,D}
7  C u1 p0 c0 {4,S} {8,S} {21,S}
8  O u0 p2 c0 {6,S} {7,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 O u0 p2 c0 {5,D}
20 O u0 p2 c0 {6,D}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.07291,0.113374,-0.000104917,4.97538e-08,-9.27668e-12,-55633.9,54.657], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[26.0058,0.0268924,-8.68913e-06,1.29807e-09,-7.33156e-14,-64371.6,-100.987], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 25,
    label = "EL7J",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {7,S} {8,S} {13,S} {14,S}
4  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {4,S} {18,D}
6  C u0 p0 c0 {2,S} {8,S} {19,D}
7  C u1 p0 c0 {3,S} {20,S} {21,S}
8  O u0 p2 c0 {3,S} {6,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {6,D}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.91425,0.101326,-8.40727e-05,3.5859e-08,-6.175e-12,-53236.7,52.7753], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[25.244,0.0285844,-1.07974e-05,1.89268e-09,-1.20648e-13,-62285.3,-95.9283], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 26,
    label = "EL1OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {8,S} {14,S} {15,S}
4  C u0 p0 c0 {6,S} {9,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {4,S} {21,D}
7  C u0 p0 c0 {2,S} {8,S} {22,D}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {4,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 O u1 p2 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.105067,0.106923,-2.79818e-05,-2.09955e-07,2.40535e-10,-68689.9,38.9584], Tmin=(100,'K'), Tmax=(441.42,'K')),
            NASAPolynomial(coeffs=[8.95545,0.0674995,-3.25762e-05,6.25031e-09,-4.33078e-13,-69868.5,-1.00194], Tmin=(441.42,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 27,
    label = "EL3OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {1,S} {5,S} {21,D}
7  C u0 p0 c0 {2,S} {8,S} {22,D}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {1,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 O u1 p2 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.708427,0.112355,-0.00010812,6.09629e-08,-1.49957e-11,-71607.5,44.3015], Tmin=(100,'K'), Tmax=(944.72,'K')),
            NASAPolynomial(coeffs=[10.9038,0.0631881,-3.00543e-05,5.87364e-09,-4.17506e-13,-73801.6,-11.0606], Tmin=(944.72,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 28,
    label = "EL4OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {2,S} {5,S} {21,D}
7  C u0 p0 c0 {1,S} {8,S} {22,D}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {1,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 O u1 p2 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.708427,0.112355,-0.00010812,6.09629e-08,-1.49957e-11,-71607.5,44.3015], Tmin=(100,'K'), Tmax=(944.72,'K')),
            NASAPolynomial(coeffs=[10.9038,0.0631881,-3.00543e-05,5.87364e-09,-4.17506e-13,-73801.6,-11.0606], Tmin=(944.72,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 29,
    label = "EL6OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {1,S} {5,S} {21,D}
7  C u0 p0 c0 {2,S} {8,S} {22,D}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {3,S} {23,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 O u1 p2 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.40708,0.130414,-0.000178765,1.54651e-07,-5.59056e-11,-75236.2,45.1241], Tmin=(100,'K'), Tmax=(768.73,'K')),
            NASAPolynomial(coeffs=[7.77279,0.0694022,-3.38683e-05,6.57794e-09,-4.61125e-13,-76256.2,5.79663], Tmin=(768.73,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 30,
    label = "EL7OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {8,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {9,S} {14,S} {15,S}
5  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {1,S} {5,S} {21,D}
7  C u0 p0 c0 {2,S} {8,S} {22,D}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {4,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 O u1 p2 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.56546,0.136532,-0.00020169,1.8192e-07,-6.61605e-11,-70373.7,45.2338], Tmin=(100,'K'), Tmax=(810.89,'K')),
            NASAPolynomial(coeffs=[6.68091,0.0709928,-3.44638e-05,6.62537e-09,-4.59574e-13,-70893.7,12.2184], Tmin=(810.89,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 31,
    label = "EL34D",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {5,S} {17,D}
5  C u0 p0 c0 {4,S} {6,D} {19,S}
6  C u0 p0 c0 {5,D} {7,S} {18,S}
7  C u0 p0 c0 {6,S} {8,S} {20,D}
8  O u0 p2 c0 {1,S} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 O u0 p2 c0 {4,D}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.585914,0.0839093,-0.000109624,1.02387e-07,-4.09839e-11,-57150.5,32.9376], Tmin=(100,'K'), Tmax=(744.27,'K')),
            NASAPolynomial(coeffs=[3.11263,0.056993,-2.84985e-05,5.64428e-09,-4.01209e-13,-57157.2,23.9755], Tmin=(744.27,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 32,
    label = "EL67D",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {3,S} {16,D}
5  C u0 p0 c0 {2,S} {8,S} {17,D}
6  C u0 p0 c0 {7,D} {8,S} {18,S}
7  C u0 p0 c0 {6,D} {19,S} {20,S}
8  O u0 p2 c0 {5,S} {6,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u0 p2 c0 {4,D}
17 O u0 p2 c0 {5,D}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.213351,0.0990172,-9.7804e-05,5.50609e-08,-1.32103e-11,-64432.1,33.7811], Tmin=(100,'K'), Tmax=(979.09,'K')),
            NASAPolynomial(coeffs=[11.6263,0.0506467,-2.36984e-05,4.60177e-09,-3.26038e-13,-66750.5,-23.0883], Tmin=(979.09,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 33,
    label = "EL1OOH3J",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {7,S} {13,S} {14,S}
2  C u0 p0 c0 {4,S} {8,S} {11,S} {12,S}
3  C u0 p0 c0 {6,S} {9,S} {18,S} {19,S}
4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {6,D} {21,S}
6  C u0 p0 c0 {3,S} {5,D} {20,S}
7  C u0 p0 c0 {1,S} {8,S} {22,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {3,S} {10,S}
10 O u0 p2 c0 {9,S} {23,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 O u1 p2 c0 {6,S}
21 H u0 p0 c0 {5,S}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.766409,0.110866,-9.179e-05,3.93391e-08,-7.10057e-12,-68765.5,42.4301], Tmin=(100,'K'), Tmax=(1262.83,'K')),
            NASAPolynomial(coeffs=[16.3113,0.0567734,-2.75385e-05,5.42012e-09,-3.85744e-13,-73078.8,-43.9451], Tmin=(1262.83,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 34,
    label = "EL3OOH1J",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {8,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {7,D} {19,S}
6  C u0 p0 c0 {2,S} {8,S} {20,D}
7  C u0 p0 c0 {5,D} {21,S} {22,S}
8  O u0 p2 c0 {3,S} {6,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {23,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u1 p2 c0 {5,S}
20 O u0 p2 c0 {6,D}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.38057,0.12384,-0.000125635,6.95368e-08,-1.59781e-11,-70379.1,45.0498], Tmin=(100,'K'), Tmax=(1033.25,'K')),
            NASAPolynomial(coeffs=[16.4324,0.0548818,-2.55266e-05,4.94646e-09,-3.50248e-13,-74060.2,-41.4704], Tmin=(1033.25,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 35,
    label = "EL3OOH4J",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {9,S} {11,S}
2  C u0 p0 c0 {3,S} {8,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {4,S} {20,D}
6  C u1 p0 c0 {1,S} {7,S} {21,S}
7  C u0 p0 c0 {6,S} {8,S} {22,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {23,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {5,D}
21 H u0 p0 c0 {6,S}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.911449,0.115128,-0.00010243,4.89971e-08,-9.95118e-12,-68961.6,44.3036], Tmin=(100,'K'), Tmax=(1135.73,'K')),
            NASAPolynomial(coeffs=[14.9809,0.0591562,-2.85063e-05,5.60412e-09,-3.99418e-13,-72571.5,-34.3903], Tmin=(1135.73,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 36,
    label = "EL4OOH3J",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {7,S} {9,S} {11,S}
2  C u0 p0 c0 {3,S} {8,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {6,D} {21,S}
6  C u0 p0 c0 {4,S} {5,D} {20,S}
7  C u0 p0 c0 {1,S} {8,S} {22,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {23,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u1 p2 c0 {6,S}
21 H u0 p0 c0 {5,S}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.28113,0.117859,-0.000108723,5.32148e-08,-1.07522e-11,-71637.1,45.12], Tmin=(100,'K'), Tmax=(1166.92,'K')),
            NASAPolynomial(coeffs=[18.0676,0.0515362,-2.347e-05,4.51013e-09,-3.17859e-13,-76152.8,-51.2137], Tmin=(1166.92,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 37,
    label = "EL6OOH7J",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {7,S} {8,S} {9,S} {15,S}
4  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {4,S} {19,D}
6  C u0 p0 c0 {2,S} {8,S} {20,D}
7  C u1 p0 c0 {3,S} {21,S} {22,S}
8  O u0 p2 c0 {3,S} {6,S}
9  O u0 p2 c0 {3,S} {10,S}
10 O u0 p2 c0 {9,S} {23,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {5,D}
20 O u0 p2 c0 {6,D}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.769386,0.121812,-0.000112226,8.79764e-09,4.58326e-11,-67813,44.2623], Tmin=(100,'K'), Tmax=(520.01,'K')),
            NASAPolynomial(coeffs=[9.69261,0.0679661,-3.3718e-05,6.62746e-09,-4.69322e-13,-69261.1,-2.83151], Tmin=(520.01,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 38,
    label = "EL7OOH6J",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {7,S} {9,S} {15,S} {16,S}
4  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {4,S} {20,D}
6  C u0 p0 c0 {2,S} {8,S} {21,D}
7  C u1 p0 c0 {3,S} {8,S} {22,S}
8  O u0 p2 c0 {6,S} {7,S}
9  O u0 p2 c0 {3,S} {10,S}
10 O u0 p2 c0 {9,S} {23,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {5,D}
21 O u0 p2 c0 {6,D}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.11973,0.129577,-0.000133861,3.87071e-08,2.77398e-11,-65847.7,43.6538], Tmin=(100,'K'), Tmax=(536.86,'K')),
            NASAPolynomial(coeffs=[10.8862,0.066852,-3.32829e-05,6.54121e-09,-4.62806e-13,-67521.9,-10.3872], Tmin=(536.86,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 39,
    label = "EL13CY",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {9,S} {13,S} {14,S}
4  C u0 p0 c0 {6,S} {8,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {4,S} {20,D}
7  C u0 p0 c0 {2,S} {9,S} {21,D}
8  O u0 p2 c0 {1,S} {4,S}
9  O u0 p2 c0 {3,S} {7,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.400243,0.0808713,-2.89943e-05,-1.4259e-08,9.01922e-12,-74003.4,39.1675], Tmin=(100,'K'), Tmax=(1125.23,'K')),
            NASAPolynomial(coeffs=[18.7053,0.0431541,-1.89729e-05,3.65516e-09,-2.60102e-13,-80214.9,-63.7555], Tmin=(1125.23,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 40,
    label = "EL34CY",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {8,S} {11,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {10,S}
3  C u0 p0 c0 {4,S} {9,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {1,S} {5,S} {20,D}
7  C u0 p0 c0 {2,S} {9,S} {21,D}
8  O u0 p2 c0 {1,S} {2,S}
9  O u0 p2 c0 {3,S} {7,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.340342,0.0771609,-6.66365e-06,-5.12741e-08,2.7038e-11,-76888.7,39.8861], Tmin=(100,'K'), Tmax=(948.46,'K')),
            NASAPolynomial(coeffs=[20.2054,0.0353605,-1.14838e-05,1.96859e-09,-1.36891e-13,-82803.3,-68.7822], Tmin=(948.46,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 41,
    label = "EL67CY",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {8,S} {15,S} {16,S}
5  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {2,S} {5,S} {20,D}
7  C u0 p0 c0 {3,S} {9,S} {21,D}
8  O u0 p2 c0 {1,S} {4,S}
9  O u0 p2 c0 {1,S} {7,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.424408,0.100854,-9.98689e-05,6.09807e-08,-1.59588e-11,-79346.4,37.1295], Tmin=(100,'K'), Tmax=(907.17,'K')),
            NASAPolynomial(coeffs=[10.1943,0.0540311,-2.24444e-05,4.08051e-09,-2.77554e-13,-81272.9,-13.0649], Tmin=(907.17,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 42,
    label = "EL1OOH3OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {10,S} {12,S}
2  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
3  C u0 p0 c0 {5,S} {8,S} {15,S} {16,S}
4  C u0 p0 c0 {6,S} {9,S} {20,S} {21,S}
5  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {1,S} {4,S} {22,D}
7  C u0 p0 c0 {2,S} {8,S} {23,D}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {4,S} {11,S}
10 O u0 p2 c0 {1,S} {24,S}
11 O u0 p2 c0 {9,S} {25,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 O u0 p2 c0 {6,D}
23 O u0 p2 c0 {7,D}
24 O u1 p2 c0 {10,S}
25 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.2843,0.149842,-0.000179957,1.2323e-07,-3.52884e-11,-80423.5,52.6938], Tmin=(100,'K'), Tmax=(837.45,'K')),
            NASAPolynomial(coeffs=[14.8462,0.0680249,-3.34193e-05,6.583e-09,-4.6859e-13,-83292.8,-26.9132], Tmin=(837.45,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 43,
    label = "EL3OOH1OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {9,S} {12,S}
2  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
3  C u0 p0 c0 {5,S} {8,S} {15,S} {16,S}
4  C u0 p0 c0 {6,S} {10,S} {20,S} {21,S}
5  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {1,S} {4,S} {22,D}
7  C u0 p0 c0 {2,S} {8,S} {23,D}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {1,S} {11,S}
10 O u0 p2 c0 {4,S} {24,S}
11 O u0 p2 c0 {9,S} {25,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 O u0 p2 c0 {6,D}
23 O u0 p2 c0 {7,D}
24 O u1 p2 c0 {10,S}
25 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.2843,0.149842,-0.000179957,1.2323e-07,-3.52884e-11,-80423.5,52.6938], Tmin=(100,'K'), Tmax=(837.45,'K')),
            NASAPolynomial(coeffs=[14.8462,0.0680249,-3.34193e-05,6.583e-09,-4.6859e-13,-83292.8,-26.9132], Tmin=(837.45,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 44,
    label = "EL3OOH4OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {9,S} {13,S}
2  C u0 p0 c0 {1,S} {7,S} {10,S} {12,S}
3  C u0 p0 c0 {4,S} {8,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {6,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {5,S} {22,D}
7  C u0 p0 c0 {2,S} {8,S} {23,D}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {1,S} {11,S}
10 O u0 p2 c0 {2,S} {24,S}
11 O u0 p2 c0 {9,S} {25,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u0 p2 c0 {6,D}
23 O u0 p2 c0 {7,D}
24 O u1 p2 c0 {10,S}
25 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.89647,0.133264,-0.000124421,6.08219e-08,-1.22687e-11,-83392.4,54.1188], Tmin=(100,'K'), Tmax=(1166.66,'K')),
            NASAPolynomial(coeffs=[20.1291,0.0577473,-2.73272e-05,5.33973e-09,-3.7965e-13,-88531.7,-55.5372], Tmin=(1166.66,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 45,
    label = "EL4OOH3OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {10,S} {13,S}
2  C u0 p0 c0 {1,S} {7,S} {9,S} {12,S}
3  C u0 p0 c0 {4,S} {8,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {6,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {5,S} {22,D}
7  C u0 p0 c0 {2,S} {8,S} {23,D}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {2,S} {11,S}
10 O u0 p2 c0 {1,S} {24,S}
11 O u0 p2 c0 {9,S} {25,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u0 p2 c0 {6,D}
23 O u0 p2 c0 {7,D}
24 O u1 p2 c0 {10,S}
25 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.89647,0.133264,-0.000124421,6.08219e-08,-1.22687e-11,-83392.4,54.1188], Tmin=(100,'K'), Tmax=(1166.66,'K')),
            NASAPolynomial(coeffs=[20.1291,0.0577473,-2.73272e-05,5.33973e-09,-3.7965e-13,-88531.7,-55.5372], Tmin=(1166.66,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 46,
    label = "EL6OOH7OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {15,S} {16,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {10,S} {17,S} {18,S}
5  C u0 p0 c0 {6,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {5,S} {22,D}
7  C u0 p0 c0 {3,S} {8,S} {23,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {2,S} {11,S}
10 O u0 p2 c0 {4,S} {24,S}
11 O u0 p2 c0 {9,S} {25,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u0 p2 c0 {6,D}
23 O u0 p2 c0 {7,D}
24 O u1 p2 c0 {10,S}
25 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.88207,0.168014,-0.000258826,2.31398e-07,-8.29519e-11,-85810.9,53.8797], Tmin=(100,'K'), Tmax=(802.45,'K')),
            NASAPolynomial(coeffs=[10.3148,0.0760807,-3.80952e-05,7.40679e-09,-5.16651e-13,-87086.9,-1.63716], Tmin=(802.45,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 47,
    label = "EL7OOH6OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {15,S} {16,S}
2  C u0 p0 c0 {4,S} {8,S} {10,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {9,S} {17,S} {18,S}
5  C u0 p0 c0 {6,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {5,S} {22,D}
7  C u0 p0 c0 {3,S} {8,S} {23,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {4,S} {11,S}
10 O u0 p2 c0 {2,S} {24,S}
11 O u0 p2 c0 {9,S} {25,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u0 p2 c0 {6,D}
23 O u0 p2 c0 {7,D}
24 O u1 p2 c0 {10,S}
25 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.88207,0.168014,-0.000258826,2.31398e-07,-8.29519e-11,-85810.9,53.8797], Tmin=(100,'K'), Tmax=(802.45,'K')),
            NASAPolynomial(coeffs=[10.3148,0.0760807,-3.80952e-05,7.40679e-09,-5.16651e-13,-87086.9,-1.63716], Tmin=(802.45,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 48,
    label = "EL1O3OOH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {8,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {7,S} {19,D}
6  C u0 p0 c0 {2,S} {8,S} {20,D}
7  C u0 p0 c0 {5,S} {21,D} {22,S}
8  O u0 p2 c0 {3,S} {6,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {23,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {5,D}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.2252,0.125664,-0.000130145,7.64277e-08,-1.92284e-11,-96261.4,46.2465], Tmin=(100,'K'), Tmax=(932.8,'K')),
            NASAPolynomial(coeffs=[12.9825,0.0647367,-3.2165e-05,6.39895e-09,-4.59148e-13,-98911.9,-21.3085], Tmin=(932.8,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 49,
    label = "EL3O1OOH",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {7,S} {13,S} {14,S}
2  C u0 p0 c0 {4,S} {8,S} {11,S} {12,S}
3  C u0 p0 c0 {6,S} {9,S} {18,S} {19,S}
4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {6,S} {20,D}
6  C u0 p0 c0 {3,S} {5,S} {21,D}
7  C u0 p0 c0 {1,S} {8,S} {22,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {3,S} {10,S}
10 O u0 p2 c0 {9,S} {23,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 O u0 p2 c0 {5,D}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.69321,0.136452,-0.000162975,1.12372e-07,-3.26598e-11,-96423.5,45.5795], Tmin=(100,'K'), Tmax=(823.01,'K')),
            NASAPolynomial(coeffs=[13.0808,0.0646445,-3.20949e-05,6.35027e-09,-4.53127e-13,-98855.3,-22.8182], Tmin=(823.01,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 50,
    label = "EL3O4OOH",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {7,S} {9,S} {11,S}
2  C u0 p0 c0 {3,S} {8,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {6,S} {20,D}
6  C u0 p0 c0 {4,S} {5,S} {21,D}
7  C u0 p0 c0 {1,S} {8,S} {22,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {23,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {5,D}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.19207,0.124839,-0.000130165,7.79695e-08,-2.00788e-11,-100879,45.0139], Tmin=(100,'K'), Tmax=(911.93,'K')),
            NASAPolynomial(coeffs=[12.3772,0.0653205,-3.22649e-05,6.39962e-09,-4.58362e-13,-103354,-19.1989], Tmin=(911.93,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 51,
    label = "EL4O3OOH",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {6,S} {9,S} {11,S}
2  C u0 p0 c0 {3,S} {8,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {4,S} {20,D}
6  C u0 p0 c0 {1,S} {7,S} {21,D}
7  C u0 p0 c0 {6,S} {8,S} {22,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {23,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {5,D}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.43309,0.131074,-0.000148968,9.85068e-08,-2.78323e-11,-99078.9,45.1777], Tmin=(100,'K'), Tmax=(839.72,'K')),
            NASAPolynomial(coeffs=[12.1685,0.0662817,-3.32269e-05,6.6164e-09,-4.74316e-13,-101363,-18.0658], Tmin=(839.72,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 52,
    label = "EL6O7OOH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {7,S} {9,S} {15,S} {16,S}
4  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {4,S} {20,D}
6  C u0 p0 c0 {2,S} {8,S} {22,D}
7  C u0 p0 c0 {3,S} {8,S} {21,D}
8  O u0 p2 c0 {6,S} {7,S}
9  O u0 p2 c0 {3,S} {10,S}
10 O u0 p2 c0 {9,S} {23,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {5,D}
21 O u0 p2 c0 {7,D}
22 O u0 p2 c0 {6,D}
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.17928,0.149835,-0.000227853,2.0033e-07,-7.08596e-11,-102869,49.8559], Tmin=(100,'K'), Tmax=(799.38,'K')),
            NASAPolynomial(coeffs=[10.6602,0.0656789,-3.25797e-05,6.31948e-09,-4.40529e-13,-104286,-5.23324], Tmin=(799.38,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 53,
    label = "EL7O6OOH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {7,S} {8,S} {9,S} {15,S}
4  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {4,S} {19,D}
6  C u0 p0 c0 {2,S} {8,S} {20,D}
7  C u0 p0 c0 {3,S} {21,D} {22,S}
8  O u0 p2 c0 {3,S} {6,S}
9  O u0 p2 c0 {3,S} {10,S}
10 O u0 p2 c0 {9,S} {23,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {5,D}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.68711,0.136932,-0.00018697,1.59142e-07,-5.73248e-11,-103251,48.2845], Tmin=(100,'K'), Tmax=(730.11,'K')),
            NASAPolynomial(coeffs=[9.0814,0.0705673,-3.54869e-05,6.99943e-09,-4.95826e-13,-104627,1.06492], Tmin=(730.11,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 54,
    label = "C5H8O3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {14,D}
5  C u0 p0 c0 {2,S} {6,S} {15,D}
6  O u0 p2 c0 {5,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 O u0 p2 c0 {5,D}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.9439,0.0460434,-1.63509e-05,-1.99729e-09,1.686e-12,-77253.1,10.0527], Tmin=(298,'K'), Tmax=(1482,'K')),
            NASAPolynomial(coeffs=[19.7917,0.02129,-7.15548e-06,1.0993e-09,-6.33571e-14,-83284.3,-73.0169], Tmin=(1482,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 55,
    label = "C=C",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65151,-0.00535067,5.16486e-05,-6.36869e-08,2.50743e-11,5114.51,5.38561], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.14446,0.0102648,-3.61247e-06,5.74009e-10,-3.39296e-14,4190.59,-1.14778], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 56,
    label = "CC(=O)CCC([O])=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {3,S} {13,D}
5  C u0 p0 c0 {2,S} {14,S} {15,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 O u1 p2 c0 {5,S}
15 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70903,0.0518333,-3.3289e-05,1.00007e-08,-9.47599e-13,-47015.1,16.4119], Tmin=(298,'K'), Tmax=(1205,'K')),
            NASAPolynomial(coeffs=[28.7614,0.00841632,-8.25587e-06,4.19857e-09,-4.40515e-13,-57481.4,-124.056], Tmin=(1205,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 57,
    label = "CC(=O)CC[C]=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {3,S} {13,D}
5  C u1 p0 c0 {2,S} {14,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.18978,0.0684213,-9.45413e-05,8.36069e-08,-3.02791e-11,-24538.5,26.1648], Tmin=(100,'K'), Tmax=(810.93,'K')),
            NASAPolynomial(coeffs=[4.97289,0.0384052,-1.80148e-05,3.42611e-09,-2.36684e-13,-24778.7,11.0084], Tmin=(810.93,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 58,
    label = "CCO[C]=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  O u0 p2 c0 {1,S} {4,S}
4  C u1 p0 c0 {3,S} {10,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.59613,0.0340977,-2.48184e-05,1.0883e-08,-2.25691e-12,-24943.8,15.8575], Tmin=(100,'K'), Tmax=(1034.25,'K')),
            NASAPolynomial(coeffs=[5.00214,0.0247925,-1.13229e-05,2.18399e-09,-1.54203e-13,-25441.5,4.16885], Tmin=(1034.25,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 59,
    label = "[CH2]CC(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  C u1 p0 c0 {1,S} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.40256,0.0367294,-1.97317e-05,5.07323e-09,-4.99655e-13,-6150.07,19.3993], Tmin=(200,'K'), Tmax=(1380,'K')),
            NASAPolynomial(coeffs=[12.4694,0.0171022,-5.92157e-06,9.26817e-10,-5.40731e-14,-10137.8,-36.2186], Tmin=(1380,'K'), Tmax=(5000,'K')),
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
    index = 60,
    label = "CCOC(=O)CC[C]=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {6,S} {17,D}
6  O u0 p2 c0 {2,S} {5,S}
7  C u1 p0 c0 {3,S} {18,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u0 p2 c0 {5,D}
18 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.33595,0.062888,-3.7578e-05,1.0567e-08,-1.02978e-12,-53704.7,19.9971], Tmin=(298,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[21.3884,0.0243388,-8.05871e-06,1.22515e-09,-7.00825e-14,-60260.7,-78.1163], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 61,
    label = "C[C]=O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03587,0.000877295,3.071e-05,-3.92476e-08,1.52969e-11,-2682.07,7.86177], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.31372,0.00917378,-3.32204e-06,5.39475e-10,-3.24524e-14,-3645.04,-1.67576], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 62,
    label = "[CH2]CC(=O)OCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {14,D}
5  C u1 p0 c0 {2,S} {15,S} {16,S}
6  O u0 p2 c0 {1,S} {4,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.40418,0.0609507,-4.15181e-05,1.39208e-08,-1.94508e-12,-33043.9,25.1943], Tmin=(100,'K'), Tmax=(1563.9,'K')),
            NASAPolynomial(coeffs=[11.7402,0.034514,-1.61616e-05,3.11168e-09,-2.17158e-13,-36276.8,-29.293], Tmin=(1563.9,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 63,
    label = "[CH2]C(C)=O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u1 p2 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.84406,0.0189152,1.20804e-05,-2.62117e-08,1.05279e-11,-5215.42,14.5362], Tmin=(100,'K'), Tmax=(1005.62,'K')),
            NASAPolynomial(coeffs=[7.59011,0.0155447,-6.02335e-06,1.12468e-09,-8.02421e-14,-6954.09,-12.286], Tmin=(1005.62,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 64,
    label = "[CH2]C(=O)OCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {5,S} {11,D}
4  C u1 p0 c0 {3,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.34362,0.0529483,-3.83994e-05,1.41492e-08,-2.08906e-12,-32990.3,21.5108], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[16.8748,0.0161432,-5.37911e-06,8.21491e-10,-4.7147e-14,-38264,-61.604], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 65,
    label = "[CH2]OC(=O)CCC(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {3,S} {15,D}
5  C u0 p0 c0 {2,S} {7,S} {16,D}
6  C u1 p0 c0 {7,S} {17,S} {18,S}
7  O u0 p2 c0 {5,S} {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {4,D}
16 O u0 p2 c0 {5,D}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.21272,0.0746572,-2.33402e-05,-1.0538e-07,1.19076e-10,-49357.7,29.1361], Tmin=(100,'K'), Tmax=(454,'K')),
            NASAPolynomial(coeffs=[6.09626,0.0535636,-2.61139e-05,5.10494e-09,-3.6066e-13,-50027.2,6.94277], Tmin=(454,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 66,
    label = "C=C=O",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.13241,0.0181319,-1.74093e-05,9.35336e-09,-2.01725e-12,-7148.09,13.3808], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.75871,0.00635124,-2.25955e-06,3.62322e-10,-2.15856e-14,-8085.33,-4.9649], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 67,
    label = "CCOC(=O)CC=C=O",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {6,S} {15,D}
5  C u0 p0 c0 {2,S} {7,D} {16,S}
6  O u0 p2 c0 {1,S} {4,S}
7  C u0 p0 c0 {5,D} {17,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {4,D}
16 H u0 p0 c0 {5,S}
17 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.05446,0.0684445,-4.68985e-05,1.6495e-08,-2.47808e-12,-56218.1,30.0616], Tmin=(100,'K'), Tmax=(1448.37,'K')),
            NASAPolynomial(coeffs=[10.8663,0.0413471,-1.88351e-05,3.57779e-09,-2.48476e-13,-59060.3,-20.9094], Tmin=(1448.37,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 68,
    label = "C=CC(C)=O",
    molecule = 
"""
1  O u0 p2 c0 {3,D}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,D} {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {4,D} {10,S} {11,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.245579,0.0426432,-2.91127e-05,1.03478e-08,-1.53551e-12,-17030.5,26.4431], Tmin=(200,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[12.5572,0.0149673,-5.20015e-06,8.15864e-10,-4.76824e-14,-21462.3,-40.1434], Tmin=(1386,'K'), Tmax=(5000,'K')),
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
    index = 69,
    label = "C=CC(=O)OCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {5,D} {12,S}
4  C u0 p0 c0 {3,S} {6,S} {13,D}
5  C u0 p0 c0 {3,D} {14,S} {15,S}
6  O u0 p2 c0 {1,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.35534,0.0463001,-1.00615e-06,-2.93049e-08,1.35736e-11,-44436.8,27.7595], Tmin=(100,'K'), Tmax=(1027.55,'K')),
            NASAPolynomial(coeffs=[13.2433,0.0264773,-1.06863e-05,2.03003e-09,-1.4576e-13,-48276.5,-36.712], Tmin=(1027.55,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 70,
    label = "CC(=O)CC=C=O",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {11,D}
4  C u0 p0 c0 {1,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {13,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 H u0 p0 c0 {4,S}
13 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.82806,0.0488221,-3.35641e-05,1.18821e-08,-1.7782e-12,-28495.5,23.1054], Tmin=(100,'K'), Tmax=(1476.2,'K')),
            NASAPolynomial(coeffs=[9.5083,0.0280115,-1.24183e-05,2.33256e-09,-1.60977e-13,-30763,-16.9386], Tmin=(1476.2,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 71,
    label = "H2O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.20148,-0.00205584,6.56547e-06,-5.52907e-09,1.78283e-12,-30295,-0.860611], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.73118,0.00295137,-8.3536e-07,1.26089e-10,-8.40532e-15,-29916.9,6.55183], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 72,
    label = "C",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.00702,-0.0126484,4.66821e-05,-4.59211e-08,1.57634e-11,-10222.4,-4.04227], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.68377,0.010013,-3.31268e-06,5.30234e-10,-3.13372e-14,-10018.8,9.71477], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 73,
    label = "C(=O)C(=O)CCC(=O)OCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {7,S} {18,D}
6  C u0 p0 c0 {2,S} {8,S} {19,D}
7  C u0 p0 c0 {5,S} {20,D} {21,S}
8  O u0 p2 c0 {3,S} {6,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {6,D}
20 O u0 p2 c0 {7,D}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.70363,0.113502,-0.000148739,1.28466e-07,-4.73916e-11,-84448.8,38.7615], Tmin=(100,'K'), Tmax=(748.99,'K')),
            NASAPolynomial(coeffs=[6.30315,0.0657107,-3.22573e-05,6.30005e-09,-4.43857e-13,-85207.5,8.92505], Tmin=(748.99,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 74,
    label = "C([O])C(=O)CCC(=O)OCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {1,S} {5,S} {21,D}
7  C u0 p0 c0 {2,S} {8,S} {22,D}
8  O u0 p2 c0 {3,S} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u1 p2 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.981855,0.119913,-0.000161135,1.38258e-07,-4.96264e-11,-66205.8,41.6649], Tmin=(100,'K'), Tmax=(778.24,'K')),
            NASAPolynomial(coeffs=[7.20459,0.065161,-3.11757e-05,6.00328e-09,-4.18792e-13,-67096.2,6.68858], Tmin=(778.24,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 75,
    label = "[O]C(=O)CCC(=O)OCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {7,S} {17,D}
6  C u0 p0 c0 {2,S} {18,S} {19,D}
7  O u0 p2 c0 {3,S} {5,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u0 p2 c0 {5,D}
18 O u1 p2 c0 {6,S}
19 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.96482,0.0649387,-3.22143e-05,6.28333e-09,-4.39524e-13,-76437.1,24.367], Tmin=(100,'K'), Tmax=(3057,'K')),
            NASAPolynomial(coeffs=[70.5143,-0.0146059,2.47781e-06,-3.3614e-10,2.44367e-14,-121868,-383.76], Tmin=(3057,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 76,
    label = "C=O",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.77187,-0.00976266,3.70122e-05,-3.76922e-08,1.31327e-11,-14379.8,0.696586], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.91333,0.0067004,-2.55521e-06,4.27795e-10,-2.44073e-14,-14462.2,7.43823], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 77,
    label = "CC(=O)C(=O)CC(=O)OCC",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {7,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {8,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {6,S} {20,D}
6  C u0 p0 c0 {4,S} {5,S} {19,D}
7  C u0 p0 c0 {1,S} {8,S} {21,D}
8  O u0 p2 c0 {2,S} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {6,D}
20 O u0 p2 c0 {5,D}
21 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0910902,0.0986551,-9.00454e-05,4.86489e-08,-1.17137e-11,-87608.7,37.0931], Tmin=(100,'K'), Tmax=(950.57,'K')),
            NASAPolynomial(coeffs=[9.14485,0.0597904,-2.8717e-05,5.63733e-09,-4.01711e-13,-89364.6,-6.99684], Tmin=(950.57,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 78,
    label = "CC(=O)C([O])CC(=O)OCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {1,S} {5,S} {21,D}
7  C u0 p0 c0 {2,S} {8,S} {22,D}
8  O u0 p2 c0 {3,S} {7,S}
9  O u1 p2 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0729214,0.0965565,-7.87881e-05,3.62766e-08,-7.35652e-12,-69196.6,41.2617], Tmin=(100,'K'), Tmax=(1110.57,'K')),
            NASAPolynomial(coeffs=[10.5542,0.05828,-2.70896e-05,5.24226e-09,-3.70386e-13,-71557,-11.1226], Tmin=(1110.57,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 79,
    label = "CC(=O)C1CC(=O)OO1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {14,D}
5  C u0 p0 c0 {2,S} {7,S} {15,D}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {5,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.49717,0.026928,9.18569e-05,-1.42317e-07,5.66535e-11,-65285.6,29.2494], Tmin=(100,'K'), Tmax=(965.97,'K')),
            NASAPolynomial(coeffs=[20.2286,0.0199225,-6.83274e-06,1.41287e-09,-1.15405e-13,-72196.4,-77.5099], Tmin=(965.97,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 80,
    label = "CCOC(=O)C(=O)CC(C)=O",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {6,S} {11,S} {12,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {4,S} {19,D}
6  C u0 p0 c0 {1,S} {7,S} {20,D}
7  C u0 p0 c0 {6,S} {8,S} {21,D}
8  O u0 p2 c0 {2,S} {7,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {5,D}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.348592,0.105045,-0.000109213,6.94396e-08,-1.94937e-11,-85807.7,37.3186], Tmin=(100,'K'), Tmax=(833.03,'K')),
            NASAPolynomial(coeffs=[8.83713,0.0609381,-2.97945e-05,5.88285e-09,-4.20141e-13,-87338.1,-5.31932], Tmin=(833.03,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 81,
    label = "CC(=O)CC1OOC1=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {3,S} {14,D}
5  C u0 p0 c0 {1,S} {7,S} {15,D}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {5,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.13842,0.0382615,5.9015e-05,-1.06903e-07,4.34537e-11,-55441.8,30.3458], Tmin=(100,'K'), Tmax=(983.56,'K')),
            NASAPolynomial(coeffs=[20.101,0.0219042,-8.70314e-06,1.80503e-09,-1.42098e-13,-62110.9,-75.7639], Tmin=(983.56,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 82,
    label = "CC(=O)OC(=O)CCC(C)=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
4  C u0 p0 c0 {7,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {3,S} {19,D}
6  C u0 p0 c0 {2,S} {8,S} {21,D}
7  C u0 p0 c0 {4,S} {8,S} {20,D}
8  O u0 p2 c0 {6,S} {7,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 O u0 p2 c0 {5,D}
20 O u0 p2 c0 {7,D}
21 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.643601,0.112687,-0.000156573,1.37966e-07,-5.02071e-11,-94051.5,41.6166], Tmin=(100,'K'), Tmax=(789.66,'K')),
            NASAPolynomial(coeffs=[6.37792,0.0614849,-2.96141e-05,5.70966e-09,-3.98037e-13,-94673,12.4864], Tmin=(789.66,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 83,
    label = "CC(=O)OC(=O)CCCC=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {8,S} {19,D}
6  C u0 p0 c0 {4,S} {8,S} {18,D}
7  C u0 p0 c0 {3,S} {20,D} {21,S}
8  O u0 p2 c0 {5,S} {6,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u0 p2 c0 {6,D}
19 O u0 p2 c0 {5,D}
20 O u0 p2 c0 {7,D}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.631305,0.112157,-0.000153902,1.34834e-07,-4.90631e-11,-90312.4,42.2255], Tmin=(100,'K'), Tmax=(783.93,'K')),
            NASAPolynomial(coeffs=[6.42691,0.0617023,-2.97308e-05,5.73876e-09,-4.00582e-13,-90975.3,12.7219], Tmin=(783.93,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 84,
    label = "CCOC(=O)[CH]CC(=O)COO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {13,S} {14,S}
2  C u0 p0 c0 {4,S} {8,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {9,S} {18,S} {19,S}
4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {3,S} {20,D}
6  C u1 p0 c0 {1,S} {7,S} {21,S}
7  C u0 p0 c0 {6,S} {8,S} {22,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {3,S} {10,S}
10 O u0 p2 c0 {9,S} {23,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 O u0 p2 c0 {5,D}
21 H u0 p0 c0 {6,S}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.30698,0.130855,-0.000148741,8.53846e-08,-1.18889e-11,-65992.6,42.9546], Tmin=(100,'K'), Tmax=(586.24,'K')),
            NASAPolynomial(coeffs=[10.5071,0.0680988,-3.38476e-05,6.67363e-09,-4.74185e-13,-67684.5,-10.3489], Tmin=(586.24,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 85,
    label = "[CH2]C(=O)CC(OO)C(=O)OCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {8,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {7,D} {19,S}
6  C u0 p0 c0 {1,S} {8,S} {20,D}
7  C u0 p0 c0 {5,D} {21,S} {22,S}
8  O u0 p2 c0 {3,S} {6,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {23,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u1 p2 c0 {5,S}
20 O u0 p2 c0 {6,D}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.63515,0.118322,-0.000105146,4.79039e-08,-8.8162e-12,-70009.1,47.4936], Tmin=(100,'K'), Tmax=(1292.16,'K')),
            NASAPolynomial(coeffs=[22.2324,0.0444379,-1.93765e-05,3.65247e-09,-2.54611e-13,-76177.2,-73.7708], Tmin=(1292.16,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 86,
    label = "C[CH]OC(=O)C(CC(C)=O)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
4  C u0 p0 c0 {7,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {3,S} {20,D}
6  C u0 p0 c0 {1,S} {8,S} {21,D}
7  C u1 p0 c0 {4,S} {8,S} {22,S}
8  O u0 p2 c0 {6,S} {7,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {23,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 O u0 p2 c0 {5,D}
21 O u0 p2 c0 {6,D}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.19962,0.119811,-0.000111485,5.48505e-08,-1.12479e-11,-67042,45.8943], Tmin=(100,'K'), Tmax=(1140.74,'K')),
            NASAPolynomial(coeffs=[17.2155,0.055238,-2.65762e-05,5.22873e-09,-3.73062e-13,-71243.4,-45.3731], Tmin=(1140.74,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 87,
    label = "CC(=O)[CH]CC(=O)OC(C)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {8,S} {9,S} {11,S}
2  C u0 p0 c0 {5,S} {7,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {2,S} {6,D} {21,S}
6  C u0 p0 c0 {4,S} {5,D} {20,S}
7  C u0 p0 c0 {2,S} {8,S} {22,D}
8  O u0 p2 c0 {1,S} {7,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {23,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u1 p2 c0 {6,S}
21 H u0 p0 c0 {5,S}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.959819,0.112087,-9.1207e-05,3.7162e-08,-6.25483e-12,-74420.6,42.5236], Tmin=(100,'K'), Tmax=(1362.12,'K')),
            NASAPolynomial(coeffs=[19.3438,0.0524645,-2.55501e-05,5.02776e-09,-3.57087e-13,-79951.9,-61.7045], Tmin=(1362.12,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 88,
    label = "CC(=O)C[CH]C(=O)OC(C)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {8,S} {9,S} {11,S}
2  C u0 p0 c0 {5,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {2,S} {4,S} {20,D}
6  C u1 p0 c0 {2,S} {7,S} {21,S}
7  C u0 p0 c0 {6,S} {8,S} {22,D}
8  O u0 p2 c0 {1,S} {7,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {23,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {5,D}
21 H u0 p0 c0 {6,S}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.38099,0.129752,-0.000157583,1.17561e-07,-3.78283e-11,-72599.2,44.3528], Tmin=(100,'K'), Tmax=(741.37,'K')),
            NASAPolynomial(coeffs=[9.90049,0.068885,-3.44345e-05,6.82352e-09,-4.86765e-13,-74272,-6.69801], Tmin=(741.37,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 89,
    label = "CC(=O)CC1C(=O)OC1C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {5,S} {19,D}
7  C u0 p0 c0 {1,S} {8,S} {20,D}
8  O u0 p2 c0 {2,S} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u0 p2 c0 {6,D}
20 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.246825,0.0695438,-1.4453e-05,-2.76417e-08,1.51107e-11,-62861.5,33.4635], Tmin=(100,'K'), Tmax=(986.05,'K')),
            NASAPolynomial(coeffs=[14.6152,0.0404877,-1.47179e-05,2.60012e-09,-1.78673e-13,-67116.1,-42.8594], Tmin=(986.05,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 90,
    label = "CC(=O)C1CC(=O)OC1C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {10,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {5,S} {19,D}
7  C u0 p0 c0 {3,S} {8,S} {20,D}
8  O u0 p2 c0 {2,S} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u0 p2 c0 {6,D}
20 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.539133,0.0604771,1.2119e-05,-5.49896e-08,2.4724e-11,-70309.5,32.0644], Tmin=(100,'K'), Tmax=(972.68,'K')),
            NASAPolynomial(coeffs=[14.4428,0.0405117,-1.4476e-05,2.56899e-09,-1.78574e-13,-74774.6,-43.6763], Tmin=(972.68,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 91,
    label = "O=[C]COO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {4,S}
3 C u1 p0 c0 {1,S} {7,D}
4 O u0 p2 c0 {2,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {3,D}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.93015,0.0435985,-5.03168e-05,2.8606e-08,-6.31892e-12,-11055.3,17.9195], Tmin=(100,'K'), Tmax=(1113.08,'K')),
            NASAPolynomial(coeffs=[11.5568,0.0090041,-3.69723e-06,6.84001e-10,-4.76218e-14,-13198.3,-29.555], Tmin=(1113.08,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 92,
    label = "CCOC(=O)CC=O",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {14,D}
5  C u0 p0 c0 {2,S} {15,D} {16,S}
6  O u0 p2 c0 {1,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 O u0 p2 c0 {5,D}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.43366,0.0599647,-3.747e-05,1.15516e-08,-1.49498e-12,-67076.1,27.3098], Tmin=(100,'K'), Tmax=(1646.45,'K')),
            NASAPolynomial(coeffs=[10.8571,0.0370705,-1.66121e-05,3.10598e-09,-2.12569e-13,-70179.1,-22.8516], Tmin=(1646.45,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 93,
    label = "CC(=O)CC([C]=O)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {14,D}
5  O u0 p2 c0 {2,S} {7,S}
6  C u1 p0 c0 {2,S} {15,D}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 O u0 p2 c0 {6,D}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.401946,0.0840391,-8.97391e-05,5.25e-08,-1.27534e-11,-36339.8,34.5858], Tmin=(100,'K'), Tmax=(980.44,'K')),
            NASAPolynomial(coeffs=[11.9587,0.0368888,-1.76013e-05,3.44767e-09,-2.45471e-13,-38605.9,-20.9405], Tmin=(980.44,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 94,
    label = "CC=O",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.72946,-0.00319329,4.75349e-05,-5.74586e-08,2.19311e-11,-21572.9,4.10302], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.40411,0.0117231,-4.22631e-06,6.83725e-10,-4.09849e-14,-22593.1,-3.48079], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 95,
    label = "CC(=O)C1CC1=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {2,S} {13,D}
5  C u0 p0 c0 {1,S} {3,S} {12,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {5,D}
13 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.77081,0.0375027,1.00348e-05,-3.86412e-08,1.70525e-11,-19768.1,21.8854], Tmin=(100,'K'), Tmax=(989.93,'K')),
            NASAPolynomial(coeffs=[12.2103,0.022518,-8.47147e-06,1.57609e-09,-1.13246e-13,-23167.6,-35.1043], Tmin=(989.93,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 96,
    label = "CC([O])OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  O u0 p2 c0 {1,S} {4,S}
4  O u0 p2 c0 {3,S} {10,S}
5  O u1 p2 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.18031,0.0443064,-5.65119e-05,5.07463e-08,-1.98439e-11,-19133.1,19.1312], Tmin=(100,'K'), Tmax=(732.7,'K')),
            NASAPolynomial(coeffs=[4.02918,0.0290111,-1.45496e-05,2.87609e-09,-2.04262e-13,-19264.4,11.7393], Tmin=(732.7,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 97,
    label = "CCOC(=O)C1CC(=O)CO1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {9,S} {13,S} {14,S}
4  C u0 p0 c0 {6,S} {8,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {2,S} {4,S} {20,D}
7  C u0 p0 c0 {1,S} {9,S} {21,D}
8  O u0 p2 c0 {1,S} {4,S}
9  O u0 p2 c0 {3,S} {7,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.00159064,0.0691872,4.46527e-06,-4.95145e-08,2.17031e-11,-83849.1,37.9204], Tmin=(100,'K'), Tmax=(1043.46,'K')),
            NASAPolynomial(coeffs=[17.8908,0.0426854,-1.79393e-05,3.4546e-09,-2.48928e-13,-89874.3,-60.1401], Tmin=(1043.46,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 98,
    label = "CC(=O)CC1OC(C)OC1=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {8,S} {9,S} {13,S}
4  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {2,S} {5,S} {20,D}
7  C u0 p0 c0 {1,S} {9,S} {21,D}
8  O u0 p2 c0 {1,S} {3,S}
9  O u0 p2 c0 {3,S} {7,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.196833,0.0637455,1.79682e-05,-6.19227e-08,2.56023e-11,-90467.5,37.7088], Tmin=(100,'K'), Tmax=(1041.34,'K')),
            NASAPolynomial(coeffs=[17.4714,0.0431828,-1.83731e-05,3.57085e-09,-2.58885e-13,-96548.1,-58.2521], Tmin=(1041.34,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 99,
    label = "CC(=O)C1CC(=O)OC(C)O1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {8,S} {10,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {13,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {1,S} {5,S} {20,D}
7  C u0 p0 c0 {3,S} {9,S} {21,D}
8  O u0 p2 c0 {1,S} {2,S}
9  O u0 p2 c0 {2,S} {7,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.0150837,0.0656219,2.08573e-05,-6.51544e-08,2.57124e-11,-93037,33.9586], Tmin=(100,'K'), Tmax=(1085.85,'K')),
            NASAPolynomial(coeffs=[19.6169,0.0447938,-2.13477e-05,4.33484e-09,-3.19386e-13,-100323,-76.1709], Tmin=(1085.85,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 100,
    label = "CCOC(=O)C=CC(=O)C[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {5,S} {17,D}
5  C u0 p0 c0 {4,S} {6,D} {19,S}
6  C u0 p0 c0 {5,D} {7,S} {18,S}
7  C u0 p0 c0 {6,S} {8,S} {20,D}
8  O u0 p2 c0 {1,S} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 O u1 p2 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 O u0 p2 c0 {4,D}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0980193,0.101964,-0.000156041,1.47122e-07,-5.58092e-11,-45284.5,38.1377], Tmin=(100,'K'), Tmax=(791.39,'K')),
            NASAPolynomial(coeffs=[4.86171,0.0556936,-2.81561e-05,5.53996e-09,-3.89874e-13,-45405.6,19.565], Tmin=(791.39,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 101,
    label = "CCOC(=O)C(O[O])CC(=O)COO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {10,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {5,S} {8,S} {15,S} {16,S}
4  C u0 p0 c0 {6,S} {9,S} {20,S} {21,S}
5  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {2,S} {4,S} {22,D}
7  C u0 p0 c0 {1,S} {8,S} {23,D}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {4,S} {11,S}
10 O u0 p2 c0 {1,S} {24,S}
11 O u0 p2 c0 {9,S} {25,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 O u0 p2 c0 {6,D}
23 O u0 p2 c0 {7,D}
24 O u1 p2 c0 {10,S}
25 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.2843,0.149842,-0.000179957,1.2323e-07,-3.52884e-11,-80423.5,52.6938], Tmin=(100,'K'), Tmax=(837.45,'K')),
            NASAPolynomial(coeffs=[14.8462,0.0680249,-3.34193e-05,6.583e-09,-4.6859e-13,-83292.8,-26.9132], Tmin=(837.45,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 102,
    label = "C(O[O])C(=O)CC(OO)C(=O)OCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {9,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {5,S} {8,S} {15,S} {16,S}
4  C u0 p0 c0 {6,S} {10,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {2,S} {4,S} {22,D}
7  C u0 p0 c0 {1,S} {8,S} {23,D}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {1,S} {11,S}
10 O u0 p2 c0 {4,S} {24,S}
11 O u0 p2 c0 {9,S} {25,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u0 p2 c0 {6,D}
23 O u0 p2 c0 {7,D}
24 O u1 p2 c0 {10,S}
25 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.2843,0.149842,-0.000179957,1.2323e-07,-3.52884e-11,-80423.5,52.6938], Tmin=(100,'K'), Tmax=(837.45,'K')),
            NASAPolynomial(coeffs=[14.8462,0.0680249,-3.34193e-05,6.583e-09,-4.6859e-13,-83292.8,-26.9132], Tmin=(837.45,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 103,
    label = "CC(O[O])OC(=O)C(CC(C)=O)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {9,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
3  C u0 p0 c0 {4,S} {8,S} {10,S} {13,S}
4  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {6,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {2,S} {5,S} {22,D}
7  C u0 p0 c0 {1,S} {8,S} {23,D}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {1,S} {11,S}
10 O u0 p2 c0 {3,S} {24,S}
11 O u0 p2 c0 {9,S} {25,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u0 p2 c0 {6,D}
23 O u0 p2 c0 {7,D}
24 O u1 p2 c0 {10,S}
25 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.97379,0.143041,-0.000161518,1.04128e-07,-2.83846e-11,-87046.7,52.7758], Tmin=(100,'K'), Tmax=(872.47,'K')),
            NASAPolynomial(coeffs=[14.1955,0.0689121,-3.40761e-05,6.75155e-09,-4.82858e-13,-89868.2,-23.0263], Tmin=(872.47,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 104,
    label = "CC(=O)C(O[O])CC(=O)OC(C)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {10,S} {12,S}
2  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
3  C u0 p0 c0 {4,S} {8,S} {9,S} {15,S}
4  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {6,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {5,S} {22,D}
7  C u0 p0 c0 {2,S} {8,S} {23,D}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {3,S} {11,S}
10 O u0 p2 c0 {1,S} {24,S}
11 O u0 p2 c0 {9,S} {25,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u0 p2 c0 {6,D}
23 O u0 p2 c0 {7,D}
24 O u1 p2 c0 {10,S}
25 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.97379,0.143041,-0.000161518,1.04128e-07,-2.83846e-11,-87046.7,52.7758], Tmin=(100,'K'), Tmax=(872.47,'K')),
            NASAPolynomial(coeffs=[14.1955,0.0689121,-3.40761e-05,6.75155e-09,-4.82858e-13,-89868.2,-23.0263], Tmin=(872.47,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 105,
    label = "CC(=O)CC(O[O])C(=O)OC(C)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {10,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {4,S} {8,S} {9,S} {15,S}
4  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {6,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {2,S} {5,S} {22,D}
7  C u0 p0 c0 {1,S} {8,S} {23,D}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {3,S} {11,S}
10 O u0 p2 c0 {1,S} {24,S}
11 O u0 p2 c0 {9,S} {25,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u0 p2 c0 {6,D}
23 O u0 p2 c0 {7,D}
24 O u1 p2 c0 {10,S}
25 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.97379,0.143041,-0.000161518,1.04128e-07,-2.83846e-11,-87046.7,52.7758], Tmin=(100,'K'), Tmax=(872.47,'K')),
            NASAPolynomial(coeffs=[14.1955,0.0689121,-3.40761e-05,6.75155e-09,-4.82858e-13,-89868.2,-23.0263], Tmin=(872.47,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 106,
    label = "CCOC(=O)C=CC(=O)COO",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {8,S} {11,S} {12,S}
2  C u0 p0 c0 {4,S} {9,S} {16,S} {17,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {5,S} {18,D}
5  C u0 p0 c0 {4,S} {6,D} {20,S}
6  C u0 p0 c0 {5,D} {7,S} {19,S}
7  C u0 p0 c0 {6,S} {8,S} {21,D}
8  O u0 p2 c0 {1,S} {7,S}
9  O u0 p2 c0 {2,S} {10,S}
10 O u0 p2 c0 {9,S} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 O u0 p2 c0 {4,D}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.949505,0.121045,-0.000180789,1.64424e-07,-6.13689e-11,-65968.4,41.1765], Tmin=(100,'K'), Tmax=(761.74,'K')),
            NASAPolynomial(coeffs=[7.42571,0.061131,-3.14303e-05,6.24582e-09,-4.42997e-13,-66782,6.08478], Tmin=(761.74,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 107,
    label = "CC(OO)OC(=O)C=CC(=O)C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {5,S} {18,D}
5  C u0 p0 c0 {4,S} {6,D} {20,S}
6  C u0 p0 c0 {5,D} {7,S} {19,S}
7  C u0 p0 c0 {6,S} {8,S} {21,D}
8  O u0 p2 c0 {1,S} {7,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 O u0 p2 c0 {4,D}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.718291,0.115232,-0.000166146,1.51011e-07,-5.74043e-11,-72588.2,41.54], Tmin=(100,'K'), Tmax=(738.44,'K')),
            NASAPolynomial(coeffs=[6.6991,0.0621676,-3.21825e-05,6.43859e-09,-4.59384e-13,-73332.3,10.3832], Tmin=(738.44,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 108,
    label = "CCOC(=O)C=C(OO)C(=O)C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
3  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
4  C u0 p0 c0 {5,S} {6,D} {9,S}
5  C u0 p0 c0 {3,S} {4,S} {19,D}
6  C u0 p0 c0 {4,D} {7,S} {20,S}
7  C u0 p0 c0 {6,S} {8,S} {21,D}
8  O u0 p2 c0 {1,S} {7,S}
9  O u0 p2 c0 {4,S} {10,S}
10 O u0 p2 c0 {9,S} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 O u0 p2 c0 {5,D}
20 H u0 p0 c0 {6,S}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.900191,0.120477,-0.000183902,1.68911e-07,-6.28388e-11,-66970.6,40.981], Tmin=(100,'K'), Tmax=(780.53,'K')),
            NASAPolynomial(coeffs=[7.04219,0.0602729,-3.07248e-05,6.06849e-09,-4.28236e-13,-67616.4,8.43706], Tmin=(780.53,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 109,
    label = "C=COC(=O)C(CC(C)=O)OO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {3,S} {17,D}
5  C u0 p0 c0 {1,S} {8,S} {18,D}
6  C u0 p0 c0 {7,D} {8,S} {19,S}
7  C u0 p0 c0 {6,D} {20,S} {21,S}
8  O u0 p2 c0 {5,S} {6,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 O u0 p2 c0 {4,D}
18 O u0 p2 c0 {5,D}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.49268,0.120908,-0.000117135,5.83735e-08,-1.17914e-11,-76212.8,43.9325], Tmin=(100,'K'), Tmax=(1179.92,'K')),
            NASAPolynomial(coeffs=[20.7968,0.0453438,-2.10703e-05,4.09472e-09,-2.90632e-13,-81472.7,-67.2887], Tmin=(1179.92,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 110,
    label = "C(OO)=COC(=O)CCC(C)=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {1,S} {3,S} {18,D}
5  C u0 p0 c0 {2,S} {8,S} {19,D}
6  C u0 p0 c0 {7,D} {8,S} {21,S}
7  C u0 p0 c0 {6,D} {9,S} {20,S}
8  O u0 p2 c0 {5,S} {6,S}
9  O u0 p2 c0 {7,S} {10,S}
10 O u0 p2 c0 {9,S} {22,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 O u0 p2 c0 {4,D}
19 O u0 p2 c0 {5,D}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.595,0.130658,-0.000153112,9.81235e-08,-2.57787e-11,-74522.2,42.6476], Tmin=(100,'K'), Tmax=(916.95,'K')),
            NASAPolynomial(coeffs=[16.3879,0.0522118,-2.47862e-05,4.82551e-09,-3.41859e-13,-77820.1,-42.5504], Tmin=(916.95,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 111,
    label = "C=C(OO)OC(=O)CCC(C)=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {1,S} {3,S} {18,D}
5  C u0 p0 c0 {2,S} {8,S} {19,D}
6  C u0 p0 c0 {7,D} {8,S} {9,S}
7  C u0 p0 c0 {6,D} {20,S} {21,S}
8  O u0 p2 c0 {5,S} {6,S}
9  O u0 p2 c0 {6,S} {10,S}
10 O u0 p2 c0 {9,S} {22,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 O u0 p2 c0 {4,D}
19 O u0 p2 c0 {5,D}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.90931,0.146563,-0.000235373,2.16738e-07,-7.87539e-11,-68307.7,43.672], Tmin=(100,'K'), Tmax=(817.91,'K')),
            NASAPolynomial(coeffs=[7.94761,0.0675702,-3.40402e-05,6.61132e-09,-4.59728e-13,-68890.3,4.39474], Tmin=(817.91,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 112,
    label = "C(=O)C(=O)CC(OO)C(=O)OCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {8,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {7,S} {19,D}
6  C u0 p0 c0 {1,S} {8,S} {20,D}
7  C u0 p0 c0 {5,S} {21,D} {22,S}
8  O u0 p2 c0 {3,S} {6,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {23,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {5,D}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.2252,0.125664,-0.000130145,7.64277e-08,-1.92284e-11,-96261.4,46.2465], Tmin=(100,'K'), Tmax=(932.8,'K')),
            NASAPolynomial(coeffs=[12.9825,0.0647367,-3.2165e-05,6.39895e-09,-4.59148e-13,-98911.9,-21.3085], Tmin=(932.8,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 113,
    label = "CC(=O)C(=O)CC(=O)OC(OO)C",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {8,S} {9,S} {11,S}
2  C u0 p0 c0 {5,S} {7,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {2,S} {6,S} {21,D}
6  C u0 p0 c0 {4,S} {5,S} {20,D}
7  C u0 p0 c0 {2,S} {8,S} {22,D}
8  O u0 p2 c0 {1,S} {7,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {23,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {5,D}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.37443,0.129543,-0.000144107,9.26311e-08,-2.54411e-11,-103047,45.6325], Tmin=(100,'K'), Tmax=(862.01,'K')),
            NASAPolynomial(coeffs=[12.4136,0.065561,-3.27692e-05,6.52305e-09,-4.67751e-13,-105424,-18.8393], Tmin=(862.01,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 114,
    label = "C(OO)C(=O)CC(=O)C(=O)OCC",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {6,S} {11,S} {12,S}
2  C u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
3  C u0 p0 c0 {5,S} {9,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {3,S} {20,D}
6  C u0 p0 c0 {1,S} {7,S} {21,D}
7  C u0 p0 c0 {6,S} {8,S} {22,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {3,S} {10,S}
10 O u0 p2 c0 {9,S} {23,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {5,D}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.96479,0.143186,-0.00018421,1.3711e-07,-4.27087e-11,-94622.1,45.8441], Tmin=(100,'K'), Tmax=(772.92,'K')),
            NASAPolynomial(coeffs=[13.113,0.0651563,-3.27803e-05,6.49861e-09,-4.63204e-13,-96952.9,-23.0141], Tmin=(772.92,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 115,
    label = "CC(=O)CC(=O)C(=O)OC(OO)C",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {8,S} {9,S} {11,S}
2  C u0 p0 c0 {5,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {2,S} {4,S} {20,D}
6  C u0 p0 c0 {2,S} {7,S} {21,D}
7  C u0 p0 c0 {6,S} {8,S} {22,D}
8  O u0 p2 c0 {1,S} {7,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {23,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {5,D}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.63811,0.136117,-0.000164447,1.15685e-07,-3.45142e-11,-101246,45.8728], Tmin=(100,'K'), Tmax=(800.55,'K')),
            NASAPolynomial(coeffs=[12.3402,0.0662732,-3.35793e-05,6.70248e-09,-4.80514e-13,-103484,-18.4548], Tmin=(800.55,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 116,
    label = "CC(=O)CC(OO)C(=O)OC(=O)C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {7,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {2,S} {3,S} {20,D}
6  C u0 p0 c0 {1,S} {8,S} {21,D}
7  C u0 p0 c0 {4,S} {8,S} {22,D}
8  O u0 p2 c0 {6,S} {7,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {23,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {5,D}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.28684,0.126299,-0.000143241,9.33986e-08,-2.57394e-11,-105859,49.5378], Tmin=(100,'K'), Tmax=(864.16,'K')),
            NASAPolynomial(coeffs=[12.8333,0.0609396,-2.97906e-05,5.87594e-09,-4.19168e-13,-108299,-16.522], Tmin=(864.16,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 117,
    label = "CCOC(=O)[CH]C(OO)C(=O)COO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {9,S} {13,S}
2  C u0 p0 c0 {4,S} {8,S} {14,S} {15,S}
3  C u0 p0 c0 {5,S} {10,S} {19,S} {20,S}
4  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {3,S} {21,D}
6  C u1 p0 c0 {1,S} {7,S} {22,S}
7  C u0 p0 c0 {6,S} {8,S} {23,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {1,S} {11,S}
10 O u0 p2 c0 {3,S} {12,S}
11 O u0 p2 c0 {9,S} {24,S}
12 O u0 p2 c0 {10,S} {25,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 O u0 p2 c0 {5,D}
22 H u0 p0 c0 {6,S}
23 O u0 p2 c0 {7,D}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.35268,0.150778,-0.000166809,1.00334e-07,-2.51026e-11,-77782.8,52.2313], Tmin=(100,'K'), Tmax=(951.67,'K')),
            NASAPolynomial(coeffs=[17.8485,0.0658685,-3.29732e-05,6.57736e-09,-4.72615e-13,-81627.7,-44.2265], Tmin=(951.67,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 118,
    label = "CCOC(=O)CC(OO)C(=O)[CH]OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {9,S} {13,S}
2  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
3  C u0 p0 c0 {4,S} {8,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {1,S} {7,S} {21,D}
6  C u0 p0 c0 {2,S} {8,S} {22,D}
7  C u1 p0 c0 {5,S} {10,S} {23,S}
8  O u0 p2 c0 {3,S} {6,S}
9  O u0 p2 c0 {1,S} {11,S}
10 O u0 p2 c0 {7,S} {12,S}
11 O u0 p2 c0 {9,S} {24,S}
12 O u0 p2 c0 {10,S} {25,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {5,D}
22 O u0 p2 c0 {6,D}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.50844,0.155617,-0.000188635,1.29066e-07,-3.68536e-11,-82042.2,52.5], Tmin=(100,'K'), Tmax=(840.1,'K')),
            NASAPolynomial(coeffs=[15.6066,0.0693683,-3.46417e-05,6.86778e-09,-4.90567e-13,-85086,-31.7389], Tmin=(840.1,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 119,
    label = "CCOC(=O)C([CH]C(=O)COO)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {7,S} {9,S} {13,S}
2  C u0 p0 c0 {4,S} {8,S} {14,S} {15,S}
3  C u0 p0 c0 {6,S} {10,S} {19,S} {20,S}
4  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {6,D} {22,S}
6  C u0 p0 c0 {3,S} {5,D} {21,S}
7  C u0 p0 c0 {1,S} {8,S} {23,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {1,S} {12,S}
10 O u0 p2 c0 {3,S} {11,S}
11 O u0 p2 c0 {10,S} {24,S}
12 O u0 p2 c0 {9,S} {25,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 O u1 p2 c0 {6,S}
22 H u0 p0 c0 {5,S}
23 O u0 p2 c0 {7,D}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.30992,0.146725,-0.000160175,9.46497e-08,-2.30477e-11,-81423,53.3518], Tmin=(100,'K'), Tmax=(982.06,'K')),
            NASAPolynomial(coeffs=[18.7469,0.0609564,-2.91673e-05,5.71324e-09,-4.0671e-13,-85558.7,-47.8535], Tmin=(982.06,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 120,
    label = "C[CH]OC(=O)C(CC(=O)COO)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {9,S} {13,S}
2  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
3  C u0 p0 c0 {5,S} {10,S} {16,S} {17,S}
4  C u0 p0 c0 {7,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {2,S} {3,S} {21,D}
6  C u0 p0 c0 {1,S} {8,S} {22,D}
7  C u1 p0 c0 {4,S} {8,S} {23,S}
8  O u0 p2 c0 {6,S} {7,S}
9  O u0 p2 c0 {1,S} {12,S}
10 O u0 p2 c0 {3,S} {11,S}
11 O u0 p2 c0 {10,S} {24,S}
12 O u0 p2 c0 {9,S} {25,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {5,D}
22 O u0 p2 c0 {6,D}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.58511,0.154844,-0.000173883,1.03834e-07,-2.54714e-11,-75865.7,53.6193], Tmin=(100,'K'), Tmax=(975.35,'K')),
            NASAPolynomial(coeffs=[20.0627,0.0619629,-3.10407e-05,6.19966e-09,-4.45955e-13,-80283.7,-55.0781], Tmin=(975.35,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 121,
    label = "CCOC(=O)C(CC(=O)[CH]OO)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {9,S} {13,S}
2  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
3  C u0 p0 c0 {4,S} {8,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {2,S} {7,S} {21,D}
6  C u0 p0 c0 {1,S} {8,S} {22,D}
7  C u1 p0 c0 {5,S} {10,S} {23,S}
8  O u0 p2 c0 {3,S} {6,S}
9  O u0 p2 c0 {1,S} {11,S}
10 O u0 p2 c0 {7,S} {12,S}
11 O u0 p2 c0 {9,S} {25,S}
12 O u0 p2 c0 {10,S} {24,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {5,D}
22 O u0 p2 c0 {6,D}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.50844,0.155617,-0.000188635,1.29066e-07,-3.68536e-11,-82042.2,52.5], Tmin=(100,'K'), Tmax=(840.1,'K')),
            NASAPolynomial(coeffs=[15.6066,0.0693683,-3.46417e-05,6.86778e-09,-4.90567e-13,-85086,-31.7389], Tmin=(840.1,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 122,
    label = "CCOC(=O)C[C](OO)C(=O)COO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {7,S} {15,S} {16,S}
2  C u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
3  C u0 p0 c0 {6,S} {9,S} {20,S} {21,S}
4  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {6,D} {10,S}
6  C u0 p0 c0 {3,S} {5,D} {22,S}
7  C u0 p0 c0 {1,S} {8,S} {23,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {3,S} {11,S}
10 O u0 p2 c0 {5,S} {12,S}
11 O u0 p2 c0 {9,S} {25,S}
12 O u0 p2 c0 {10,S} {24,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 O u1 p2 c0 {6,S}
23 O u0 p2 c0 {7,D}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.94606,0.143007,-0.00015447,9.22139e-08,-2.32309e-11,-79559.9,50.8082], Tmin=(100,'K'), Tmax=(938.11,'K')),
            NASAPolynomial(coeffs=[15.6589,0.0679398,-3.44393e-05,6.91333e-09,-4.9851e-13,-82863,-33.0006], Tmin=(938.11,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 123,
    label = "CCOC(=O)C(OO)[C](OO)C(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {7,S} {9,S} {13,S}
2  C u0 p0 c0 {3,S} {8,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
4  C u0 p0 c0 {6,S} {19,S} {20,S} {21,S}
5  C u0 p0 c0 {1,S} {6,D} {10,S}
6  C u0 p0 c0 {4,S} {5,D} {22,S}
7  C u0 p0 c0 {1,S} {8,S} {23,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {1,S} {11,S}
10 O u0 p2 c0 {5,S} {12,S}
11 O u0 p2 c0 {9,S} {24,S}
12 O u0 p2 c0 {10,S} {25,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 O u1 p2 c0 {6,S}
23 O u0 p2 c0 {7,D}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.3878,0.14937,-0.000170088,1.05287e-07,-2.67997e-11,-82435.3,53.2185], Tmin=(100,'K'), Tmax=(942.98,'K')),
            NASAPolynomial(coeffs=[18.4784,0.0608576,-2.92894e-05,5.74468e-09,-4.0896e-13,-86370.6,-46.2234], Tmin=(942.98,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 124,
    label = "C[CH]OC(=O)C(OO)C(OO)C(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {10,S} {14,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {13,S}
3  C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
4  C u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {3,S} {21,D}
6  C u0 p0 c0 {2,S} {8,S} {22,D}
7  C u1 p0 c0 {4,S} {8,S} {23,S}
8  O u0 p2 c0 {6,S} {7,S}
9  O u0 p2 c0 {2,S} {11,S}
10 O u0 p2 c0 {1,S} {12,S}
11 O u0 p2 c0 {9,S} {24,S}
12 O u0 p2 c0 {10,S} {25,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 O u0 p2 c0 {5,D}
22 O u0 p2 c0 {6,D}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.64661,0.143539,-0.000136603,6.48338e-08,-1.2352e-11,-78815.3,56.6565], Tmin=(100,'K'), Tmax=(1251.9,'K')),
            NASAPolynomial(coeffs=[26.8788,0.0492002,-2.35675e-05,4.63934e-09,-3.31301e-13,-86207.9,-92.4196], Tmin=(1251.9,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 125,
    label = "[CH2]C(=O)C(OO)C(OO)C(=O)OCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {9,S} {13,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {14,S}
3  C u0 p0 c0 {4,S} {8,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {7,D} {20,S}
6  C u0 p0 c0 {2,S} {8,S} {21,D}
7  C u0 p0 c0 {5,D} {22,S} {23,S}
8  O u0 p2 c0 {3,S} {6,S}
9  O u0 p2 c0 {1,S} {11,S}
10 O u0 p2 c0 {2,S} {12,S}
11 O u0 p2 c0 {9,S} {24,S}
12 O u0 p2 c0 {10,S} {25,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u1 p2 c0 {5,S}
21 O u0 p2 c0 {6,D}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.71712,0.146349,-0.000146883,7.5047e-08,-1.5395e-11,-82157.2,55.4105], Tmin=(100,'K'), Tmax=(1170.42,'K')),
            NASAPolynomial(coeffs=[25.5781,0.0496468,-2.29487e-05,4.4533e-09,-3.16122e-13,-88780.6,-85.5498], Tmin=(1170.42,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 126,
    label = "CCOC(=O)[C](CC(=O)COO)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {15,S} {16,S}
2  C u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
3  C u0 p0 c0 {6,S} {9,S} {20,S} {21,S}
4  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
5  C u1 p0 c0 {1,S} {7,S} {10,S}
6  C u0 p0 c0 {1,S} {3,S} {22,D}
7  C u0 p0 c0 {5,S} {8,S} {23,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {3,S} {11,S}
10 O u0 p2 c0 {5,S} {12,S}
11 O u0 p2 c0 {9,S} {24,S}
12 O u0 p2 c0 {10,S} {25,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 O u0 p2 c0 {6,D}
23 O u0 p2 c0 {7,D}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.59843,0.158332,-0.000209548,1.62384e-07,-5.2693e-11,-76217.3,53.3452], Tmin=(100,'K'), Tmax=(743.42,'K')),
            NASAPolynomial(coeffs=[13.3371,0.0725866,-3.65336e-05,7.2261e-09,-5.13711e-13,-78586.6,-18.809], Tmin=(743.42,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 127,
    label = "CCOC(=O)[C](OO)C(OO)C(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {9,S} {13,S}
2  C u0 p0 c0 {3,S} {8,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
4  C u0 p0 c0 {6,S} {19,S} {20,S} {21,S}
5  C u1 p0 c0 {1,S} {7,S} {10,S}
6  C u0 p0 c0 {1,S} {4,S} {22,D}
7  C u0 p0 c0 {5,S} {8,S} {23,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {1,S} {11,S}
10 O u0 p2 c0 {5,S} {12,S}
11 O u0 p2 c0 {9,S} {25,S}
12 O u0 p2 c0 {10,S} {24,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 O u0 p2 c0 {6,D}
23 O u0 p2 c0 {7,D}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.78641,0.136352,-0.000133226,7.01387e-08,-1.55249e-11,-79203.9,53.2756], Tmin=(100,'K'), Tmax=(1058.33,'K')),
            NASAPolynomial(coeffs=[17.1213,0.0648907,-3.19441e-05,6.34014e-09,-4.54554e-13,-83206.1,-39.0152], Tmin=(1058.33,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 128,
    label = "[CH2]C(OO)OC(=O)C(CC(C)=O)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {9,S} {13,S}
2  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
3  C u0 p0 c0 {7,S} {8,S} {10,S} {16,S}
4  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {2,S} {4,S} {20,D}
6  C u0 p0 c0 {1,S} {8,S} {21,D}
7  C u1 p0 c0 {3,S} {22,S} {23,S}
8  O u0 p2 c0 {3,S} {6,S}
9  O u0 p2 c0 {1,S} {12,S}
10 O u0 p2 c0 {3,S} {11,S}
11 O u0 p2 c0 {10,S} {24,S}
12 O u0 p2 c0 {9,S} {25,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {5,D}
21 O u0 p2 c0 {6,D}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.22516,0.148443,-0.000166822,1.03281e-07,-2.67005e-11,-79585.5,54.9137], Tmin=(100,'K'), Tmax=(921.4,'K')),
            NASAPolynomial(coeffs=[16.6765,0.0663871,-3.32378e-05,6.62758e-09,-4.75957e-13,-83068.7,-34.7286], Tmin=(921.4,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 129,
    label = "CC(=O)C[C](OO)C(=O)OC(C)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {8,S} {9,S} {13,S}
2  C u0 p0 c0 {5,S} {6,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
4  C u0 p0 c0 {6,S} {19,S} {20,S} {21,S}
5  C u1 p0 c0 {2,S} {7,S} {10,S}
6  C u0 p0 c0 {2,S} {4,S} {22,D}
7  C u0 p0 c0 {5,S} {8,S} {23,D}
8  O u0 p2 c0 {1,S} {7,S}
9  O u0 p2 c0 {1,S} {11,S}
10 O u0 p2 c0 {5,S} {12,S}
11 O u0 p2 c0 {9,S} {25,S}
12 O u0 p2 c0 {10,S} {24,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 O u0 p2 c0 {6,D}
23 O u0 p2 c0 {7,D}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.26814,0.151181,-0.000189288,1.3996e-07,-4.38852e-11,-82841.3,53.3633], Tmin=(100,'K'), Tmax=(764.19,'K')),
            NASAPolynomial(coeffs=[12.5151,0.0737988,-3.73928e-05,7.44514e-09,-5.32341e-13,-85100.7,-13.9809], Tmin=(764.19,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 130,
    label = "CC(=O)[CH]C(OO)C(=O)OC(C)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {7,S} {9,S} {13,S}
2  C u0 p0 c0 {3,S} {8,S} {10,S} {14,S}
3  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {1,S} {6,D} {22,S}
6  C u0 p0 c0 {4,S} {5,D} {21,S}
7  C u0 p0 c0 {1,S} {8,S} {23,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {1,S} {11,S}
10 O u0 p2 c0 {2,S} {12,S}
11 O u0 p2 c0 {9,S} {24,S}
12 O u0 p2 c0 {10,S} {25,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u1 p2 c0 {6,S}
22 H u0 p0 c0 {5,S}
23 O u0 p2 c0 {7,D}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.35592,0.14625,-0.000153951,8.56654e-08,-1.95369e-11,-87084.3,52.9151], Tmin=(100,'K'), Tmax=(1046.34,'K')),
            NASAPolynomial(coeffs=[20.5871,0.0585437,-2.8219e-05,5.55745e-09,-3.97109e-13,-91885.6,-58.8115], Tmin=(1046.34,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 131,
    label = "CC(=O)C([CH]C(=O)OC(C)OO)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {10,S} {13,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {14,S}
3  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {1,S} {4,S} {21,D}
6  C u1 p0 c0 {1,S} {7,S} {22,S}
7  C u0 p0 c0 {6,S} {8,S} {23,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {2,S} {11,S}
10 O u0 p2 c0 {1,S} {12,S}
11 O u0 p2 c0 {9,S} {24,S}
12 O u0 p2 c0 {10,S} {25,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {5,D}
22 H u0 p0 c0 {6,S}
23 O u0 p2 c0 {7,D}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.07723,0.144499,-0.000150678,8.48714e-08,-2.00192e-11,-84404.7,52.4316], Tmin=(100,'K'), Tmax=(1000.66,'K')),
            NASAPolynomial(coeffs=[17.5131,0.0661887,-3.32897e-05,6.66315e-09,-4.79868e-13,-88325.3,-42.093], Tmin=(1000.66,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 132,
    label = "[CH2]C(=O)C(CC(=O)OC(C)OO)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {9,S} {13,S}
2  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
3  C u0 p0 c0 {4,S} {8,S} {10,S} {16,S}
4  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {7,D} {20,S}
6  C u0 p0 c0 {2,S} {8,S} {21,D}
7  C u0 p0 c0 {5,D} {22,S} {23,S}
8  O u0 p2 c0 {3,S} {6,S}
9  O u0 p2 c0 {1,S} {12,S}
10 O u0 p2 c0 {3,S} {11,S}
11 O u0 p2 c0 {10,S} {24,S}
12 O u0 p2 c0 {9,S} {25,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u1 p2 c0 {5,S}
21 O u0 p2 c0 {6,D}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.55899,0.153464,-0.000175164,1.07478e-07,-2.70442e-11,-85821.9,53.2151], Tmin=(100,'K'), Tmax=(954.03,'K')),
            NASAPolynomial(coeffs=[19.4972,0.0609881,-2.97668e-05,5.87556e-09,-4.19817e-13,-90030.4,-52.1551], Tmin=(954.03,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 133,
    label = "C[C](OO)OC(=O)C(CC(C)=O)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {9,S} {13,S}
2  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
3  C u0 p0 c0 {5,S} {19,S} {20,S} {21,S}
4  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {3,S} {22,D}
6  C u1 p0 c0 {4,S} {8,S} {10,S}
7  C u0 p0 c0 {1,S} {8,S} {23,D}
8  O u0 p2 c0 {6,S} {7,S}
9  O u0 p2 c0 {1,S} {11,S}
10 O u0 p2 c0 {6,S} {12,S}
11 O u0 p2 c0 {9,S} {25,S}
12 O u0 p2 c0 {10,S} {24,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 O u0 p2 c0 {5,D}
23 O u0 p2 c0 {7,D}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.09881,0.146147,-0.000162893,1.01209e-07,-2.64532e-11,-80638.9,53.155], Tmin=(100,'K'), Tmax=(908.74,'K')),
            NASAPolynomial(coeffs=[15.6069,0.0682121,-3.42531e-05,6.83749e-09,-4.91275e-13,-83856.9,-30.5707], Tmin=(908.74,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 134,
    label = "[CH2]C(=O)CC(OO)C(=O)OC(C)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {9,S} {13,S}
2  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
3  C u0 p0 c0 {4,S} {8,S} {10,S} {16,S}
4  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {2,S} {7,D} {20,S}
6  C u0 p0 c0 {1,S} {8,S} {21,D}
7  C u0 p0 c0 {5,D} {22,S} {23,S}
8  O u0 p2 c0 {3,S} {6,S}
9  O u0 p2 c0 {1,S} {11,S}
10 O u0 p2 c0 {3,S} {12,S}
11 O u0 p2 c0 {9,S} {24,S}
12 O u0 p2 c0 {10,S} {25,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u1 p2 c0 {5,S}
21 O u0 p2 c0 {6,D}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.55749,0.145064,-0.000145273,7.46056e-08,-1.54825e-11,-85463.2,54.7317], Tmin=(100,'K'), Tmax=(1152.62,'K')),
            NASAPolynomial(coeffs=[24.164,0.0523296,-2.45877e-05,4.80075e-09,-3.41722e-13,-91623,-77.9789], Tmin=(1152.62,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 135,
    label = "CC(=O)CCC(=O)O[C](COO)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
3  C u0 p0 c0 {6,S} {9,S} {17,S} {18,S}
4  C u0 p0 c0 {5,S} {19,S} {20,S} {21,S}
5  C u0 p0 c0 {1,S} {4,S} {22,D}
6  C u1 p0 c0 {3,S} {8,S} {10,S}
7  C u0 p0 c0 {2,S} {8,S} {23,D}
8  O u0 p2 c0 {6,S} {7,S}
9  O u0 p2 c0 {3,S} {11,S}
10 O u0 p2 c0 {6,S} {12,S}
11 O u0 p2 c0 {9,S} {24,S}
12 O u0 p2 c0 {10,S} {25,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 O u0 p2 c0 {5,D}
23 O u0 p2 c0 {7,D}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.08574,0.172067,-0.000263664,2.33377e-07,-8.34002e-11,-79399.6,54.5403], Tmin=(100,'K'), Tmax=(786.92,'K')),
            NASAPolynomial(coeffs=[11.637,0.0755552,-3.8383e-05,7.52079e-09,-5.27516e-13,-81045.6,-8.69667], Tmin=(786.92,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 136,
    label = "CC(=O)CCC(=O)OC([CH]OO)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {6,S} {15,S} {16,S}
3  C u0 p0 c0 {7,S} {8,S} {9,S} {17,S}
4  C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {1,S} {4,S} {21,D}
6  C u0 p0 c0 {2,S} {8,S} {22,D}
7  C u1 p0 c0 {3,S} {10,S} {23,S}
8  O u0 p2 c0 {3,S} {6,S}
9  O u0 p2 c0 {3,S} {11,S}
10 O u0 p2 c0 {7,S} {12,S}
11 O u0 p2 c0 {9,S} {25,S}
12 O u0 p2 c0 {10,S} {24,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {5,D}
22 O u0 p2 c0 {6,D}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.14869,0.174431,-0.000271347,2.42832e-07,-8.7197e-11,-81402.5,54.2267], Tmin=(100,'K'), Tmax=(795.52,'K')),
            NASAPolynomial(coeffs=[11.1232,0.0769815,-3.91624e-05,7.66323e-09,-5.36514e-13,-82860.3,-6.25314], Tmin=(795.52,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 137,
    label = "CC(=O)C[CH]C(=O)OC(COO)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {8,S} {9,S} {13,S}
2  C u0 p0 c0 {5,S} {6,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {10,S} {16,S} {17,S}
4  C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {2,S} {4,S} {21,D}
6  C u1 p0 c0 {2,S} {7,S} {22,S}
7  C u0 p0 c0 {6,S} {8,S} {23,D}
8  O u0 p2 c0 {1,S} {7,S}
9  O u0 p2 c0 {1,S} {12,S}
10 O u0 p2 c0 {3,S} {11,S}
11 O u0 p2 c0 {10,S} {24,S}
12 O u0 p2 c0 {9,S} {25,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {5,D}
22 H u0 p0 c0 {6,S}
23 O u0 p2 c0 {7,D}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.88341,0.151588,-0.000153484,1.62231e-08,6.39463e-11,-83215.6,49.8453], Tmin=(100,'K'), Tmax=(512.87,'K')),
            NASAPolynomial(coeffs=[12.664,0.0751931,-3.84516e-05,7.60365e-09,-5.38308e-13,-85195.3,-15.3759], Tmin=(512.87,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 138,
    label = "CC(=O)[CH]CC(=O)OC(COO)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {8,S} {9,S} {13,S}
2  C u0 p0 c0 {5,S} {7,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {10,S} {16,S} {17,S}
4  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {2,S} {6,D} {22,S}
6  C u0 p0 c0 {4,S} {5,D} {21,S}
7  C u0 p0 c0 {2,S} {8,S} {23,D}
8  O u0 p2 c0 {1,S} {7,S}
9  O u0 p2 c0 {1,S} {12,S}
10 O u0 p2 c0 {3,S} {11,S}
11 O u0 p2 c0 {10,S} {24,S}
12 O u0 p2 c0 {9,S} {25,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u1 p2 c0 {6,S}
22 H u0 p0 c0 {5,S}
23 O u0 p2 c0 {7,D}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.02083,0.144211,-0.000149787,8.35407e-08,-1.9547e-11,-85011.6,49.8396], Tmin=(100,'K'), Tmax=(1006.11,'K')),
            NASAPolynomial(coeffs=[17.4987,0.0666069,-3.40877e-05,6.87652e-09,-4.97331e-13,-88939.3,-44.4501], Tmin=(1006.11,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 139,
    label = "CCOC(=O)C(OO)=CC(=O)C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
3  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
4  C u0 p0 c0 {6,D} {7,S} {9,S}
5  C u0 p0 c0 {3,S} {6,S} {19,D}
6  C u0 p0 c0 {4,D} {5,S} {20,S}
7  C u0 p0 c0 {4,S} {8,S} {21,D}
8  O u0 p2 c0 {1,S} {7,S}
9  O u0 p2 c0 {4,S} {10,S}
10 O u0 p2 c0 {9,S} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 O u0 p2 c0 {5,D}
20 H u0 p0 c0 {6,S}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.46612,0.134963,-0.000208333,1.92161e-07,-7.12225e-11,-62893.6,44.8149], Tmin=(100,'K'), Tmax=(795.17,'K')),
            NASAPolynomial(coeffs=[6.89696,0.0678404,-3.44527e-05,6.75672e-09,-4.7403e-13,-63431.6,11.3651], Tmin=(795.17,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 140,
    label = "CC1OC(=O)C1CC(=O)COO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {6,S} {9,S} {18,S} {19,S}
6  C u0 p0 c0 {3,S} {5,S} {20,D}
7  C u0 p0 c0 {1,S} {8,S} {21,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {5,S} {10,S}
10 O u0 p2 c0 {9,S} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.45213,0.108476,-9.11633e-05,4.03288e-08,-7.19987e-12,-71672.3,42.2964], Tmin=(100,'K'), Tmax=(1339.08,'K')),
            NASAPolynomial(coeffs=[21.1085,0.0410845,-1.56735e-05,2.74598e-09,-1.83346e-13,-77714.4,-73.1332], Tmin=(1339.08,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 141,
    label = "CC(=O)C(OO)C1C(=O)OC1C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {9,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {3,S} {5,S} {20,D}
7  C u0 p0 c0 {1,S} {8,S} {21,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {3,S} {10,S}
10 O u0 p2 c0 {9,S} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.952459,0.0902792,-2.89177e-05,-3.14818e-08,1.98185e-11,-74645.1,43.3437], Tmin=(100,'K'), Tmax=(979.32,'K')),
            NASAPolynomial(coeffs=[22.3496,0.0376727,-1.35453e-05,2.44068e-09,-1.72344e-13,-81250.6,-79.0107], Tmin=(979.32,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 142,
    label = "CC(=O)CC1C(=O)OC1(C)OO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {3,S} {5,S} {20,D}
7  C u0 p0 c0 {1,S} {8,S} {21,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {2,S} {10,S}
10 O u0 p2 c0 {9,S} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.60806,0.100135,-3.21732e-05,-4.75824e-08,3.07791e-11,-79702.6,40.7119], Tmin=(100,'K'), Tmax=(935.51,'K')),
            NASAPolynomial(coeffs=[29.4577,0.0257755,-6.69667e-06,1.0725e-09,-7.72583e-14,-88073.6,-120.766], Tmin=(935.51,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 143,
    label = "CC(=O)C1C(C)OC(=O)C1OO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {9,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {1,S} {5,S} {20,D}
7  C u0 p0 c0 {3,S} {8,S} {21,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {3,S} {10,S}
10 O u0 p2 c0 {9,S} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.663893,0.0812566,-2.4987e-06,-5.86353e-08,2.93517e-11,-82093,41.2649], Tmin=(100,'K'), Tmax=(971.05,'K')),
            NASAPolynomial(coeffs=[22.1965,0.0376642,-1.32848e-05,2.40517e-09,-1.71884e-13,-88917.2,-80.6294], Tmin=(971.05,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 144,
    label = "CC(=O)C1CC(=O)OC1COO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {9,S} {15,S} {16,S}
5  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {1,S} {5,S} {20,D}
7  C u0 p0 c0 {3,S} {8,S} {21,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {4,S} {10,S}
10 O u0 p2 c0 {9,S} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.21372,0.101027,-7.6629e-05,3.05264e-08,-4.93901e-12,-80871.8,41.8373], Tmin=(100,'K'), Tmax=(1461,'K')),
            NASAPolynomial(coeffs=[20.4765,0.0416419,-1.56576e-05,2.70436e-09,-1.78161e-13,-87209.6,-71.0287], Tmin=(1461,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 145,
    label = "CC(=O)CC1(OO)C(=O)OC1C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {3,S} {5,S} {20,D}
7  C u0 p0 c0 {1,S} {8,S} {21,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {22,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.55289,0.109669,-8.67383e-05,2.90731e-08,-1.53724e-12,-75154.5,40.6211], Tmin=(100,'K'), Tmax=(1016.23,'K')),
            NASAPolynomial(coeffs=[21.9875,0.0387385,-1.41115e-05,2.46688e-09,-1.67442e-13,-81060.9,-78.8468], Tmin=(1016.23,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 146,
    label = "CC(=O)CC1C(=O)OC1COO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {9,S} {15,S} {16,S}
5  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {3,S} {5,S} {20,D}
7  C u0 p0 c0 {1,S} {8,S} {21,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {4,S} {10,S}
10 O u0 p2 c0 {9,S} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.09391,0.10546,-8.80173e-05,3.95645e-08,-7.29831e-12,-73442.1,41.7425], Tmin=(100,'K'), Tmax=(1282.68,'K')),
            NASAPolynomial(coeffs=[18.0693,0.0457005,-1.81333e-05,3.24293e-09,-2.19111e-13,-78358.2,-55.4798], Tmin=(1282.68,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 147,
    label = "CCOC(=O)C(OO)C1OCC1=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {8,S} {13,S}
2  C u0 p0 c0 {1,S} {7,S} {10,S} {12,S}
3  C u0 p0 c0 {5,S} {9,S} {14,S} {15,S}
4  C u0 p0 c0 {6,S} {8,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {4,S} {21,D}
7  C u0 p0 c0 {2,S} {9,S} {22,D}
8  O u0 p2 c0 {1,S} {4,S}
9  O u0 p2 c0 {3,S} {7,S}
10 O u0 p2 c0 {2,S} {11,S}
11 O u0 p2 c0 {10,S} {23,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.59355,0.101602,-4.3764e-05,-1.72159e-08,1.31313e-11,-85787.4,49.0221], Tmin=(100,'K'), Tmax=(1073.13,'K')),
            NASAPolynomial(coeffs=[25.9817,0.0410636,-1.81964e-05,3.58561e-09,-2.61004e-13,-94138.3,-97.2926], Tmin=(1073.13,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 148,
    label = "CCOC(=O)CC1(OO)OCC1=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {9,S} {14,S} {15,S}
4  C u0 p0 c0 {6,S} {8,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {4,S} {21,D}
7  C u0 p0 c0 {2,S} {9,S} {22,D}
8  O u0 p2 c0 {1,S} {4,S}
9  O u0 p2 c0 {3,S} {7,S}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {10,S} {23,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.37937,0.118698,-7.53881e-05,2.35585e-09,9.61657e-12,-90940.4,45.2734], Tmin=(100,'K'), Tmax=(1030.51,'K')),
            NASAPolynomial(coeffs=[30.4522,0.033859,-1.39041e-05,2.6938e-09,-1.96872e-13,-99969,-125.081], Tmin=(1030.51,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 149,
    label = "CCOC(=O)C1OCC(=O)C1OO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {13,S}
3  C u0 p0 c0 {5,S} {9,S} {14,S} {15,S}
4  C u0 p0 c0 {6,S} {8,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {4,S} {21,D}
7  C u0 p0 c0 {1,S} {9,S} {22,D}
8  O u0 p2 c0 {1,S} {4,S}
9  O u0 p2 c0 {3,S} {7,S}
10 O u0 p2 c0 {2,S} {11,S}
11 O u0 p2 c0 {10,S} {23,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.20171,0.0899509,-1.0192e-05,-5.29549e-08,2.61691e-11,-95632.7,47.1094], Tmin=(100,'K'), Tmax=(1024.14,'K')),
            NASAPolynomial(coeffs=[25.5267,0.0400282,-1.68537e-05,3.31504e-09,-2.44207e-13,-103964,-96.4235], Tmin=(1024.14,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 150,
    label = "CCOC(=O)C1(OO)CC(=O)CO1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {9,S} {14,S} {15,S}
4  C u0 p0 c0 {6,S} {8,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {4,S} {21,D}
7  C u0 p0 c0 {1,S} {9,S} {22,D}
8  O u0 p2 c0 {1,S} {4,S}
9  O u0 p2 c0 {3,S} {7,S}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {10,S} {23,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.98608,0.106985,-4.13711e-05,-3.43127e-08,2.3214e-11,-100786,44.0516], Tmin=(100,'K'), Tmax=(992.64,'K')),
            NASAPolynomial(coeffs=[30.2599,0.032406,-1.23323e-05,2.37112e-09,-1.75875e-13,-109915,-125.017], Tmin=(992.64,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 151,
    label = "CCOC(=O)CC1OC(OO)C1=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {8,S} {12,S}
2  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
3  C u0 p0 c0 {6,S} {8,S} {10,S} {17,S}
4  C u0 p0 c0 {5,S} {9,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {1,S} {3,S} {21,D}
7  C u0 p0 c0 {2,S} {9,S} {22,D}
8  O u0 p2 c0 {1,S} {3,S}
9  O u0 p2 c0 {4,S} {7,S}
10 O u0 p2 c0 {3,S} {11,S}
11 O u0 p2 c0 {10,S} {23,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.37034,0.109337,-8.05367e-05,2.85105e-08,-4.04571e-12,-91191.7,46.5833], Tmin=(100,'K'), Tmax=(1633.1,'K')),
            NASAPolynomial(coeffs=[25.5442,0.0434143,-1.99861e-05,3.79233e-09,-2.61745e-13,-99982.5,-96.4646], Tmin=(1633.1,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 152,
    label = "CC(OO)OC(=O)CC1OCC1=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {8,S} {12,S}
2  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
3  C u0 p0 c0 {5,S} {9,S} {10,S} {13,S}
4  C u0 p0 c0 {6,S} {8,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {4,S} {21,D}
7  C u0 p0 c0 {2,S} {9,S} {22,D}
8  O u0 p2 c0 {1,S} {4,S}
9  O u0 p2 c0 {3,S} {7,S}
10 O u0 p2 c0 {3,S} {11,S}
11 O u0 p2 c0 {10,S} {23,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.76914,0.112595,-8.50539e-05,3.07551e-08,-4.41307e-12,-89438,48.0241], Tmin=(100,'K'), Tmax=(1639.22,'K')),
            NASAPolynomial(coeffs=[28.4493,0.0388563,-1.75773e-05,3.3124e-09,-2.27732e-13,-99344.9,-112.697], Tmin=(1639.22,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 153,
    label = "CCOC(=O)C1OC1C(=O)COO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {8,S} {13,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {12,S}
3  C u0 p0 c0 {5,S} {9,S} {14,S} {15,S}
4  C u0 p0 c0 {6,S} {10,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {4,S} {21,D}
7  C u0 p0 c0 {2,S} {9,S} {22,D}
8  O u0 p2 c0 {1,S} {2,S}
9  O u0 p2 c0 {3,S} {7,S}
10 O u0 p2 c0 {4,S} {11,S}
11 O u0 p2 c0 {10,S} {23,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.95195,0.115188,-8.08869e-05,1.46054e-08,5.07042e-12,-85703.3,48.3984], Tmin=(100,'K'), Tmax=(990.38,'K')),
            NASAPolynomial(coeffs=[24.9639,0.0387475,-1.39852e-05,2.46895e-09,-1.70317e-13,-92617.3,-89.1844], Tmin=(990.38,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 154,
    label = "CCOC(=O)C(OO)1OC1C(=O)C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {12,S}
3  C u0 p0 c0 {4,S} {9,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {2,S} {5,S} {21,D}
7  C u0 p0 c0 {1,S} {9,S} {22,D}
8  O u0 p2 c0 {1,S} {2,S}
9  O u0 p2 c0 {3,S} {7,S}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {10,S} {23,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.31472,0.114738,-5.11928e-05,-3.86602e-08,3.01003e-11,-93825.7,45.9871], Tmin=(100,'K'), Tmax=(926.77,'K')),
            NASAPolynomial(coeffs=[33.0205,0.02436,-5.47622e-06,7.93084e-10,-5.63654e-14,-103043,-136.193], Tmin=(926.77,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 155,
    label = "CC(OO)OC(=O)C1OC1C(=O)C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {8,S} {13,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {12,S}
3  C u0 p0 c0 {4,S} {9,S} {10,S} {14,S}
4  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {1,S} {5,S} {21,D}
7  C u0 p0 c0 {2,S} {9,S} {22,D}
8  O u0 p2 c0 {1,S} {2,S}
9  O u0 p2 c0 {3,S} {7,S}
10 O u0 p2 c0 {3,S} {11,S}
11 O u0 p2 c0 {10,S} {23,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.76372,0.109868,-6.78192e-05,2.76993e-09,8.72249e-12,-92321.4,48.9162], Tmin=(100,'K'), Tmax=(994.82,'K')),
            NASAPolynomial(coeffs=[24.5845,0.039177,-1.43799e-05,2.57599e-09,-1.79509e-13,-99308,-86.8287], Tmin=(994.82,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 156,
    label = "CCOC(=O)C1CC(=O)C(OO)O1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {6,S} {8,S} {10,S} {17,S}
4  C u0 p0 c0 {5,S} {9,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {2,S} {3,S} {21,D}
7  C u0 p0 c0 {1,S} {9,S} {22,D}
8  O u0 p2 c0 {1,S} {3,S}
9  O u0 p2 c0 {4,S} {7,S}
10 O u0 p2 c0 {3,S} {11,S}
11 O u0 p2 c0 {10,S} {23,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.42207,0.102706,-6.3699e-05,1.35155e-08,5.13155e-13,-101017,46.9716], Tmin=(100,'K'), Tmax=(1250.59,'K')),
            NASAPolynomial(coeffs=[23.316,0.0448851,-1.98986e-05,3.78771e-09,-2.65203e-13,-108870,-84.5675], Tmin=(1250.59,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 157,
    label = "CC(OO)OC(=O)C1CC(=O)CO1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
3  C u0 p0 c0 {5,S} {9,S} {10,S} {13,S}
4  C u0 p0 c0 {6,S} {8,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {4,S} {21,D}
7  C u0 p0 c0 {1,S} {9,S} {22,D}
8  O u0 p2 c0 {1,S} {4,S}
9  O u0 p2 c0 {3,S} {7,S}
10 O u0 p2 c0 {3,S} {11,S}
11 O u0 p2 c0 {10,S} {23,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.46016,0.102118,-5.65124e-05,2.80679e-09,4.81394e-12,-99280,47.0889], Tmin=(100,'K'), Tmax=(1148.71,'K')),
            NASAPolynomial(coeffs=[23.5953,0.0443888,-1.96734e-05,3.79706e-09,-2.70161e-13,-106984,-85.7399], Tmin=(1148.71,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 158,
    label = "CCOC(=O)C1OC(OO)1C(=O)C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {12,S}
3  C u0 p0 c0 {4,S} {9,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {1,S} {5,S} {21,D}
7  C u0 p0 c0 {2,S} {9,S} {22,D}
8  O u0 p2 c0 {1,S} {2,S}
9  O u0 p2 c0 {3,S} {7,S}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {10,S} {23,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.31472,0.114738,-5.11928e-05,-3.86602e-08,3.01003e-11,-93825.7,45.9871], Tmin=(100,'K'), Tmax=(926.77,'K')),
            NASAPolynomial(coeffs=[33.0205,0.02436,-5.47622e-06,7.93084e-10,-5.63654e-14,-103043,-136.193], Tmin=(926.77,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 159,
    label = "CC(=O)C(OO)CC(=O)OC(=O)C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {7,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {3,S} {20,D}
6  C u0 p0 c0 {2,S} {8,S} {21,D}
7  C u0 p0 c0 {4,S} {8,S} {22,D}
8  O u0 p2 c0 {6,S} {7,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {23,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {5,D}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.28684,0.126299,-0.000143241,9.33986e-08,-2.57394e-11,-105859,49.5378], Tmin=(100,'K'), Tmax=(864.16,'K')),
            NASAPolynomial(coeffs=[12.8333,0.0609396,-2.97906e-05,5.87594e-09,-4.19168e-13,-108299,-16.522], Tmin=(864.16,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 160,
    label = "CO",
    molecule = 
"""
1 O u0 p1 c+1 {2,T}
2 C u0 p1 c-1 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59508,-0.000721197,1.28238e-06,6.52429e-10,-8.21715e-13,-14344.9,3.44356], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.03397,0.00137328,-4.96445e-07,8.10281e-11,-4.85332e-15,-14258.6,6.10076], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 161,
    label = "CO2",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.20664,0.010097,-9.96339e-06,5.47156e-09,-1.27734e-12,-48353,10.5262], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.63537,0.00274559,-9.98282e-07,1.61014e-10,-9.22019e-15,-49020.4,-1.92888], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 162,
    label = "HOCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 C u1 p0 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.82191,0.00966218,-2.7856e-06,-4.12692e-09,2.61472e-12,-23546.5,11.4285], Tmin=(200,'K'), Tmax=(998.4,'K')),
            NASAPolynomial(coeffs=[4.63989,0.00566363,-2.67855e-06,6.17049e-10,-5.60954e-14,-24052.7,1.90175], Tmin=(998.4,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 163,
    label = "HCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97075,-0.00149122,9.54042e-06,-8.8272e-09,2.67645e-12,3842.03,4.4466], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.85781,0.00264114,-7.44177e-07,1.23313e-10,-8.88959e-15,3616.43,3.92451], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 164,
    label = "CH2",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74843,0.00107656,3.62462e-06,-4.46166e-09,1.95225e-12,45899,1.63509], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.81413,0.00379513,-7.38425e-07,7.19949e-11,-2.63189e-15,46186,6.52946], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 165,
    label = "CH2(S)",
    molecule = 
"""
1 C u0 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.1849,-0.00216397,7.68524e-06,-5.98243e-09,1.6791e-12,50392.3,-0.717772], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.86931,0.00339757,-1.006e-06,1.50563e-10,-8.61238e-15,50628.5,5.53164], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 166,
    label = "CH",
    molecule = 
"""
multiplicity 2
1 C u1 p1 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49602,0.000277424,-1.57434e-06,3.07039e-09,-1.40468e-12,70650,2.05802], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.74989,0.00136248,-2.71161e-07,2.47828e-11,-1.18068e-15,70899.9,6.13979], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 167,
    label = "CH3OH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.52796,-0.0138922,6.21716e-05,-6.82045e-08,2.52019e-11,-25596.8,-0.715601], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.71776,0.0100962,-3.53785e-06,5.61843e-10,-3.32714e-14,-26022.2,4.04183], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 168,
    label = "CH2OH",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.40537,-0.000758358,2.61926e-05,-3.46319e-08,1.4082e-11,-3442.28,3.60691], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.20504,0.00243666,1.94377e-06,-1.61013e-09,3.14355e-13,-4258.44,-7.46071], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 169,
    label = "HCOH",
    molecule = 
"""
1 O u0 p1 c+1 {2,D} {4,S}
2 C u0 p1 c-1 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.65733,-0.00953742,4.04679e-05,-4.45318e-08,1.64762e-11,13861.5,1.97861], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.65237,0.00555807,-1.97617e-06,3.16823e-10,-1.88748e-14,13553.6,4.22141], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 170,
    label = "C-2",
    molecule = 
"""
multiplicity 3
1 C u2 p1 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.55138,-0.000299926,6.79035e-07,-6.75577e-10,2.46001e-13,85469.3,4.54305], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.60607,-0.000196384,1.0681e-07,-1.6408e-11,8.15424e-16,85437.8,4.18935], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 171,
    label = "C2H2",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.626264,0.0247264,-3.89556e-05,3.16485e-08,-9.87351e-12,26455.6,14.6968], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.66166,0.00488862,-1.61257e-06,2.48284e-10,-1.39737e-14,25769.5,-4.01062], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 172,
    label = "C2H",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {3,S}
2 C u1 p0 c0 {1,T}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.89868,0.0132988,-2.80733e-05,2.89485e-08,-1.07502e-11,67061.6,6.18548], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.6627,0.00382492,-1.36633e-06,2.13455e-10,-1.23217e-14,67168.4,3.92206], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 173,
    label = "CH3OOH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {7,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.85837,0.0159701,-2.52104e-06,-5.736e-09,2.80535e-12,-16883,12.897], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.45931,0.0141051,-6.53177e-06,1.47663e-09,-1.32512e-13,-17430.1,4.03867], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 174,
    label = "CH2OOH",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.83127,-0.00351771,4.54551e-05,-5.66903e-08,2.21633e-11,6061.87,-0.579143], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.98746,0.00900484,-3.24367e-06,5.24325e-10,-3.13587e-14,5012.58,-10.2619], Tmin=(1000,'K'), Tmax=(2500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (2500,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 175,
    label = "HOCH2O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 O u1 p2 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.97309,0.0426372,-5.84444e-05,4.12219e-08,-1.13585e-11,-21382.8,32.869], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.64142,0.0146739,-8.24143e-06,2.2479e-09,-2.38671e-13,-22230.4,7.15858], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 176,
    label = "HOCHO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89836,-0.00355878,3.55205e-05,-4.385e-08,1.71078e-11,-46778.6,7.34954], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.61383,0.00644964,-2.29083e-06,3.6716e-10,-2.18737e-14,-45330.3,0.847884], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 177,
    label = "C2H6",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.14633,-0.00442384,5.70676e-05,-6.76419e-08,2.57224e-11,-11514.5,3.26636], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.97869,0.0154587,-5.37527e-06,8.59587e-10,-5.11298e-14,-12444.6,-0.62717], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 178,
    label = "CH2CH2OOH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {7,S} {8,S}
3 O u0 p2 c0 {1,S} {4,S}
4 O u0 p2 c0 {3,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.07456,0.013239,2.53759e-05,-4.3809e-08,1.89062e-11,3710.63,2.7229], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.4138,0.0133542,-4.68068e-06,7.43231e-10,-4.39824e-14,1984.6,-22.4517], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 179,
    label = "cC2H4O",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75905,-0.00944122,8.03097e-05,-1.00808e-07,4.00399e-11,-7560.81,7.84975], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.48876,0.0120462,-4.33369e-06,7.00283e-10,-4.19491e-14,-9180.43,-7.07996], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 180,
    label = "CH2CHO",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.66874,0.0096233,1.60617e-05,-2.87682e-08,1.2503e-11,219.438,12.5694], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.91637,0.0088465,-3.14955e-06,5.05413e-10,-3.01305e-14,-1047.8,-6.1065], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 181,
    label = "H2CC",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p1 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78898,0.00591795,-1.08086e-06,-1.85638e-09,1.06887e-12,48196,3.71766], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.47848,0.00484708,-1.76213e-06,2.92788e-10,-1.76554e-14,47949,-0.0784806], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 182,
    label = "CH2CHOH",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.28758,0.0197013,1.96383e-06,-1.9439e-08,1.02617e-11,-16537.3,14.1333], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.49818,0.0103957,-3.66891e-06,5.85206e-10,-3.47374e-14,-18164.3,-13.8388], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 183,
    label = "CH2CH2OH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 O u0 p2 c0 {1,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.20954,0.00912965,2.47462e-05,-3.92946e-08,1.66541e-11,-4915.11,8.30445], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.01349,0.0120204,-4.21992e-06,6.70676e-10,-3.97135e-14,-6161.62,-8.62052], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 184,
    label = "CH2CHOO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 O u1 p2 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.41461,0.0297546,-2.58394e-05,1.12221e-08,-1.86781e-12,11371.2,19.0226], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.41603,0.0299337,-2.63852e-05,1.17707e-08,-2.05116e-12,11361.7,18.9695], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 185,
    label = "CHCHO",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u1 p0 c0 {2,D} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.06864,0.0187233,-1.21319e-05,-3.33727e-10,2.32882e-12,29739.4,14.7866], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.96288,0.00799899,-4.30606e-06,1.11076e-09,-1.11415e-13,28725.6,-5.17392], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 186,
    label = "OCHCHO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u0 p0 c0 {1,S} {4,D} {6,S}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {2,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.68412,0.000478013,4.26391e-05,-5.79018e-08,2.31669e-11,-27198.5,4.51187], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.72507,0.00633097,-2.35575e-06,3.89783e-10,-2.37487e-14,-29102.4,-20.3904], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 187,
    label = "HCCO",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {3,S}
2 C u0 p0 c0 {3,T} {4,S}
3 C u0 p0 c0 {1,S} {2,T}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87608,0.0221205,-3.58869e-05,3.05403e-08,-1.01281e-11,20163.4,13.6968], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.91479,0.00371409,-1.30137e-06,2.06473e-10,-1.21477e-14,19359.6,-5.50567], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 188,
    label = "HCCOH",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,T}
2 O u0 p2 c0 {1,S} {5,S}
3 C u0 p0 c0 {1,T} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.05541,0.0252003,-3.80822e-05,3.09891e-08,-9.898e-12,9768.72,12.2272], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.3751,0.00549429,-1.88137e-06,2.93804e-10,-1.71772e-14,8932.78,-8.24498], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 189,
    label = "CHCHOH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 O u0 p2 c0 {1,S} {6,S}
3 C u1 p0 c0 {1,D} {5,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.99181,0.0473233,-6.66059e-05,4.68997e-08,-1.30686e-11,15200.1,31.4259], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.78246,0.00524797,-1.71857e-06,2.59722e-10,-1.48227e-14,12883.6,-21.0851], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 190,
    label = "C2",
    molecule = 
"""
multiplicity 3
1 C u1 p0 c0 {2,T}
2 C u1 p0 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.33655,0.0359693,-0.00011185,1.31762e-07,-5.29904e-11,98422.1,9.54587], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.5587,0.000786412,-1.25558e-07,8.97793e-12,-1.32453e-16,98890.4,4.18695], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 191,
    label = "C2O",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u1 p0 c0 {2,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.86278,0.0119701,-1.80851e-05,1.52778e-08,-5.20063e-12,44312.6,8.89759], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.42468,0.00185394,-5.17933e-07,6.77646e-11,-3.53315e-15,43716.1,-3.69608], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 192,
    label = "CH3CH2OH",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 O u0 p2 c0 {1,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.8587,-0.00374017,6.95554e-05,-8.86548e-08,3.51688e-11,-29996.1,4.80185], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.56244,0.0152042,-5.38968e-06,8.6225e-10,-5.12898e-14,-31525.6,-9.47302], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 193,
    label = "CH3CHOH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {7,S}
3 O u0 p2 c0 {2,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.22283,0.00512175,3.48387e-05,-4.91944e-08,2.01184e-11,-8356.22,8.01676], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.35842,0.0124356,-4.33097e-06,6.8453e-10,-4.03713e-14,-9530.19,-6.05106], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 194,
    label = "HOCH2CH2OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  O u0 p2 c0 {1,S} {9,S}
4  O u0 p2 c0 {2,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u1 p2 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.556418,0.0412519,-3.10647e-05,1.2293e-08,-1.99691e-12,-22047.4,24.9983], Tmin=(298,'K'), Tmax=(800,'K')),
            NASAPolynomial(coeffs=[0.556418,0.0412519,-3.10647e-05,1.2293e-08,-1.99691e-12,-22047.4,24.9983], Tmin=(800,'K'), Tmax=(2500,'K')),
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
    index = 195,
    label = "cC2H3O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {3,S} {6,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58349,-0.00602276,6.32427e-05,-8.18541e-08,3.30445e-11,18568.1,9.59726], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.60158,0.00917614,-3.28029e-06,5.27904e-10,-3.15362e-14,17144.6,-5.47229], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 196,
    label = "OCHCO",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {3,S}
2 O u0 p2 c0 {4,D}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.39406,0.0143629,-8.84138e-06,1.60961e-09,3.20389e-13,-8684.14,10.592], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.94994,0.010163,-5.5772e-06,1.4572e-09,-1.47435e-13,-9096.51,2.57988], Tmin=(1000,'K'), Tmax=(2900,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2900,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 197,
    label = "CH3CH2OOH",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.14672,0.00978668,4.91492e-05,-7.42532e-08,3.11169e-11,-21467.1,9.84025], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.58691,0.0148604,-5.29788e-06,8.47317e-10,-5.03436e-14,-23836.8,-22.8311], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 198,
    label = "CH3CHOOH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u1 p0 c0 {1,S} {3,S} {8,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {3,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.26854,0.000111351,6.15944e-05,-7.95035e-08,3.12333e-11,962.571,-0.180971], Tmin=(200,'K'), Tmax=(999.99,'K')),
            NASAPolynomial(coeffs=[9.10837,0.0152964,-5.54864e-06,9.02286e-10,-5.4412e-14,-932.703,-20.3914], Tmin=(999.99,'K'), Tmax=(2500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (2500,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 199,
    label = "CH2CHOOH",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 O u0 p2 c0 {1,S} {4,S}
4 O u0 p2 c0 {3,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.79821,0.0274377,-2.03468e-05,7.62127e-09,-1.12671e-12,-6315.53,9.11829], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.82519,0.0274167,-2.04456e-05,7.77399e-09,-1.18661e-12,-6325.27,8.96641], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 200,
    label = "OCHO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 O u1 p2 c0 {1,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6286,0.00812496,-1.41561e-06,-3.27952e-09,1.61554e-12,-16747.8,7.8317], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.41052,0.00750888,-4.2589e-06,1.12761e-09,-1.14144e-13,-17029.8,3.43148], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 201,
    label = "NH2",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06463,-0.00110021,4.25849e-06,-2.68224e-09,5.89267e-13,21176.9,0.439851], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.62499,0.00339841,-1.01631e-06,1.25511e-10,-2.66501e-15,21541.9,7.73537], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 202,
    label = "NH3",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.14028,-0.00358489,1.89476e-05,-1.98834e-08,7.15268e-12,-6685.45,-0.0166755], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.36074,0.0063185,-2.28967e-06,4.11767e-10,-2.90837e-14,-6415.96,8.02154], Tmin=(1000,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (4000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 203,
    label = "NH",
    molecule = 
"""
multiplicity 3
1 N u2 p1 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45887,0.000493904,-1.87863e-06,2.85542e-09,-1.16865e-12,42108.8,2.00373], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.79499,0.0012926,-3.85559e-07,6.26028e-11,-3.70422e-15,42340.9,5.68414], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 204,
    label = "HNO",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {3,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.55326,-0.00584532,1.88854e-05,-1.7604e-08,5.7289e-12,11631.6,1.66851], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.24129,0.00272377,-1.60633e-07,-9.79135e-11,1.17104e-14,11774.6,7.27914], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 205,
    label = "H2NO",
    molecule = 
"""
multiplicity 2
1 N u1 p0 c+1 {2,S} {3,S} {4,S}
2 O u0 p3 c-1 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93201,-0.000164028,1.39161e-05,-1.62748e-08,6.00353e-12,6711.79,4.58837], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.75556,0.00516219,-1.76387e-06,2.75053e-10,-1.60643e-14,6518.26,4.30933], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 206,
    label = "HON",
    molecule = 
"""
1 O u0 p1 c+1 {2,D} {3,S}
2 N u0 p2 c-1 {1,D}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.15272,-0.00387826,2.05476e-05,-2.49049e-08,9.87365e-12,24603.7,4.56636], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.12045,0.00228738,-7.14685e-07,1.03332e-10,-5.70484e-15,24364.4,3.38858], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 207,
    label = "N",
    molecule = 
"""
multiplicity 4
1 N u3 p1 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.49977,5.0215e-07,1.93091e-09,-4.94633e-12,2.7409e-15,56076.1,4.19499], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.41604,0.000174664,-1.18865e-07,3.0185e-11,-2.0326e-15,56105.2,4.64906], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 208,
    label = "NO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 N u1 p1 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08518,-0.00364693,8.49608e-06,-6.62406e-09,1.77647e-12,9840.61,2.83578], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.25487,0.0011987,-4.33029e-07,7.02943e-11,-4.09789e-15,9907,6.40395], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 209,
    label = "NNH",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,D} {3,S}
2 N u1 p1 c0 {1,D}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.25475,-0.00345098,1.37789e-05,-1.33264e-08,4.41023e-12,28832.4,3.28552], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.42744,0.00323295,-1.17296e-06,1.90508e-10,-1.14492e-14,28806.8,6.39209], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 210,
    label = "HONO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 N u0 p1 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.16416,0.00850518,5.48562e-07,-8.27656e-09,4.39957e-12,-10774.4,10.0232], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.79145,0.00364631,-1.29113e-06,2.06498e-10,-1.22139e-14,-11597.4,-4.07145], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 211,
    label = "NO2",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {3,S}
2 O u0 p2 c0 {3,D}
3 N u0 p1 c0 {1,S} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78713,-0.000429577,1.37384e-05,-1.74264e-08,6.7125e-12,2895,6.96592], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.90482,0.00214474,-8.12654e-07,1.55512e-10,-1.04114e-14,2289.59,-0.233567], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 212,
    label = "N2O",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 N u0 p0 c+1 {1,D} {3,D}
3 N u0 p2 c-1 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.13942,0.0121801,-1.59189e-05,1.2092e-08,-3.85126e-12,8870.09,11.2478], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.80641,0.00265307,-9.70797e-07,1.6259e-10,-9.96738e-15,8197.98,-2.10608], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 213,
    label = "NH2OH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 N u0 p1 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.21016,0.00619672,1.10595e-05,-1.96668e-08,8.82517e-12,-6581.48,7.93294], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.88113,0.00815708,-2.82616e-06,4.37931e-10,-2.52725e-14,-6860.18,3.79156], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 214,
    label = "HNOH",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 N u1 p1 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95608,-0.00302611,2.56874e-05,-3.15645e-08,1.24085e-11,10920,5.55951], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.98322,0.00488846,-1.65087e-06,2.55371e-10,-1.48309e-14,10578,3.62583], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 215,
    label = "HNO2",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,D} {4,S}
2 O u0 p3 c-1 {1,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03779,-0.00446123,3.19441e-05,-3.79359e-08,1.44571e-11,-6530.88,5.9062], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.66359,0.00489854,-1.79694e-06,2.9442e-10,-1.78236e-14,-7252.16,-0.0306054], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 216,
    label = "NO3",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {4,S}
2 O u0 p3 c-1 {4,S}
3 O u0 p2 c0 {4,D}
4 N u0 p0 c+1 {1,S} {2,S} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.35587,0.0106545,-2.8669e-06,-5.14712e-09,3.08532e-12,7475.35,8.94787], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.37569,0.00221733,-5.75696e-07,6.69775e-11,-2.58935e-15,6224.46,-12.4945], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 217,
    label = "HONO2",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p3 c-1 {4,S}
3 O u0 p2 c0 {4,D}
4 N u0 p0 c+1 {1,S} {2,S} {3,D}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.55975,0.0201502,-1.15217e-05,-2.31891e-09,3.17581e-12,-17395.6,17.7295], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.03061,0.00446368,-1.72273e-06,2.91612e-10,-1.80487e-14,-19303.4,-16.2543], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 218,
    label = "N2H2",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {3,S}
2 N u0 p1 c0 {1,D} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.91066,-0.0107792,3.86516e-05,-3.86502e-08,1.34852e-11,22824.2,0.0910273], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.31115,0.00900187,-3.14912e-06,4.8145e-10,-2.71898e-14,23386.3,16.4091], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 219,
    label = "H2NN(S)",
    molecule = 
"""
1 N u0 p0 c+1 {2,D} {3,S} {4,S}
2 N u0 p2 c-1 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.53204,-0.00732419,3.00804e-05,-3.04001e-08,1.04701e-11,34958,1.51074], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.05904,0.00618382,-2.22171e-06,3.58539e-10,-2.14533e-14,34853,6.69894], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 220,
    label = "N2H3",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u1 p1 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.42126,0.00134902,2.23459e-05,-2.99728e-08,1.20979e-11,25819.9,7.83176], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.04484,0.0073113,-2.47626e-06,3.83733e-10,-2.23108e-14,25324.1,2.88423], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 221,
    label = "N2H4",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83472,-0.00064913,3.76848e-05,-5.00709e-08,2.03362e-11,10089.4,5.75272], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.93957,0.00875017,-2.99399e-06,4.67278e-10,-2.73069e-14,9282.66,-2.6944], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 222,
    label = "HCN",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 N u0 p1 c0 {1,T}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.10572,0.0111841,-1.62402e-05,1.31663e-08,-4.17254e-12,14542.7,9.55501], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.79525,0.0031633,-1.07317e-06,1.67852e-10,-9.83948e-15,14225,1.61357], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 223,
    label = "CN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,T}
2 C u1 p0 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6292,-0.00107173,2.42398e-06,-5.85516e-10,-3.75364e-13,51866.8,3.91231], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.73484,5.83996e-05,2.90444e-07,-6.74404e-11,4.33382e-15,51701.9,2.85163], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 224,
    label = "HNC",
    molecule = 
"""
1 N u0 p0 c+1 {2,T} {3,S}
2 C u0 p1 c-1 {1,T}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.36665,0.0149943,-3.03606e-05,2.99846e-08,-1.09095e-11,21980.8,7.87288], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.17272,0.0026657,-8.923e-07,1.37331e-10,-7.95546e-15,21797.7,0.215196], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 225,
    label = "NCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 N u1 p1 c0 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.77405,0.00924523,-9.91774e-06,6.68461e-09,-2.09521e-12,14237,9.75459], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.08064,0.00237444,-9.07099e-07,1.52287e-10,-9.31009e-15,13578.1,-2.15734], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 226,
    label = "HOCN",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 C u0 p0 c0 {1,S} {3,T}
3 N u0 p1 c0 {2,T}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.88944,0.0116487,-1.08005e-05,5.44139e-09,-1.06857e-12,-3152.97,9.51296], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.28768,0.00401747,-1.40407e-06,2.22563e-10,-1.31562e-14,-3774.1,-2.64471], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 227,
    label = "HNCO",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {4,S}
2 C u0 p0 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.24009,0.01456,-1.54352e-05,8.55535e-09,-1.79632e-12,-15459,12.1664], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.30045,0.00402251,-1.40962e-06,2.23855e-10,-1.325e-14,-16199.5,-3.11771], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 228,
    label = "NCCN",
    molecule = 
"""
multiplicity 3
1 N u1 p1 c0 {3,D}
2 N u0 p1 c0 {4,T}
3 C u1 p0 c0 {1,D} {4,S}
4 C u0 p0 c0 {2,T} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.32928,0.0261541,-4.9001e-05,4.61923e-08,-1.64326e-11,35690.1,9.86348], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.7055,0.00364271,-1.3094e-06,2.16421e-10,-1.31194e-14,34882.4,-10.4803], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 229,
    label = "HNCN",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {3,S} {4,S}
2 N u0 p1 c0 {3,T}
3 C u0 p0 c0 {1,S} {2,T}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.06754,0.010679,-7.96224e-06,2.59883e-09,-1.27058e-13,36662.4,9.41075], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.53846,0.00389054,-1.38105e-06,2.21295e-10,-1.31827e-14,35963.5,-3.39587], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 230,
    label = "NCN",
    molecule = 
"""
multiplicity 3
1 N u1 p1 c0 {3,D}
2 N u1 p1 c0 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.00703,0.00838874,-6.90467e-06,2.84869e-09,-5.74273e-13,53004.5,7.78171], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.65712,0.00164211,-6.37923e-07,1.11209e-10,-6.99328e-15,52209.7,-6.1405], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 231,
    label = "HNCNH",
    molecule = 
"""
1 N u0 p1 c0 {3,D} {4,S}
2 N u0 p1 c0 {3,D} {5,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.00198,0.0246402,-2.75977e-05,1.53247e-08,-3.26828e-12,16793.7,16.9432], Tmin=(298,'K'), Tmax=(1500,'K')),
            NASAPolynomial(coeffs=[8.37414,0.00236614,-3.50232e-07,-4.3911e-11,1.09686e-14,14610.9,-21.0739], Tmin=(1500,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (4000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 232,
    label = "HCNO",
    molecule = 
"""
1 N u0 p0 c+1 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 O u0 p3 c-1 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.607949,0.0282182,-4.60452e-05,3.82559e-08,-1.23227e-11,19071.4,16.9199], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.9198,0.00400115,-1.42063e-06,2.2757e-10,-1.35505e-14,18038.6,-8.26935], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 233,
    label = "CH3CN",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,T}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 N u0 p1 c0 {2,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82393,0.00408202,2.1621e-05,-2.89808e-08,1.12963e-11,7444.3,5.52656], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.09922,0.00969586,-3.48052e-06,5.6142e-10,-3.35836e-14,6609.67,-3.36087], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 234,
    label = "CH2CN",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 C u0 p0 c0 {1,S} {5,T}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 N u0 p1 c0 {2,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.63064,0.0173644,-1.70284e-05,9.86551e-09,-2.46034e-12,29579.2,11.2776], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.14874,0.006066,-2.17175e-06,3.4975e-10,-2.09004e-14,28649.1,-6.59236], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 235,
    label = "CH2NH",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {5,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.8185,0.00511983,6.38887e-06,-6.61375e-09,1.65532e-12,9884.43,10.3391], Tmin=(298,'K'), Tmax=(1577,'K')),
            NASAPolynomial(coeffs=[4.54738,0.00717721,-2.47935e-06,3.87692e-10,-2.26113e-14,8640.57,-1.16687], Tmin=(1577,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 236,
    label = "H2CN",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 N u1 p1 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.978,-0.00343276,2.59134e-05,-3.04692e-08,1.16273e-11,27485.4,4.43067], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.80316,0.00547197,-1.95315e-06,3.13362e-10,-1.86249e-14,27130.3,3.31759], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 237,
    label = "CH3NO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {6,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.18535,-0.00634086,4.57171e-05,-5.30422e-08,1.99502e-11,6937.72,2.18493], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.04712,0.00921544,-3.29035e-06,5.2894e-10,-3.1569e-14,6237.18,-0.774396], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 238,
    label = "CH2NH2",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.85538,0.00727364,1.65713e-05,-2.70977e-08,1.16328e-11,16616.6,10.2445], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.5533,0.00942003,-3.20781e-06,4.98962e-10,-2.90872e-14,15871.7,-0.0245945], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 239,
    label = "NCNOH",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 N u1 p1 c0 {1,S} {4,S}
3 N u0 p1 c0 {4,T}
4 C u0 p0 c0 {2,S} {3,T}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.56418,-0.0166876,4.46094e-05,-4.38687e-08,1.49943e-11,25410.3,-7.23938], Tmin=(100,'K'), Tmax=(942.36,'K')),
            NASAPolynomial(coeffs=[3.4173,-0.000492619,8.01276e-07,-1.21784e-10,4.77703e-15,25123.5,-4.44293], Tmin=(942.36,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 240,
    label = "NCNO",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 N u0 p1 c0 {1,D} {4,S}
3 N u0 p1 c0 {4,T}
4 C u0 p0 c0 {2,S} {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.27607,0.0174736,-2.73909e-05,2.38161e-08,-8.27602e-12,37083.6,9.634], Tmin=(100,'K'), Tmax=(798.02,'K')),
            NASAPolynomial(coeffs=[5.02882,0.00670212,-3.41119e-06,6.64942e-10,-4.6398e-14,36867.1,1.96968], Tmin=(798.02,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 241,
    label = "CH2NO",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {5,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87819,-0.00665309,5.39476e-05,-6.81768e-08,2.71817e-11,25716.9,7.46188], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.40282,0.0069057,-2.5163e-06,4.10141e-10,-2.47183e-14,24528.7,-4.45743], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 242,
    label = "C2H5NO",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.19503,0.0284612,-1.06193e-05,-3.12526e-09,2.4706e-12,3551.62,20.6492], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.22313,0.0251564,-1.28736e-05,3.18527e-09,-3.0895e-13,2905.61,9.66286], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 243,
    label = "CH3CHNO",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 N u0 p1 c0 {1,S} {4,D}
3 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {2,D} {3,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.92228,0.0244337,-9.49024e-06,-2.40398e-09,2.05477e-12,12313.6,16.9273], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.74755,0.0212797,-1.09796e-05,2.73592e-09,-2.66954e-13,11741.2,7.08475], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 244,
    label = "CH2CHNO",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 C u0 p0 c0 {3,D} {6,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.782134,0.0286251,-2.14511e-05,7.40944e-09,-7.1095e-13,18547.8,21.0235], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.48741,0.0170182,-8.86195e-06,2.23083e-09,-2.19836e-13,17646,2.34417], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 245,
    label = "CHCHNO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 C u1 p0 c0 {3,D} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.66767,0.0279986,-2.86416e-05,1.53555e-08,-3.31674e-12,48996,17.1916], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.91529,0.012105,-6.44647e-06,1.65557e-09,-1.65983e-13,48091.6,-3.57487], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 246,
    label = "CH3NO2",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 N u0 p0 c+1 {1,S} {6,S} {7,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p3 c-1 {2,S}
7 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54054,0.0018656,4.44947e-05,-5.87057e-08,2.30684e-11,-11138.6,10.6885], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.73035,0.0109601,-4.05358e-06,6.67102e-10,-4.04687e-14,-12914.3,-10.1801], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 247,
    label = "CH2NO2",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 O u0 p2 c0 {3,D}
3 N u0 p0 c+1 {1,S} {2,D} {4,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.42742,0.0160496,2.84728e-06,-1.82218e-08,9.35384e-12,14012.1,16.1086], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.57505,0.00701471,-2.51481e-06,4.05671e-10,-2.42797e-14,12388,-11.5986], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 248,
    label = "C2H5NO2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  N u0 p0 c+1 {1,S} {9,S} {10,D}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p3 c-1 {3,S}
10 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.4372,0.00825502,5.01014e-05,-7.12335e-08,2.88208e-11,-14991.3,9.09921], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.29092,0.0161242,-5.95123e-06,9.76015e-10,-5.90148e-14,-17371.9,-21.1218], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 249,
    label = "CH3CH2ONO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  O u0 p2 c0 {1,S} {4,S}
4  N u0 p1 c0 {3,S} {10,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.37138,0.0137914,3.84688e-05,-6.02381e-08,2.49655e-11,-14019.9,15.8651], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.21849,0.0162002,-5.9816e-06,9.81277e-10,-5.93456e-14,-16554.4,-18.8592], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 250,
    label = "CH2CH2NO2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 N u0 p0 c+1 {1,S} {6,S} {7,D}
3 C u1 p0 c0 {1,S} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p3 c-1 {2,S}
7 O u0 p2 c0 {2,D}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.19815,0.0383712,-3.03909e-05,1.17681e-08,-1.57118e-12,11332.9,22.1405], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.21841,0.022024,-1.1471e-05,2.8888e-09,-2.84836e-13,10142.1,-3.01283], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 251,
    label = "CH3CHNO2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {7,S}
3 N u0 p0 c+1 {2,S} {8,S} {9,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 O u0 p3 c-1 {3,S}
9 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.948311,0.037343,-2.65343e-05,7.9225e-09,-3.22058e-13,5946.38,23.8211], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.75403,0.0229073,-1.20613e-05,3.06099e-09,-3.0346e-13,4745.88,-0.560534], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 252,
    label = "CH3ONO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {3,S}
3 N u0 p1 c0 {2,S} {7,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.15261,-0.00291937,4.14527e-05,-4.93955e-08,1.85608e-11,-9852.6,0.804057], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.93605,0.00997319,-3.60643e-06,5.83462e-10,-3.50059e-14,-10838.2,-6.98145], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 253,
    label = "CH3ONO2",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p3 c-1 {4,S}
3 O u0 p2 c0 {4,D}
4 N u0 p0 c+1 {1,S} {2,S} {3,D}
5 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91364,0.0152138,1.73479e-05,-3.37074e-08,1.44322e-11,-16610.3,9.44208], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.77845,0.011007,-4.25929e-06,7.18198e-10,-4.42042e-14,-18880.4,-23.9163], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 254,
    label = "CH3CH2ONO2",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {5,S}
2  O u0 p3 c-1 {4,S}
3  O u0 p2 c0 {4,D}
4  N u0 p0 c+1 {1,S} {2,S} {3,D}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75722,0.0193623,3.87534e-05,-6.6409e-08,2.82506e-11,-20844.4,11.1813], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.1361,0.0170091,-6.4374e-06,1.0722e-09,-6.54951e-14,-24190.2,-37.1641], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 255,
    label = "CH3NH2",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.65718,-0.00737953,5.45297e-05,-6.24994e-08,2.33762e-11,-3760.73,1.63875], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.7861,0.012697,-4.46779e-06,7.11022e-10,-4.21333e-14,-4381,1.86269], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 256,
    label = "CH3NH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 N u1 p1 c0 {1,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.70974,-0.00731947,4.95106e-05,-5.7279e-08,2.16524e-11,20061.9,1.8546], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.02244,0.0103512,-3.6456e-06,5.80492e-10,-3.44104e-14,19505.1,1.64484], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 257,
    label = "HCNH",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,D} {4,S}
2 C u1 p0 c0 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97115,-0.00388876,2.92919e-05,-3.57482e-08,1.40304e-11,31578.9,5.06389], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.04015,0.00516592,-1.82277e-06,2.90299e-10,-1.71615e-14,31154,2.58894], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 258,
    label = "CH3CH2NH2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  N u0 p1 c0 {1,S} {9,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.64408,0.0314867,-1.71052e-05,3.57316e-09,1.95649e-13,-7471.2,21.3696], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.82805,0.025375,-1.1874e-05,2.70991e-09,-2.44591e-13,-8039.21,10.1772], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 259,
    label = "CH3CHNH2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {7,S}
3 N u0 p1 c0 {2,S} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.64075,0.0285827,-1.89469e-05,6.7295e-09,-9.08174e-13,12515.5,17.4881], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.08789,0.0205228,-9.45004e-06,2.12695e-09,-1.89706e-13,11939.7,5.24988], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 260,
    label = "CH2CH2NH2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {8,S} {9,S}
3 C u1 p0 c0 {1,S} {6,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.25929,0.0301867,-2.18269e-05,8.94597e-09,-1.52898e-12,17667,19.6477], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.10303,0.0203085,-9.25456e-06,2.06112e-09,-1.8195e-13,17023.4,5.55411], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 261,
    label = "CH3CH2NH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 N u1 p1 c0 {1,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.92366,0.0238729,-7.86535e-06,-2.71982e-09,1.89902e-12,16912.9,16.7828], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.09795,0.0224758,-1.07197e-05,2.48314e-09,-2.26728e-13,16513,10.2925], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 262,
    label = "CH2CHNH2",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.710306,0.0374245,-3.66191e-05,1.98714e-08,-4.41925e-12,3580.17,25.7562], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.59217,0.0172596,-7.93921e-06,1.79645e-09,-1.61749e-13,2467.43,-0.08638], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 263,
    label = "CH3CHNH",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 N u0 p1 c0 {2,D} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.24231,0.0146071,8.25387e-06,-1.56259e-08,5.70542e-12,4797.01,14.5454], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.99419,0.0212775,-1.02687e-05,2.40039e-09,-2.20648e-13,4562.73,14.3229], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 264,
    label = "H2NCHO",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.17952,0.0019459,3.4333e-05,-4.64826e-08,1.87268e-11,-24058,9.94755], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.93695,0.00960834,-3.32935e-06,5.16598e-10,-2.99203e-14,-25091,-2.00078], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 265,
    label = "CHCHNH2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 C u1 p0 c0 {1,D} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.583298,0.0310085,-3.08423e-05,1.72291e-08,-3.96983e-12,36294.5,20.6175], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.77535,0.0146042,-6.78153e-06,1.55237e-09,-1.41604e-13,35437.9,0.30232], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 266,
    label = "CH2CNH2",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,S} {6,S} {7,S}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u1 p0 c0 {1,S} {2,D}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.01233,0.0256068,-2.42451e-05,1.39182e-08,-3.46136e-12,30777.7,15.07], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.21874,0.0156981,-7.7573e-06,1.84326e-09,-1.71838e-13,30390.6,4.69612], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 267,
    label = "CH2CHNH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u1 p0 c0 {1,S} {5,S} {6,S}
3 N u0 p1 c0 {1,D} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.168729,0.0291658,-2.2416e-05,8.51021e-09,-1.09138e-12,23563.8,24.4877], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.67016,0.0167406,-8.17363e-06,1.94564e-09,-1.82823e-13,22649.5,5.23472], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 268,
    label = "H2NCO",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 C u1 p0 c0 {1,S} {5,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5364,0.00973407,-3.87293e-07,-5.90128e-09,3.01182e-12,-3096.24,8.47952], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.69169,0.00608718,-2.09434e-06,3.28449e-10,-1.92704e-14,-3810.29,-3.2271], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 269,
    label = "CH3CNH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {3,D}
3 N u0 p1 c0 {2,D} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.23656,0.0158045,1.22159e-06,-9.86661e-09,4.14655e-12,25585.4,15.0702], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.2967,0.0169751,-8.65109e-06,2.12636e-09,-2.04493e-13,25102.8,8.60277], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 270,
    label = "CH3CHN",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 N u1 p1 c0 {2,D}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.81409,0.0132951,3.533e-06,-9.87941e-09,3.74397e-12,22555.6,12.3157], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.67758,0.0176422,-8.68917e-06,2.06973e-09,-1.93574e-13,22392.9,12.024], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 271,
    label = "CHCNH2",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.3481,0.0260893,-3.14512e-05,2.11896e-08,-5.70653e-12,26621.5,14.8874], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.67245,0.010499,-4.6263e-06,1.01346e-09,-8.92617e-14,26071.3,-0.577431], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 272,
    label = "CH2CNH",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,D}
3 N u0 p1 c0 {2,D} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.674453,0.0266535,-2.72826e-05,1.57426e-08,-3.7599e-12,21320.3,19.3645], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.08696,0.0127931,-6.17629e-06,1.46136e-09,-1.3698e-13,20648.3,2.95368], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 273,
    label = "CH2CHN",
    molecule = 
"""
multiplicity 3
1 N u1 p1 c0 {3,D}
2 C u1 p0 c0 {3,S} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.385115,0.0263156,-2.31525e-05,1.07917e-08,-1.99498e-12,41885.6,22.3684], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.14454,0.0131732,-6.28186e-06,1.4399e-09,-1.30842e-13,41038.9,3.75755], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 274,
    label = "CH2CHN(S)",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 N u0 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.385115,0.0263156,-2.31525e-05,1.07917e-08,-1.99498e-12,49434,22.3684], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.14454,0.0131732,-6.28186e-06,1.4399e-09,-1.30842e-13,48587.4,3.75755], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 275,
    label = "CHCNH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,T}
2 N u1 p1 c0 {1,S} {4,S}
3 C u0 p0 c0 {1,T} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.87301,0.0198561,-2.4152e-05,1.60559e-08,-4.26088e-12,45853.8,9.34467], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.54663,0.00765158,-3.57998e-06,8.31109e-10,-7.71667e-14,45394.6,-3.17646], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 276,
    label = "c-C2H3N",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 N u0 p1 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.0828524,0.0220081,-1.21834e-05,1.00059e-09,1.0153e-12,31399.6,23.0893], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.80979,0.0150202,-7.58142e-06,1.85247e-09,-1.77642e-13,30658.2,8.95343], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 277,
    label = "CH2NCH2",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {3,S} {4,S} {5,S}
2 C u0 p0 c0 {3,D} {6,S} {7,S}
3 N u0 p1 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.869061,0.0252858,-1.51436e-05,3.01037e-09,3.70027e-13,25778.2,19.1044], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.32005,0.0185257,-9.56913e-06,2.33792e-09,-2.22817e-13,25135.8,6.51881], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 278,
    label = "CH3NHCH2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 N u0 p1 c0 {1,S} {3,S} {7,S}
3 C u1 p0 c0 {2,S} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.71402,0.0275573,-1.6131e-05,4.10455e-09,-8.07562e-14,16625.5,16.377], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.95751,0.0209452,-9.75571e-06,2.21626e-09,-1.99156e-13,16058.8,4.96297], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 279,
    label = "CH3NHCH3",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  N u0 p1 c0 {1,S} {2,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.22882,0.0260431,-4.95078e-06,-6.74954e-09,3.27739e-12,-3768.13,18.4832], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.13913,0.0268643,-1.28763e-05,2.99663e-09,-2.74772e-13,-4173.32,12.9759], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 280,
    label = "CH3NCH3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3 N u1 p1 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61165,0.00906653,2.27492e-05,-2.78392e-08,9.27267e-12,17306.4,11.2643], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.54968,0.0247836,-1.20303e-05,2.81641e-09,-2.5854e-13,17345.3,19.3448], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 281,
    label = "CH3NCH2",
    molecule = 
"""
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,D} {7,S} {8,S}
3 N u0 p1 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.12431,0.0161642,4.57771e-06,-1.2116e-08,4.53506e-12,7335.42,14.5092], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.74096,0.0220935,-1.09102e-05,2.60524e-09,-2.44225e-13,7192.29,15.2596], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 282,
    label = "CH3NCH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 N u0 p1 c0 {1,S} {3,D}
3 C u1 p0 c0 {2,D} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.23656,0.0158045,1.22159e-06,-9.86661e-09,4.14655e-12,25585.4,15.0702], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.2967,0.0169751,-8.65109e-06,2.12636e-09,-2.04493e-13,25102.8,8.60277], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 283,
    label = "HCOH-2",
    molecule = 
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {4,S}
2 C u2 p0 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75937,0.00296141,8.9037e-06,-1.3501e-08,5.39791e-12,24775.6,6.76289], Tmin=(100,'K'), Tmax=(940.44,'K')),
            NASAPolynomial(coeffs=[5.09115,0.00321234,-9.31656e-07,1.59608e-10,-1.15723e-14,24263.5,-0.971162], Tmin=(940.44,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 284,
    label = "HO2CHO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {6,S}
3 O u0 p2 c0 {4,D}
4 C u0 p0 c0 {1,S} {3,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.52176,0.0292763,-3.46797e-05,1.99827e-08,-4.36097e-12,-36539.7,12.1191], Tmin=(100,'K'), Tmax=(1220.23,'K')),
            NASAPolynomial(coeffs=[9.73196,0.00362919,-6.79504e-07,5.58352e-11,-1.58408e-15,-38149.5,-23.4874], Tmin=(1220.23,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 285,
    label = "OCH2O2H",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {7,S}
4 O u1 p2 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.44714,0.0340634,-4.14969e-05,2.61185e-08,-6.46109e-12,-12765,14.0867], Tmin=(100,'K'), Tmax=(992.64,'K')),
            NASAPolynomial(coeffs=[8.67812,0.00895442,-3.5537e-06,6.35248e-10,-4.2952e-14,-14002,-15.928], Tmin=(992.64,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 286,
    label = "HOCH2O2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u1 p2 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.69194,0.0271135,-2.49832e-05,1.1931e-08,-2.28596e-12,-21673.7,14.0558], Tmin=(100,'K'), Tmax=(1253.51,'K')),
            NASAPolynomial(coeffs=[8.21381,0.00949295,-3.89778e-06,7.16891e-10,-4.94196e-14,-23058.1,-13.8317], Tmin=(1253.51,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 287,
    label = "HOCH2O2H",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,S} {7,S}
3 O u0 p2 c0 {1,S} {8,S}
4 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.22804,0.0340318,-3.13934e-05,1.44114e-08,-2.58882e-12,-39822.7,15.0578], Tmin=(100,'K'), Tmax=(1356.77,'K')),
            NASAPolynomial(coeffs=[10.8689,0.00855674,-3.22854e-06,5.7201e-10,-3.87175e-14,-42167.4,-29.2654], Tmin=(1356.77,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 288,
    label = "H2CC-2",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u2 p0 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9483,-0.00181652,2.07125e-05,-2.3669e-08,8.45458e-12,72206.8,5.3155], Tmin=(100,'K'), Tmax=(953.67,'K')),
            NASAPolynomial(coeffs=[4.20274,0.0047342,-1.57303e-06,2.859e-10,-2.08639e-14,71811.9,2.28382], Tmin=(953.67,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 289,
    label = "CH3CO3H",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 O u0 p2 c0 {1,S} {9,S}
3 O u0 p2 c0 {5,D}
4 C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
5 C u0 p0 c0 {1,S} {3,D} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.43748,0.0339384,-2.25467e-05,5.77205e-09,1.28452e-13,-44070.1,19.8194], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.64132,0.0217231,-1.11238e-05,2.75682e-09,-2.67754e-13,-45140.9,-1.61172], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 290,
    label = "C3H3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u1 p0 c0 {2,D} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.09018,0.0173589,-8.30795e-06,-2.47825e-09,2.58697e-12,40755.8,8.11429], Tmin=(100,'K'), Tmax=(949.37,'K')),
            NASAPolynomial(coeffs=[6.99887,0.00724416,-2.36571e-06,3.9859e-10,-2.69783e-14,39727.3,-12.0479], Tmin=(949.37,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 291,
    label = "CH3CO2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u1 p2 c0 {2,S}
7 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.25778,0.00985484,2.14046e-05,-3.31495e-08,1.28434e-11,-24124.9,11.9071], Tmin=(100,'K'), Tmax=(980.88,'K')),
            NASAPolynomial(coeffs=[7.1002,0.0102744,-3.84062e-06,7.30877e-10,-5.38134e-14,-25652.6,-10.5014], Tmin=(980.88,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 292,
    label = "O2CH2CHO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {7,S}
3 O u0 p2 c0 {1,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {2,S}
8 O u1 p2 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.29854,0.0327818,-2.77436e-05,1.17559e-08,-1.97285e-12,-11417.8,17.2937], Tmin=(100,'K'), Tmax=(1433.49,'K')),
            NASAPolynomial(coeffs=[10.4206,0.010118,-4.02818e-06,7.26608e-10,-4.93433e-14,-13746.4,-24.8153], Tmin=(1433.49,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 293,
    label = "CH3OCH3",
    molecule = 
"""
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.24109,0.0138085,9.93057e-06,-1.47147e-08,4.62542e-12,-23739.6,9.23359], Tmin=(100,'K'), Tmax=(1170.38,'K')),
            NASAPolynomial(coeffs=[3.88839,0.0197267,-8.07483e-06,1.477e-09,-1.01102e-13,-24448,3.62994], Tmin=(1170.38,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 294,
    label = "CH3OCH2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u1 p0 c0 {3,S} {7,S} {8,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.17261,0.0154262,2.08683e-06,-8.24038e-09,2.8839e-12,-1244.92,11.1769], Tmin=(100,'K'), Tmax=(1183.81,'K')),
            NASAPolynomial(coeffs=[5.01061,0.0156871,-6.44363e-06,1.18134e-09,-8.09894e-14,-2133.54,0.0842452], Tmin=(1183.81,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 295,
    label = "CH3OCH2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  O u0 p2 c0 {1,S} {2,S}
4  O u0 p2 c0 {1,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.39931,0.030946,-1.92548e-05,5.76034e-09,-6.16082e-13,-20443.3,13.943], Tmin=(200,'K'), Tmax=(1441,'K')),
            NASAPolynomial(coeffs=[11.9179,0.0119413,-3.93526e-06,5.95756e-10,-3.39598e-14,-23423.2,-32.0097], Tmin=(1441,'K'), Tmax=(5000,'K')),
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
    index = 296,
    label = "CH3OCH2O2H",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {5,S}
2  O u0 p2 c0 {3,S} {4,S}
3  O u0 p2 c0 {2,S} {11,S}
4  C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
5  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.05787,0.0436787,-3.46384e-05,1.44809e-08,-2.46101e-12,-36885.1,24.3392], Tmin=(200,'K'), Tmax=(1404,'K')),
            NASAPolynomial(coeffs=[12.8159,0.0134818,-4.50398e-06,6.88229e-10,-3.94884e-14,-40674.6,-37.8048], Tmin=(1404,'K'), Tmax=(5000,'K')),
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
    index = 297,
    label = "CH2OCH2O2H",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u1 p0 c0 {3,S} {8,S} {9,S}
3  O u0 p2 c0 {1,S} {2,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.162245,0.0476101,-4.52047e-05,2.18379e-08,-4.11296e-12,-14649.8,29.8253], Tmin=(200,'K'), Tmax=(1418,'K')),
            NASAPolynomial(coeffs=[12.3893,0.0111759,-3.59249e-06,5.34196e-10,-3.00537e-14,-18055.2,-32.9577], Tmin=(1418,'K'), Tmax=(5000,'K')),
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
    index = 298,
    label = "O2CH2OCH2O2H",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,S} {7,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {5,S} {7,S}
4  O u0 p2 c0 {2,S} {12,S}
5  O u1 p2 c0 {3,S}
6  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
7  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
8  H u0 p0 c0 {7,S}
9  H u0 p0 c0 {7,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.39978,0.0539882,-4.8797e-05,2.19792e-08,-3.86107e-12,-33782.5,23.0683], Tmin=(200,'K'), Tmax=(1433,'K')),
            NASAPolynomial(coeffs=[17.7378,0.011359,-3.67383e-06,5.49256e-10,-3.10406e-14,-38290.3,-56.661], Tmin=(1433,'K'), Tmax=(5000,'K')),
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
    index = 299,
    label = "HO2CH2OCHO",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {6,S}
2  O u0 p2 c0 {3,S} {5,S}
3  O u0 p2 c0 {2,S} {10,S}
4  O u0 p2 c0 {6,D}
5  C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
6  C u0 p0 c0 {1,S} {4,D} {9,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.2191,0.0428858,-3.17634e-05,1.11543e-08,-1.49753e-12,-57928.8,24.9759], Tmin=(200,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[15.7136,0.0096443,-3.44136e-06,5.49722e-10,-3.2536e-14,-62940.9,-52.9505], Tmin=(1386,'K'), Tmax=(5000,'K')),
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
    index = 300,
    label = "CH3OCH2O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
3 O u0 p2 c0 {1,S} {2,S}
4 O u1 p2 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.92891,0.0176098,1.24833e-05,-2.45572e-08,9.44511e-12,-19413.5,15.0279], Tmin=(100,'K'), Tmax=(1028.1,'K')),
            NASAPolynomial(coeffs=[6.84082,0.0165551,-6.64489e-06,1.24792e-09,-8.8634e-14,-20966.5,-7.594], Tmin=(1028.1,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 301,
    label = "OCH2OCHO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {7,D} {8,S}
3 O u0 p2 c0 {1,S} {2,S}
4 O u1 p2 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.8954,0.0274119,-1.36476e-05,1.26326e-09,5.1797e-13,-42787.9,20.2333], Tmin=(200,'K'), Tmax=(1523,'K')),
            NASAPolynomial(coeffs=[12.4013,0.00783738,-2.82993e-06,4.55559e-10,-2.71061e-14,-46845.3,-37.8085], Tmin=(1523,'K'), Tmax=(5000,'K')),
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
    index = 302,
    label = "HOCH2OCO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {4,S}
3 O u0 p2 c0 {1,S} {7,S}
4 C u1 p0 c0 {2,S} {8,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.95255,0.00842196,1.36742e-05,-1.46786e-08,3.84144e-12,-44447,2.85657], Tmin=(200,'K'), Tmax=(1443,'K')),
            NASAPolynomial(coeffs=[11.1498,0.00934737,-3.35542e-06,5.38037e-10,-3.1926e-14,-47501.2,-29.5984], Tmin=(1443,'K'), Tmax=(5000,'K')),
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
    index = 303,
    label = "CH3OCHO",
    molecule = 
"""
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {7,D} {8,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.28124,0.011318,1.8448e-05,-2.41949e-08,7.75149e-12,-44672.6,12.0363], Tmin=(100,'K'), Tmax=(1141.77,'K')),
            NASAPolynomial(coeffs=[4.90984,0.0187531,-8.58334e-06,1.66848e-09,-1.18613e-13,-45901,0.212516], Tmin=(1141.77,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 304,
    label = "CH2OCHO",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {3,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {4,D} {7,S}
3 O u0 p2 c0 {1,S} {2,S}
4 O u0 p2 c0 {2,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.79263,0.022294,-9.08424e-06,-2.40324e-09,1.82255e-12,-20487.5,13.1527], Tmin=(100,'K'), Tmax=(1184.74,'K')),
            NASAPolynomial(coeffs=[8.25875,0.0116085,-5.39247e-06,1.0548e-09,-7.52248e-14,-22328,-16.4461], Tmin=(1184.74,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 305,
    label = "CH3OCO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u1 p0 c0 {2,S} {7,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.17386,0.0160845,-2.93031e-06,-3.33806e-09,1.28649e-12,-20557.3,12.7605], Tmin=(100,'K'), Tmax=(1366.08,'K')),
            NASAPolynomial(coeffs=[6.09094,0.0131504,-5.8656e-06,1.09912e-09,-7.54115e-14,-21877.5,-4.13773], Tmin=(1366.08,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 306,
    label = "C3H8",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.06334,0.0129217,3.47024e-05,-4.70935e-08,1.71379e-11,-14390.6,10.7836], Tmin=(100,'K'), Tmax=(990,'K')),
            NASAPolynomial(coeffs=[5.60448,0.0219527,-8.22073e-06,1.50102e-09,-1.05634e-13,-15839.4,-6.22666], Tmin=(990,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 307,
    label = "NC3H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.02815,0.0147024,2.40506e-05,-3.66733e-08,1.38609e-11,10512.1,12.4699], Tmin=(100,'K'), Tmax=(984.47,'K')),
            NASAPolynomial(coeffs=[6.16547,0.0184494,-6.79026e-06,1.23048e-09,-8.6386e-14,9095.05,-6.67625], Tmin=(984.47,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 308,
    label = "IC3H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.23517,0.0111018,2.80207e-05,-3.5945e-08,1.23654e-11,9053.76,11.9814], Tmin=(100,'K'), Tmax=(1029.99,'K')),
            NASAPolynomial(coeffs=[4.3659,0.0214398,-8.48551e-06,1.568e-09,-1.09812e-13,8039.53,2.70013], Tmin=(1029.99,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 309,
    label = "C3H5-A",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u1 p0 c0 {1,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29615,0.00579223,4.33921e-05,-5.9989e-08,2.33815e-11,18908.2,9.01994], Tmin=(100,'K'), Tmax=(942.18,'K')),
            NASAPolynomial(coeffs=[8.06863,0.0101837,-2.84795e-06,5.0088e-10,-3.79628e-14,16914.7,-19.5272], Tmin=(942.18,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 310,
    label = "C3H6",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.31913,0.00817948,3.3474e-05,-4.36199e-08,1.58216e-11,749.325,9.54022], Tmin=(100,'K'), Tmax=(983.75,'K')),
            NASAPolynomial(coeffs=[5.36752,0.0170744,-6.35111e-06,1.1662e-09,-8.27627e-14,-487.124,-4.54448], Tmin=(983.75,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 311,
    label = "NC3H7O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  O u0 p2 c0 {2,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.15077,0.0341093,-6.28775e-06,-1.16905e-08,5.70826e-12,-6992.04,19.9651], Tmin=(100,'K'), Tmax=(1072.55,'K')),
            NASAPolynomial(coeffs=[8.78442,0.0227415,-9.09063e-06,1.67579e-09,-1.16717e-13,-9184.16,-16.0886], Tmin=(1072.55,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 312,
    label = "NC3H7O2H",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {2,S} {5,S}
5  O u0 p2 c0 {4,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.72478,0.0452898,-2.97046e-05,1.0046e-08,-1.39809e-12,-24074.5,20.2775], Tmin=(100,'K'), Tmax=(1639.49,'K')),
            NASAPolynomial(coeffs=[11.0854,0.0224522,-8.8103e-06,1.54982e-09,-1.0255e-13,-27143.8,-29.5098], Tmin=(1639.49,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 313,
    label = "IC3H7O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  O u0 p2 c0 {1,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.95851,0.0414289,-2.74437e-05,9.4942e-09,-1.36273e-12,-9431.92,18.3292], Tmin=(100,'K'), Tmax=(1582.74,'K')),
            NASAPolynomial(coeffs=[9.8846,0.0213978,-8.45983e-06,1.49806e-09,-9.97238e-14,-11940.9,-23.549], Tmin=(1582.74,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 314,
    label = "IC3H7O2H",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.67829,0.0492833,-3.78189e-05,1.5722e-08,-2.7332e-12,-26381,18.7785], Tmin=(100,'K'), Tmax=(1330.82,'K')),
            NASAPolynomial(coeffs=[9.85767,0.0246986,-1.01086e-05,1.8406e-09,-1.25489e-13,-28558,-23.0199], Tmin=(1330.82,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 315,
    label = "CH3COCH3",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.01141,0.0154683,2.15013e-05,-3.24616e-08,1.17876e-11,-27871.2,13.2203], Tmin=(100,'K'), Tmax=(1023.94,'K')),
            NASAPolynomial(coeffs=[5.79588,0.0200764,-7.93434e-06,1.47306e-09,-1.03776e-13,-29253.3,-4.24315], Tmin=(1023.94,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 316,
    label = "NC3H7O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  O u1 p2 c0 {3,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.49,0.0272742,1.66472e-06,-1.66154e-08,7.01484e-12,-6000.76,15.8164], Tmin=(100,'K'), Tmax=(1050.44,'K')),
            NASAPolynomial(coeffs=[7.46142,0.0213308,-8.39407e-06,1.53869e-09,-1.07024e-13,-7761.72,-11.8231], Tmin=(1050.44,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 317,
    label = "IC3H7O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  O u1 p2 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.47204,0.0275919,1.27874e-06,-1.70115e-08,7.40023e-12,-7309.35,14.2688], Tmin=(100,'K'), Tmax=(1031.38,'K')),
            NASAPolynomial(coeffs=[7.67896,0.020676,-7.97419e-06,1.45196e-09,-1.00894e-13,-9089.63,-14.4361], Tmin=(1031.38,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 318,
    label = "C2H5CHO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,D} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.90578,0.0240644,-7.06364e-06,-9.81763e-10,5.55804e-13,-24535.9,13.5806], Tmin=(100,'K'), Tmax=(1712.5,'K')),
            NASAPolynomial(coeffs=[7.69127,0.018924,-7.84922e-06,1.3827e-09,-8.99038e-14,-27060.2,-14.6658], Tmin=(1712.5,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 319,
    label = "C3H6OOH1-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {2,S} {11,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.03865,0.0408811,-2.67535e-05,9.01763e-09,-1.26357e-12,133.04,21.7174], Tmin=(100,'K'), Tmax=(1602.59,'K')),
            NASAPolynomial(coeffs=[9.65917,0.0218605,-8.95035e-06,1.61158e-09,-1.08232e-13,-2309.46,-18.6411], Tmin=(1602.59,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 320,
    label = "C3H6OOH1-3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {10,S} {11,S}
4  O u0 p2 c0 {2,S} {5,S}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.73075,0.0457841,-3.51689e-05,1.42448e-08,-2.36092e-12,1161.01,22.4746], Tmin=(100,'K'), Tmax=(1415.62,'K')),
            NASAPolynomial(coeffs=[10.8293,0.0200752,-7.92784e-06,1.41612e-09,-9.53847e-14,-1415.05,-24.5834], Tmin=(1415.62,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 321,
    label = "C3H6OOH2-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {10,S} {11,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.76765,0.0506123,-4.86078e-05,2.65249e-08,-6.07398e-12,-343.084,20.4945], Tmin=(100,'K'), Tmax=(1033.8,'K')),
            NASAPolynomial(coeffs=[8.54818,0.0243766,-1.05405e-05,1.97622e-09,-1.37392e-13,-1745.01,-12.443], Tmin=(1033.8,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 322,
    label = "C3H6O1-2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {2,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.04895,0.010722,4.34912e-05,-6.00654e-08,2.26238e-11,-12859.2,12.4765], Tmin=(100,'K'), Tmax=(972.99,'K')),
            NASAPolynomial(coeffs=[7.70292,0.017291,-6.25833e-06,1.16981e-09,-8.54001e-14,-14981.4,-16.1007], Tmin=(972.99,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 323,
    label = "C3H6O1-3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
4  O u0 p2 c0 {2,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4757,-0.00369723,8.70656e-05,-1.0561e-07,3.87165e-11,-11002.7,11.3085], Tmin=(100,'K'), Tmax=(960.54,'K')),
            NASAPolynomial(coeffs=[8.01387,0.0165131,-5.56907e-06,1.07257e-09,-8.24756e-14,-13678.7,-19.7942], Tmin=(960.54,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 324,
    label = "C3H6OOH1-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {2,S} {6,S}
5  O u0 p2 c0 {1,S} {13,S}
6  O u0 p2 c0 {4,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u1 p2 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.018727,0.0937588,-0.000141618,1.12765e-07,-3.51744e-11,-18835.6,26.4568], Tmin=(100,'K'), Tmax=(860.83,'K')),
            NASAPolynomial(coeffs=[12.8567,0.0265397,-1.16094e-05,2.10572e-09,-1.40381e-13,-20778.5,-32.1393], Tmin=(860.83,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 325,
    label = "C3H6OOH1-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
4  O u0 p2 c0 {2,S} {6,S}
5  O u0 p2 c0 {3,S} {13,S}
6  O u0 p2 c0 {4,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u1 p2 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.315747,0.0885607,-0.000136735,1.16893e-07,-3.94943e-11,-17192.7,26.2345], Tmin=(100,'K'), Tmax=(834.97,'K')),
            NASAPolynomial(coeffs=[9.34156,0.0332589,-1.57164e-05,2.96614e-09,-2.02792e-13,-18279.4,-13.1639], Tmin=(834.97,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 326,
    label = "C3H6OOH2-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {1,S} {6,S}
5  O u0 p2 c0 {2,S} {13,S}
6  O u0 p2 c0 {4,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u1 p2 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.0907103,0.0907532,-0.000126243,9.31258e-08,-2.73469e-11,-18788.6,26.0637], Tmin=(100,'K'), Tmax=(834.45,'K')),
            NASAPolynomial(coeffs=[13.2712,0.0275737,-1.26759e-05,2.39725e-09,-1.65727e-13,-20988.3,-35.1397], Tmin=(834.45,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 327,
    label = "C3H51-2,3OOH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {11,S} {12,S}
4  O u0 p2 c0 {1,S} {7,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {13,S}
7  O u0 p2 c0 {4,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.254673,0.0870748,-0.000119011,8.69786e-08,-2.54119e-11,-11021.4,29.2386], Tmin=(100,'K'), Tmax=(837.28,'K')),
            NASAPolynomial(coeffs=[12.661,0.0278058,-1.2831e-05,2.43606e-09,-1.68987e-13,-13098.9,-28.4118], Tmin=(837.28,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 328,
    label = "C3H52-1,3OOH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
3  C u1 p0 c0 {1,S} {2,S} {12,S}
4  O u0 p2 c0 {1,S} {6,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {4,S} {13,S}
7  O u0 p2 c0 {5,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.60656,0.110614,-0.000129243,6.52423e-08,-1.1548e-11,-10675.6,40.7312], Tmin=(100,'K'), Tmax=(1737.12,'K')),
            NASAPolynomial(coeffs=[30.7551,-0.0101006,1.09077e-05,-2.3271e-09,1.59884e-13,-16338.4,-125.957], Tmin=(1737.12,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 329,
    label = "AC3H5OOH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.84686,0.0510073,-6.52613e-05,5.25162e-08,-1.77876e-11,-8323.49,18.0257], Tmin=(100,'K'), Tmax=(775.71,'K')),
            NASAPolynomial(coeffs=[6.14842,0.0261422,-1.19895e-05,2.27271e-09,-1.57396e-13,-8910.1,-1.11389], Tmin=(775.71,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 330,
    label = "C3H5O1-2OOH-3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  O u0 p2 c0 {1,S} {2,S}
5  O u0 p2 c0 {3,S} {6,S}
6  O u0 p2 c0 {5,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.0058,0.058173,-4.86791e-05,1.58512e-08,-4.33801e-13,-22729.4,20.3642], Tmin=(100,'K'), Tmax=(1019.17,'K')),
            NASAPolynomial(coeffs=[15.5387,0.015011,-5.57658e-06,1.0157e-09,-7.16064e-14,-26412.3,-53.5602], Tmin=(1019.17,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 331,
    label = "C3H5O1-3OOH-2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
4  O u0 p2 c0 {2,S} {3,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.43959,0.0716533,-7.15032e-05,3.51738e-08,-6.63683e-12,-22725,45.6394], Tmin=(200,'K'), Tmax=(1434,'K')),
            NASAPolynomial(coeffs=[14.4493,0.0136373,-4.25837e-06,6.20006e-10,-3.43452e-14,-27737.2,-50.6099], Tmin=(1434,'K'), Tmax=(5000,'K')),
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
    index = 332,
    label = "C3KET12",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,D} {11,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.43377,0.0582181,-6.02715e-05,3.37927e-08,-7.77732e-12,-34772.7,20.5903], Tmin=(100,'K'), Tmax=(1039.05,'K')),
            NASAPolynomial(coeffs=[10.328,0.0239777,-1.08405e-05,2.07667e-09,-1.46202e-13,-36621,-22.6599], Tmin=(1039.05,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 333,
    label = "C3KET13",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,D} {11,S}
4  O u0 p2 c0 {2,S} {5,S}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.14212,0.0721014,-0.000120049,1.11919e-07,-4.02162e-11,-33743.7,21.5572], Tmin=(100,'K'), Tmax=(851.7,'K')),
            NASAPolynomial(coeffs=[5.25945,0.0328799,-1.5953e-05,3.0254e-09,-2.06492e-13,-33723.9,6.58824], Tmin=(851.7,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 334,
    label = "C3KET21",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {11,D}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.3061,0.0570377,-5.46083e-05,2.71466e-08,-5.42262e-12,-37193.6,20.951], Tmin=(100,'K'), Tmax=(1203.12,'K')),
            NASAPolynomial(coeffs=[12.438,0.0200274,-8.46529e-06,1.57791e-09,-1.09613e-13,-39872.1,-34.8124], Tmin=(1203.12,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 335,
    label = "CH3COCH2O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  O u1 p2 c0 {2,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.34419,0.0284803,2.09194e-06,-2.15819e-08,9.66851e-12,-17717,17.6523], Tmin=(100,'K'), Tmax=(1024.44,'K')),
            NASAPolynomial(coeffs=[10.0095,0.0165278,-6.72995e-06,1.28902e-09,-9.31498e-14,-20230.9,-24.1178], Tmin=(1024.44,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 336,
    label = "C2H3CHO",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {5,D} {8,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {3,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.94492,0.0175282,8.67105e-06,-2.09285e-08,8.38162e-12,-9500.47,10.6676], Tmin=(100,'K'), Tmax=(1025.09,'K')),
            NASAPolynomial(coeffs=[7.26666,0.0139911,-5.65419e-06,1.07051e-09,-7.6579e-14,-11086.7,-13.7047], Tmin=(1025.09,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 337,
    label = "C2H3CO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 C u1 p0 c0 {1,S} {7,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.08334,0.0153204,6.54282e-06,-1.77538e-08,7.39383e-12,10067.5,11.895], Tmin=(100,'K'), Tmax=(1002.99,'K')),
            NASAPolynomial(coeffs=[6.97837,0.0111885,-4.3295e-06,8.06754e-10,-5.75268e-14,8712.68,-9.76681], Tmin=(1002.99,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 338,
    label = "C2H5CO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {9,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.91313,0.0225012,-8.59328e-06,4.8032e-10,2.48743e-13,-5274.24,14.655], Tmin=(100,'K'), Tmax=(1673.18,'K')),
            NASAPolynomial(coeffs=[7.46306,0.0158512,-6.42141e-06,1.12499e-09,-7.32055e-14,-7388.54,-11.406], Tmin=(1673.18,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 339,
    label = "C3H5O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 O u1 p2 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.74067,0.0217951,4.8776e-06,-1.91825e-08,8.13708e-12,10130.3,14.3776], Tmin=(100,'K'), Tmax=(1016.98,'K')),
            NASAPolynomial(coeffs=[7.73995,0.0156908,-6.11761e-06,1.13522e-09,-8.0312e-14,8412.28,-13.2725], Tmin=(1016.98,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 340,
    label = "CC3H6",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68011,-0.00873313,9.3403e-05,-1.1324e-07,4.2318e-11,5223.45,6.92114], Tmin=(100,'K'), Tmax=(940.77,'K')),
            NASAPolynomial(coeffs=[8.53676,0.0110486,-2.60257e-06,4.75664e-10,-4.00707e-14,2520.45,-25.7221], Tmin=(940.77,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 341,
    label = "C3H5-T",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,D} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.2624,0.0120171,1.39877e-05,-2.15736e-08,7.78289e-12,28853.5,10.3012], Tmin=(100,'K'), Tmax=(1030.45,'K')),
            NASAPolynomial(coeffs=[5.02497,0.0154866,-6.07289e-06,1.11597e-09,-7.79099e-14,27942.8,-0.911499], Tmin=(1030.45,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 342,
    label = "C3H5-S",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u1 p0 c0 {2,D} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.22799,0.0118523,1.72176e-05,-2.70806e-08,1.0284e-11,30640.6,10.1788], Tmin=(100,'K'), Tmax=(988.72,'K')),
            NASAPolynomial(coeffs=[5.81119,0.0140189,-5.21089e-06,9.48994e-10,-6.67715e-14,29513.1,-5.37308], Tmin=(988.72,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 343,
    label = "CH3CHCO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.00497,0.0183621,-5.85939e-07,-8.19991e-09,3.38657e-12,-9308.28,12.0089], Tmin=(100,'K'), Tmax=(1106.36,'K')),
            NASAPolynomial(coeffs=[5.96283,0.0150317,-6.05415e-06,1.11099e-09,-7.67706e-14,-10413.4,-4.59672], Tmin=(1106.36,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 344,
    label = "C3H4-A",
    molecule = 
"""
1 C u0 p0 c0 {3,D} {4,S} {5,S}
2 C u0 p0 c0 {3,D} {6,S} {7,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.37445,0.00704644,2.78297e-05,-3.99433e-08,1.55724e-11,21188.6,7.62055], Tmin=(100,'K'), Tmax=(949.71,'K')),
            NASAPolynomial(coeffs=[6.79962,0.00959968,-3.02062e-06,5.37812e-10,-3.92593e-14,19772.2,-12.7586], Tmin=(949.71,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 345,
    label = "C3H4-P",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.30523,0.0109265,1.31988e-05,-2.25162e-08,8.87412e-12,20738.2,7.19164], Tmin=(100,'K'), Tmax=(969.99,'K')),
            NASAPolynomial(coeffs=[5.80056,0.0113536,-4.0349e-06,7.19062e-10,-5.02183e-14,19750,-7.36971], Tmin=(969.99,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 346,
    label = "CH3CHCHO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {7,S}
3 C u0 p0 c0 {2,S} {8,D} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 O u0 p2 c0 {3,D}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.81534,0.0223479,-3.54584e-06,-5.96757e-09,2.5156e-12,-4657.75,13.3711], Tmin=(100,'K'), Tmax=(1196.39,'K')),
            NASAPolynomial(coeffs=[6.28588,0.0181143,-7.47803e-06,1.37249e-09,-9.41323e-14,-6015.61,-6.19881], Tmin=(1196.39,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 347,
    label = "CH2CHOCH2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 C u1 p0 c0 {4,S} {8,S} {9,S}
4 O u0 p2 c0 {1,S} {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.59645,0.024414,9.3789e-07,-1.8389e-08,8.69566e-12,9280.22,14.723], Tmin=(100,'K'), Tmax=(988.87,'K')),
            NASAPolynomial(coeffs=[9.07399,0.0132333,-4.88768e-06,8.99501e-10,-6.42054e-14,7264.69,-20.1684], Tmin=(988.87,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 348,
    label = "CH2CH2CHO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {6,D} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {3,D}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.76345,0.0293577,-2.47894e-05,1.49241e-08,-4.38509e-12,1397.08,14.4322], Tmin=(100,'K'), Tmax=(767.81,'K')),
            NASAPolynomial(coeffs=[4.24223,0.0216538,-9.7387e-06,1.85597e-09,-1.3004e-13,1170,7.68864], Tmin=(767.81,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 349,
    label = "AC4H7OOH",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {4,S}
3  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {6,D} {12,S}
6  C u0 p0 c0 {5,D} {13,S} {14,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.33471,0.0527831,-3.58861e-05,1.32495e-08,-2.06619e-12,-8878.92,24.3857], Tmin=(200,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[14.7661,0.0212235,-7.09403e-06,1.08424e-09,-6.22146e-14,-13561.7,-47.7449], Tmin=(1395,'K'), Tmax=(5000,'K')),
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
    index = 350,
    label = "C3H5OH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  O u0 p2 c0 {1,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.70167,0.0329592,-1.64644e-05,-1.88006e-08,2.39354e-11,-17234.3,12.1895], Tmin=(100,'K'), Tmax=(515.48,'K')),
            NASAPolynomial(coeffs=[4.96613,0.023077,-1.00832e-05,1.88372e-09,-1.30032e-13,-17569.9,1.77443], Tmin=(515.48,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 351,
    label = "IC3H5OH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  O u0 p2 c0 {2,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.38641,0.0274093,4.34148e-06,-2.73979e-08,1.32363e-11,-22341.8,13.2843], Tmin=(100,'K'), Tmax=(947.68,'K')),
            NASAPolynomial(coeffs=[10.6449,0.0125719,-3.86211e-06,6.65035e-10,-4.73689e-14,-24806.1,-30.8579], Tmin=(947.68,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 352,
    label = "SC3H5OH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  O u0 p2 c0 {3,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.43519,0.0321429,-2.11365e-05,7.43423e-09,-1.09823e-12,-20020.5,13.0756], Tmin=(100,'K'), Tmax=(1529.3,'K')),
            NASAPolynomial(coeffs=[8.00325,0.0175792,-6.85174e-06,1.20709e-09,-8.02557e-14,-21723.5,-16.1524], Tmin=(1529.3,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 353,
    label = "C3H6OH1-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  O u0 p2 c0 {1,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.51532,0.0312457,-1.61816e-05,4.02432e-09,-4.02053e-13,-8943.85,17.5114], Tmin=(100,'K'), Tmax=(2194.63,'K')),
            NASAPolynomial(coeffs=[10.2171,0.017208,-6.587e-06,1.10973e-09,-7.00371e-14,-12324.3,-25.699], Tmin=(2194.63,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 354,
    label = "C3H6OH2-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.18969,0.0381965,-2.88367e-05,1.21306e-08,-2.1507e-12,-9521.42,16.5386], Tmin=(100,'K'), Tmax=(1304.99,'K')),
            NASAPolynomial(coeffs=[8.15445,0.0199134,-7.82137e-06,1.39467e-09,-9.39839e-14,-11078.2,-13.8257], Tmin=(1304.99,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 355,
    label = "CH2CCH2OH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,D} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {2,D}
4 O u0 p2 c0 {1,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.88423,0.0242428,-1.14152e-05,1.71775e-09,1.42177e-13,11793.6,15.2102], Tmin=(200,'K'), Tmax=(1372,'K')),
            NASAPolynomial(coeffs=[9.70702,0.0113973,-3.77994e-06,5.75209e-10,-3.29229e-14,9132.13,-22.5013], Tmin=(1372,'K'), Tmax=(5000,'K')),
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
    index = 356,
    label = "HOC3H6O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {5,S} {13,S}
3  O u1 p2 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
6  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.8496,0.0477245,-3.60393e-05,1.4348e-08,-2.33508e-12,-28210.6,17.6479], Tmin=(200,'K'), Tmax=(1407,'K')),
            NASAPolynomial(coeffs=[15.6948,0.0157704,-5.30502e-06,8.14308e-10,-4.68666e-14,-32454.1,-50.6084], Tmin=(1407,'K'), Tmax=(5000,'K')),
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
    index = 357,
    label = "CC3H4",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {1,S} {2,D} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63519,-0.00323129,6.10381e-05,-7.68393e-08,2.92232e-11,32671.6,7.35716], Tmin=(100,'K'), Tmax=(938.64,'K')),
            NASAPolynomial(coeffs=[7.97929,0.00707116,-1.47308e-06,2.63789e-10,-2.3197e-14,30586.7,-20.0873], Tmin=(938.64,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 358,
    label = "SC3H4OH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u1 p0 c0 {1,S} {7,S} {8,S}
3 C u0 p0 c0 {1,D} {5,S} {6,S}
4 O u0 p2 c0 {1,S} {9,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.45197,0.0252315,7.36788e-06,-3.20551e-08,1.54969e-11,-2653.17,13.2869], Tmin=(100,'K'), Tmax=(934.46,'K')),
            NASAPolynomial(coeffs=[11.5253,0.00876817,-2.12256e-06,3.4011e-10,-2.53343e-14,-5325.84,-35.099], Tmin=(934.46,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 359,
    label = "PC3H4OH-2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {3,D} {4,S} {8,S}
3 C u1 p0 c0 {1,S} {2,D}
4 O u0 p2 c0 {2,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.56676,0.0231267,9.16417e-06,-3.0078e-08,1.35646e-11,9376.94,14.6341], Tmin=(100,'K'), Tmax=(966.68,'K')),
            NASAPolynomial(coeffs=[10.4411,0.010989,-3.72694e-06,6.91354e-10,-5.122e-14,6899.25,-28.0294], Tmin=(966.68,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 360,
    label = "C3H3O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,D} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {4,D} {7,S}
3 C u1 p0 c0 {1,D} {2,S}
4 O u0 p2 c0 {2,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.94303,0.0199369,-7.68289e-06,-1.86787e-09,1.48738e-12,21035.9,13.002], Tmin=(100,'K'), Tmax=(1149.86,'K')),
            NASAPolynomial(coeffs=[6.82982,0.0121551,-5.01835e-06,9.27997e-10,-6.4247e-14,19762.6,-7.94215], Tmin=(1149.86,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 361,
    label = "C3H3O2H",
    molecule = 
"""
1 C u0 p0 c0 {3,D} {4,S} {6,S}
2 C u0 p0 c0 {3,D} {7,S} {8,S}
3 C u0 p0 c0 {1,D} {2,D}
4 O u0 p2 c0 {1,S} {5,S}
5 O u0 p2 c0 {4,S} {9,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.11811,0.0353626,-2.38197e-05,1.98138e-09,2.62189e-12,12565.2,6.66283], Tmin=(100,'K'), Tmax=(1008.98,'K')),
            NASAPolynomial(coeffs=[11.7719,0.00940162,-3.52672e-06,6.65914e-10,-4.84841e-14,9990.46,-43.103], Tmin=(1008.98,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 362,
    label = "C2HCHO",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {5,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {6,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.06054,0.0177781,-8.66411e-06,-1.08537e-09,1.595e-12,14366.7,10.6366], Tmin=(100,'K'), Tmax=(1040.53,'K')),
            NASAPolynomial(coeffs=[6.91877,0.0084981,-3.28959e-06,5.98838e-10,-4.16222e-14,13263.2,-9.57469], Tmin=(1040.53,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 363,
    label = "C3H2",
    molecule = 
"""
multiplicity 3
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 C u0 p0 c0 {1,S} {5,T}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 C u1 p0 c0 {2,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.19757,0.0177615,-1.90654e-05,1.13245e-08,-2.73191e-12,70228.5,7.16215], Tmin=(100,'K'), Tmax=(1002.82,'K')),
            NASAPolynomial(coeffs=[5.92594,0.00687878,-2.78724e-06,5.02956e-10,-3.4163e-14,69681.3,-6.00839], Tmin=(1002.82,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 364,
    label = "C3H2C",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {3,S} {5,S}
3 C u2 p0 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.12959,0.0172874,-1.13668e-05,3.45693e-09,-3.6616e-13,58419.1,17.3314], Tmin=(200,'K'), Tmax=(1500,'K')),
            NASAPolynomial(coeffs=[6.56327,0.00523633,-1.75448e-06,2.68661e-10,-1.54285e-14,56514.6,-12.0006], Tmin=(1500,'K'), Tmax=(5000,'K')),
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
    index = 365,
    label = "CH3COCH2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  O u0 p2 c0 {1,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.84097,0.0464944,-4.03241e-05,1.85913e-08,-3.5255e-12,-18394.8,21.0358], Tmin=(100,'K'), Tmax=(1242.87,'K')),
            NASAPolynomial(coeffs=[9.98394,0.020287,-8.69442e-06,1.62515e-09,-1.12754e-13,-20418.9,-20.0197], Tmin=(1242.87,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 366,
    label = "CCCC(=O)OCC",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {8,S}
2  O u0 p2 c0 {8,D}
3  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {8,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
7  C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
8  C u0 p0 c0 {1,S} {2,D} {4,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.180158,0.071282,-2.53459e-05,-1.75363e-08,1.19412e-11,-61356.7,32.189], Tmin=(100,'K'), Tmax=(993.25,'K')),
            NASAPolynomial(coeffs=[16.0924,0.035077,-1.27679e-05,2.27751e-09,-1.57914e-13,-65892.8,-51.3926], Tmin=(993.25,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 367,
    label = "COC(=O)CCC(C)=O",
    molecule = 
"""
1  O u0 p2 c0 {7,S} {9,S}
2  O u0 p2 c0 {8,D}
3  O u0 p2 c0 {9,D}
4  C u0 p0 c0 {5,S} {8,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {9,S} {12,S} {13,S}
6  C u0 p0 c0 {8,S} {14,S} {15,S} {16,S}
7  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
8  C u0 p0 c0 {2,D} {4,S} {6,S}
9  C u0 p0 c0 {1,S} {3,D} {5,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.471426,0.0854259,-0.00010097,8.81969e-08,-3.39715e-11,-73584.1,31.8714], Tmin=(100,'K'), Tmax=(753.86,'K')),
            NASAPolynomial(coeffs=[3.35081,0.0595796,-2.85131e-05,5.52455e-09,-3.88033e-13,-73717.9,20.7853], Tmin=(753.86,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 368,
    label = "C=C(C)OCC(=O)OCC",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {6,S} {8,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {7,D} {8,S}
6  C u0 p0 c0 {2,S} {9,S} {20,D}
7  C u0 p0 c0 {5,D} {21,S} {22,S}
8  O u0 p2 c0 {2,S} {5,S}
9  O u0 p2 c0 {1,S} {6,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {6,D}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.37689,0.102633,-8.0625e-05,3.17981e-08,-5.0002e-12,-69487.4,37.9995], Tmin=(100,'K'), Tmax=(1515.37,'K')),
            NASAPolynomial(coeffs=[24.0982,0.0353882,-1.40617e-05,2.5143e-09,-1.69036e-13,-77208.2,-95.492], Tmin=(1515.37,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 369,
    label = "C=C(OCC)OCC(C)=O",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {8,S} {10,S} {11,S}
2  C u0 p0 c0 {5,S} {9,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {2,S} {4,S} {20,D}
6  C u0 p0 c0 {7,D} {8,S} {9,S}
7  C u0 p0 c0 {6,D} {21,S} {22,S}
8  O u0 p2 c0 {1,S} {6,S}
9  O u0 p2 c0 {2,S} {6,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {5,D}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.90391,0.11557,-0.000107063,4.98522e-08,-9.13076e-12,-57863,36.9373], Tmin=(100,'K'), Tmax=(1326.94,'K')),
            NASAPolynomial(coeffs=[25.9463,0.0316167,-1.21598e-05,2.17186e-09,-1.47587e-13,-65254.1,-105.302], Tmin=(1326.94,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 370,
    label = "CCOC(=O)CC=C(C)O",
    molecule = 
"""
1  C u0 p0 c0 {6,S} {7,S} {10,S} {11,S}
2  C u0 p0 c0 {3,S} {8,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,D} {9,S}
6  C u0 p0 c0 {1,S} {5,D} {20,S}
7  C u0 p0 c0 {1,S} {8,S} {21,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {5,S} {22,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {6,S}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.23775,0.098256,-7.11337e-05,2.4766e-08,-3.40935e-12,-75484.9,38.1579], Tmin=(100,'K'), Tmax=(1715.51,'K')),
            NASAPolynomial(coeffs=[26.8057,0.0328673,-1.39589e-05,2.54697e-09,-1.71362e-13,-85106.6,-112.271], Tmin=(1715.51,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 371,
    label = "C=C(O)CCC(=O)OCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {8,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {7,D} {9,S}
6  C u0 p0 c0 {2,S} {8,S} {19,D}
7  C u0 p0 c0 {5,D} {20,S} {21,S}
8  O u0 p2 c0 {3,S} {6,S}
9  O u0 p2 c0 {5,S} {22,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {6,D}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.845503,0.102092,-8.51196e-05,3.73417e-08,-6.71413e-12,-74780.6,37.5812], Tmin=(100,'K'), Tmax=(1308.58,'K')),
            NASAPolynomial(coeffs=[18.1476,0.0440353,-1.85703e-05,3.43776e-09,-2.36928e-13,-79751.5,-59.1578], Tmin=(1308.58,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 372,
    label = "CCOC(O)=CCC(C)=O",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {6,S} {10,S} {11,S}
2  C u0 p0 c0 {3,S} {8,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {4,S} {20,D}
6  C u0 p0 c0 {1,S} {7,D} {21,S}
7  C u0 p0 c0 {6,D} {8,S} {9,S}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {7,S} {22,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {5,D}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.65029,0.110075,-9.45765e-05,3.99697e-08,-6.66868e-12,-63866.2,36.6673], Tmin=(100,'K'), Tmax=(1440.56,'K')),
            NASAPolynomial(coeffs=[26.3028,0.0324571,-1.3756e-05,2.56719e-09,-1.77703e-13,-71919.8,-108.394], Tmin=(1440.56,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 373,
    label = "CCOC(=O)CC[C](C)O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {8,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {6,S} {19,S} {20,S} {21,S}
6  C u1 p0 c0 {1,S} {5,S} {9,S}
7  C u0 p0 c0 {2,S} {8,S} {22,D}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {6,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.261661,0.106186,-9.12459e-05,1.78317e-08,2.19168e-11,-63880.3,36.861], Tmin=(100,'K'), Tmax=(553.21,'K')),
            NASAPolynomial(coeffs=[8.0412,0.0649408,-3.03567e-05,5.8473e-09,-4.10795e-13,-65086.4,-0.878649], Tmin=(553.21,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 374,
    label = "CCO[C](O)CCC(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {8,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {6,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {5,S} {22,D}
7  C u1 p0 c0 {2,S} {8,S} {9,S}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u0 p2 c0 {6,D}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.915515,0.117039,-0.000140523,1.06293e-07,-3.46077e-11,-54385.3,40.607], Tmin=(100,'K'), Tmax=(734.91,'K')),
            NASAPolynomial(coeffs=[9.06454,0.062723,-2.96679e-05,5.73808e-09,-4.03507e-13,-55852.3,-4.46773], Tmin=(734.91,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 375,
    label = "CCOC(=O)CCC(C)[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {6,S} {8,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {20,S} {21,S} {22,S}
6  C u0 p0 c0 {4,S} {17,S} {18,S} {19,S}
7  C u0 p0 c0 {3,S} {8,S} {23,D}
8  O u0 p2 c0 {4,S} {7,S}
9  O u1 p2 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.130642,0.0977146,-7.58808e-05,3.33972e-08,-6.53643e-12,-57416.4,36.6589], Tmin=(100,'K'), Tmax=(1136.76,'K')),
            NASAPolynomial(coeffs=[10.1506,0.0615379,-2.81449e-05,5.40235e-09,-3.79805e-13,-59753.8,-14.26], Tmin=(1136.76,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 376,
    label = "CCOC([O])CCC(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {8,S} {13,S} {16,S}
4  C u0 p0 c0 {5,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {4,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {7,S} {20,S} {21,S} {22,S}
7  C u0 p0 c0 {2,S} {6,S} {23,D}
8  O u0 p2 c0 {3,S} {4,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u1 p2 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.77808,0.116076,-0.000152802,1.35452e-07,-5.07359e-11,-51932,40.2675], Tmin=(100,'K'), Tmax=(772.09,'K')),
            NASAPolynomial(coeffs=[4.91646,0.0708121,-3.42411e-05,6.6385e-09,-4.6525e-13,-52341.5,17.3101], Tmin=(772.09,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 377,
    label = "[CH]C",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p1 c0 {1,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.36869,0.0164233,-2.16504e-05,2.18229e-08,-8.70188e-12,42868.3,21.8539], Tmin=(100,'K'), Tmax=(846.1,'K')),
            NASAPolynomial(coeffs=[2.62345,0.0138429,-6.25541e-06,1.16703e-09,-7.95359e-14,43212.9,26.6158], Tmin=(846.1,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 378,
    label = "CCCC([O])=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u1 p2 c0 {4,S}
13 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.97164,0.0428384,-2.34823e-05,5.77731e-09,-5.48282e-13,-32204.2,19.2123], Tmin=(100,'K'), Tmax=(2440.79,'K')),
            NASAPolynomial(coeffs=[19.004,0.0149245,-6.32695e-06,1.0914e-09,-6.83052e-14,-40518.3,-78.1569], Tmin=(2440.79,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 379,
    label = "C=C(C)OCC([O])=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,D} {6,S}
4  C u0 p0 c0 {1,S} {12,S} {13,D}
5  C u0 p0 c0 {3,D} {14,S} {15,S}
6  O u0 p2 c0 {1,S} {3,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u1 p2 c0 {4,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.561107,0.0678925,-5.14996e-05,1.92125e-08,-2.87159e-12,-40025.1,26.7311], Tmin=(100,'K'), Tmax=(1570.48,'K')),
            NASAPolynomial(coeffs=[17.1729,0.0255823,-1.1088e-05,2.05775e-09,-1.40777e-13,-45242.8,-60.9092], Tmin=(1570.48,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 380,
    label = "[CH2]C(=O)OCC(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {12,D}
4  C u0 p0 c0 {5,S} {6,S} {13,D}
5  C u1 p0 c0 {4,S} {14,S} {15,S}
6  O u0 p2 c0 {1,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {3,D}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.11402,0.0613807,-4.33129e-05,1.52699e-08,-2.21292e-12,-44799.5,29.3234], Tmin=(100,'K'), Tmax=(1564.68,'K')),
            NASAPolynomial(coeffs=[13.3526,0.0300933,-1.33183e-05,2.48992e-09,-1.70938e-13,-48629.4,-35.1992], Tmin=(1564.68,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 381,
    label = "CC(=O)CC[C]1OO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {3,S} {15,D}
5  C u1 p0 c0 {2,S} {6,S} {7,S}
6  O u0 p2 c0 {5,S} {7,S}
7  O u0 p2 c0 {5,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.639912,0.066049,-4.96046e-05,1.56624e-08,-6.55824e-13,-4992.88,29.3874], Tmin=(100,'K'), Tmax=(1040.53,'K')),
            NASAPolynomial(coeffs=[14.5054,0.0254611,-9.42181e-06,1.65992e-09,-1.12885e-13,-8566.61,-41.3634], Tmin=(1040.53,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 382,
    label = "C[C]1CCC(=O)OO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {3,S} {6,S}
5  C u0 p0 c0 {2,S} {7,S} {15,D}
6  O u0 p2 c0 {4,S} {7,S}
7  O u0 p2 c0 {5,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.40413,0.0355881,5.58228e-05,-9.16529e-08,3.44485e-11,-32107,21.9653], Tmin=(100,'K'), Tmax=(1038.63,'K')),
            NASAPolynomial(coeffs=[16.304,0.0314117,-1.49874e-05,3.12105e-09,-2.35953e-13,-38071.9,-64.2983], Tmin=(1038.63,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 383,
    label = "CC1([O])CCC(=O)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {6,S} {15,D}
6  O u0 p2 c0 {1,S} {5,S}
7  O u1 p2 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.65491,0.0303532,6.74652e-05,-1.13838e-07,4.75851e-11,-47849.1,24.1207], Tmin=(100,'K'), Tmax=(930.24,'K')),
            NASAPolynomial(coeffs=[16.3959,0.0211687,-5.12295e-06,8.16755e-10,-6.08091e-14,-52936.8,-58.5353], Tmin=(930.24,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 384,
    label = "CC(O)=CCC([O])=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,D} {6,S}
4  C u0 p0 c0 {1,S} {3,D} {12,S}
5  C u0 p0 c0 {1,S} {13,S} {14,D}
6  O u0 p2 c0 {3,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 O u1 p2 c0 {5,S}
14 O u0 p2 c0 {5,D}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.643649,0.0640386,-4.33024e-05,1.33033e-08,-1.59122e-12,-46019.7,27.1042], Tmin=(100,'K'), Tmax=(1960.83,'K')),
            NASAPolynomial(coeffs=[22.4358,0.0195825,-9.29342e-06,1.74019e-09,-1.16919e-13,-54565.6,-92.7036], Tmin=(1960.83,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 385,
    label = "CC(=O)C[CH]C(=O)O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {12,D}
4  C u1 p0 c0 {1,S} {5,S} {13,S}
5  C u0 p0 c0 {4,S} {6,S} {14,D}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {3,D}
13 H u0 p0 c0 {4,S}
14 O u0 p2 c0 {5,D}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.83838,0.0572684,-1.40441e-05,-7.52669e-08,8.02593e-11,-52816.6,26.4488], Tmin=(100,'K'), Tmax=(458.34,'K')),
            NASAPolynomial(coeffs=[4.844,0.0453529,-2.1897e-05,4.29654e-09,-3.0544e-13,-53242.5,12.653], Tmin=(458.34,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 386,
    label = "[CH2]C(=O)CCC(=O)O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,D}
4  C u0 p0 c0 {2,S} {6,S} {12,D}
5  C u1 p0 c0 {3,S} {13,S} {14,S}
6  O u0 p2 c0 {4,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.23151,0.0700853,-5.80378e-05,5.48689e-09,2.01355e-11,-55585.4,26.3015], Tmin=(100,'K'), Tmax=(526.74,'K')),
            NASAPolynomial(coeffs=[6.11255,0.0452743,-2.22823e-05,4.40297e-09,-3.14091e-13,-56269.6,4.26853], Tmin=(526.74,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 387,
    label = "[CH2]C=C(C)O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u1 p0 c0 {3,S} {10,S} {11,S}
5  O u0 p2 c0 {2,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.65237,0.0402052,-1.24888e-06,-3.34669e-08,1.76542e-11,-11085.7,17.7359], Tmin=(100,'K'), Tmax=(939.66,'K')),
            NASAPolynomial(coeffs=[14.798,0.0129178,-3.45889e-06,5.73692e-10,-4.19419e-14,-14821.9,-51.6012], Tmin=(939.66,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 388,
    label = "C=C([O])CC(=O)OCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {7,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {6,D} {15,S}
5  C u0 p0 c0 {1,S} {7,S} {16,D}
6  C u0 p0 c0 {4,D} {17,S} {18,S}
7  O u0 p2 c0 {2,S} {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u1 p2 c0 {4,S}
16 O u0 p2 c0 {5,D}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0942979,0.0771926,-5.29728e-05,1.71388e-08,-2.18511e-12,-54622.5,33.7479], Tmin=(100,'K'), Tmax=(1838.57,'K')),
            NASAPolynomial(coeffs=[23.2714,0.0263595,-1.15016e-05,2.10176e-09,-1.40499e-13,-63214.6,-93.2081], Tmin=(1838.57,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 389,
    label = "[CH2]CC(=O)O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,D}
3  C u1 p0 c0 {1,S} {8,S} {9,S}
4  O u0 p2 c0 {2,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  O u0 p2 c0 {2,D}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.19349,0.0337443,-1.58596e-05,-2.4854e-09,2.97487e-12,-30969.1,18.4655], Tmin=(100,'K'), Tmax=(1080.5,'K')),
            NASAPolynomial(coeffs=[10.0577,0.0157693,-6.36828e-06,1.19872e-09,-8.49023e-14,-33318.7,-23.0923], Tmin=(1080.5,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 390,
    label = "C[CH]OC(=O)CC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {6,S} {15,D}
5  C u1 p0 c0 {3,S} {6,S} {16,S}
6  O u0 p2 c0 {4,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {4,D}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.814153,0.0650055,-4.5793e-05,1.53004e-08,-2.036e-12,-35636.1,27.3171], Tmin=(100,'K'), Tmax=(1734.68,'K')),
            NASAPolynomial(coeffs=[17.8513,0.0257201,-1.18227e-05,2.24517e-09,-1.54519e-13,-41546.9,-64.2617], Tmin=(1734.68,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 391,
    label = "C[CH]OC(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
3  C u1 p0 c0 {1,S} {5,S} {13,S}
4  C u0 p0 c0 {2,S} {5,S} {12,D}
5  O u0 p2 c0 {3,S} {4,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.25548,0.0474761,-5.43559e-06,-8.80175e-08,9.37216e-11,-33187.9,18.1082], Tmin=(100,'K'), Tmax=(430.42,'K')),
            NASAPolynomial(coeffs=[4.59989,0.038632,-1.97203e-05,3.97118e-09,-2.86437e-13,-33509.6,7.38131], Tmin=(430.42,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 392,
    label = "CCOC(=O)[CH]C=C=O",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {7,S}
2  O u0 p2 c0 {7,D}
3  O u0 p2 c0 {9,D}
4  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
6  C u1 p0 c0 {7,S} {8,S} {15,S}
7  C u0 p0 c0 {1,S} {2,D} {6,S}
8  C u0 p0 c0 {6,S} {9,D} {16,S}
9  C u0 p0 c0 {3,D} {8,D}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.765675,0.0731321,-5.6864e-05,2.28934e-08,-3.87668e-12,-42144.1,28.3053], Tmin=(100,'K'), Tmax=(1339.09,'K')),
            NASAPolynomial(coeffs=[12.4618,0.0381947,-1.77285e-05,3.40992e-09,-2.39237e-13,-45276.6,-31.5369], Tmin=(1339.09,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 393,
    label = "CCOC(=O)C[C]C=O",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {7,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {6,S} {15,D}
5  C u0 p0 c0 {7,S} {16,D} {17,S}
6  O u0 p2 c0 {1,S} {4,S}
7  C u0 p1 c0 {2,S} {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {4,D}
16 O u0 p2 c0 {5,D}
17 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.891198,0.0755067,-6.6358e-05,3.83209e-08,-1.05936e-11,-19527.4,41.6881], Tmin=(100,'K'), Tmax=(812.23,'K')),
            NASAPolynomial(coeffs=[5.34467,0.0535751,-2.58563e-05,5.07839e-09,-3.61926e-13,-20250.9,21.1288], Tmin=(812.23,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 394,
    label = "C=CC(=O)O[CH]C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {6,S} {11,S}
3  C u0 p0 c0 {4,S} {5,D} {10,S}
4  C u0 p0 c0 {3,S} {6,S} {12,D}
5  C u0 p0 c0 {3,D} {13,S} {14,S}
6  O u0 p2 c0 {2,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.10107,0.0502709,-8.53627e-06,-2.77501e-08,1.4519e-11,-21599.6,29.2745], Tmin=(100,'K'), Tmax=(1009.55,'K')),
            NASAPolynomial(coeffs=[16.5883,0.0193035,-7.68685e-06,1.51241e-09,-1.12728e-13,-26275.6,-53.2613], Tmin=(1009.55,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 395,
    label = "C=[C]C(=O)OCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {6,S} {12,D}
4  C u0 p0 c0 {6,D} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {3,S}
6  C u1 p0 c0 {3,S} {4,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {3,D}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.19132,0.0514949,-2.17721e-05,-8.13405e-09,6.32268e-12,-15091.1,29.0501], Tmin=(100,'K'), Tmax=(1069.57,'K')),
            NASAPolynomial(coeffs=[14.3567,0.0224639,-9.3943e-06,1.81299e-09,-1.30658e-13,-19063.1,-40.7534], Tmin=(1069.57,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 396,
    label = "[CH]=CC(=O)OCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {5,S} {12,D}
4  C u0 p0 c0 {3,S} {6,D} {13,S}
5  O u0 p2 c0 {1,S} {3,S}
6  C u1 p0 c0 {4,D} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {3,D}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.2657,0.0500379,-1.84293e-05,-1.09605e-08,7.27169e-12,-14716.9,28.48], Tmin=(100,'K'), Tmax=(1053.76,'K')),
            NASAPolynomial(coeffs=[13.7082,0.0232746,-9.46729e-06,1.80184e-09,-1.29042e-13,-18475.5,-37.5916], Tmin=(1053.76,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 397,
    label = "C=CC(=O)O",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u0 p0 c0 {1,S} {4,S} {6,D}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 O u0 p2 c0 {2,S} {9,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.49362,0.0234065,1.34333e-05,-3.67609e-08,1.63433e-11,-40743.5,15.5102], Tmin=(100,'K'), Tmax=(963.1,'K')),
            NASAPolynomial(coeffs=[11.3905,0.0103364,-3.40484e-06,6.41151e-10,-4.87449e-14,-43564.8,-32.8277], Tmin=(963.1,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 398,
    label = "C=CC(=O)C(C)=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,D}
3  C u0 p0 c0 {2,S} {4,S} {10,D}
4  C u0 p0 c0 {3,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {12,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {2,D}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.92616,0.0497265,-3.40783e-05,1.19968e-08,-1.82304e-12,-29482.2,21.637], Tmin=(100,'K'), Tmax=(1412.6,'K')),
            NASAPolynomial(coeffs=[8.40485,0.0313812,-1.45981e-05,2.80336e-09,-1.9601e-13,-31312.6,-11.857], Tmin=(1412.6,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 399,
    label = "CC(=O)C[C]C=O",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {11,D}
4  C u0 p0 c0 {5,S} {12,D} {13,S}
5  C u0 p1 c0 {1,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.02222,0.0504765,-2.55778e-05,-2.2876e-08,3.05707e-11,8179.24,33.5079], Tmin=(100,'K'), Tmax=(503.03,'K')),
            NASAPolynomial(coeffs=[4.56251,0.0392512,-1.88665e-05,3.69741e-09,-2.63147e-13,7810.13,21.8693], Tmin=(503.03,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 400,
    label = "CCOC(=O)[CH]C(=O)C(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {5,S} {17,D}
5  C u0 p0 c0 {4,S} {6,S} {18,D}
6  C u1 p0 c0 {5,S} {7,S} {19,S}
7  C u0 p0 c0 {6,S} {8,S} {20,D}
8  O u0 p2 c0 {1,S} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 O u0 p2 c0 {4,D}
18 O u0 p2 c0 {5,D}
19 H u0 p0 c0 {6,S}
20 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0906334,0.0983762,-9.02754e-05,4.68894e-08,-1.06274e-11,-66689.2,37.1368], Tmin=(100,'K'), Tmax=(1013.46,'K')),
            NASAPolynomial(coeffs=[10.7176,0.0557186,-2.71403e-05,5.35944e-09,-3.8309e-13,-68880,-15.1515], Tmin=(1013.46,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 401,
    label = "C[CH]OC(=O)CC(=O)C(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
2  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {7,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {5,S} {18,D}
5  C u0 p0 c0 {2,S} {4,S} {17,D}
6  C u0 p0 c0 {1,S} {8,S} {19,D}
7  C u1 p0 c0 {3,S} {8,S} {20,S}
8  O u0 p2 c0 {6,S} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 O u0 p2 c0 {5,D}
18 O u0 p2 c0 {4,D}
19 O u0 p2 c0 {6,D}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.339696,0.102647,-9.81006e-05,5.13956e-08,-1.14346e-11,-64771.5,38.5837], Tmin=(100,'K'), Tmax=(1047.65,'K')),
            NASAPolynomial(coeffs=[13.0087,0.051683,-2.51332e-05,4.96419e-09,-3.5498e-13,-67568.5,-26.4363], Tmin=(1047.65,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 402,
    label = "CCOC(=O)CC(=O)[C]=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {6,S} {16,D}
5  C u0 p0 c0 {1,S} {7,S} {15,D}
6  O u0 p2 c0 {2,S} {4,S}
7  C u1 p0 c0 {5,S} {17,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {5,D}
16 O u0 p2 c0 {4,D}
17 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.236993,0.0900316,-0.000101563,6.82644e-08,-1.96671e-11,-60784.8,34.901], Tmin=(100,'K'), Tmax=(824.61,'K')),
            NASAPolynomial(coeffs=[9.18313,0.0466338,-2.26169e-05,4.43639e-09,-3.15268e-13,-62260.2,-6.53333], Tmin=(824.61,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 403,
    label = "CCOC(=O)C[C]=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {5,S} {14,D}
5  O u0 p2 c0 {1,S} {4,S}
6  C u1 p0 c0 {2,S} {15,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.816577,0.075647,-9.08574e-05,6.85764e-08,-2.22447e-11,-47808.2,28.1566], Tmin=(100,'K'), Tmax=(738.19,'K')),
            NASAPolynomial(coeffs=[7.34253,0.0402807,-1.89843e-05,3.65904e-09,-2.56689e-13,-48771.5,-1.34557], Tmin=(738.19,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 404,
    label = "CCOC(=O)C(=O)C=C(C)[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {5,D} {17,S}
5  C u0 p0 c0 {4,D} {6,S} {19,S}
6  C u0 p0 c0 {5,S} {7,S} {18,D}
7  C u0 p0 c0 {6,S} {8,S} {20,D}
8  O u0 p2 c0 {1,S} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 O u1 p2 c0 {4,S}
18 O u0 p2 c0 {6,D}
19 H u0 p0 c0 {5,S}
20 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.466518,0.106528,-0.000116998,7.55831e-08,-2.08702e-11,-68918.8,37.1087], Tmin=(100,'K'), Tmax=(858.86,'K')),
            NASAPolynomial(coeffs=[10.6911,0.054564,-2.62434e-05,5.13797e-09,-3.65029e-13,-70835.4,-15.0228], Tmin=(858.86,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 405,
    label = "C[CH]OC(=O)C(=O)CC(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {2,S} {17,D}
5  C u0 p0 c0 {1,S} {7,S} {18,D}
6  C u1 p0 c0 {3,S} {8,S} {19,S}
7  C u0 p0 c0 {5,S} {8,S} {20,D}
8  O u0 p2 c0 {6,S} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 O u0 p2 c0 {4,D}
18 O u0 p2 c0 {5,D}
19 H u0 p0 c0 {6,S}
20 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.499431,0.107817,-0.000112725,6.5913e-08,-1.63677e-11,-62974.5,38.4635], Tmin=(100,'K'), Tmax=(948.16,'K')),
            NASAPolynomial(coeffs=[12.422,0.0533045,-2.64831e-05,5.27384e-09,-3.78713e-13,-65424.8,-23.1867], Tmin=(948.16,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 406,
    label = "C=C([O])CC(=O)C(=O)OCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {17,D}
5  C u0 p0 c0 {1,S} {7,D} {16,S}
6  C u0 p0 c0 {4,S} {8,S} {18,D}
7  C u0 p0 c0 {5,D} {19,S} {20,S}
8  O u0 p2 c0 {2,S} {6,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u1 p2 c0 {5,S}
17 O u0 p2 c0 {4,D}
18 O u0 p2 c0 {6,D}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.220208,0.0966996,-7.82787e-05,3.16127e-08,-5.28912e-12,-66825.1,36.1069], Tmin=(100,'K'), Tmax=(1363.26,'K')),
            NASAPolynomial(coeffs=[16.9346,0.0463652,-2.28958e-05,4.52926e-09,-3.22479e-13,-71502.5,-51.9713], Tmin=(1363.26,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 407,
    label = "CC(=O)CC=O",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  C u0 p0 c0 {1,S} {11,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.18311,0.0405603,-2.46576e-05,7.3782e-09,-9.14201e-13,-39352.1,20.4457], Tmin=(100,'K'), Tmax=(1746.51,'K')),
            NASAPolynomial(coeffs=[9.51242,0.0237741,-1.02406e-05,1.87506e-09,-1.26467e-13,-41912.3,-19.0009], Tmin=(1746.51,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 408,
    label = "[CH2]C(=O)OC(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,D}
3  C u0 p0 c0 {4,S} {5,S} {10,D}
4  C u1 p0 c0 {3,S} {11,S} {12,S}
5  O u0 p2 c0 {2,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {2,D}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.8439,0.0406507,-1.69346e-05,-1.99015e-09,2.09271e-12,-45946.2,27.6374], Tmin=(100,'K'), Tmax=(1272.82,'K')),
            NASAPolynomial(coeffs=[11.1599,0.0233018,-1.05457e-05,2.0259e-09,-1.42174e-13,-49283.9,-23.3497], Tmin=(1272.82,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 409,
    label = "[CH2]C(=O)OC(=O)CCC(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {3,S} {16,D}
5  C u0 p0 c0 {2,S} {8,S} {17,D}
6  C u0 p0 c0 {7,S} {8,S} {18,D}
7  C u1 p0 c0 {6,S} {19,S} {20,S}
8  O u0 p2 c0 {5,S} {6,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u0 p2 c0 {4,D}
17 O u0 p2 c0 {5,D}
18 O u0 p2 c0 {6,D}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.842403,0.118431,-0.000178248,1.59462e-07,-5.72079e-11,-68597.4,43.6561], Tmin=(100,'K'), Tmax=(813.52,'K')),
            NASAPolynomial(coeffs=[7.44994,0.0572509,-2.78122e-05,5.34541e-09,-3.70493e-13,-69271.3,9.51231], Tmin=(813.52,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 410,
    label = "CC(=O)O",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,D}
3 O u0 p2 c0 {2,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.21749,0.0102436,2.71475e-05,-3.7638e-08,1.35869e-11,-53545.7,12.0525], Tmin=(100,'K'), Tmax=(1020.01,'K')),
            NASAPolynomial(coeffs=[6.3612,0.0155129,-6.47988e-06,1.25443e-09,-9.10572e-14,-55102.4,-7.66372], Tmin=(1020.01,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 411,
    label = "C[CH]OC(=O)CC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,D}
4  C u1 p0 c0 {2,S} {6,S} {13,S}
5  C u0 p0 c0 {1,S} {14,D} {15,S}
6  O u0 p2 c0 {3,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {3,D}
13 H u0 p0 c0 {4,S}
14 O u0 p2 c0 {5,D}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.997728,0.0658364,-5.08605e-05,1.99428e-08,-3.2351e-12,-44229.7,29.4985], Tmin=(100,'K'), Tmax=(1410.68,'K')),
            NASAPolynomial(coeffs=[13.0375,0.0316974,-1.45599e-05,2.78767e-09,-1.94873e-13,-47626.5,-32.7291], Tmin=(1410.68,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 412,
    label = "CCOC(=O)[CH]C=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u1 p0 c0 {4,S} {5,S} {12,S}
4  C u0 p0 c0 {3,S} {6,S} {13,D}
5  C u0 p0 c0 {3,S} {14,D} {15,S}
6  O u0 p2 c0 {1,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 O u0 p2 c0 {5,D}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.30807,0.0609942,-4.15796e-05,1.40652e-08,-1.98429e-12,-46150.6,27.8193], Tmin=(100,'K'), Tmax=(1560.91,'K')),
            NASAPolynomial(coeffs=[11.8769,0.0339106,-1.55532e-05,2.94938e-09,-2.03962e-13,-49450,-27.8753], Tmin=(1560.91,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 413,
    label = "C[C]1CC(OO)C(=O)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {2,S} {3,S} {6,S}
5  C u0 p0 c0 {1,S} {6,S} {15,D}
6  O u0 p2 c0 {4,S} {5,S}
7  O u0 p2 c0 {1,S} {8,S}
8  O u0 p2 c0 {7,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {5,D}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.965793,0.0488483,2.32925e-05,-6.66149e-08,2.92467e-11,-37894.6,31.7301], Tmin=(100,'K'), Tmax=(972.16,'K')),
            NASAPolynomial(coeffs=[16.8407,0.0268515,-9.6097e-06,1.78538e-09,-1.30448e-13,-43028.3,-54.9375], Tmin=(972.16,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 414,
    label = "CC(=O)C[CH]OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {12,D}
4  C u1 p0 c0 {1,S} {5,S} {13,S}
5  O u0 p2 c0 {4,S} {6,S}
6  O u0 p2 c0 {5,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {3,D}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.19268,0.0691217,-9.37476e-05,8.69769e-08,-3.37827e-11,-18245.1,27.0825], Tmin=(100,'K'), Tmax=(772.25,'K')),
            NASAPolynomial(coeffs=[3.54348,0.0445706,-2.20236e-05,4.30925e-09,-3.03405e-13,-18239.2,18.738], Tmin=(772.25,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 415,
    label = "O=C=C1CC(=O)CO1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {11,D}
4  C u0 p0 c0 {1,S} {5,S} {6,D}
5  O u0 p2 c0 {2,S} {4,S}
6  C u0 p0 c0 {4,D} {12,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.52201,0.0316892,5.22449e-05,-1.03807e-07,4.56503e-11,-33384,21.6925], Tmin=(100,'K'), Tmax=(933.68,'K')),
            NASAPolynomial(coeffs=[21.2285,0.00552685,6.746e-07,-1.51417e-10,8.59417e-16,-39603.5,-85.6272], Tmin=(933.68,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 416,
    label = "O=[C]C1CC(=O)CO1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {6,S}
2  O u0 p2 c0 {7,D}
3  O u0 p2 c0 {8,D}
4  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
7  C u0 p0 c0 {2,D} {5,S} {6,S}
8  C u1 p0 c0 {3,D} {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.75472,0.0326845,3.45213e-05,-7.01245e-08,2.9342e-11,-30327.2,26.6532], Tmin=(100,'K'), Tmax=(973.75,'K')),
            NASAPolynomial(coeffs=[15.2282,0.0183566,-6.59435e-06,1.28474e-09,-9.80407e-14,-34895.9,-47.9758], Tmin=(973.75,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 417,
    label = "O=C1C[CH]OC1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  C u1 p0 c0 {1,S} {5,S} {11,S}
5  O u0 p2 c0 {2,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.24437,0.026122,2.67096e-05,-5.4585e-08,2.30539e-11,-13855.7,17.8284], Tmin=(100,'K'), Tmax=(961.78,'K')),
            NASAPolynomial(coeffs=[12.185,0.0156889,-5.22617e-06,9.6718e-10,-7.19899e-14,-17197.5,-37.1742], Tmin=(961.78,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 418,
    label = "CCOC(=O)[C]1CC(=O)CO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {9,S} {12,S} {13,S}
3  C u0 p0 c0 {6,S} {8,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u1 p0 c0 {1,S} {7,S} {8,S}
6  C u0 p0 c0 {1,S} {3,S} {19,D}
7  C u0 p0 c0 {5,S} {9,S} {20,D}
8  O u0 p2 c0 {3,S} {5,S}
9  O u0 p2 c0 {2,S} {7,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 O u0 p2 c0 {6,D}
20 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.239403,0.0811032,-4.84315e-05,1.19368e-08,-6.80109e-13,-62113.1,39.442], Tmin=(100,'K'), Tmax=(1400.12,'K')),
            NASAPolynomial(coeffs=[18.6082,0.0394316,-1.68298e-05,3.09994e-09,-2.11114e-13,-68584.2,-62.0914], Tmin=(1400.12,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 419,
    label = "O=C[CH]OO",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {7,S}
3 O u0 p2 c0 {1,S} {4,S}
4 O u0 p2 c0 {3,S} {8,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.2682,0.0293993,-4.21346e-06,-1.81288e-08,9.28374e-12,-12778.5,20.8233], Tmin=(100,'K'), Tmax=(1015.96,'K')),
            NASAPolynomial(coeffs=[12.2317,0.00978322,-4.20736e-06,8.67975e-10,-6.64666e-14,-15815.1,-32.3837], Tmin=(1015.96,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 420,
    label = "CC(=O)CCC(=O)OC=C[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {3,S} {16,D}
5  C u0 p0 c0 {2,S} {8,S} {17,D}
6  C u0 p0 c0 {7,D} {8,S} {18,S}
7  C u0 p0 c0 {6,D} {19,S} {20,S}
8  O u0 p2 c0 {5,S} {6,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u0 p2 c0 {4,D}
17 O u0 p2 c0 {5,D}
18 H u0 p0 c0 {6,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.12426,0.111397,-0.000112411,5.87837e-08,-1.23632e-11,-72490.8,38.3033], Tmin=(100,'K'), Tmax=(1143.93,'K')),
            NASAPolynomial(coeffs=[19.6544,0.0387408,-1.7139e-05,3.26103e-09,-2.29107e-13,-77244.7,-64.7359], Tmin=(1143.93,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 421,
    label = "[CH2]C(=O)OO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,D}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 O u0 p2 c0 {1,S} {4,S}
4 O u0 p2 c0 {3,S} {8,S}
5 O u0 p2 c0 {1,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.15419,0.0316287,-7.95049e-06,-1.60029e-08,8.8765e-12,-19671.7,15.8795], Tmin=(100,'K'), Tmax=(1014.63,'K')),
            NASAPolynomial(coeffs=[12.999,0.00890179,-3.95903e-06,8.28242e-10,-6.39705e-14,-22903.2,-41.6781], Tmin=(1014.63,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 422,
    label = "CC(=O)C(=O)CC(=O)OC(C)[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {7,S} {11,S} {12,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {6,S} {20,D}
6  C u0 p0 c0 {4,S} {5,S} {19,D}
7  C u0 p0 c0 {1,S} {8,S} {21,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u1 p2 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {6,D}
20 O u0 p2 c0 {5,D}
21 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.335427,0.0973243,-4.84739e-05,-9.37113e-08,1.194e-10,-84570.1,39.8318], Tmin=(100,'K'), Tmax=(463.68,'K')),
            NASAPolynomial(coeffs=[6.95606,0.0664385,-3.34071e-05,6.62045e-09,-4.71538e-13,-85466.1,9.93909], Tmin=(463.68,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 423,
    label = "CC(=O)C(=O)CC(=O)OC(C)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {5,S} {7,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {6,S} {20,D}
6  C u0 p0 c0 {4,S} {5,S} {19,D}
7  C u0 p0 c0 {2,S} {8,S} {21,D}
8  O u0 p2 c0 {1,S} {7,S}
9  O u0 p2 c0 {1,S} {22,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {6,D}
20 O u0 p2 c0 {5,D}
21 O u0 p2 c0 {7,D}
22 O u1 p2 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.39845,0.12956,-0.000162514,1.21499e-07,-3.84754e-11,-84764.4,46.4634], Tmin=(100,'K'), Tmax=(757.83,'K')),
            NASAPolynomial(coeffs=[11.1458,0.0633477,-3.14569e-05,6.20614e-09,-4.41291e-13,-86665.7,-10.5768], Tmin=(757.83,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 424,
    label = "CCOC(=O)C(=O)CC(=O)C[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {8,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {4,S} {19,D}
6  C u0 p0 c0 {1,S} {7,S} {20,D}
7  C u0 p0 c0 {6,S} {8,S} {21,D}
8  O u0 p2 c0 {2,S} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u1 p2 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {5,D}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.850623,0.119893,-0.000137586,7.56899e-08,-7.24409e-12,-73949.6,41.9226], Tmin=(100,'K'), Tmax=(581.43,'K')),
            NASAPolynomial(coeffs=[10.5435,0.0597605,-2.9545e-05,5.80471e-09,-4.11256e-13,-75583.1,-9.5221], Tmin=(581.43,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 425,
    label = "CCOC(=O)C(=O)CC(=O)CO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {8,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {9,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {3,S} {19,D}
6  C u0 p0 c0 {1,S} {7,S} {20,D}
7  C u0 p0 c0 {6,S} {8,S} {21,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {3,S} {22,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {5,D}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
22 O u1 p2 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.00613,0.143627,-0.000205266,1.71317e-07,-5.9004e-11,-76338.7,46.7241], Tmin=(100,'K'), Tmax=(746.79,'K')),
            NASAPolynomial(coeffs=[12.1537,0.0623487,-3.10944e-05,6.08779e-09,-4.2859e-13,-78302.1,-16.4401], Tmin=(746.79,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 426,
    label = "[CH2]C(=O)COO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,D}
3  C u1 p0 c0 {2,S} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.11361,0.0605111,-6.39436e-05,3.35608e-08,-6.90977e-12,-15935.4,21.8883], Tmin=(100,'K'), Tmax=(1184.15,'K')),
            NASAPolynomial(coeffs=[14.5254,0.0152067,-6.55522e-06,1.25164e-09,-8.86009e-14,-19111.7,-45.0829], Tmin=(1184.15,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 427,
    label = "CC(=O)CC(=O)C(=O)OC(C)[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {11,S} {12,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {4,S} {19,D}
6  C u0 p0 c0 {1,S} {7,S} {20,D}
7  C u0 p0 c0 {6,S} {8,S} {21,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u1 p2 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {5,D}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.04742,0.122371,-0.000169786,1.49669e-07,-5.5691e-11,-82721.4,43.8104], Tmin=(100,'K'), Tmax=(739.84,'K')),
            NASAPolynomial(coeffs=[7.22471,0.0664676,-3.37776e-05,6.68768e-09,-4.74449e-13,-83639.4,8.46246], Tmin=(739.84,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 428,
    label = "CC(=O)CC(=O)C(=O)OC(C)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {5,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {4,S} {19,D}
6  C u0 p0 c0 {2,S} {7,S} {20,D}
7  C u0 p0 c0 {6,S} {8,S} {21,D}
8  O u0 p2 c0 {1,S} {7,S}
9  O u0 p2 c0 {1,S} {22,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {5,D}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
22 O u1 p2 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.23266,0.129733,-0.000151931,8.57042e-08,-9.30378e-12,-82981.8,45.2352], Tmin=(100,'K'), Tmax=(577.17,'K')),
            NASAPolynomial(coeffs=[11.0709,0.0640804,-3.22871e-05,6.39184e-09,-4.54673e-13,-84728.7,-10.1907], Tmin=(577.17,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 429,
    label = "CC(=O)C(OO)C1OC(C)OC1=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {10,S} {12,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {13,S}
3  C u0 p0 c0 {4,S} {8,S} {9,S} {14,S}
4  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {1,S} {5,S} {21,D}
7  C u0 p0 c0 {2,S} {9,S} {22,D}
8  O u0 p2 c0 {2,S} {3,S}
9  O u0 p2 c0 {3,S} {7,S}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {10,S} {23,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.0057,0.084537,3.21665e-06,-6.52469e-08,3.00217e-11,-102251,47.5995], Tmin=(100,'K'), Tmax=(1024.01,'K')),
            NASAPolynomial(coeffs=[25.1218,0.0405014,-1.72739e-05,3.42811e-09,-2.53902e-13,-110644,-93.9246], Tmin=(1024.01,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 430,
    label = "CCOC(=O)C1OCC(=O)C1[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {9,S} {13,S} {14,S}
4  C u0 p0 c0 {6,S} {8,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {2,S} {4,S} {20,D}
7  C u0 p0 c0 {1,S} {9,S} {21,D}
8  O u0 p2 c0 {1,S} {4,S}
9  O u0 p2 c0 {3,S} {7,S}
10 H u0 p0 c0 {1,S}
11 O u1 p2 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.242057,0.0696429,1.84577e-05,-7.43664e-08,3.28401e-11,-74953.5,43.6807], Tmin=(100,'K'), Tmax=(1002.03,'K')),
            NASAPolynomial(coeffs=[22.0518,0.0361473,-1.44808e-05,2.82278e-09,-2.08848e-13,-82207.5,-77.8223], Tmin=(1002.03,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 431,
    label = "CCOC(=O)[C]1OCC(=O)C1OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {10,S} {12,S}
2  C u0 p0 c0 {4,S} {9,S} {13,S} {14,S}
3  C u0 p0 c0 {6,S} {8,S} {18,S} {19,S}
4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
5  C u1 p0 c0 {1,S} {7,S} {8,S}
6  C u0 p0 c0 {1,S} {3,S} {20,D}
7  C u0 p0 c0 {5,S} {9,S} {21,D}
8  O u0 p2 c0 {3,S} {5,S}
9  O u0 p2 c0 {2,S} {7,S}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {10,S} {22,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.39023,0.101539,-6.30581e-05,9.90313e-09,2.63608e-12,-73899.4,48.4363], Tmin=(100,'K'), Tmax=(1150.02,'K')),
            NASAPolynomial(coeffs=[23.5595,0.0408341,-1.78891e-05,3.43461e-09,-2.4377e-13,-81362.2,-82.9157], Tmin=(1150.02,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 432,
    label = "CCOC(=O)C1([O])CC(=O)CO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {9,S} {13,S} {14,S}
4  C u0 p0 c0 {6,S} {8,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {2,S} {4,S} {20,D}
7  C u0 p0 c0 {1,S} {9,S} {21,D}
8  O u0 p2 c0 {1,S} {4,S}
9  O u0 p2 c0 {3,S} {7,S}
10 O u1 p2 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.0264,0.086653,-1.25168e-05,-5.61883e-08,3.01802e-11,-80106.4,40.6242], Tmin=(100,'K'), Tmax=(972.28,'K')),
            NASAPolynomial(coeffs=[26.9085,0.0283258,-9.84884e-06,1.85346e-09,-1.38456e-13,-88213.7,-107.117], Tmin=(972.28,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 433,
    label = "CCOC(=O)C1(O[O])CC(=O)CO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {9,S} {13,S} {14,S}
4  C u0 p0 c0 {6,S} {8,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {2,S} {4,S} {20,D}
7  C u0 p0 c0 {1,S} {9,S} {21,D}
8  O u0 p2 c0 {1,S} {4,S}
9  O u0 p2 c0 {3,S} {7,S}
10 O u0 p2 c0 {1,S} {22,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
22 O u1 p2 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.70024,0.103149,-4.53059e-05,-2.58615e-08,1.97498e-11,-82516.2,43.7839], Tmin=(100,'K'), Tmax=(989.51,'K')),
            NASAPolynomial(coeffs=[28.3794,0.0312443,-1.16299e-05,2.19874e-09,-1.61428e-13,-90901.6,-113.308], Tmin=(989.51,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 434,
    label = "CCOC(=O)C1OC=C(COO)O1",
    molecule = 
"""
1  C u0 p0 c0 {6,S} {8,S} {10,S} {13,S}
2  C u0 p0 c0 {4,S} {9,S} {14,S} {15,S}
3  C u0 p0 c0 {5,S} {11,S} {19,S} {20,S}
4  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {7,D} {8,S}
6  C u0 p0 c0 {1,S} {9,S} {21,D}
7  C u0 p0 c0 {5,D} {10,S} {22,S}
8  O u0 p2 c0 {1,S} {5,S}
9  O u0 p2 c0 {2,S} {6,S}
10 O u0 p2 c0 {1,S} {7,S}
11 O u0 p2 c0 {3,S} {12,S}
12 O u0 p2 c0 {11,S} {23,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 O u0 p2 c0 {6,D}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.88154,0.0986628,-6.58454e-06,-7.87097e-08,4.10754e-11,-98336.6,44.0546], Tmin=(100,'K'), Tmax=(966.71,'K')),
            NASAPolynomial(coeffs=[33.4573,0.0262229,-8.66841e-06,1.67893e-09,-1.31223e-13,-108617,-143.071], Tmin=(966.71,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 435,
    label = "CCOC(=O)C1(OO)OC=C(C)O1",
    molecule = 
"""
1  C u0 p0 c0 {6,S} {8,S} {9,S} {11,S}
2  C u0 p0 c0 {3,S} {10,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {7,D} {8,S}
6  C u0 p0 c0 {1,S} {10,S} {21,D}
7  C u0 p0 c0 {5,D} {9,S} {22,S}
8  O u0 p2 c0 {1,S} {5,S}
9  O u0 p2 c0 {1,S} {7,S}
10 O u0 p2 c0 {2,S} {6,S}
11 O u0 p2 c0 {1,S} {12,S}
12 O u0 p2 c0 {11,S} {23,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {6,D}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.89607,0.101214,-1.71917e-05,-6.66844e-08,3.69398e-11,-101614,42.2085], Tmin=(100,'K'), Tmax=(961.36,'K')),
            NASAPolynomial(coeffs=[32.4014,0.0271173,-8.62465e-06,1.60642e-09,-1.22786e-13,-111379,-138.394], Tmin=(961.36,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 436,
    label = "CC1=COC(C(=O)OC(C)OO)O1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {9,S} {11,S} {13,S}
2  C u0 p0 c0 {6,S} {8,S} {10,S} {14,S}
3  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {7,D} {8,S}
6  C u0 p0 c0 {2,S} {9,S} {21,D}
7  C u0 p0 c0 {5,D} {10,S} {22,S}
8  O u0 p2 c0 {2,S} {5,S}
9  O u0 p2 c0 {1,S} {6,S}
10 O u0 p2 c0 {2,S} {7,S}
11 O u0 p2 c0 {1,S} {12,S}
12 O u0 p2 c0 {11,S} {23,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {6,D}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.96437,0.09853,-1.17141e-06,-8.70783e-08,4.44663e-11,-103996,43.7565], Tmin=(100,'K'), Tmax=(967.76,'K')),
            NASAPolynomial(coeffs=[35.0068,0.0243409,-8.04205e-06,1.60204e-09,-1.28349e-13,-114834,-152.418], Tmin=(967.76,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 437,
    label = "CC([O])OC(=O)C1CC(=O)CO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {9,S} {13,S} {14,S}
4  C u0 p0 c0 {6,S} {8,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {2,S} {4,S} {20,D}
7  C u0 p0 c0 {1,S} {9,S} {21,D}
8  O u0 p2 c0 {1,S} {4,S}
9  O u0 p2 c0 {3,S} {7,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u1 p2 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.372014,0.0817354,-3.46129e-05,-5.28415e-09,5.14395e-12,-80776.3,43.2896], Tmin=(100,'K'), Tmax=(1211.17,'K')),
            NASAPolynomial(coeffs=[18.3062,0.0450961,-2.02567e-05,3.88855e-09,-2.73867e-13,-87138,-57.9847], Tmin=(1211.17,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 438,
    label = "[CH2]C1OO1",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 O u0 p2 c0 {1,S} {4,S}
4 O u0 p2 c0 {1,S} {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.01098,0.00838814,4.73229e-05,-7.76432e-08,3.38958e-11,18254,14.0737], Tmin=(100,'K'), Tmax=(894.89,'K')),
            NASAPolynomial(coeffs=[13.0759,-0.00110213,3.72977e-06,-8.4194e-10,5.73871e-14,15031.2,-41.3075], Tmin=(894.89,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 439,
    label = "O=CCO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {7,S}
3 O u0 p2 c0 {1,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.75092,0.0145254,3.55414e-05,-6.12342e-08,2.54828e-11,-39934.3,13.5048], Tmin=(100,'K'), Tmax=(953.77,'K')),
            NASAPolynomial(coeffs=[12.7142,0.00531895,-1.21597e-06,2.71917e-10,-2.64254e-14,-43316.6,-41.859], Tmin=(953.77,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 440,
    label = "[CH2]C1CO1",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3 C u1 p0 c0 {1,S} {8,S} {9,S}
4 O u0 p2 c0 {1,S} {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.82507,0.0153706,3.12913e-05,-5.25732e-08,2.14877e-11,11358.7,13.545], Tmin=(100,'K'), Tmax=(953.4,'K')),
            NASAPolynomial(coeffs=[10.0993,0.0111447,-3.42695e-06,6.29437e-10,-4.78486e-14,8776.7,-27.4688], Tmin=(953.4,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 441,
    label = "C=CCO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  O u0 p2 c0 {1,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.29532,0.0323535,-1.53572e-05,-7.98947e-10,1.9865e-12,8683.79,18.5043], Tmin=(100,'K'), Tmax=(1108.68,'K')),
            NASAPolynomial(coeffs=[8.87094,0.0173881,-6.95984e-06,1.2773e-09,-8.84653e-14,6687.43,-16.3253], Tmin=(1108.68,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 442,
    label = "CC(C=O)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,D} {10,S}
4  O u0 p2 c0 {1,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
11 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.73324,0.0479594,-4.24008e-05,1.9641e-08,-3.70049e-12,-16742.8,21.2499], Tmin=(100,'K'), Tmax=(1260.32,'K')),
            NASAPolynomial(coeffs=[10.8047,0.0191684,-8.13438e-06,1.51518e-09,-1.04984e-13,-19029.4,-24.6133], Tmin=(1260.32,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 443,
    label = "[O]OCCC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,D} {10,S}
4  O u0 p2 c0 {2,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
11 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.42135,0.0630319,-9.78957e-05,8.65486e-08,-3.01124e-11,-16354.3,21.212], Tmin=(100,'K'), Tmax=(843.07,'K')),
            NASAPolynomial(coeffs=[6.44938,0.0271945,-1.28159e-05,2.41386e-09,-1.6471e-13,-16776.2,0.338217], Tmin=(843.07,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 444,
    label = "[O]OCC(=O)CCC(=O)O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {14,D}
5  C u0 p0 c0 {2,S} {7,S} {15,D}
6  O u0 p2 c0 {3,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 O u0 p2 c0 {5,D}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.452967,0.108693,-0.000166915,1.48764e-07,-5.30212e-11,-66264.8,36.0357], Tmin=(100,'K'), Tmax=(810.64,'K')),
            NASAPolynomial(coeffs=[8.02545,0.0492461,-2.43259e-05,4.69843e-09,-3.2633e-13,-67060.8,0.48129], Tmin=(810.64,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 445,
    label = "CC(=O)CCC(=O)CC=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {5,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {3,S} {18,D}
6  C u0 p0 c0 {1,S} {4,S} {17,D}
7  C u0 p0 c0 {3,S} {19,D} {20,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u0 p2 c0 {6,D}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {7,D}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.432381,0.107681,-0.000150278,1.32779e-07,-4.83254e-11,-61741.5,37.0389], Tmin=(100,'K'), Tmax=(793.07,'K')),
            NASAPolynomial(coeffs=[6.18352,0.058738,-2.82528e-05,5.44069e-09,-3.78899e-13,-62301.1,9.74266], Tmin=(793.07,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 446,
    label = "C=COC(=O)CCC(=C)[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,D} {13,S}
4  C u0 p0 c0 {2,S} {8,S} {14,D}
5  C u0 p0 c0 {7,D} {8,S} {15,S}
6  C u0 p0 c0 {3,D} {16,S} {17,S}
7  C u0 p0 c0 {5,D} {18,S} {19,S}
8  O u0 p2 c0 {4,S} {5,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 O u1 p2 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.84626,0.10094,-9.76218e-05,4.86362e-08,-9.66564e-12,-44564.2,36.6861], Tmin=(100,'K'), Tmax=(1215.27,'K')),
            NASAPolynomial(coeffs=[19.8617,0.0327804,-1.34932e-05,2.48523e-09,-1.7165e-13,-49597.3,-67.255], Tmin=(1215.27,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 447,
    label = "CCOC(=O)C1OC=C(C)O1",
    molecule = 
"""
1  C u0 p0 c0 {6,S} {8,S} {10,S} {11,S}
2  C u0 p0 c0 {3,S} {9,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {7,D} {8,S}
6  C u0 p0 c0 {1,S} {9,S} {20,D}
7  C u0 p0 c0 {5,D} {10,S} {21,S}
8  O u0 p2 c0 {1,S} {5,S}
9  O u0 p2 c0 {2,S} {6,S}
10 O u0 p2 c0 {1,S} {7,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {6,D}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.579839,0.0662814,5.83881e-05,-1.39093e-07,6.19454e-11,-88561.8,34.8655], Tmin=(100,'K'), Tmax=(949.66,'K')),
            NASAPolynomial(coeffs=[30.8288,0.0201844,-4.95064e-06,9.48671e-10,-8.19262e-14,-98414.2,-135.505], Tmin=(949.66,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 448,
    label = "CCOC(=O)CC(=O)C(=O)C[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {7,S} {11,S} {12,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {6,S} {19,D}
6  C u0 p0 c0 {4,S} {5,S} {20,D}
7  C u0 p0 c0 {1,S} {8,S} {21,D}
8  O u0 p2 c0 {2,S} {7,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u1 p2 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {5,D}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.995437,0.11937,-0.000146251,1.07358e-07,-3.34211e-11,-75733.1,43.0808], Tmin=(100,'K'), Tmax=(770.14,'K')),
            NASAPolynomial(coeffs=[10.6263,0.0590147,-2.87075e-05,5.61731e-09,-3.97736e-13,-77523.4,-9.95289], Tmin=(770.14,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 449,
    label = "CCOC(=O)C(O[O])C(=O)C(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {7,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {8,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {6,S} {19,D}
6  C u0 p0 c0 {4,S} {5,S} {20,D}
7  C u0 p0 c0 {1,S} {8,S} {21,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {1,S} {22,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {5,D}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
22 O u1 p2 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.18234,0.124326,-0.000146061,1.02558e-07,-3.07862e-11,-82597.8,45.7321], Tmin=(100,'K'), Tmax=(794.24,'K')),
            NASAPolynomial(coeffs=[10.8927,0.063511,-3.1201e-05,6.14415e-09,-4.37176e-13,-84515.8,-9.74107], Tmin=(794.24,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 450,
    label = "CCOC(=O)C(=O)C([O])C(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {8,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {4,S} {19,D}
6  C u0 p0 c0 {1,S} {7,S} {20,D}
7  C u0 p0 c0 {6,S} {8,S} {21,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u1 p2 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {5,D}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.739157,0.114008,-0.000132152,9.3148e-08,-2.83382e-11,-78388.3,42.6946], Tmin=(100,'K'), Tmax=(781.27,'K')),
            NASAPolynomial(coeffs=[9.66377,0.0607489,-2.99005e-05,5.8988e-09,-4.20259e-13,-80013.9,-4.92615], Tmin=(781.27,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 451,
    label = "CCOC(=O)C(=O)C(O[O])C(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {8,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {4,S} {19,D}
6  C u0 p0 c0 {1,S} {7,S} {20,D}
7  C u0 p0 c0 {6,S} {8,S} {21,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {1,S} {22,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {5,D}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
22 O u1 p2 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.47545,0.13138,-0.000168767,1.29803e-07,-4.22262e-11,-80795.5,46.0699], Tmin=(100,'K'), Tmax=(739.26,'K')),
            NASAPolynomial(coeffs=[10.9967,0.0638869,-3.18019e-05,6.27141e-09,-4.45433e-13,-82639.3,-10.3315], Tmin=(739.26,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 452,
    label = "C=C([O])C(OO)C(=O)C(=O)OCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {9,S} {11,S}
2  C u0 p0 c0 {3,S} {8,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {6,S} {18,D}
5  C u0 p0 c0 {1,S} {7,D} {17,S}
6  C u0 p0 c0 {4,S} {8,S} {19,D}
7  C u0 p0 c0 {5,D} {20,S} {21,S}
8  O u0 p2 c0 {2,S} {6,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 O u1 p2 c0 {5,S}
18 O u0 p2 c0 {4,D}
19 O u0 p2 c0 {6,D}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.67174,0.131482,-0.000143022,8.24756e-08,-1.94813e-11,-79486.4,46.6994], Tmin=(100,'K'), Tmax=(1012.75,'K')),
            NASAPolynomial(coeffs=[18.4464,0.0520241,-2.53372e-05,5.00778e-09,-3.58417e-13,-83561.4,-50.6142], Tmin=(1012.75,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 453,
    label = "CC(=O)CCC(=O)OC(=O)CO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {7,S} {9,S} {14,S} {15,S}
4  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {4,S} {19,D}
6  C u0 p0 c0 {2,S} {8,S} {21,D}
7  C u0 p0 c0 {3,S} {8,S} {20,D}
8  O u0 p2 c0 {6,S} {7,S}
9  O u0 p2 c0 {3,S} {22,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {5,D}
20 O u0 p2 c0 {7,D}
21 O u0 p2 c0 {6,D}
22 O u1 p2 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.95867,0.146761,-0.000234337,2.11714e-07,-7.52934e-11,-84597.1,49.822], Tmin=(100,'K'), Tmax=(827.82,'K')),
            NASAPolynomial(coeffs=[9.22944,0.0637386,-3.14223e-05,6.03855e-09,-4.17011e-13,-85457.1,3.95379], Tmin=(827.82,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 454,
    label = "[CH2]C(=O)OC(=O)COO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,D}
3  C u0 p0 c0 {4,S} {5,S} {11,D}
4  C u1 p0 c0 {3,S} {12,S} {13,S}
5  O u0 p2 c0 {2,S} {3,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 O u0 p2 c0 {2,D}
11 O u0 p2 c0 {3,D}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.33806,0.0869597,-0.000117559,8.72735e-08,-2.63932e-11,-55029.2,34.9667], Tmin=(100,'K'), Tmax=(803.33,'K')),
            NASAPolynomial(coeffs=[11.2325,0.0327096,-1.62547e-05,3.19752e-09,-2.2662e-13,-56779.4,-15.206], Tmin=(803.33,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 455,
    label = "CC(=O)CCC(=O)OC(C=O)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {7,S} {8,S} {9,S} {14,S}
4  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {4,S} {18,D}
6  C u0 p0 c0 {2,S} {8,S} {19,D}
7  C u0 p0 c0 {3,S} {20,D} {21,S}
8  O u0 p2 c0 {3,S} {6,S}
9  O u0 p2 c0 {3,S} {22,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {6,D}
20 O u0 p2 c0 {7,D}
21 H u0 p0 c0 {7,S}
22 O u1 p2 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.5368,0.134772,-0.000197043,1.7569e-07,-6.41378e-11,-84976.1,48.4972], Tmin=(100,'K'), Tmax=(781.59,'K')),
            NASAPolynomial(coeffs=[7.88936,0.0681913,-3.40652e-05,6.6538e-09,-4.66794e-13,-85889.5,8.92787], Tmin=(781.59,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 456,
    label = "C=C(C)OCC(=O)O",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {5,D} {6,S}
4  C u0 p0 c0 {1,S} {7,S} {13,D}
5  C u0 p0 c0 {3,D} {14,S} {15,S}
6  O u0 p2 c0 {1,S} {3,S}
7  O u0 p2 c0 {4,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.207105,0.0707732,-4.08936e-05,-1.7006e-09,6.511e-12,-67153.6,27.8206], Tmin=(100,'K'), Tmax=(1028.29,'K')),
            NASAPolynomial(coeffs=[18.6609,0.0241563,-9.60423e-06,1.8151e-09,-1.30361e-13,-72279.4,-68.1927], Tmin=(1028.29,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 457,
    label = "C=C(O)CCC(=O)O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,D} {6,S}
4  C u0 p0 c0 {2,S} {7,S} {12,D}
5  C u0 p0 c0 {3,D} {13,S} {14,S}
6  O u0 p2 c0 {3,S} {15,S}
7  O u0 p2 c0 {4,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.0887203,0.0774371,-6.84855e-05,3.0893e-08,-5.54251e-12,-72417.9,29.7644], Tmin=(100,'K'), Tmax=(1343.07,'K')),
            NASAPolynomial(coeffs=[17.7341,0.0248847,-9.79253e-06,1.75924e-09,-1.19537e-13,-77157.7,-60.569], Tmin=(1343.07,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 458,
    label = "CCOC=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,D} {11,S}
4  O u0 p2 c0 {1,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.70616,0.0287774,-6.64036e-06,-3.1591e-09,1.17558e-12,-48720.7,15.8493], Tmin=(100,'K'), Tmax=(1646.39,'K')),
            NASAPolynomial(coeffs=[8.73322,0.0236138,-1.05725e-05,1.93033e-09,-1.28283e-13,-51990,-20.1345], Tmin=(1646.39,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 459,
    label = "O=C[CH]O",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 C u0 p0 c0 {1,S} {5,D} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.73077,0.0175103,1.90204e-05,-4.158e-08,1.80498e-11,-23280.5,13.329], Tmin=(100,'K'), Tmax=(963.67,'K')),
            NASAPolynomial(coeffs=[12.0193,0.00477211,-1.33666e-06,3.02999e-10,-2.7719e-14,-26269.4,-37.3585], Tmin=(963.67,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 460,
    label = "CCOC(=O)CO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {5,S} {14,D}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {3,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.19723,0.0662947,-5.71961e-05,2.82341e-08,-6.11273e-12,-46235.6,27.3967], Tmin=(100,'K'), Tmax=(1054.18,'K')),
            NASAPolynomial(coeffs=[8.44039,0.038811,-1.80894e-05,3.50291e-09,-2.47679e-13,-47762.7,-7.92955], Tmin=(1054.18,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 461,
    label = "CCOC(=O)C([O])CC(=O)C=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {7,S} {18,D}
6  C u0 p0 c0 {2,S} {8,S} {19,D}
7  C u0 p0 c0 {5,S} {20,D} {21,S}
8  O u0 p2 c0 {3,S} {6,S}
9  O u1 p2 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {6,D}
20 O u0 p2 c0 {7,D}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.488648,0.107993,-0.00011071,6.69153e-08,-1.75993e-11,-75572.6,43.6173], Tmin=(100,'K'), Tmax=(889.81,'K')),
            NASAPolynomial(coeffs=[10.2872,0.0595517,-2.90496e-05,5.73298e-09,-4.09491e-13,-77490.3,-7.11187], Tmin=(889.81,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 462,
    label = "CCOC(=O)C([C]=O)C(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {7,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {4,S} {18,D}
6  C u0 p0 c0 {1,S} {7,S} {19,D}
7  O u0 p2 c0 {2,S} {6,S}
8  C u1 p0 c0 {1,S} {20,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {6,D}
20 O u0 p2 c0 {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.224059,0.0839807,-5.84566e-05,2.04347e-08,-2.97756e-12,-69399.5,40.1236], Tmin=(100,'K'), Tmax=(1527.9,'K')),
            NASAPolynomial(coeffs=[14.9923,0.0453177,-2.04994e-05,3.87283e-09,-2.6764e-13,-73912.4,-37.385], Tmin=(1527.9,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 463,
    label = "CCOC(=O)[CH]C(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {5,S} {16,D}
5  C u1 p0 c0 {4,S} {6,S} {17,S}
6  C u0 p0 c0 {5,S} {7,S} {18,D}
7  O u0 p2 c0 {1,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u0 p2 c0 {4,D}
17 H u0 p0 c0 {5,S}
18 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.760364,0.0750104,-5.37038e-05,1.98789e-08,-3.13929e-12,-52731.8,31.3782], Tmin=(100,'K'), Tmax=(1395.75,'K')),
            NASAPolynomial(coeffs=[11.6527,0.0437945,-2.01561e-05,3.85501e-09,-2.69145e-13,-55772.4,-24.8027], Tmin=(1395.75,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 464,
    label = "CCOC(=O)C(CC([O])=CO)OO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {9,S} {12,S}
2  O u0 p2 c0 {4,S} {7,S}
3  O u0 p2 c0 {13,S} {23,S}
4  O u0 p2 c0 {2,S} {24,S}
5  O u1 p2 c0 {11,S}
6  O u0 p2 c0 {12,D}
7  C u0 p0 c0 {2,S} {8,S} {12,S} {14,S}
8  C u0 p0 c0 {7,S} {11,S} {15,S} {16,S}
9  C u0 p0 c0 {1,S} {10,S} {17,S} {18,S}
10 C u0 p0 c0 {9,S} {19,S} {20,S} {21,S}
11 C u0 p0 c0 {5,S} {8,S} {13,D}
12 C u0 p0 c0 {1,S} {6,D} {7,S}
13 C u0 p0 c0 {3,S} {11,D} {22,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {13,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.09661,0.139142,-0.00012776,5.11379e-08,-5.75672e-12,-95058.2,52.5961], Tmin=(100,'K'), Tmax=(1031.94,'K')),
            NASAPolynomial(coeffs=[31.6345,0.0320157,-1.20158e-05,2.18674e-09,-1.53707e-13,-103690,-123.148], Tmin=(1031.94,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 465,
    label = "CCOC(=O)C(OO)C(OO)C(=O)CO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {9,S} {14,S}
2  C u0 p0 c0 {1,S} {7,S} {10,S} {15,S}
3  C u0 p0 c0 {5,S} {8,S} {16,S} {17,S}
4  C u0 p0 c0 {6,S} {11,S} {21,S} {22,S}
5  C u0 p0 c0 {3,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {1,S} {4,S} {23,D}
7  C u0 p0 c0 {2,S} {8,S} {24,D}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {1,S} {12,S}
10 O u0 p2 c0 {2,S} {13,S}
11 O u0 p2 c0 {4,S} {25,S}
12 O u0 p2 c0 {9,S} {26,S}
13 O u0 p2 c0 {10,S} {27,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 O u0 p2 c0 {6,D}
24 O u0 p2 c0 {7,D}
25 O u1 p2 c0 {11,S}
26 H u0 p0 c0 {12,S}
27 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.21507,0.167535,-0.000184289,1.0672e-07,-2.52572e-11,-92219,61.6023], Tmin=(100,'K'), Tmax=(1011.73,'K')),
            NASAPolynomial(coeffs=[22.771,0.0647958,-3.19674e-05,6.35022e-09,-4.557e-13,-97477.2,-64.0687], Tmin=(1011.73,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 466,
    label = "CC(=O)C(OO)C(O[O])C(=O)OC(C)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {9,S} {14,S}
2  C u0 p0 c0 {1,S} {7,S} {11,S} {15,S}
3  C u0 p0 c0 {4,S} {8,S} {10,S} {16,S}
4  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {6,S} {20,S} {21,S} {22,S}
6  C u0 p0 c0 {1,S} {5,S} {23,D}
7  C u0 p0 c0 {2,S} {8,S} {24,D}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {1,S} {13,S}
10 O u0 p2 c0 {3,S} {12,S}
11 O u0 p2 c0 {2,S} {25,S}
12 O u0 p2 c0 {10,S} {26,S}
13 O u0 p2 c0 {9,S} {27,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 O u0 p2 c0 {6,D}
24 O u0 p2 c0 {7,D}
25 O u1 p2 c0 {11,S}
26 H u0 p0 c0 {12,S}
27 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.97702,0.161702,-0.000169735,9.33034e-08,-2.1043e-11,-98839.3,61.9361], Tmin=(100,'K'), Tmax=(1055.44,'K')),
            NASAPolynomial(coeffs=[22.5658,0.0649002,-3.2162e-05,6.40766e-09,-4.60632e-13,-104231,-62.6718], Tmin=(1055.44,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 467,
    label = "CC(OO)OC(=O)C(CC(=O)CO[O])OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {9,S} {14,S}
2  C u0 p0 c0 {1,S} {6,S} {15,S} {16,S}
3  C u0 p0 c0 {5,S} {8,S} {10,S} {17,S}
4  C u0 p0 c0 {6,S} {11,S} {21,S} {22,S}
5  C u0 p0 c0 {3,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {2,S} {4,S} {23,D}
7  C u0 p0 c0 {1,S} {8,S} {24,D}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {1,S} {12,S}
10 O u0 p2 c0 {3,S} {13,S}
11 O u0 p2 c0 {4,S} {25,S}
12 O u0 p2 c0 {9,S} {26,S}
13 O u0 p2 c0 {10,S} {27,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 O u0 p2 c0 {6,D}
24 O u0 p2 c0 {7,D}
25 O u1 p2 c0 {11,S}
26 H u0 p0 c0 {12,S}
27 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.55974,0.180744,-0.000234573,1.68624e-07,-4.99133e-11,-95862.4,61.1978], Tmin=(100,'K'), Tmax=(816.19,'K')),
            NASAPolynomial(coeffs=[18.353,0.0733504,-3.7197e-05,7.40066e-09,-5.2878e-13,-99439.2,-40.0671], Tmin=(816.19,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 468,
    label = "[CH2]C1C(=O)OC1C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {7,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {6,S} {12,D}
5  C u1 p0 c0 {2,S} {13,S} {14,S}
6  O u0 p2 c0 {1,S} {4,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.72264,0.0354873,3.26987e-05,-7.15076e-08,3.17783e-11,-18176,22.6508], Tmin=(100,'K'), Tmax=(919.08,'K')),
            NASAPolynomial(coeffs=[13.7178,0.0210475,-5.37056e-06,8.15294e-10,-5.57859e-14,-21975.9,-42.884], Tmin=(919.08,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 469,
    label = "O=C1CO1",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {6,D}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44431,0.00399082,3.44359e-05,-4.79572e-08,1.86603e-11,-22065.1,9.78945], Tmin=(100,'K'), Tmax=(953.57,'K')),
            NASAPolynomial(coeffs=[7.91507,0.0061303,-1.79536e-06,3.50344e-10,-2.85978e-14,-23867.7,-16.5476], Tmin=(953.57,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 470,
    label = "O=C1COC1",
    molecule = 
"""
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {2,S} {9,D}
4 O u0 p2 c0 {1,S} {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.9751,0.00701285,6.3625e-05,-8.78527e-08,3.37582e-11,-20939.1,12.8077], Tmin=(100,'K'), Tmax=(966.6,'K')),
            NASAPolynomial(coeffs=[11.49,0.0111325,-3.84163e-06,8.01734e-10,-6.57028e-14,-24423.8,-37.4926], Tmin=(966.6,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 471,
    label = "C=COC(C)=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,D}
3  C u0 p0 c0 {4,D} {5,S} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {2,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {2,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.04147,0.0348669,-1.68892e-06,-1.72047e-08,7.20201e-12,-40080,17.6371], Tmin=(100,'K'), Tmax=(1130.49,'K')),
            NASAPolynomial(coeffs=[10.1701,0.0239184,-1.07974e-05,2.10507e-09,-1.50572e-13,-43056.1,-27.6104], Tmin=(1130.49,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 472,
    label = "CC(=O)OC=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,D}
3  C u0 p0 c0 {4,S} {9,D} {10,S}
4  O u0 p2 c0 {2,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.44436,0.0335282,-2.10383e-05,6.27838e-09,-7.56044e-13,-64958,21.0243], Tmin=(100,'K'), Tmax=(1848.63,'K')),
            NASAPolynomial(coeffs=[10.1937,0.0167604,-7.4327e-06,1.37182e-09,-9.25039e-14,-67823.1,-21.1233], Tmin=(1848.63,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 473,
    label = "CCOC(=O)C(CC(=O)C(O)O[O])OO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {12,S} {15,S}
2  O u0 p2 c0 {5,S} {9,S}
3  O u0 p2 c0 {8,S} {11,S}
4  O u0 p2 c0 {11,S} {25,S}
5  O u0 p2 c0 {2,S} {26,S}
6  O u0 p2 c0 {14,D}
7  O u0 p2 c0 {15,D}
8  O u1 p2 c0 {3,S}
9  C u0 p0 c0 {2,S} {10,S} {15,S} {16,S}
10 C u0 p0 c0 {9,S} {14,S} {17,S} {18,S}
11 C u0 p0 c0 {3,S} {4,S} {14,S} {21,S}
12 C u0 p0 c0 {1,S} {13,S} {19,S} {20,S}
13 C u0 p0 c0 {12,S} {22,S} {23,S} {24,S}
14 C u0 p0 c0 {6,D} {10,S} {11,S}
15 C u0 p0 c0 {1,S} {7,D} {9,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {12,S}
20 H u0 p0 c0 {12,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {13,S}
23 H u0 p0 c0 {13,S}
24 H u0 p0 c0 {13,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.94904,0.165953,-0.000217638,1.62478e-07,-5.02357e-11,-106218,58.9345], Tmin=(100,'K'), Tmax=(781.74,'K')),
            NASAPolynomial(coeffs=[15.6198,0.0709303,-3.52876e-05,6.95375e-09,-4.9365e-13,-109121,-26.0752], Tmin=(781.74,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 474,
    label = "O=CC(=O)O",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {7,S}
2 O u0 p2 c0 {4,D}
3 O u0 p2 c0 {5,D}
4 C u0 p0 c0 {1,S} {2,D} {5,S}
5 C u0 p0 c0 {3,D} {4,S} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.79803,0.025593,-1.64983e-05,4.66667e-09,-5.12198e-13,-57904.5,13.8298], Tmin=(100,'K'), Tmax=(2089.56,'K')),
            NASAPolynomial(coeffs=[11.4245,0.00907941,-4.64397e-06,8.84586e-10,-5.97001e-14,-61509.6,-34.1455], Tmin=(2089.56,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 475,
    label = "C=C(C)OC=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u0 p0 c0 {2,D} {9,S} {10,S}
4  C u0 p0 c0 {5,S} {11,D} {12,S}
5  O u0 p2 c0 {2,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.50754,0.0473374,-3.27001e-05,1.08473e-08,-1.4279e-12,-40314.4,20.103], Tmin=(100,'K'), Tmax=(1776.85,'K')),
            NASAPolynomial(coeffs=[14.8538,0.0172928,-7.33677e-06,1.33108e-09,-8.89914e-14,-45057.2,-51.9569], Tmin=(1776.85,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 476,
    label = "[O]OC(=O)O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p2 c0 {5,S} {6,S}
3 O u0 p2 c0 {5,D}
4 O u1 p2 c0 {1,S}
5 C u0 p0 c0 {1,S} {2,S} {3,D}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.78581,0.0412568,-5.57497e-05,3.29377e-08,-7.00882e-12,-42560.3,16.2277], Tmin=(100,'K'), Tmax=(1359.92,'K')),
            NASAPolynomial(coeffs=[13.9628,-0.00336328,3.17666e-06,-7.09633e-10,5.1772e-14,-45058.2,-43.2695], Tmin=(1359.92,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 477,
    label = "[O]OC(O)C=O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {7,S}
3 O u0 p2 c0 {1,S} {8,S}
4 O u0 p2 c0 {1,S} {9,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {2,S}
8 O u1 p2 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.03935,0.0466238,-6.20536e-05,4.7508e-08,-1.50353e-11,-37734.4,22.453], Tmin=(100,'K'), Tmax=(765.23,'K')),
            NASAPolynomial(coeffs=[7.15217,0.0199018,-9.68039e-06,1.88688e-09,-1.32983e-13,-38517,-0.846024], Tmin=(765.23,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 478,
    label = "C=COC(=O)C=C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,D} {7,S}
2  C u0 p0 c0 {1,S} {6,S} {8,D}
3  C u0 p0 c0 {5,D} {6,S} {9,S}
4  C u0 p0 c0 {1,D} {12,S} {13,S}
5  C u0 p0 c0 {3,D} {10,S} {11,S}
6  O u0 p2 c0 {2,S} {3,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.69912,0.0490309,-4.50522e-05,2.11233e-08,-3.97331e-12,-23256.7,20.498], Tmin=(100,'K'), Tmax=(1269.92,'K')),
            NASAPolynomial(coeffs=[11.7611,0.0173372,-7.61582e-06,1.47012e-09,-1.04281e-13,-25812.2,-30.4494], Tmin=(1269.92,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 479,
    label = "[CH2]C(O)C(=O)OCC",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,S} {7,S}
2  O u0 p2 c0 {4,S} {17,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
6  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
7  C u0 p0 c0 {1,S} {3,D} {4,S}
8  C u1 p0 c0 {4,S} {15,S} {16,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.207591,0.0726642,-4.99958e-05,1.05215e-08,1.7174e-12,-53742.5,35.3259], Tmin=(100,'K'), Tmax=(1058.14,'K')),
            NASAPolynomial(coeffs=[17.419,0.026057,-1.00885e-05,1.86151e-09,-1.30879e-13,-58418.1,-53.564], Tmin=(1058.14,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 480,
    label = "C=COC(=O)CC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,D}
4  C u0 p0 c0 {5,D} {6,S} {13,S}
5  C u0 p0 c0 {4,D} {14,S} {15,S}
6  O u0 p2 c0 {3,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {3,D}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.39676,0.0457847,-1.72684e-06,-2.71895e-08,1.24809e-11,-44162.9,25.0623], Tmin=(100,'K'), Tmax=(1041.1,'K')),
            NASAPolynomial(coeffs=[12.848,0.0270424,-1.11094e-05,2.11855e-09,-1.51912e-13,-47915.9,-37.2175], Tmin=(1041.1,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 481,
    label = "[CH2]C(O)C(=O)O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,D}
3  C u1 p0 c0 {1,S} {8,S} {9,S}
4  O u0 p2 c0 {1,S} {10,S}
5  O u0 p2 c0 {2,S} {11,S}
6  H u0 p0 c0 {1,S}
7  O u0 p2 c0 {2,D}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.53682,0.0484116,-4.30783e-05,1.96374e-08,-3.54623e-12,-51455,23.5742], Tmin=(100,'K'), Tmax=(1339.62,'K')),
            NASAPolynomial(coeffs=[12.7405,0.0149584,-5.61991e-06,9.96086e-10,-6.73719e-14,-54456.7,-33.7527], Tmin=(1339.62,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 482,
    label = "[O]C(=O)O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,D}
2 O u0 p2 c0 {1,S} {5,S}
3 O u1 p2 c0 {1,S}
4 O u0 p2 c0 {1,D}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.28603,0.00907563,1.53519e-05,-2.86388e-08,1.19721e-11,-45835.1,11.0209], Tmin=(100,'K'), Tmax=(968.18,'K')),
            NASAPolynomial(coeffs=[8.68687,0.0032255,-1.09079e-06,2.46308e-10,-2.1583e-14,-47652.5,-18.8452], Tmin=(968.18,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 483,
    label = "[O]OCCC(=O)O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,D}
4  O u0 p2 c0 {2,S} {11,S}
5  O u0 p2 c0 {3,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 O u1 p2 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.29168,0.0659477,-9.56055e-05,8.47436e-08,-3.0503e-11,-48658.3,24.6436], Tmin=(100,'K'), Tmax=(805.8,'K')),
            NASAPolynomial(coeffs=[5.68671,0.033739,-1.63045e-05,3.13079e-09,-2.17207e-13,-49029.2,6.48251], Tmin=(805.8,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 484,
    label = "CC(=O)OCO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {11,D}
4  O u0 p2 c0 {1,S} {3,S}
5  O u0 p2 c0 {1,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.32842,0.0439417,3.30712e-06,-4.47414e-08,2.26772e-11,-47324.1,25.0271], Tmin=(100,'K'), Tmax=(948.11,'K')),
            NASAPolynomial(coeffs=[17.8282,0.0110962,-2.89449e-06,5.18784e-10,-4.14872e-14,-52105.2,-62.4101], Tmin=(948.11,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 485,
    label = "CCC(=O)CC=O",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {2,S} {13,D}
5  C u0 p0 c0 {2,S} {14,D} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 O u0 p2 c0 {5,D}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.36467,0.0629463,-6.37173e-05,4.40914e-08,-1.39998e-11,-42382.9,24.737], Tmin=(100,'K'), Tmax=(734.8,'K')),
            NASAPolynomial(coeffs=[5.36895,0.0411475,-1.92159e-05,3.71473e-09,-2.61946e-13,-42971.3,6.65277], Tmin=(734.8,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 486,
    label = "CCOC(=O)C(C=C=O)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {7,S} {9,S}
2  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {6,S} {15,D}
5  C u0 p0 c0 {1,S} {8,D} {16,S}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {1,S} {17,S}
8  C u0 p0 c0 {5,D} {18,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {4,D}
16 H u0 p0 c0 {5,S}
17 O u1 p2 c0 {7,S}
18 O u0 p2 c0 {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.914141,0.11799,-0.00017582,1.50165e-07,-5.15263e-11,-51021.8,38.9829], Tmin=(100,'K'), Tmax=(812.43,'K')),
            NASAPolynomial(coeffs=[10.2546,0.0492848,-2.36434e-05,4.51159e-09,-3.1142e-13,-52383.9,-9.79393], Tmin=(812.43,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 487,
    label = "CC(=O)OC(C)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {5,S} {14,D}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {1,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.44419,0.0605183,-4.34074e-05,1.63169e-08,-2.65609e-12,-52856.9,27.6852], Tmin=(100,'K'), Tmax=(1340.55,'K')),
            NASAPolynomial(coeffs=[9.26915,0.0371697,-1.72814e-05,3.32416e-09,-2.33055e-13,-54954.9,-12.359], Tmin=(1340.55,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 488,
    label = "C=C(CCC(C)=O)OC=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {6,D} {8,S}
5  C u0 p0 c0 {1,S} {3,S} {16,D}
6  C u0 p0 c0 {4,D} {17,S} {18,S}
7  C u0 p0 c0 {8,S} {19,D} {20,S}
8  O u0 p2 c0 {4,S} {7,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u0 p2 c0 {5,D}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 O u0 p2 c0 {7,D}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.105463,0.0916234,-7.82469e-05,3.64349e-08,-7.28496e-12,-62416.8,33.8992], Tmin=(100,'K'), Tmax=(1142.89,'K')),
            NASAPolynomial(coeffs=[11.9727,0.0500891,-2.37346e-05,4.63698e-09,-3.29366e-13,-65129.4,-24.9385], Tmin=(1142.89,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 489,
    label = "C=C([O])CC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {1,S} {8,D} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  O u1 p2 c0 {2,S}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.91842,0.0361418,-4.85416e-06,-1.84164e-08,8.7351e-12,-20350.2,20.7004], Tmin=(100,'K'), Tmax=(1074.82,'K')),
            NASAPolynomial(coeffs=[12.4652,0.0177008,-8.15957e-06,1.64714e-09,-1.21496e-13,-23819.4,-36.5345], Tmin=(1074.82,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 490,
    label = "CCOC(=O)C1OOC(C)([O])C1=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {6,S} {9,S} {11,S}
2  C u0 p0 c0 {6,S} {7,S} {10,S} {12,S}
3  C u0 p0 c0 {5,S} {8,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {2,S} {21,D}
7  C u0 p0 c0 {2,S} {8,S} {22,D}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {2,S} {9,S}
11 O u1 p2 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.48555,0.0930267,-8.16542e-06,-6.80231e-08,3.52974e-11,-77030.4,44.4944], Tmin=(100,'K'), Tmax=(976.73,'K')),
            NASAPolynomial(coeffs=[30.0296,0.0292641,-1.05277e-05,2.03797e-09,-1.54881e-13,-86301.7,-122.752], Tmin=(976.73,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 491,
    label = "CCOC(=O)C1OC1(C)C=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {10,S}
3  C u0 p0 c0 {5,S} {9,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {2,S} {9,S} {19,D}
7  C u0 p0 c0 {1,S} {20,D} {21,S}
8  O u0 p2 c0 {1,S} {2,S}
9  O u0 p2 c0 {3,S} {6,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {6,D}
20 O u0 p2 c0 {7,D}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.871722,0.0933952,-4.96714e-05,-1.0592e-08,1.4009e-11,-74352.3,37.4315], Tmin=(100,'K'), Tmax=(930.31,'K')),
            NASAPolynomial(coeffs=[20.9303,0.034463,-1.07757e-05,1.75451e-09,-1.1691e-13,-79915.2,-74.2714], Tmin=(930.31,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 492,
    label = "CCOC(=O)[C]1OC=C(C)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
3  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {6,D} {9,S}
5  C u1 p0 c0 {7,S} {9,S} {10,S}
6  C u0 p0 c0 {4,D} {10,S} {20,S}
7  C u0 p0 c0 {5,S} {8,S} {19,D}
8  O u0 p2 c0 {1,S} {7,S}
9  O u0 p2 c0 {4,S} {5,S}
10 O u0 p2 c0 {5,S} {6,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 O u0 p2 c0 {7,D}
20 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.538821,0.0669705,4.80901e-05,-1.27034e-07,5.75873e-11,-63879.3,36.0994], Tmin=(100,'K'), Tmax=(949.41,'K')),
            NASAPolynomial(coeffs=[30.5941,0.0179379,-4.20948e-06,8.12442e-10,-7.18428e-14,-73492.6,-131.977], Tmin=(949.41,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 493,
    label = "[CH2]COOC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u1 p0 c0 {1,S} {8,S} {9,S}
3  C u0 p0 c0 {5,S} {10,D} {11,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.61857,0.0392565,3.76092e-06,-3.60666e-08,1.68937e-11,-24076.5,23.918], Tmin=(100,'K'), Tmax=(999.65,'K')),
            NASAPolynomial(coeffs=[15.2135,0.0154302,-6.36178e-06,1.27798e-09,-9.68434e-14,-28322.1,-49.3051], Tmin=(999.65,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 494,
    label = "[O]C(=O)C=O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,D} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {5,D}
3 O u1 p2 c0 {2,S}
4 O u0 p2 c0 {1,D}
5 O u0 p2 c0 {2,D}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.94679,0.0265977,-2.97429e-05,1.90562e-08,-5.37289e-12,-26451.4,14.3848], Tmin=(100,'K'), Tmax=(825.85,'K')),
            NASAPolynomial(coeffs=[5.38714,0.0147782,-8.27525e-06,1.72678e-09,-1.27056e-13,-26854.5,3.07839], Tmin=(825.85,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 495,
    label = "[O]OCC(O)C(=O)O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,D}
4  O u0 p2 c0 {1,S} {12,S}
5  O u0 p2 c0 {2,S} {11,S}
6  O u0 p2 c0 {3,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 O u1 p2 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.03625,0.0664862,-6.68153e-05,3.54469e-08,-7.67922e-12,-69076,30.3804], Tmin=(100,'K'), Tmax=(1101.58,'K')),
            NASAPolynomial(coeffs=[12.1006,0.02631,-1.21083e-05,2.33878e-09,-1.65441e-13,-71513.6,-24.0689], Tmin=(1101.58,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 496,
    label = "CC(=O)OCOO",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {7,S}
2  O u0 p2 c0 {3,S} {5,S}
3  O u0 p2 c0 {2,S} {13,S}
4  O u0 p2 c0 {7,D}
5  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
6  C u0 p0 c0 {7,S} {10,S} {11,S} {12,S}
7  C u0 p0 c0 {1,S} {4,D} {6,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.04152,0.0477974,7.13084e-06,-5.29795e-08,2.60153e-11,-65593.5,25.2982], Tmin=(100,'K'), Tmax=(957.61,'K')),
            NASAPolynomial(coeffs=[19.678,0.0123078,-3.62478e-06,6.97569e-10,-5.64551e-14,-71104.8,-73.9447], Tmin=(957.61,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 497,
    label = "O=COC(=O)C1CC(=O)CO1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {3,S} {14,D}
5  C u0 p0 c0 {1,S} {8,S} {15,D}
6  C u0 p0 c0 {8,S} {16,D} {17,S}
7  O u0 p2 c0 {1,S} {3,S}
8  O u0 p2 c0 {5,S} {6,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 O u0 p2 c0 {5,D}
16 O u0 p2 c0 {6,D}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.341451,0.065506,-1.92683e-05,-2.10986e-08,1.18826e-11,-93134.2,38.292], Tmin=(100,'K'), Tmax=(1061.1,'K')),
            NASAPolynomial(coeffs=[17.9856,0.0300397,-1.30197e-05,2.54897e-09,-1.8522e-13,-98626.5,-56.113], Tmin=(1061.1,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 498,
    label = "CC(=O)CC(O[O])C(=O)OC(COO)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {11,S} {14,S}
2  C u0 p0 c0 {1,S} {6,S} {16,S} {17,S}
3  C u0 p0 c0 {4,S} {8,S} {9,S} {15,S}
4  C u0 p0 c0 {3,S} {10,S} {18,S} {19,S}
5  C u0 p0 c0 {6,S} {20,S} {21,S} {22,S}
6  C u0 p0 c0 {2,S} {5,S} {23,D}
7  C u0 p0 c0 {1,S} {8,S} {24,D}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {3,S} {13,S}
10 O u0 p2 c0 {4,S} {12,S}
11 O u0 p2 c0 {1,S} {25,S}
12 O u0 p2 c0 {10,S} {26,S}
13 O u0 p2 c0 {9,S} {27,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 O u0 p2 c0 {6,D}
24 O u0 p2 c0 {7,D}
25 O u1 p2 c0 {11,S}
26 H u0 p0 c0 {12,S}
27 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.65023,0.183148,-0.000251104,1.94741e-07,-6.22738e-11,-97612.8,62.2461], Tmin=(100,'K'), Tmax=(757.82,'K')),
            NASAPolynomial(coeffs=[16.716,0.0756563,-3.83545e-05,7.59508e-09,-5.39767e-13,-100700,-30.3628], Tmin=(757.82,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 499,
    label = "CC(=O)C(CC(=O)OC(COO)OO)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {11,S} {14,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {15,S}
3  C u0 p0 c0 {1,S} {7,S} {16,S} {17,S}
4  C u0 p0 c0 {2,S} {10,S} {18,S} {19,S}
5  C u0 p0 c0 {6,S} {20,S} {21,S} {22,S}
6  C u0 p0 c0 {1,S} {5,S} {23,D}
7  C u0 p0 c0 {3,S} {8,S} {24,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {2,S} {13,S}
10 O u0 p2 c0 {4,S} {12,S}
11 O u0 p2 c0 {1,S} {25,S}
12 O u0 p2 c0 {10,S} {26,S}
13 O u0 p2 c0 {9,S} {27,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 O u0 p2 c0 {6,D}
24 O u0 p2 c0 {7,D}
25 O u1 p2 c0 {11,S}
26 H u0 p0 c0 {12,S}
27 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.65023,0.183148,-0.000251104,1.94741e-07,-6.22738e-11,-97612.8,62.2461], Tmin=(100,'K'), Tmax=(757.82,'K')),
            NASAPolynomial(coeffs=[16.716,0.0756563,-3.83545e-05,7.59508e-09,-5.39767e-13,-100700,-30.3628], Tmin=(757.82,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 500,
    label = "CC1([O])CC(C(=O)OC(COO)OO)OO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {9,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {7,S} {10,S} {16,S}
4  C u0 p0 c0 {5,S} {8,S} {11,S} {19,S}
5  C u0 p0 c0 {4,S} {12,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {22,S} {23,S} {24,S}
7  C u0 p0 c0 {3,S} {8,S} {25,D}
8  O u0 p2 c0 {4,S} {7,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {3,S} {9,S}
11 O u0 p2 c0 {4,S} {14,S}
12 O u0 p2 c0 {5,S} {13,S}
13 O u0 p2 c0 {12,S} {26,S}
14 O u0 p2 c0 {11,S} {27,S}
15 O u1 p2 c0 {1,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 O u0 p2 c0 {7,D}
26 H u0 p0 c0 {13,S}
27 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.07941,0.158669,-0.000140863,5.62488e-08,-6.76715e-12,-91133.7,59.1125], Tmin=(100,'K'), Tmax=(1049.5,'K')),
            NASAPolynomial(coeffs=[33.6297,0.0432925,-1.64731e-05,2.96844e-09,-2.05646e-13,-100610,-132.071], Tmin=(1049.5,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 501,
    label = "CC1C[CH]C(=O)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {2,S} {5,S} {13,S}
5  C u0 p0 c0 {4,S} {6,S} {14,D}
6  O u0 p2 c0 {1,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.21292,0.0190602,8.18256e-05,-1.20782e-07,4.83692e-11,-29335.1,21.0707], Tmin=(100,'K'), Tmax=(933.7,'K')),
            NASAPolynomial(coeffs=[13.5561,0.0220445,-5.83122e-06,9.6975e-10,-7.17634e-14,-33701.6,-44.9152], Tmin=(933.7,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 502,
    label = "[O]OC(O)C(=O)O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,D}
3  O u0 p2 c0 {1,S} {8,S}
4  O u0 p2 c0 {1,S} {9,S}
5  O u0 p2 c0 {2,S} {10,S}
6  H u0 p0 c0 {1,S}
7  O u0 p2 c0 {2,D}
8  O u1 p2 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.68986,0.0550667,-6.84877e-05,4.76191e-08,-1.37101e-11,-69677,25.0222], Tmin=(100,'K'), Tmax=(836.38,'K')),
            NASAPolynomial(coeffs=[8.31812,0.0233664,-1.16342e-05,2.30122e-09,-1.64073e-13,-70785.7,-5.77097], Tmin=(836.38,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 503,
    label = "C=CC(=O)OC(C)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {5,D} {12,S}
4  C u0 p0 c0 {3,S} {6,S} {13,D}
5  C u0 p0 c0 {3,D} {14,S} {15,S}
6  O u0 p2 c0 {1,S} {4,S}
7  O u0 p2 c0 {1,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.877201,0.075778,-0.000108508,9.6169e-08,-3.53117e-11,-34076.4,30.5254], Tmin=(100,'K'), Tmax=(758.24,'K')),
            NASAPolynomial(coeffs=[6.39492,0.0386707,-1.92753e-05,3.79874e-09,-2.6864e-13,-34683.2,6.94895], Tmin=(758.24,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 504,
    label = "CC1=COC(C(=O)OC(C)[O])O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {6,S} {8,S} {10,S} {13,S}
2  C u0 p0 c0 {3,S} {9,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {7,D} {8,S}
6  C u0 p0 c0 {1,S} {9,S} {20,D}
7  C u0 p0 c0 {5,D} {10,S} {21,S}
8  O u0 p2 c0 {1,S} {5,S}
9  O u0 p2 c0 {2,S} {6,S}
10 O u0 p2 c0 {1,S} {7,S}
11 O u1 p2 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {6,D}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.901788,0.0785518,1.88268e-05,-9.20095e-08,4.31538e-11,-85491.5,40.0421], Tmin=(100,'K'), Tmax=(972.68,'K')),
            NASAPolynomial(coeffs=[29.0139,0.0261271,-9.20105e-06,1.82173e-09,-1.42214e-13,-94650.9,-120.623], Tmin=(972.68,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 505,
    label = "CC1CC(O[O])C(=O)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {7,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {6,S} {15,D}
6  O u0 p2 c0 {1,S} {5,S}
7  O u0 p2 c0 {3,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u0 p2 c0 {5,D}
16 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.34307,0.0357878,6.49529e-05,-1.15797e-07,4.90334e-11,-43770.8,29.7835], Tmin=(100,'K'), Tmax=(932.24,'K')),
            NASAPolynomial(coeffs=[18.086,0.0216852,-5.25688e-06,8.48125e-10,-6.38312e-14,-49401.3,-63.273], Tmin=(932.24,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 506,
    label = "O=[C]CC(=O)CCC(=O)O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {14,D}
5  C u0 p0 c0 {2,S} {7,S} {15,D}
6  C u1 p0 c0 {3,S} {16,D}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 O u0 p2 c0 {5,D}
16 O u0 p2 c0 {6,D}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.62631,0.115588,-0.000191761,1.76903e-07,-6.33603e-11,-67846.5,36.0517], Tmin=(100,'K'), Tmax=(840.29,'K')),
            NASAPolynomial(coeffs=[7.22885,0.0501452,-2.48656e-05,4.76589e-09,-3.27676e-13,-68176.3,5.41457], Tmin=(840.29,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 507,
    label = "O=[C]CCC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,D} {10,S}
4  C u1 p0 c0 {2,S} {11,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
11 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.60551,0.0330499,-2.13102e-05,7.37021e-09,-1.08289e-12,-18546.1,10.1599], Tmin=(200,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[13.2139,0.0137339,-4.6264e-06,7.10941e-10,-4.09538e-14,-21653.5,-36.4185], Tmin=(1388,'K'), Tmax=(5000,'K')),
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
    index = 508,
    label = "O=[C]C(=O)O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,D}
2 O u0 p2 c0 {1,S} {6,S}
3 C u1 p0 c0 {1,S} {5,D}
4 O u0 p2 c0 {1,D}
5 O u0 p2 c0 {3,D}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.74337,0.0260452,-2.26906e-05,9.41167e-09,-1.55069e-12,-38835.4,14.7947], Tmin=(100,'K'), Tmax=(1438.17,'K')),
            NASAPolynomial(coeffs=[9.12274,0.00830218,-4.18473e-06,8.33218e-10,-5.94746e-14,-40670.3,-18.3001], Tmin=(1438.17,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 509,
    label = "O=C=CCO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {4,D} {7,S}
3 O u0 p2 c0 {1,S} {8,S}
4 C u0 p0 c0 {2,D} {9,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.09554,0.0444918,-6.12347e-05,4.83712e-08,-1.52756e-11,-28501.7,16.784], Tmin=(100,'K'), Tmax=(867.07,'K')),
            NASAPolynomial(coeffs=[7.01799,0.0175594,-7.3354e-06,1.31124e-09,-8.70528e-14,-29196.6,-5.34621], Tmin=(867.07,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 510,
    label = "C[C]C(=O)O",
    molecule = 
"""
1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {3,S} {4,S} {8,D}
3 C u0 p1 c0 {1,S} {2,S}
4 O u0 p2 c0 {2,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 O u0 p2 c0 {2,D}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.75051,0.0306245,-1.63621e-05,3.84652e-09,-3.50345e-13,-4595.87,25.3458], Tmin=(100,'K'), Tmax=(2441.76,'K')),
            NASAPolynomial(coeffs=[12.6301,0.0144401,-6.41991e-06,1.13202e-09,-7.24213e-14,-9420.6,-31.1373], Tmin=(2441.76,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 511,
    label = "CC(=O)OC(=O)C1OC=C(C)O1",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {8,S} {9,S} {11,S}
2  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {2,S} {7,D} {8,S}
5  C u0 p0 c0 {1,S} {10,S} {18,D}
6  C u0 p0 c0 {3,S} {10,S} {19,D}
7  C u0 p0 c0 {4,D} {9,S} {20,S}
8  O u0 p2 c0 {1,S} {4,S}
9  O u0 p2 c0 {1,S} {7,S}
10 O u0 p2 c0 {5,S} {6,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {6,D}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.822977,0.0758737,2.08501e-05,-9.98724e-08,4.83687e-11,-104546,39.6522], Tmin=(100,'K'), Tmax=(949.46,'K')),
            NASAPolynomial(coeffs=[31.1717,0.016234,-3.65483e-06,6.97439e-10,-6.21973e-14,-114009,-130.882], Tmin=(949.46,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 512,
    label = "CC1=COC(C(=O)OC=O)O1",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {7,S} {8,S} {10,S}
2  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {5,D} {7,S}
4  C u0 p0 c0 {1,S} {9,S} {14,D}
5  C u0 p0 c0 {3,D} {8,S} {15,S}
6  C u0 p0 c0 {9,S} {16,D} {17,S}
7  O u0 p2 c0 {1,S} {3,S}
8  O u0 p2 c0 {1,S} {5,S}
9  O u0 p2 c0 {4,S} {6,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {5,S}
16 O u0 p2 c0 {6,D}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.234704,0.062578,3.4723e-05,-1.10759e-07,5.21608e-11,-97847,35.2294], Tmin=(100,'K'), Tmax=(944.13,'K')),
            NASAPolynomial(coeffs=[30.8903,0.00759049,-5.90356e-08,4.93179e-11,-1.87177e-14,-107151,-131.288], Tmin=(944.13,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 513,
    label = "CCOC(=O)C(O[O])C(OO)C(=O)COO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {9,S} {14,S}
2  C u0 p0 c0 {1,S} {7,S} {11,S} {15,S}
3  C u0 p0 c0 {5,S} {8,S} {16,S} {17,S}
4  C u0 p0 c0 {6,S} {10,S} {21,S} {22,S}
5  C u0 p0 c0 {3,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {1,S} {4,S} {23,D}
7  C u0 p0 c0 {2,S} {8,S} {24,D}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {1,S} {12,S}
10 O u0 p2 c0 {4,S} {13,S}
11 O u0 p2 c0 {2,S} {25,S}
12 O u0 p2 c0 {9,S} {26,S}
13 O u0 p2 c0 {10,S} {27,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 O u0 p2 c0 {6,D}
24 O u0 p2 c0 {7,D}
25 O u1 p2 c0 {11,S}
26 H u0 p0 c0 {12,S}
27 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.21507,0.167535,-0.000184289,1.0672e-07,-2.52572e-11,-92219,61.6023], Tmin=(100,'K'), Tmax=(1011.73,'K')),
            NASAPolynomial(coeffs=[22.771,0.0647958,-3.19674e-05,6.35022e-09,-4.557e-13,-97477.2,-64.0687], Tmin=(1011.73,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 514,
    label = "CC(=O)CC(OO)C(=O)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {3,S} {15,D}
5  C u0 p0 c0 {1,S} {7,S} {16,D}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {5,S} {17,S}
8  O u0 p2 c0 {6,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {4,D}
16 O u0 p2 c0 {5,D}
17 O u1 p2 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.18674,0.12081,-0.000170343,1.28974e-07,-3.89969e-11,-54941.8,41.0757], Tmin=(100,'K'), Tmax=(810.24,'K')),
            NASAPolynomial(coeffs=[15.5239,0.0383164,-1.76276e-05,3.32452e-09,-2.29048e-13,-57649.8,-36.0276], Tmin=(810.24,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 515,
    label = "CC(=O)C1OC1C(=O)OC=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {9,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {14,D}
5  C u0 p0 c0 {2,S} {8,S} {15,D}
6  C u0 p0 c0 {8,S} {16,D} {17,S}
7  O u0 p2 c0 {1,S} {2,S}
8  O u0 p2 c0 {5,S} {6,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 O u0 p2 c0 {5,D}
16 O u0 p2 c0 {6,D}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.0133358,0.0733504,-2.9924e-05,-2.35115e-08,1.75192e-11,-86174.3,40.2197], Tmin=(100,'K'), Tmax=(934.93,'K')),
            NASAPolynomial(coeffs=[20.2472,0.0228012,-6.61268e-06,1.07418e-09,-7.40971e-14,-91532,-64.4546], Tmin=(934.93,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 516,
    label = "CC1([O])CC(OO)C(=O)OO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {5,S} {7,S} {11,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {8,S} {17,D}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {3,S} {9,S}
8  O u0 p2 c0 {5,S} {6,S}
9  O u0 p2 c0 {7,S} {18,S}
10 O u1 p2 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u0 p2 c0 {5,D}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.51324,0.0638792,5.48879e-05,-1.28239e-07,5.46985e-11,-63845.9,34.2004], Tmin=(100,'K'), Tmax=(991.49,'K')),
            NASAPolynomial(coeffs=[31.5487,0.0203503,-9.09275e-06,2.07978e-09,-1.73151e-13,-74421.9,-141.478], Tmin=(991.49,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 517,
    label = "CCOC(=O)C(C=O)OC[C]=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {7,S} {10,S}
2  C u0 p0 c0 {3,S} {8,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {7,S} {9,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {8,S} {18,D}
6  C u0 p0 c0 {1,S} {19,D} {20,S}
7  O u0 p2 c0 {1,S} {4,S}
8  O u0 p2 c0 {2,S} {5,S}
9  C u1 p0 c0 {4,S} {21,D}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {6,D}
20 H u0 p0 c0 {6,S}
21 O u0 p2 c0 {9,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.235877,0.101468,-8.92969e-05,4.34947e-08,-9.20229e-12,-80354.2,42.5933], Tmin=(100,'K'), Tmax=(1078.62,'K')),
            NASAPolynomial(coeffs=[11.6898,0.0572423,-2.77926e-05,5.47999e-09,-3.9124e-13,-82926.9,-15.8435], Tmin=(1078.62,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 518,
    label = "CCOC(=O)[C]1OCC(=O)C1O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {9,S} {12,S} {13,S}
3  C u0 p0 c0 {6,S} {8,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u1 p0 c0 {1,S} {7,S} {8,S}
6  C u0 p0 c0 {1,S} {3,S} {19,D}
7  C u0 p0 c0 {5,S} {9,S} {20,D}
8  O u0 p2 c0 {3,S} {5,S}
9  O u0 p2 c0 {2,S} {7,S}
10 O u0 p2 c0 {1,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 O u0 p2 c0 {6,D}
20 O u0 p2 c0 {7,D}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.592841,0.0833459,-2.83539e-05,-2.16881e-08,1.33444e-11,-82527.2,44.8022], Tmin=(100,'K'), Tmax=(1055.12,'K')),
            NASAPolynomial(coeffs=[20.7154,0.0386995,-1.62519e-05,3.1223e-09,-2.24458e-13,-89035.2,-68.6727], Tmin=(1055.12,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 519,
    label = "[CH2]OC(C=O)C(=O)OCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {7,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {7,S} {15,D}
5  C u0 p0 c0 {1,S} {16,D} {17,S}
6  C u1 p0 c0 {8,S} {18,S} {19,S}
7  O u0 p2 c0 {2,S} {4,S}
8  O u0 p2 c0 {1,S} {6,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {4,D}
16 O u0 p2 c0 {5,D}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.201773,0.0894443,-7.91246e-05,3.89916e-08,-8.28525e-12,-64365.7,35.7166], Tmin=(100,'K'), Tmax=(1082.27,'K')),
            NASAPolynomial(coeffs=[11.13,0.0490543,-2.31451e-05,4.5088e-09,-3.19872e-13,-66731.1,-17.8697], Tmin=(1082.27,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 520,
    label = "CCOC(=O)C1[CH]OCO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {7,S} {10,S}
2  C u0 p0 c0 {3,S} {8,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {7,S} {9,S} {16,S} {17,S}
5  C u1 p0 c0 {1,S} {9,S} {19,S}
6  C u0 p0 c0 {1,S} {8,S} {18,D}
7  O u0 p2 c0 {1,S} {4,S}
8  O u0 p2 c0 {2,S} {6,S}
9  O u0 p2 c0 {4,S} {5,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u0 p2 c0 {6,D}
19 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.217319,0.0597396,5.96521e-05,-1.57467e-07,7.7745e-11,-65696.8,32.3016], Tmin=(100,'K'), Tmax=(880.76,'K')),
            NASAPolynomial(coeffs=[34.0668,-0.00405198,1.17622e-05,-2.73527e-09,1.94024e-13,-75300.9,-148.984], Tmin=(880.76,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 521,
    label = "CCOC(=O)C(C=O)OCO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {7,S} {10,S}
2  C u0 p0 c0 {3,S} {8,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {7,S} {9,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {8,S} {18,D}
6  C u0 p0 c0 {1,S} {19,D} {20,S}
7  O u0 p2 c0 {1,S} {4,S}
8  O u0 p2 c0 {2,S} {5,S}
9  O u0 p2 c0 {4,S} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {6,D}
20 H u0 p0 c0 {6,S}
21 O u1 p2 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.75289,0.114499,-0.000105534,4.86173e-08,-8.84761e-12,-82565.6,46.7406], Tmin=(100,'K'), Tmax=(1328.81,'K')),
            NASAPolynomial(coeffs=[25.2916,0.0330887,-1.36351e-05,2.51139e-09,-1.73266e-13,-89753,-91.4216], Tmin=(1328.81,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 522,
    label = "C=C([O])C(CC(=O)OC(COO)OO)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {9,S} {15,S}
2  C u0 p0 c0 {4,S} {8,S} {10,S} {16,S}
3  C u0 p0 c0 {1,S} {6,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {11,S} {19,S} {20,S}
5  C u0 p0 c0 {1,S} {7,D} {21,S}
6  C u0 p0 c0 {3,S} {8,S} {22,D}
7  C u0 p0 c0 {5,D} {23,S} {24,S}
8  O u0 p2 c0 {2,S} {6,S}
9  O u0 p2 c0 {1,S} {14,S}
10 O u0 p2 c0 {2,S} {13,S}
11 O u0 p2 c0 {4,S} {12,S}
12 O u0 p2 c0 {11,S} {26,S}
13 O u0 p2 c0 {10,S} {27,S}
14 O u0 p2 c0 {9,S} {25,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u1 p2 c0 {5,S}
22 O u0 p2 c0 {6,D}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {14,S}
26 H u0 p0 c0 {12,S}
27 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.06079,0.191207,-0.000254962,1.8299e-07,-5.32869e-11,-96395.3,62.0783], Tmin=(100,'K'), Tmax=(833.97,'K')),
            NASAPolynomial(coeffs=[21.479,0.0687097,-3.46353e-05,6.86317e-09,-4.88975e-13,-100655,-56.4992], Tmin=(833.97,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 523,
    label = "CCOC(=O)C1OCOOC1[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {11,S}
2  C u0 p0 c0 {1,S} {9,S} {12,S} {15,S}
3  C u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {7,S} {10,S} {19,S} {20,S}
6  C u0 p0 c0 {1,S} {8,S} {21,D}
7  O u0 p2 c0 {1,S} {5,S}
8  O u0 p2 c0 {3,S} {6,S}
9  O u0 p2 c0 {2,S} {10,S}
10 O u0 p2 c0 {5,S} {9,S}
11 H u0 p0 c0 {1,S}
12 O u1 p2 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.929686,0.0751825,4.80387e-05,-1.4341e-07,6.95671e-11,-78976.2,40.6258], Tmin=(100,'K'), Tmax=(903.77,'K')),
            NASAPolynomial(coeffs=[32.8858,0.0142512,1.89573e-06,-7.37065e-10,5.02995e-14,-88712.3,-139.141], Tmin=(903.77,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 524,
    label = "CCOC(=O)[C](C=O)OCOO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
3  C u0 p0 c0 {7,S} {9,S} {16,S} {17,S}
4  C u1 p0 c0 {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {8,S} {18,D}
6  C u0 p0 c0 {4,S} {19,D} {20,S}
7  O u0 p2 c0 {3,S} {4,S}
8  O u0 p2 c0 {1,S} {5,S}
9  O u0 p2 c0 {3,S} {10,S}
10 O u0 p2 c0 {9,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {6,D}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.46194,0.121117,-0.000124871,6.66547e-08,-1.43645e-11,-79135.1,44.8841], Tmin=(100,'K'), Tmax=(1114.16,'K')),
            NASAPolynomial(coeffs=[20.2502,0.0431661,-1.99228e-05,3.8565e-09,-2.73299e-13,-83973.1,-62.211], Tmin=(1114.16,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 525,
    label = "O=C(CC1OCC1=O)OC(COO)OO",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {8,S} {14,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {15,S}
3  C u0 p0 c0 {1,S} {7,S} {16,S} {17,S}
4  C u0 p0 c0 {2,S} {11,S} {18,S} {19,S}
5  C u0 p0 c0 {6,S} {8,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {5,S} {22,D}
7  C u0 p0 c0 {3,S} {9,S} {23,D}
8  O u0 p2 c0 {1,S} {5,S}
9  O u0 p2 c0 {2,S} {7,S}
10 O u0 p2 c0 {2,S} {12,S}
11 O u0 p2 c0 {4,S} {13,S}
12 O u0 p2 c0 {10,S} {24,S}
13 O u0 p2 c0 {11,S} {25,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u0 p2 c0 {6,D}
23 O u0 p2 c0 {7,D}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.12352,0.137457,-0.000122669,5.51726e-08,-1.01684e-11,-100062,52.7265], Tmin=(100,'K'), Tmax=(1268.06,'K')),
            NASAPolynomial(coeffs=[23.1265,0.0578089,-2.84546e-05,5.64129e-09,-4.03388e-13,-106466,-75.0874], Tmin=(1268.06,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 526,
    label = "[O]OCC(=O)CC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  C u0 p0 c0 {1,S} {11,D} {12,S}
5  O u0 p2 c0 {2,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {4,S}
13 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.09329,0.07112,-8.55611e-05,5.08433e-08,-7.77266e-12,-29906.4,27.8979], Tmin=(100,'K'), Tmax=(603.2,'K')),
            NASAPolynomial(coeffs=[8.58966,0.0321775,-1.54986e-05,3.00381e-09,-2.10917e-13,-31006.6,-6.10215], Tmin=(603.2,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 527,
    label = "CCOC(=O)C(C=O)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {6,S} {14,D}
5  C u0 p0 c0 {1,S} {15,D} {16,S}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {1,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 O u0 p2 c0 {5,D}
16 H u0 p0 c0 {5,S}
17 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.561212,0.0825546,-8.08486e-05,4.71038e-08,-1.20645e-11,-62072.9,35.2045], Tmin=(100,'K'), Tmax=(907.18,'K')),
            NASAPolynomial(coeffs=[8.51622,0.047479,-2.2852e-05,4.48349e-09,-3.1926e-13,-63516.2,-2.39889], Tmin=(907.18,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 528,
    label = "CCOC(=O)[C](C=O)OC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3  C u1 p0 c0 {4,S} {5,S} {8,S}
4  C u0 p0 c0 {3,S} {7,S} {14,D}
5  C u0 p0 c0 {3,S} {15,D} {16,S}
6  C u0 p0 c0 {8,S} {17,D} {18,S}
7  O u0 p2 c0 {1,S} {4,S}
8  O u0 p2 c0 {3,S} {6,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 O u0 p2 c0 {4,D}
15 O u0 p2 c0 {5,D}
16 H u0 p0 c0 {5,S}
17 O u0 p2 c0 {6,D}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.568576,0.0837259,-7.25931e-05,3.58604e-08,-7.90287e-12,-83102.4,38.3039], Tmin=(100,'K'), Tmax=(1022.4,'K')),
            NASAPolynomial(coeffs=[8.81215,0.0514741,-2.52752e-05,5.00624e-09,-3.58334e-13,-84788.1,-1.64916], Tmin=(1022.4,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 529,
    label = "[O]OCC(=O)C(CC(=O)OC(COO)OO)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {9,S} {16,S}
2  C u0 p0 c0 {4,S} {8,S} {10,S} {17,S}
3  C u0 p0 c0 {1,S} {7,S} {18,S} {19,S}
4  C u0 p0 c0 {2,S} {11,S} {20,S} {21,S}
5  C u0 p0 c0 {6,S} {12,S} {22,S} {23,S}
6  C u0 p0 c0 {1,S} {5,S} {24,D}
7  C u0 p0 c0 {3,S} {8,S} {25,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {1,S} {15,S}
10 O u0 p2 c0 {2,S} {14,S}
11 O u0 p2 c0 {4,S} {13,S}
12 O u0 p2 c0 {5,S} {26,S}
13 O u0 p2 c0 {11,S} {28,S}
14 O u0 p2 c0 {10,S} {29,S}
15 O u0 p2 c0 {9,S} {27,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 O u0 p2 c0 {6,D}
25 O u0 p2 c0 {7,D}
26 O u1 p2 c0 {12,S}
27 H u0 p0 c0 {15,S}
28 H u0 p0 c0 {13,S}
29 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.25807,0.221268,-0.000326439,2.6351e-07,-8.62908e-11,-106428,70.737], Tmin=(100,'K'), Tmax=(744.78,'K')),
            NASAPolynomial(coeffs=[21.1114,0.0796415,-4.11926e-05,8.17352e-09,-5.79577e-13,-110355,-48.7093], Tmin=(744.78,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 530,
    label = "CCOC(=O)C(=O)C=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {5,S} {12,D}
4  C u0 p0 c0 {3,S} {6,S} {13,D}
5  C u0 p0 c0 {3,S} {14,D} {15,S}
6  O u0 p2 c0 {1,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {3,D}
13 O u0 p2 c0 {4,D}
14 O u0 p2 c0 {5,D}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.0332,0.0765921,-6.71454e-05,-9.09329e-09,4.28892e-11,-71610.9,27.8875], Tmin=(100,'K'), Tmax=(506.2,'K')),
            NASAPolynomial(coeffs=[7.83171,0.0419009,-2.07396e-05,4.05942e-09,-2.86232e-13,-72543,-2.69117], Tmin=(506.2,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 531,
    label = "CC(O[O])OC(=O)CC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {14,D}
5  C u0 p0 c0 {2,S} {15,D} {16,S}
6  O u0 p2 c0 {1,S} {4,S}
7  O u0 p2 c0 {1,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 O u0 p2 c0 {5,D}
16 H u0 p0 c0 {5,S}
17 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.366144,0.0874255,-9.54588e-05,6.27596e-08,-1.79126e-11,-64240.3,35.8675], Tmin=(100,'K'), Tmax=(826.86,'K')),
            NASAPolynomial(coeffs=[8.58664,0.047659,-2.33202e-05,4.59822e-09,-3.27916e-13,-65599.8,-2.22898], Tmin=(826.86,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 532,
    label = "CC(OO)OC(=O)[CH]C=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3  C u1 p0 c0 {4,S} {5,S} {13,S}
4  C u0 p0 c0 {3,S} {6,S} {14,D}
5  C u0 p0 c0 {3,S} {15,D} {16,S}
6  O u0 p2 c0 {1,S} {4,S}
7  O u0 p2 c0 {1,S} {8,S}
8  O u0 p2 c0 {7,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 O u0 p2 c0 {5,D}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.285307,0.0886569,-8.39746e-05,4.27889e-08,-9.25731e-12,-61599.4,35.4391], Tmin=(100,'K'), Tmax=(1072.26,'K')),
            NASAPolynomial(coeffs=[12.0984,0.0445887,-2.23264e-05,4.4595e-09,-3.20667e-13,-64132.7,-22.3762], Tmin=(1072.26,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 533,
    label = "CCOC(=O)C(C=O)(O[O])OC=O",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {9,S} {11,S}
2  O u0 p2 c0 {8,S} {13,S}
3  O u0 p2 c0 {7,S} {8,S}
4  O u0 p2 c0 {11,D}
5  O u0 p2 c0 {12,D}
6  O u0 p2 c0 {13,D}
7  O u1 p2 c0 {3,S}
8  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
9  C u0 p0 c0 {1,S} {10,S} {14,S} {15,S}
10 C u0 p0 c0 {9,S} {16,S} {17,S} {18,S}
11 C u0 p0 c0 {1,S} {4,D} {8,S}
12 C u0 p0 c0 {5,D} {8,S} {19,S}
13 C u0 p0 c0 {2,S} {6,D} {20,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {12,S}
20 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.12397,0.117157,-0.000108404,4.86369e-08,-8.50607e-12,-105640,48.373], Tmin=(100,'K'), Tmax=(1392.25,'K')),
            NASAPolynomial(coeffs=[29.3005,0.0268741,-1.11341e-05,2.06018e-09,-1.42555e-13,-114390,-113.631], Tmin=(1392.25,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 534,
    label = "CC1OC(=O)C(C=O)O1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {5,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {7,S} {13,D}
5  C u0 p0 c0 {2,S} {14,D} {15,S}
6  O u0 p2 c0 {1,S} {2,S}
7  O u0 p2 c0 {1,S} {4,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 O u0 p2 c0 {5,D}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.7266,0.0308678,5.59956e-05,-8.96327e-08,3.4368e-11,-80944.1,27.6799], Tmin=(100,'K'), Tmax=(1004.77,'K')),
            NASAPolynomial(coeffs=[13.9812,0.029325,-1.22286e-05,2.42883e-09,-1.81109e-13,-85791.5,-43.3671], Tmin=(1004.77,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 535,
    label = "CC1OCC(=O)O1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {6,S} {13,D}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.46877,0.0131939,8.52695e-05,-1.16556e-07,4.40035e-11,-65111.1,20.1959], Tmin=(100,'K'), Tmax=(977.28,'K')),
            NASAPolynomial(coeffs=[12.8597,0.0224909,-8.54816e-06,1.70829e-09,-1.3138e-13,-69617.1,-42.3581], Tmin=(977.28,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 536,
    label = "O=C(O)[CH]O",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {6,S}
2 C u0 p0 c0 {1,S} {4,S} {5,D}
3 O u0 p2 c0 {1,S} {8,S}
4 O u0 p2 c0 {2,S} {7,S}
5 O u0 p2 c0 {2,D}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.44224,0.0324073,-2.58573e-05,1.05288e-08,-1.74963e-12,-54108.5,16.6843], Tmin=(100,'K'), Tmax=(1406.09,'K')),
            NASAPolynomial(coeffs=[8.97795,0.0138147,-6.02286e-06,1.12471e-09,-7.76083e-14,-55946.4,-17.0741], Tmin=(1406.09,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 537,
    label = "CCOC(=O)C1OC=C(C[O])O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {6,S} {8,S} {10,S} {11,S}
2  C u0 p0 c0 {3,S} {9,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {7,D} {8,S}
6  C u0 p0 c0 {1,S} {9,S} {20,D}
7  C u0 p0 c0 {5,D} {10,S} {21,S}
8  O u0 p2 c0 {1,S} {5,S}
9  O u0 p2 c0 {2,S} {6,S}
10 O u0 p2 c0 {1,S} {7,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 O u1 p2 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {6,D}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.819538,0.0786917,1.33864e-05,-8.36022e-08,3.9745e-11,-79832,40.3421], Tmin=(100,'K'), Tmax=(971.91,'K')),
            NASAPolynomial(coeffs=[27.4654,0.0280074,-9.82637e-06,1.89837e-09,-1.45067e-13,-88434.4,-111.281], Tmin=(971.91,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 538,
    label = "CCOC(=O)C1([O])OC=C(C)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {6,S} {8,S} {10,S} {11,S}
2  C u0 p0 c0 {3,S} {9,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {7,D} {8,S}
6  C u0 p0 c0 {1,S} {9,S} {20,D}
7  C u0 p0 c0 {5,D} {10,S} {21,S}
8  O u0 p2 c0 {1,S} {5,S}
9  O u0 p2 c0 {2,S} {6,S}
10 O u0 p2 c0 {1,S} {7,S}
11 O u1 p2 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {6,D}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.944965,0.0809651,1.14791e-05,-8.85069e-08,4.39801e-11,-80934.9,38.813], Tmin=(100,'K'), Tmax=(946.43,'K')),
            NASAPolynomial(coeffs=[29.1839,0.0228157,-6.01606e-06,1.05966e-09,-8.29805e-14,-89736.4,-121.252], Tmin=(946.43,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 539,
    label = "CCOC(=O)C1(O[O])OC=C(C)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {6,S} {8,S} {9,S} {11,S}
2  C u0 p0 c0 {3,S} {10,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {7,D} {8,S}
6  C u0 p0 c0 {1,S} {10,S} {20,D}
7  C u0 p0 c0 {5,D} {9,S} {21,S}
8  O u0 p2 c0 {1,S} {5,S}
9  O u0 p2 c0 {1,S} {7,S}
10 O u0 p2 c0 {2,S} {6,S}
11 O u0 p2 c0 {1,S} {22,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {6,D}
21 H u0 p0 c0 {7,S}
22 O u1 p2 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.60817,0.097348,-2.09845e-05,-5.84745e-08,3.36072e-11,-83345.1,41.9338], Tmin=(100,'K'), Tmax=(956.02,'K')),
            NASAPolynomial(coeffs=[30.5414,0.0259229,-7.90414e-06,1.42992e-09,-1.08007e-13,-92375.3,-126.802], Tmin=(956.02,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 540,
    label = "C[CH]OC(=O)C1(OO)OC=C(C)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {8,S} {9,S} {11,S}
2  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
3  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {7,D} {8,S}
5  C u0 p0 c0 {1,S} {10,S} {19,D}
6  C u1 p0 c0 {3,S} {10,S} {20,S}
7  C u0 p0 c0 {4,D} {9,S} {21,S}
8  O u0 p2 c0 {1,S} {4,S}
9  O u0 p2 c0 {1,S} {7,S}
10 O u0 p2 c0 {5,S} {6,S}
11 O u0 p2 c0 {1,S} {12,S}
12 O u0 p2 c0 {11,S} {22,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 O u0 p2 c0 {5,D}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.15097,0.105139,-2.4409e-05,-6.57352e-08,3.82338e-11,-78776.8,43.7317], Tmin=(100,'K'), Tmax=(957.1,'K')),
            NASAPolynomial(coeffs=[35.7494,0.0199407,-5.60108e-06,1.06982e-09,-8.76512e-14,-89384.3,-154.968], Tmin=(957.1,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 541,
    label = "CCOC(=O)C(C=O)(O[O])OCOO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {9,S} {12,S}
2  O u0 p2 c0 {10,S} {13,S}
3  O u0 p2 c0 {5,S} {12,S}
4  O u0 p2 c0 {8,S} {9,S}
5  O u0 p2 c0 {3,S} {23,S}
6  O u0 p2 c0 {13,D}
7  O u0 p2 c0 {14,D}
8  O u1 p2 c0 {4,S}
9  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
10 C u0 p0 c0 {2,S} {11,S} {15,S} {16,S}
11 C u0 p0 c0 {10,S} {17,S} {18,S} {19,S}
12 C u0 p0 c0 {1,S} {3,S} {20,S} {21,S}
13 C u0 p0 c0 {2,S} {6,D} {9,S}
14 C u0 p0 c0 {7,D} {9,S} {22,S}
15 H u0 p0 c0 {10,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {11,S}
18 H u0 p0 c0 {11,S}
19 H u0 p0 c0 {11,S}
20 H u0 p0 c0 {12,S}
21 H u0 p0 c0 {12,S}
22 H u0 p0 c0 {14,S}
23 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.60456,0.145218,-0.000124606,3.19623e-08,4.6645e-12,-99406.9,53.9679], Tmin=(100,'K'), Tmax=(979.51,'K')),
            NASAPolynomial(coeffs=[38.3268,0.0212719,-7.21312e-06,1.34974e-09,-1.01486e-13,-109890,-159.038], Tmin=(979.51,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 542,
    label = "CCOC(=O)C(C=O)(OO)OC=O",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {7,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {7,S} {16,D}
5  C u0 p0 c0 {1,S} {17,D} {18,S}
6  C u0 p0 c0 {8,S} {19,D} {20,S}
7  O u0 p2 c0 {2,S} {4,S}
8  O u0 p2 c0 {1,S} {6,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {21,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u0 p2 c0 {4,D}
17 O u0 p2 c0 {5,D}
18 H u0 p0 c0 {5,S}
19 O u0 p2 c0 {6,D}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.22938,0.119034,-9.84079e-05,3.34459e-08,-2.63484e-12,-123918,47.9823], Tmin=(100,'K'), Tmax=(1114.55,'K')),
            NASAPolynomial(coeffs=[29.1073,0.0312999,-1.36157e-05,2.63554e-09,-1.89374e-13,-132439,-113.489], Tmin=(1114.55,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 543,
    label = "C=C([O])COC(=O)C(=O)OCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {8,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {9,S} {15,S} {16,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {7,D} {17,S}
5  C u0 p0 c0 {6,S} {9,S} {18,D}
6  C u0 p0 c0 {5,S} {8,S} {19,D}
7  C u0 p0 c0 {4,D} {20,S} {21,S}
8  O u0 p2 c0 {1,S} {6,S}
9  O u0 p2 c0 {2,S} {5,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 O u1 p2 c0 {4,S}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {6,D}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.60646,0.109998,-0.000109115,6.13298e-08,-1.47981e-11,-89788.2,40.5075], Tmin=(100,'K'), Tmax=(968.42,'K')),
            NASAPolynomial(coeffs=[12.0607,0.057677,-2.80738e-05,5.5403e-09,-3.9591e-13,-92241.6,-20.198], Tmin=(968.42,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 544,
    label = "CCOC1([O])CC(=O)COC1=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {8,S} {13,S} {14,S}
4  C u0 p0 c0 {6,S} {9,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {2,S} {4,S} {20,D}
7  C u0 p0 c0 {1,S} {9,S} {21,D}
8  O u0 p2 c0 {1,S} {3,S}
9  O u0 p2 c0 {4,S} {7,S}
10 O u1 p2 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.08731,0.0909997,-3.01802e-05,-3.21075e-08,1.9931e-11,-82719.5,34.4465], Tmin=(100,'K'), Tmax=(1002.36,'K')),
            NASAPolynomial(coeffs=[25.0022,0.0331683,-1.28959e-05,2.461e-09,-1.79839e-13,-90274.6,-103.079], Tmin=(1002.36,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 545,
    label = "CCOC(=O)C(=O)OC=C(C)[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {5,D} {18,S}
5  C u0 p0 c0 {4,D} {9,S} {21,S}
6  C u0 p0 c0 {7,S} {8,S} {20,D}
7  C u0 p0 c0 {6,S} {9,S} {19,D}
8  O u0 p2 c0 {1,S} {6,S}
9  O u0 p2 c0 {5,S} {7,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 O u1 p2 c0 {4,S}
19 O u0 p2 c0 {7,D}
20 O u0 p2 c0 {6,D}
21 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.35651,0.122593,-0.000130317,7.31261e-08,-1.67541e-11,-93626.5,39.4916], Tmin=(100,'K'), Tmax=(1044.47,'K')),
            NASAPolynomial(coeffs=[18.2047,0.0476803,-2.27321e-05,4.45673e-09,-3.17739e-13,-97712.7,-55.7309], Tmin=(1044.47,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 546,
    label = "CCOC(=O)C(=O)OCC(=O)CO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {8,S} {11,S} {12,S}
2  C u0 p0 c0 {5,S} {9,S} {16,S} {17,S}
3  C u0 p0 c0 {5,S} {10,S} {18,S} {19,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {2,S} {3,S} {20,D}
6  C u0 p0 c0 {7,S} {9,S} {21,D}
7  C u0 p0 c0 {6,S} {8,S} {22,D}
8  O u0 p2 c0 {1,S} {7,S}
9  O u0 p2 c0 {2,S} {6,S}
10 O u0 p2 c0 {3,S} {23,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 O u0 p2 c0 {5,D}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 O u1 p2 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.93392,0.143071,-0.000179558,1.30925e-07,-4.02502e-11,-98886.2,47.9077], Tmin=(100,'K'), Tmax=(780.12,'K')),
            NASAPolynomial(coeffs=[12.7921,0.0675647,-3.43752e-05,6.85607e-09,-4.90752e-13,-101184,-19.4804], Tmin=(780.12,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 547,
    label = "CCOC(=O)CC(=O)CO[C]=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {7,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {8,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {3,S} {19,D}
6  C u0 p0 c0 {1,S} {7,S} {20,D}
7  O u0 p2 c0 {2,S} {6,S}
8  O u0 p2 c0 {3,S} {9,S}
9  C u1 p0 c0 {8,S} {21,D}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 O u0 p2 c0 {5,D}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {9,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.683881,0.108997,-0.000105814,5.60807e-08,-1.24831e-11,-85461.2,41.8472], Tmin=(100,'K'), Tmax=(1055.59,'K')),
            NASAPolynomial(coeffs=[14.3892,0.0518801,-2.46494e-05,4.82072e-09,-3.42963e-13,-88643.4,-31.6873], Tmin=(1055.59,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 548,
    label = "C[CH]OC(=O)CC(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {10,S} {14,S} {15,S}
3  C u0 p0 c0 {6,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {2,S} {16,D}
5  C u0 p0 c0 {1,S} {7,S} {17,D}
6  C u1 p0 c0 {3,S} {7,S} {18,S}
7  O u0 p2 c0 {5,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 O u0 p2 c0 {4,D}
17 O u0 p2 c0 {5,D}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.441857,0.0799551,-6.33348e-05,2.6158e-08,-4.53138e-12,-50810.6,33.0855], Tmin=(100,'K'), Tmax=(1318.18,'K')),
            NASAPolynomial(coeffs=[13.3614,0.040751,-1.87233e-05,3.59595e-09,-2.52371e-13,-54216.7,-32.813], Tmin=(1318.18,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 549,
    label = "CCOC(=O)CC(=O)CO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {7,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {8,S} {16,S} {17,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {3,S} {18,D}
6  C u0 p0 c0 {1,S} {7,S} {19,D}
7  O u0 p2 c0 {2,S} {6,S}
8  O u0 p2 c0 {3,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {6,D}
20 O u1 p2 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.593518,0.109438,-0.000130164,9.29984e-08,-2.82477e-11,-64193.9,39.7077], Tmin=(100,'K'), Tmax=(787.74,'K')),
            NASAPolynomial(coeffs=[10.1484,0.0548975,-2.63197e-05,5.12287e-09,-3.6189e-13,-65886.5,-9.55397], Tmin=(787.74,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 550,
    label = "CC(=O)C(=O)CC(=O)OC=O",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {4,S} {14,D}
4  C u0 p0 c0 {2,S} {3,S} {13,D}
5  C u0 p0 c0 {1,S} {7,S} {15,D}
6  C u0 p0 c0 {7,S} {16,D} {17,S}
7  O u0 p2 c0 {5,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {4,D}
14 O u0 p2 c0 {3,D}
15 O u0 p2 c0 {5,D}
16 O u0 p2 c0 {6,D}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.168395,0.100128,-0.000132845,1.03639e-07,-3.3895e-11,-96875.8,38.96], Tmin=(100,'K'), Tmax=(737.58,'K')),
            NASAPolynomial(coeffs=[9.76287,0.0462652,-2.32963e-05,4.6146e-09,-3.28379e-13,-98340.7,-5.92895], Tmin=(737.58,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 551,
    label = "C=CC(C)(O)C(=O)OCC",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {9,S}
2  C u0 p0 c0 {4,S} {8,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {7,D} {18,S}
6  C u0 p0 c0 {1,S} {8,S} {19,D}
7  C u0 p0 c0 {5,D} {20,S} {21,S}
8  O u0 p2 c0 {2,S} {6,S}
9  O u0 p2 c0 {1,S} {22,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 O u0 p2 c0 {6,D}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.679435,0.104129,-9.36043e-05,4.6144e-08,-9.49073e-12,-70772.3,36.0626], Tmin=(100,'K'), Tmax=(1143.44,'K')),
            NASAPolynomial(coeffs=[15.065,0.0490508,-2.13491e-05,4.01578e-09,-2.79684e-13,-74372.8,-42.0052], Tmin=(1143.44,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 552,
    label = "CCOC(=O)C[C]C(C)O",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {7,S} {9,S} {10,S}
2  C u0 p0 c0 {5,S} {8,S} {11,S} {12,S}
3  C u0 p0 c0 {6,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {8,S} {21,D}
7  C u0 p1 c0 {1,S} {3,S}
8  O u0 p2 c0 {2,S} {6,S}
9  O u0 p2 c0 {1,S} {22,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {6,D}
22 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.351225,0.103559,-9.70417e-05,5.56068e-08,-1.41875e-11,-33343.5,47.8388], Tmin=(100,'K'), Tmax=(906.08,'K')),
            NASAPolynomial(coeffs=[8.94367,0.0625257,-2.91122e-05,5.62651e-09,-3.9731e-13,-35027.9,3.91293], Tmin=(906.08,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 553,
    label = "CC(=O)CC(=O)OC(C)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {5,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {4,S} {18,D}
6  C u0 p0 c0 {2,S} {7,S} {19,D}
7  O u0 p2 c0 {1,S} {6,S}
8  O u0 p2 c0 {1,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {6,D}
20 O u1 p2 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.270321,0.102438,-0.000110783,7.22955e-08,-2.04756e-11,-70817.7,39.7473], Tmin=(100,'K'), Tmax=(833.19,'K')),
            NASAPolynomial(coeffs=[9.41546,0.0559382,-2.70711e-05,5.31485e-09,-3.7817e-13,-72431.7,-5.21355], Tmin=(833.19,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 554,
    label = "C[C]C(C)(O)C(=O)OCC",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {7,S} {9,S}
2  C u0 p0 c0 {4,S} {8,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {7,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {1,S} {8,S} {21,D}
7  C u0 p1 c0 {1,S} {5,S}
8  O u0 p2 c0 {2,S} {6,S}
9  O u0 p2 c0 {1,S} {22,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {6,D}
22 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.663365,0.109088,-0.000107036,6.17307e-08,-1.53126e-11,-35494,46.7207], Tmin=(100,'K'), Tmax=(946.88,'K')),
            NASAPolynomial(coeffs=[11.3579,0.0583041,-2.65869e-05,5.08818e-09,-3.57328e-13,-37770.6,-10.6188], Tmin=(946.88,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 555,
    label = "C=COC(=O)[C]C",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {4,D} {6,S} {10,S}
3  C u0 p0 c0 {5,S} {6,S} {11,D}
4  C u0 p0 c0 {2,D} {12,S} {13,S}
5  C u0 p1 c0 {1,S} {3,S}
6  O u0 p2 c0 {2,S} {3,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.03837,0.0627021,-5.32051e-05,2.33447e-08,-4.18329e-12,6719.67,33.5758], Tmin=(100,'K'), Tmax=(1313.41,'K')),
            NASAPolynomial(coeffs=[13.0428,0.0261429,-1.14527e-05,2.15207e-09,-1.49445e-13,3566.28,-27.6116], Tmin=(1313.41,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 556,
    label = "CCOC(=O)C=CC(C)O",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {8,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {6,D} {19,S}
6  C u0 p0 c0 {5,D} {7,S} {20,S}
7  C u0 p0 c0 {6,S} {8,S} {21,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {1,S} {22,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.489743,0.0832274,-6.81405e-05,3.13146e-08,-6.28397e-12,-64700.9,35.2325], Tmin=(100,'K'), Tmax=(1126.69,'K')),
            NASAPolynomial(coeffs=[10.1151,0.0490563,-2.26489e-05,4.39804e-09,-3.11686e-13,-66869.9,-12.3529], Tmin=(1126.69,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 557,
    label = "CC(=O)CC([O])=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  C u0 p0 c0 {1,S} {11,S} {12,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 O u1 p2 c0 {4,S}
12 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.91915,0.0384603,-1.8834e-05,3.56944e-09,-2.25956e-13,-44200.9,19.2278], Tmin=(100,'K'), Tmax=(2592.28,'K')),
            NASAPolynomial(coeffs=[27.896,0.00634746,-3.97137e-06,7.03651e-10,-4.18215e-14,-59309.9,-129.228], Tmin=(2592.28,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 558,
    label = "CCOC(=O)C(O[O])C(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {7,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {4,S} {18,D}
6  C u0 p0 c0 {1,S} {7,S} {19,D}
7  O u0 p2 c0 {2,S} {6,S}
8  O u0 p2 c0 {1,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {6,D}
20 O u1 p2 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0783872,0.0976021,-9.62906e-05,5.6787e-08,-1.46904e-11,-68650.1,39.0957], Tmin=(100,'K'), Tmax=(900.53,'K')),
            NASAPolynomial(coeffs=[9.33964,0.0557689,-2.66096e-05,5.20184e-09,-3.69665e-13,-70346.3,-5.35413], Tmin=(900.53,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 559,
    label = "C=C([O])C(OO)C(=O)OCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {8,S} {10,S}
2  C u0 p0 c0 {3,S} {7,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,D} {16,S}
5  C u0 p0 c0 {1,S} {7,S} {17,D}
6  C u0 p0 c0 {4,D} {18,S} {19,S}
7  O u0 p2 c0 {2,S} {5,S}
8  O u0 p2 c0 {1,S} {9,S}
9  O u0 p2 c0 {8,S} {20,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u1 p2 c0 {4,S}
17 O u0 p2 c0 {5,D}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.846898,0.104822,-9.71547e-05,4.65642e-08,-9.06044e-12,-67317,41.7521], Tmin=(100,'K'), Tmax=(1221.9,'K')),
            NASAPolynomial(coeffs=[18.8053,0.0404877,-1.81783e-05,3.47452e-09,-2.44249e-13,-72119.5,-56.9969], Tmin=(1221.9,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 560,
    label = "CCOC(=O)C1OCC1=O",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
2  C u0 p0 c0 {4,S} {8,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {7,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {3,S} {17,D}
6  C u0 p0 c0 {1,S} {8,S} {18,D}
7  O u0 p2 c0 {1,S} {3,S}
8  O u0 p2 c0 {2,S} {6,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 O u0 p2 c0 {5,D}
18 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.410622,0.0640438,-1.02119e-05,-2.6982e-08,1.27587e-11,-71053.9,33.3096], Tmin=(100,'K'), Tmax=(1088.53,'K')),
            NASAPolynomial(coeffs=[16.2086,0.0372547,-1.63776e-05,3.17929e-09,-2.2822e-13,-76345.4,-52.7544], Tmin=(1088.53,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 561,
    label = "CCOC(=O)C(OO)C(=O)CO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {8,S} {11,S}
2  C u0 p0 c0 {4,S} {7,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {9,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {3,S} {19,D}
6  C u0 p0 c0 {1,S} {7,S} {20,D}
7  O u0 p2 c0 {2,S} {6,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {3,S} {21,S}
10 O u0 p2 c0 {8,S} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 O u0 p2 c0 {5,D}
20 O u0 p2 c0 {6,D}
21 O u1 p2 c0 {9,S}
22 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.67283,0.135392,-0.000169587,1.21521e-07,-3.62958e-11,-77465.4,47.549], Tmin=(100,'K'), Tmax=(805.9,'K')),
            NASAPolynomial(coeffs=[13.461,0.060276,-2.97735e-05,5.86172e-09,-4.16519e-13,-79904.6,-22.1971], Tmin=(805.9,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 562,
    label = "CCOC1=COCC(=O)O1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {7,S} {10,S} {11,S}
2  C u0 p0 c0 {5,S} {8,S} {15,S} {16,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {6,D} {7,S} {9,S}
5  C u0 p0 c0 {2,S} {9,S} {17,D}
6  C u0 p0 c0 {4,D} {8,S} {18,S}
7  O u0 p2 c0 {1,S} {4,S}
8  O u0 p2 c0 {2,S} {6,S}
9  O u0 p2 c0 {4,S} {5,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 O u0 p2 c0 {5,D}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.473217,0.0698236,2.28551e-05,-9.07528e-08,4.16174e-11,-76979.3,24.3744], Tmin=(100,'K'), Tmax=(980.85,'K')),
            NASAPolynomial(coeffs=[28.2052,0.0215098,-8.23003e-06,1.72261e-09,-1.38085e-13,-85906.9,-130.259], Tmin=(980.85,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 563,
    label = "CCOC(=O)C=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {5,S} {11,D}
4  C u0 p0 c0 {3,S} {12,D} {13,S}
5  O u0 p2 c0 {1,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.99095,0.0490985,-3.03635e-05,8.75208e-09,-1.03006e-12,-60274.2,21.1614], Tmin=(100,'K'), Tmax=(1808.03,'K')),
            NASAPolynomial(coeffs=[11.1075,0.0289294,-1.36306e-05,2.58224e-09,-1.76944e-13,-63570.8,-28.2199], Tmin=(1808.03,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 564,
    label = "CCOC(=O)C1O[C]=C(CO)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {6,S} {7,S} {9,S} {12,S}
2  C u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
3  C u0 p0 c0 {5,S} {11,S} {18,S} {19,S}
4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {7,S} {10,D}
6  C u0 p0 c0 {1,S} {8,S} {20,D}
7  O u0 p2 c0 {1,S} {5,S}
8  O u0 p2 c0 {2,S} {6,S}
9  O u0 p2 c0 {1,S} {10,S}
10 C u1 p0 c0 {5,D} {9,S}
11 O u0 p2 c0 {3,S} {21,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 O u0 p2 c0 {6,D}
21 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.944364,0.0828895,-2.45983e-07,-7.09057e-08,3.59174e-11,-78140.2,43.0574], Tmin=(100,'K'), Tmax=(966.1,'K')),
            NASAPolynomial(coeffs=[27.834,0.0260242,-8.66507e-06,1.64025e-09,-1.2509e-13,-86607.5,-109.833], Tmin=(966.1,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 565,
    label = "CCOC(=O)[C]1OC=C(CO)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {8,S} {12,S} {13,S}
2  C u0 p0 c0 {4,S} {11,S} {17,S} {18,S}
3  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {6,D} {9,S}
5  C u1 p0 c0 {7,S} {9,S} {10,S}
6  C u0 p0 c0 {4,D} {10,S} {20,S}
7  C u0 p0 c0 {5,S} {8,S} {19,D}
8  O u0 p2 c0 {1,S} {7,S}
9  O u0 p2 c0 {4,S} {5,S}
10 O u0 p2 c0 {5,S} {6,S}
11 O u0 p2 c0 {2,S} {21,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 O u0 p2 c0 {7,D}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.10806,0.0817671,1.64881e-05,-9.77598e-08,4.78027e-11,-82278.9,41.897], Tmin=(100,'K'), Tmax=(951.78,'K')),
            NASAPolynomial(coeffs=[31.649,0.019803,-5.16306e-06,9.72442e-10,-8.09406e-14,-91943.3,-132.531], Tmin=(951.78,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 566,
    label = "CCOC(=O)C1OC(CO)=C(O[O])O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {7,S} {8,S} {10,S} {13,S}
2  C u0 p0 c0 {4,S} {9,S} {14,S} {15,S}
3  C u0 p0 c0 {5,S} {11,S} {19,S} {20,S}
4  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {6,D} {8,S}
6  C u0 p0 c0 {5,D} {10,S} {12,S}
7  C u0 p0 c0 {1,S} {9,S} {21,D}
8  O u0 p2 c0 {1,S} {5,S}
9  O u0 p2 c0 {2,S} {7,S}
10 O u0 p2 c0 {1,S} {6,S}
11 O u0 p2 c0 {3,S} {22,S}
12 O u0 p2 c0 {6,S} {23,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {11,S}
23 O u1 p2 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.25841,0.120705,-9.75077e-05,3.28246e-08,-2.34478e-12,-92580.3,49.2394], Tmin=(100,'K'), Tmax=(1087.83,'K')),
            NASAPolynomial(coeffs=[27.4586,0.0359796,-1.4526e-05,2.71203e-09,-1.91276e-13,-100498,-103.305], Tmin=(1087.83,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 567,
    label = "CCOC(=O)C12O[CH]C1(CO)O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {11,S} {14,S} {15,S}
4  C u0 p0 c0 {5,S} {10,S} {12,S} {13,S}
5  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
6  C u1 p0 c0 {1,S} {9,S} {20,S}
7  C u0 p0 c0 {2,S} {10,S} {19,D}
8  O u0 p2 c0 {1,S} {2,S}
9  O u0 p2 c0 {2,S} {6,S}
10 O u0 p2 c0 {4,S} {7,S}
11 O u0 p2 c0 {3,S} {21,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u0 p2 c0 {7,D}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.1044,0.112537,-7.09307e-05,-6.74654e-09,1.51441e-11,-64514.7,38.885], Tmin=(100,'K'), Tmax=(976.53,'K')),
            NASAPolynomial(coeffs=[31.8778,0.0223444,-7.66196e-06,1.44755e-09,-1.09162e-13,-73488.2,-136.216], Tmin=(976.53,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 568,
    label = "CCOC(=O)C1(O[O])OC=C(CO)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {6,S} {8,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {9,S} {13,S} {14,S}
3  C u0 p0 c0 {5,S} {12,S} {18,S} {19,S}
4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {7,D} {8,S}
6  C u0 p0 c0 {1,S} {9,S} {20,D}
7  C u0 p0 c0 {5,D} {10,S} {21,S}
8  O u0 p2 c0 {1,S} {5,S}
9  O u0 p2 c0 {2,S} {6,S}
10 O u0 p2 c0 {1,S} {7,S}
11 O u0 p2 c0 {1,S} {22,S}
12 O u0 p2 c0 {3,S} {23,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 O u0 p2 c0 {6,D}
21 H u0 p0 c0 {7,S}
22 O u1 p2 c0 {11,S}
23 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.18133,0.112191,-5.27508e-05,-2.89888e-08,2.37341e-11,-101745,47.7455], Tmin=(100,'K'), Tmax=(960.44,'K')),
            NASAPolynomial(coeffs=[31.6151,0.0277559,-8.8392e-06,1.58554e-09,-1.16742e-13,-110834,-127.461], Tmin=(960.44,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 569,
    label = "CCOC(=O)C1(OO)O[CH]C(=CO)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {8,S} {9,S} {11,S}
2  C u0 p0 c0 {3,S} {10,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
4  C u0 p0 c0 {6,S} {7,D} {8,S}
5  C u0 p0 c0 {1,S} {10,S} {19,D}
6  C u1 p0 c0 {4,S} {9,S} {20,S}
7  C u0 p0 c0 {4,D} {12,S} {21,S}
8  O u0 p2 c0 {1,S} {4,S}
9  O u0 p2 c0 {1,S} {6,S}
10 O u0 p2 c0 {2,S} {5,S}
11 O u0 p2 c0 {1,S} {13,S}
12 O u0 p2 c0 {7,S} {22,S}
13 O u0 p2 c0 {11,S} {23,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 O u0 p2 c0 {5,D}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {12,S}
23 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.33277,0.116913,-6.61596e-05,-1.13261e-08,1.59437e-11,-106432,48.1685], Tmin=(100,'K'), Tmax=(988.97,'K')),
            NASAPolynomial(coeffs=[30.7912,0.0320102,-1.18133e-05,2.21094e-09,-1.61259e-13,-115383,-123.401], Tmin=(988.97,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 570,
    label = "CCOC(=O)C1O[C](CO)C(=O)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {6,S} {8,S} {10,S} {12,S}
2  C u0 p0 c0 {4,S} {9,S} {13,S} {14,S}
3  C u0 p0 c0 {5,S} {11,S} {18,S} {19,S}
4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
5  C u1 p0 c0 {3,S} {7,S} {8,S}
6  C u0 p0 c0 {1,S} {9,S} {20,D}
7  C u0 p0 c0 {5,S} {10,S} {21,D}
8  O u0 p2 c0 {1,S} {5,S}
9  O u0 p2 c0 {2,S} {6,S}
10 O u0 p2 c0 {1,S} {7,S}
11 O u0 p2 c0 {3,S} {22,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.09961,0.0964491,-6.40926e-05,2.02609e-08,-2.53742e-12,-112586,48.5809], Tmin=(100,'K'), Tmax=(1859.95,'K')),
            NASAPolynomial(coeffs=[27.1109,0.0357784,-1.51624e-05,2.72232e-09,-1.79983e-13,-123080,-105.024], Tmin=(1859.95,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 571,
    label = "CCOC(=O)C1OC(=O)C(=CO)O1",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {8,S} {10,S} {12,S}
2  C u0 p0 c0 {3,S} {9,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {6,S} {7,D} {8,S}
5  C u0 p0 c0 {1,S} {9,S} {18,D}
6  C u0 p0 c0 {4,S} {10,S} {19,D}
7  C u0 p0 c0 {4,D} {11,S} {20,S}
8  O u0 p2 c0 {1,S} {4,S}
9  O u0 p2 c0 {2,S} {5,S}
10 O u0 p2 c0 {1,S} {6,S}
11 O u0 p2 c0 {7,S} {21,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {6,D}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.46384,0.0950217,-2.62042e-05,-4.90271e-08,2.91334e-11,-118967,42.4576], Tmin=(100,'K'), Tmax=(970.84,'K')),
            NASAPolynomial(coeffs=[30.2153,0.0238975,-8.08699e-06,1.5518e-09,-1.19208e-13,-127918,-123.855], Tmin=(970.84,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 572,
    label = "CCOC(=O)C1OC(=O)C(CO)(O[O])O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {8,S} {11,S}
2  C u0 p0 c0 {7,S} {8,S} {10,S} {13,S}
3  C u0 p0 c0 {1,S} {12,S} {16,S} {17,S}
4  C u0 p0 c0 {5,S} {9,S} {14,S} {15,S}
5  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {1,S} {10,S} {22,D}
7  C u0 p0 c0 {2,S} {9,S} {21,D}
8  O u0 p2 c0 {1,S} {2,S}
9  O u0 p2 c0 {4,S} {7,S}
10 O u0 p2 c0 {2,S} {6,S}
11 O u0 p2 c0 {1,S} {23,S}
12 O u0 p2 c0 {3,S} {24,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {7,D}
22 O u0 p2 c0 {6,D}
23 O u1 p2 c0 {11,S}
24 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.43416,0.117383,-5.86269e-05,-1.8714e-08,1.77333e-11,-132996,52.4415], Tmin=(100,'K'), Tmax=(1007.69,'K')),
            NASAPolynomial(coeffs=[31.1012,0.0358947,-1.41814e-05,2.72625e-09,-1.99977e-13,-142376,-122.611], Tmin=(1007.69,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 573,
    label = "[O]CC(O)C(=O)O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,D}
4  O u0 p2 c0 {1,S} {11,S}
5  O u0 p2 c0 {3,S} {12,S}
6  H u0 p0 c0 {1,S}
7  O u1 p2 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.96252,0.0486721,-3.73778e-05,1.52496e-08,-2.70103e-12,-68847.7,26.39], Tmin=(100,'K'), Tmax=(1249.91,'K')),
            NASAPolynomial(coeffs=[8.08835,0.029068,-1.38513e-05,2.70123e-09,-1.9119e-13,-70379,-4.53006], Tmin=(1249.91,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 574,
    label = "O=C(O)C(O)COO",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {7,S}
2  O u0 p2 c0 {6,S} {12,S}
3  O u0 p2 c0 {8,S} {13,S}
4  O u0 p2 c0 {1,S} {14,S}
5  O u0 p2 c0 {8,D}
6  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
7  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
8  C u0 p0 c0 {3,S} {5,D} {6,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.686975,0.0711217,-6.5832e-05,3.08862e-08,-5.84707e-12,-87343,30.8711], Tmin=(100,'K'), Tmax=(1256.88,'K')),
            NASAPolynomial(coeffs=[14.8711,0.0259808,-1.19595e-05,2.31145e-09,-1.63405e-13,-90908.5,-40.8022], Tmin=(1256.88,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 575,
    label = "CCOC(=O)C(O)CO[O]",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {8,S} {10,S}
2  O u0 p2 c0 {6,S} {19,S}
3  O u0 p2 c0 {5,S} {7,S}
4  O u0 p2 c0 {10,D}
5  O u1 p2 c0 {3,S}
6  C u0 p0 c0 {2,S} {7,S} {10,S} {11,S}
7  C u0 p0 c0 {3,S} {6,S} {14,S} {15,S}
8  C u0 p0 c0 {1,S} {9,S} {12,S} {13,S}
9  C u0 p0 c0 {8,S} {16,S} {17,S} {18,S}
10 C u0 p0 c0 {1,S} {4,D} {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.0102624,0.092066,-8.60511e-05,4.45573e-08,-9.7477e-12,-71434.4,38.5382], Tmin=(100,'K'), Tmax=(1070.14,'K')),
            NASAPolynomial(coeffs=[12.417,0.0456904,-2.10455e-05,4.05962e-09,-2.86633e-13,-74089.7,-22.1581], Tmin=(1070.14,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 576,
    label = "CCOC(=O)C(O)CC(=O)[C]=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {7,S} {19,D}
6  C u0 p0 c0 {2,S} {9,S} {18,D}
7  O u0 p2 c0 {3,S} {5,S}
8  O u0 p2 c0 {1,S} {20,S}
9  C u1 p0 c0 {6,S} {21,D}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u0 p2 c0 {6,D}
19 O u0 p2 c0 {5,D}
20 H u0 p0 c0 {8,S}
21 O u0 p2 c0 {9,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.819796,0.11416,-0.000123239,7.50948e-08,-1.92761e-11,-85635.1,44.8391], Tmin=(100,'K'), Tmax=(924.76,'K')),
            NASAPolynomial(coeffs=[13.0103,0.0543399,-2.62095e-05,5.14665e-09,-3.66605e-13,-88193.1,-20.8015], Tmin=(924.76,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 577,
    label = "CCOC(=O)[CH]O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {5,S} {12,D}
4  C u1 p0 c0 {3,S} {6,S} {13,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {4,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {3,D}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.50179,0.0571159,-4.26076e-05,1.70626e-08,-2.94034e-12,-56470.9,24.5252], Tmin=(100,'K'), Tmax=(1297.09,'K')),
            NASAPolynomial(coeffs=[9.26705,0.0331696,-1.49156e-05,2.82995e-09,-1.9719e-13,-58485.4,-14.9578], Tmin=(1297.09,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 578,
    label = "CCOC(=O)C(O)O[O]",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,S} {9,S}
2  O u0 p2 c0 {5,S} {7,S}
3  O u0 p2 c0 {7,S} {16,S}
4  O u0 p2 c0 {9,D}
5  O u1 p2 c0 {2,S}
6  C u0 p0 c0 {1,S} {8,S} {10,S} {11,S}
7  C u0 p0 c0 {2,S} {3,S} {9,S} {12,S}
8  C u0 p0 c0 {6,S} {13,S} {14,S} {15,S}
9  C u0 p0 c0 {1,S} {4,D} {7,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.591173,0.0814643,-9.04111e-05,6.00229e-08,-1.71274e-11,-72032.2,33.4434], Tmin=(100,'K'), Tmax=(831.2,'K')),
            NASAPolynomial(coeffs=[8.62853,0.0427842,-2.0605e-05,4.03217e-09,-2.86246e-13,-73368.2,-3.84587], Tmin=(831.2,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 579,
    label = "CCOC(=O)C(O)C[C]=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {8,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {6,S} {17,D}
6  O u0 p2 c0 {3,S} {5,S}
7  O u0 p2 c0 {1,S} {19,S}
8  C u1 p0 c0 {2,S} {18,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u0 p2 c0 {5,D}
18 O u0 p2 c0 {8,D}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.132877,0.0888113,-7.95209e-05,3.91335e-08,-8.15095e-12,-72677.3,38.9658], Tmin=(100,'K'), Tmax=(1116.95,'K')),
            NASAPolynomial(coeffs=[12.383,0.0449404,-2.06038e-05,3.96737e-09,-2.79782e-13,-75413.8,-21.4888], Tmin=(1116.95,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 580,
    label = "CCOC(=O)C([O])(C=O)OC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {7,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {7,S} {15,D}
5  C u0 p0 c0 {1,S} {16,D} {17,S}
6  C u0 p0 c0 {8,S} {18,D} {19,S}
7  O u0 p2 c0 {2,S} {4,S}
8  O u0 p2 c0 {1,S} {6,S}
9  O u1 p2 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {4,D}
16 O u0 p2 c0 {5,D}
17 H u0 p0 c0 {5,S}
18 O u0 p2 c0 {6,D}
19 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.21404,0.0981306,-6.79889e-05,1.02284e-08,4.58102e-12,-103241,44.35], Tmin=(100,'K'), Tmax=(1046.77,'K')),
            NASAPolynomial(coeffs=[25.003,0.0284364,-1.18081e-05,2.2732e-09,-1.64568e-13,-110400,-91.309], Tmin=(1046.77,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 581,
    label = "CCOC(=O)C(C=O)(OO)OC(=O)C=O",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {8,S} {10,S}
2  C u0 p0 c0 {3,S} {9,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {9,S} {17,D}
5  C u0 p0 c0 {1,S} {18,D} {20,S}
6  C u0 p0 c0 {7,S} {8,S} {19,D}
7  C u0 p0 c0 {6,S} {21,D} {22,S}
8  O u0 p2 c0 {1,S} {6,S}
9  O u0 p2 c0 {2,S} {4,S}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {10,S} {23,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 O u0 p2 c0 {4,D}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {6,D}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.82916,0.142809,-0.000139535,6.68104e-08,-1.26611e-11,-135221,52.5794], Tmin=(100,'K'), Tmax=(1271.54,'K')),
            NASAPolynomial(coeffs=[29.5613,0.0409153,-1.93338e-05,3.78897e-09,-2.70275e-13,-143458,-111.467], Tmin=(1271.54,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 582,
    label = "CC(OO)OC(=O)C1OOC(C)([O])C1OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {16,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {15,S}
3  C u0 p0 c0 {1,S} {7,S} {10,S} {17,S}
4  C u0 p0 c0 {6,S} {8,S} {12,S} {18,S}
5  C u0 p0 c0 {2,S} {22,S} {23,S} {24,S}
6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {3,S} {8,S} {25,D}
8  O u0 p2 c0 {4,S} {7,S}
9  O u0 p2 c0 {2,S} {10,S}
10 O u0 p2 c0 {3,S} {9,S}
11 O u0 p2 c0 {1,S} {14,S}
12 O u0 p2 c0 {4,S} {13,S}
13 O u0 p2 c0 {12,S} {26,S}
14 O u0 p2 c0 {11,S} {27,S}
15 O u1 p2 c0 {2,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 O u0 p2 c0 {7,D}
26 H u0 p0 c0 {13,S}
27 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.02374,0.155833,-0.000127781,3.90721e-08,1.84314e-13,-92654.6,57.8731], Tmin=(100,'K'), Tmax=(1010.44,'K')),
            NASAPolynomial(coeffs=[34.5823,0.0416054,-1.5512e-05,2.80612e-09,-1.96762e-13,-102427,-138.531], Tmin=(1010.44,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 583,
    label = "O=COC(=O)C=O",
    molecule = 
"""
1 O u0 p2 c0 {5,S} {7,S}
2 O u0 p2 c0 {5,D}
3 O u0 p2 c0 {6,D}
4 O u0 p2 c0 {7,D}
5 C u0 p0 c0 {1,S} {2,D} {6,S}
6 C u0 p0 c0 {3,D} {5,S} {8,S}
7 C u0 p0 c0 {1,S} {4,D} {9,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.00325,0.0488849,-6.48966e-05,5.04931e-08,-1.66949e-11,-69543,22.7574], Tmin=(100,'K'), Tmax=(725.07,'K')),
            NASAPolynomial(coeffs=[6.56525,0.0237181,-1.28333e-05,2.62419e-09,-1.90303e-13,-70204.6,2.21492], Tmin=(725.07,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 584,
    label = "CCOC(=O)C(=O)OC=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {6,S} {14,D}
4  C u0 p0 c0 {3,S} {7,S} {13,D}
5  C u0 p0 c0 {7,S} {15,D} {16,S}
6  O u0 p2 c0 {1,S} {3,S}
7  O u0 p2 c0 {4,S} {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {4,D}
14 O u0 p2 c0 {3,D}
15 O u0 p2 c0 {5,D}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.334252,0.0891962,-0.000110164,8.24901e-08,-2.66582e-11,-103038,34.0686], Tmin=(100,'K'), Tmax=(737.43,'K')),
            NASAPolynomial(coeffs=[8.11206,0.0470057,-2.43406e-05,4.89919e-09,-3.52629e-13,-104185,-1.08549], Tmin=(737.43,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 585,
    label = "CCOC(=O)C(=O)[CH]O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {5,S} {13,D}
4  C u0 p0 c0 {3,S} {6,S} {14,D}
5  C u1 p0 c0 {3,S} {7,S} {15,S}
6  O u0 p2 c0 {1,S} {4,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {3,D}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.360134,0.087404,-0.000100712,6.839e-08,-1.98307e-11,-68626.5,30.6165], Tmin=(100,'K'), Tmax=(820.52,'K')),
            NASAPolynomial(coeffs=[9.2075,0.0442714,-2.18572e-05,4.31786e-09,-3.07984e-13,-70078.3,-10.3163], Tmin=(820.52,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 586,
    label = "C[CH]OC(=O)C(O)(C=O)OC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {7,S} {9,S}
2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {8,S} {13,D}
4  C u1 p0 c0 {2,S} {8,S} {14,S}
5  C u0 p0 c0 {1,S} {15,D} {16,S}
6  C u0 p0 c0 {7,S} {17,D} {18,S}
7  O u0 p2 c0 {1,S} {6,S}
8  O u0 p2 c0 {3,S} {4,S}
9  O u0 p2 c0 {1,S} {19,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {3,D}
14 H u0 p0 c0 {4,S}
15 O u0 p2 c0 {5,D}
16 H u0 p0 c0 {5,S}
17 O u0 p2 c0 {6,D}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.66039,0.104427,-6.96314e-05,1.0097e-09,1.01693e-11,-109709,45.7781], Tmin=(100,'K'), Tmax=(1009.94,'K')),
            NASAPolynomial(coeffs=[29.7099,0.0218562,-8.89223e-06,1.77415e-09,-1.34033e-13,-118171,-116.398], Tmin=(1009.94,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 587,
    label = "CCOC(=O)C1OOC(=O)C1=O",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {8,S} {10,S}
2  C u0 p0 c0 {3,S} {7,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {16,D}
5  C u0 p0 c0 {1,S} {7,S} {17,D}
6  C u0 p0 c0 {4,S} {9,S} {18,D}
7  O u0 p2 c0 {2,S} {5,S}
8  O u0 p2 c0 {1,S} {9,S}
9  O u0 p2 c0 {6,S} {8,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u0 p2 c0 {4,D}
17 O u0 p2 c0 {5,D}
18 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0638818,0.0655639,1.91864e-05,-7.27459e-08,3.15733e-11,-102195,38.0642], Tmin=(100,'K'), Tmax=(1017.05,'K')),
            NASAPolynomial(coeffs=[22.4139,0.0327055,-1.42728e-05,2.88409e-09,-2.1653e-13,-109640,-84.8811], Tmin=(1017.05,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 588,
    label = "CCOC(=O)C([O])=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {5,S} {11,D}
4  C u0 p0 c0 {3,S} {12,S} {13,D}
5  O u0 p2 c0 {1,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 O u1 p2 c0 {4,S}
13 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.27212,0.0669677,-7.51739e-05,5.12096e-08,-1.538e-11,-59945.7,25.7168], Tmin=(100,'K'), Tmax=(781.94,'K')),
            NASAPolynomial(coeffs=[6.91526,0.0381025,-1.9806e-05,4.00773e-09,-2.89902e-13,-60828.3,-0.12042], Tmin=(781.94,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 589,
    label = "O=COC(=O)C(=O)O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,D}
2  C u0 p0 c0 {1,S} {5,S} {7,D}
3  C u0 p0 c0 {4,S} {8,D} {9,S}
4  O u0 p2 c0 {1,S} {3,S}
5  O u0 p2 c0 {2,S} {10,S}
6  O u0 p2 c0 {1,D}
7  O u0 p2 c0 {2,D}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.4384,0.062747,-8.81287e-05,7.00517e-08,-2.32821e-11,-100683,25.6271], Tmin=(100,'K'), Tmax=(725.45,'K')),
            NASAPolynomial(coeffs=[7.82206,0.0275471,-1.53436e-05,3.16155e-09,-2.2987e-13,-101609,-3.12119], Tmin=(725.45,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 590,
    label = "CCOC(=O)C(=O)OC1OCC1=O",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {8,S} {10,S} {13,S}
2  C u0 p0 c0 {4,S} {9,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {8,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {3,S} {19,D}
6  C u0 p0 c0 {7,S} {9,S} {21,D}
7  C u0 p0 c0 {6,S} {10,S} {20,D}
8  O u0 p2 c0 {1,S} {3,S}
9  O u0 p2 c0 {2,S} {6,S}
10 O u0 p2 c0 {1,S} {7,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 O u0 p2 c0 {5,D}
20 O u0 p2 c0 {7,D}
21 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.79493,0.0998946,-7.05573e-05,2.31386e-08,-3.01886e-12,-109664,41.6825], Tmin=(100,'K'), Tmax=(1757.77,'K')),
            NASAPolynomial(coeffs=[25.575,0.0398873,-1.93501e-05,3.71749e-09,-2.56698e-13,-118935,-100.411], Tmin=(1757.77,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 591,
    label = "CCOC(=O)C(=O)OC(=O)C=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {7,S} {15,D}
4  C u0 p0 c0 {3,S} {8,S} {14,D}
5  C u0 p0 c0 {6,S} {8,S} {16,D}
6  C u0 p0 c0 {5,S} {17,D} {18,S}
7  O u0 p2 c0 {1,S} {3,S}
8  O u0 p2 c0 {4,S} {5,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 O u0 p2 c0 {4,D}
15 O u0 p2 c0 {3,D}
16 O u0 p2 c0 {5,D}
17 O u0 p2 c0 {6,D}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.131183,0.103315,-8.23633e-05,-6.24507e-08,1.12634e-10,-114357,37.5013], Tmin=(100,'K'), Tmax=(469.38,'K')),
            NASAPolynomial(coeffs=[9.53445,0.0549056,-2.90424e-05,5.80804e-09,-4.12967e-13,-115589,-4.47464], Tmin=(469.38,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 592,
    label = "CCOC(=O)C1OOC(=O)C1[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {7,S} {18,D}
6  C u0 p0 c0 {2,S} {9,S} {19,D}
7  O u0 p2 c0 {3,S} {5,S}
8  O u0 p2 c0 {1,S} {9,S}
9  O u0 p2 c0 {6,S} {8,S}
10 H u0 p0 c0 {1,S}
11 O u1 p2 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.18048,0.0504451,8.10182e-05,-1.48274e-07,6.12269e-11,-84099.1,43.0611], Tmin=(100,'K'), Tmax=(970.9,'K')),
            NASAPolynomial(coeffs=[26.3627,0.0257198,-9.23383e-06,1.8981e-09,-1.5241e-13,-93101.9,-102.661], Tmin=(970.9,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 593,
    label = "[CH2]C(OO)C(=O)OOC(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {8,S} {15,D}
4  C u0 p0 c0 {2,S} {7,S} {14,D}
5  C u1 p0 c0 {1,S} {16,S} {17,S}
6  O u0 p2 c0 {1,S} {9,S}
7  O u0 p2 c0 {4,S} {8,S}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {6,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 O u0 p2 c0 {4,D}
15 O u0 p2 c0 {3,D}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.887775,0.081941,-9.5275e-06,-5.90643e-08,3.09044e-11,-75427.4,45.1506], Tmin=(100,'K'), Tmax=(985.44,'K')),
            NASAPolynomial(coeffs=[28.7606,0.021385,-8.36089e-06,1.71552e-09,-1.3466e-13,-84173.8,-112.181], Tmin=(985.44,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 594,
    label = "CCOC(=O)C([O])(C=O)OC(=O)C=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {8,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {8,S} {16,D}
5  C u0 p0 c0 {1,S} {17,D} {19,S}
6  C u0 p0 c0 {7,S} {9,S} {18,D}
7  C u0 p0 c0 {6,S} {20,D} {21,S}
8  O u0 p2 c0 {2,S} {4,S}
9  O u0 p2 c0 {1,S} {6,S}
10 O u1 p2 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u0 p2 c0 {4,D}
17 O u0 p2 c0 {5,D}
18 O u0 p2 c0 {6,D}
19 H u0 p0 c0 {5,S}
20 O u0 p2 c0 {7,D}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.08586,0.125003,-0.000119408,5.61299e-08,-1.04315e-11,-114533,49.9301], Tmin=(100,'K'), Tmax=(1297.72,'K')),
            NASAPolynomial(coeffs=[26.8742,0.0357409,-1.6234e-05,3.12832e-09,-2.21154e-13,-122049,-97.3333], Tmin=(1297.72,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 595,
    label = "CCOC(=O)C(C=O)(O[C]=O)OC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {7,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {7,S} {16,D}
5  C u0 p0 c0 {1,S} {17,D} {18,S}
6  C u0 p0 c0 {8,S} {19,D} {20,S}
7  O u0 p2 c0 {2,S} {4,S}
8  O u0 p2 c0 {1,S} {6,S}
9  O u0 p2 c0 {1,S} {10,S}
10 C u1 p0 c0 {9,S} {21,D}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u0 p2 c0 {4,D}
17 O u0 p2 c0 {5,D}
18 H u0 p0 c0 {5,S}
19 O u0 p2 c0 {6,D}
20 H u0 p0 c0 {6,S}
21 O u0 p2 c0 {10,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.23838,0.118618,-9.37122e-05,2.82417e-08,-9.06236e-13,-127056,49.5883], Tmin=(100,'K'), Tmax=(1107.36,'K')),
            NASAPolynomial(coeffs=[29.1398,0.0326528,-1.43521e-05,2.79145e-09,-2.01136e-13,-135684,-112.573], Tmin=(1107.36,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 596,
    label = "CC(=O)OOC(=O)C1CO1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {8,S} {16,D}
5  C u0 p0 c0 {3,S} {7,S} {15,D}
6  O u0 p2 c0 {1,S} {2,S}
7  O u0 p2 c0 {5,S} {8,S}
8  O u0 p2 c0 {4,S} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {5,D}
16 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.487094,0.0455675,7.80756e-05,-1.5325e-07,6.79266e-11,-87004.8,34.4996], Tmin=(100,'K'), Tmax=(919.89,'K')),
            NASAPolynomial(coeffs=[27.3497,0.0108246,9.11803e-07,-3.48794e-10,1.64298e-14,-95419.2,-111.727], Tmin=(919.89,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 597,
    label = "CCOC(=O)C1(OO)OC=C(C=O)O1",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {8,S} {9,S} {11,S}
2  C u0 p0 c0 {3,S} {10,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {6,D} {7,S} {8,S}
5  C u0 p0 c0 {1,S} {10,S} {18,D}
6  C u0 p0 c0 {4,D} {9,S} {19,S}
7  C u0 p0 c0 {4,S} {20,D} {21,S}
8  O u0 p2 c0 {1,S} {4,S}
9  O u0 p2 c0 {1,S} {6,S}
10 O u0 p2 c0 {2,S} {5,S}
11 O u0 p2 c0 {1,S} {12,S}
12 O u0 p2 c0 {11,S} {22,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 O u0 p2 c0 {5,D}
19 H u0 p0 c0 {6,S}
20 O u0 p2 c0 {7,D}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.41782,0.114899,-5.60314e-05,-2.71658e-08,2.24871e-11,-111155,43.9634], Tmin=(100,'K'), Tmax=(988.31,'K')),
            NASAPolynomial(coeffs=[34.3049,0.0252762,-9.56229e-06,1.89759e-09,-1.45559e-13,-121295,-147.35], Tmin=(988.31,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 598,
    label = "CCOC(=O)C1(OO)OC(=CO)C(O[O])O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {6,S} {8,S} {9,S} {11,S}
2  C u0 p0 c0 {5,S} {8,S} {12,S} {17,S}
3  C u0 p0 c0 {4,S} {10,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {2,S} {7,D} {9,S}
6  C u0 p0 c0 {1,S} {10,S} {21,D}
7  C u0 p0 c0 {5,D} {13,S} {22,S}
8  O u0 p2 c0 {1,S} {2,S}
9  O u0 p2 c0 {1,S} {5,S}
10 O u0 p2 c0 {3,S} {6,S}
11 O u0 p2 c0 {1,S} {14,S}
12 O u0 p2 c0 {2,S} {23,S}
13 O u0 p2 c0 {7,S} {24,S}
14 O u0 p2 c0 {11,S} {25,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {6,D}
22 H u0 p0 c0 {7,S}
23 O u1 p2 c0 {12,S}
24 H u0 p0 c0 {13,S}
25 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.8641,0.153377,-0.00014093,5.54976e-08,-5.96561e-12,-117727,55.6661], Tmin=(100,'K'), Tmax=(1039.8,'K')),
            NASAPolynomial(coeffs=[35.523,0.0332227,-1.28418e-05,2.38206e-09,-1.69427e-13,-127614,-144.044], Tmin=(1039.8,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 599,
    label = "CCOC(=O)C1(OO)OC=C(C(O)O[O])O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {6,S} {8,S} {9,S} {11,S}
2  C u0 p0 c0 {5,S} {12,S} {13,S} {17,S}
3  C u0 p0 c0 {4,S} {10,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {2,S} {7,D} {8,S}
6  C u0 p0 c0 {1,S} {10,S} {21,D}
7  C u0 p0 c0 {5,D} {9,S} {22,S}
8  O u0 p2 c0 {1,S} {5,S}
9  O u0 p2 c0 {1,S} {7,S}
10 O u0 p2 c0 {3,S} {6,S}
11 O u0 p2 c0 {1,S} {14,S}
12 O u0 p2 c0 {2,S} {24,S}
13 O u0 p2 c0 {2,S} {23,S}
14 O u0 p2 c0 {11,S} {25,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {6,D}
22 H u0 p0 c0 {7,S}
23 O u1 p2 c0 {13,S}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.7821,0.150084,-0.000128456,4.00587e-08,1.24076e-13,-117977,56.362], Tmin=(100,'K'), Tmax=(1010.92,'K')),
            NASAPolynomial(coeffs=[36.1875,0.0317654,-1.19989e-05,2.23563e-09,-1.61086e-13,-128093,-146.97], Tmin=(1010.92,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 600,
    label = "CCOC(=O)C1([O])OC=C(C=O)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {8,S} {10,S} {11,S}
2  C u0 p0 c0 {3,S} {9,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {6,D} {7,S} {8,S}
5  C u0 p0 c0 {1,S} {9,S} {17,D}
6  C u0 p0 c0 {4,D} {10,S} {18,S}
7  C u0 p0 c0 {4,S} {19,D} {20,S}
8  O u0 p2 c0 {1,S} {4,S}
9  O u0 p2 c0 {2,S} {5,S}
10 O u0 p2 c0 {1,S} {6,S}
11 O u1 p2 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 O u0 p2 c0 {5,D}
18 H u0 p0 c0 {6,S}
19 O u0 p2 c0 {7,D}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.46008,0.094588,-2.72382e-05,-4.89835e-08,2.94397e-11,-90475.7,40.5431], Tmin=(100,'K'), Tmax=(969.56,'K')),
            NASAPolynomial(coeffs=[30.9742,0.0211616,-7.05936e-06,1.37542e-09,-1.07768e-13,-99603.3,-129.568], Tmin=(969.56,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 601,
    label = "C[C]=COC(=O)C(=O)OCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {8,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {5,S} {7,S} {19,D}
5  C u0 p0 c0 {4,S} {9,S} {18,D}
6  C u0 p0 c0 {8,D} {9,S} {20,S}
7  O u0 p2 c0 {1,S} {4,S}
8  C u1 p0 c0 {3,S} {6,D}
9  O u0 p2 c0 {5,S} {6,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {4,D}
20 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.636572,0.11084,-0.000118539,7.09832e-08,-1.79814e-11,-55818.9,35.8371], Tmin=(100,'K'), Tmax=(933.14,'K')),
            NASAPolynomial(coeffs=[12.7085,0.0536334,-2.65784e-05,5.28208e-09,-3.78786e-13,-58309.4,-27.6215], Tmin=(933.14,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 602,
    label = "CCOC(=O)C(=O)OC(O[O])C(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {9,S} {10,S} {13,S}
2  C u0 p0 c0 {3,S} {8,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {4,S} {20,D}
6  C u0 p0 c0 {7,S} {8,S} {22,D}
7  C u0 p0 c0 {6,S} {9,S} {21,D}
8  O u0 p2 c0 {2,S} {6,S}
9  O u0 p2 c0 {1,S} {7,S}
10 O u0 p2 c0 {1,S} {23,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {5,D}
21 O u0 p2 c0 {7,D}
22 O u0 p2 c0 {6,D}
23 O u1 p2 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.7605,0.139299,-0.000178751,1.39222e-07,-4.63807e-11,-107239,49.1699], Tmin=(100,'K'), Tmax=(719.35,'K')),
            NASAPolynomial(coeffs=[10.5194,0.0710149,-3.63645e-05,7.26273e-09,-5.19734e-13,-109006,-6.02824], Tmin=(719.35,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 603,
    label = "CCOC(=O)C(=O)OC([O])C(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {8,S} {10,S} {11,S}
2  C u0 p0 c0 {5,S} {9,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {2,S} {4,S} {20,D}
6  C u0 p0 c0 {7,S} {9,S} {21,D}
7  C u0 p0 c0 {6,S} {8,S} {22,D}
8  O u0 p2 c0 {1,S} {7,S}
9  O u0 p2 c0 {2,S} {6,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 O u1 p2 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {5,D}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.00913,0.121711,-0.000141172,1.00939e-07,-3.15837e-11,-104833,45.7428], Tmin=(100,'K'), Tmax=(756.25,'K')),
            NASAPolynomial(coeffs=[9.15879,0.0679294,-3.44958e-05,6.89826e-09,-4.95264e-13,-106371,-0.470663], Tmin=(756.25,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 604,
    label = "C=C([O])C(OO)OC(=O)C(=O)OCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {8,S} {10,S} {14,S}
2  C u0 p0 c0 {3,S} {9,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {1,S} {7,D} {18,S}
5  C u0 p0 c0 {6,S} {8,S} {19,D}
6  C u0 p0 c0 {5,S} {9,S} {20,D}
7  C u0 p0 c0 {4,D} {21,S} {22,S}
8  O u0 p2 c0 {1,S} {5,S}
9  O u0 p2 c0 {2,S} {6,S}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {10,S} {23,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 O u1 p2 c0 {4,S}
19 O u0 p2 c0 {5,D}
20 O u0 p2 c0 {6,D}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.09878,0.146444,-0.000179067,1.22201e-07,-3.47347e-11,-106025,48.7467], Tmin=(100,'K'), Tmax=(843.94,'K')),
            NASAPolynomial(coeffs=[15.2836,0.0640572,-3.26345e-05,6.52747e-09,-4.6861e-13,-108959,-32.164], Tmin=(843.94,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 605,
    label = "CCOC(=O)C(=O)OC(OO)C(=O)CO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {8,S} {10,S} {15,S}
2  C u0 p0 c0 {4,S} {9,S} {13,S} {14,S}
3  C u0 p0 c0 {5,S} {11,S} {19,S} {20,S}
4  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {3,S} {21,D}
6  C u0 p0 c0 {7,S} {8,S} {22,D}
7  C u0 p0 c0 {6,S} {9,S} {23,D}
8  O u0 p2 c0 {1,S} {6,S}
9  O u0 p2 c0 {2,S} {7,S}
10 O u0 p2 c0 {1,S} {12,S}
11 O u0 p2 c0 {3,S} {24,S}
12 O u0 p2 c0 {10,S} {25,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 O u0 p2 c0 {5,D}
22 O u0 p2 c0 {6,D}
23 O u0 p2 c0 {7,D}
24 O u1 p2 c0 {11,S}
25 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.37108,0.177478,-0.000254439,2.08711e-07,-7.08521e-11,-116054,57.6693], Tmin=(100,'K'), Tmax=(714.47,'K')),
            NASAPolynomial(coeffs=[14.9415,0.0749475,-3.91689e-05,7.83263e-09,-5.58798e-13,-118671,-24.5206], Tmin=(714.47,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 606,
    label = "O=C1CC(C(=O)OC(COO)OO)OO1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {8,S} {14,S}
2  C u0 p0 c0 {4,S} {7,S} {9,S} {15,S}
3  C u0 p0 c0 {1,S} {6,S} {16,S} {17,S}
4  C u0 p0 c0 {2,S} {10,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {7,S} {20,D}
6  C u0 p0 c0 {3,S} {11,S} {21,D}
7  O u0 p2 c0 {2,S} {5,S}
8  O u0 p2 c0 {1,S} {11,S}
9  O u0 p2 c0 {2,S} {12,S}
10 O u0 p2 c0 {4,S} {13,S}
11 O u0 p2 c0 {6,S} {8,S}
12 O u0 p2 c0 {9,S} {22,S}
13 O u0 p2 c0 {10,S} {23,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {5,D}
21 O u0 p2 c0 {6,D}
22 H u0 p0 c0 {12,S}
23 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.49339,0.120257,-7.28813e-05,3.81259e-09,7.11856e-12,-119001,55.158], Tmin=(100,'K'), Tmax=(1101.75,'K')),
            NASAPolynomial(coeffs=[30.2814,0.0408966,-1.87914e-05,3.73222e-09,-2.71723e-13,-128628,-117.053], Tmin=(1101.75,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 607,
    label = "[O]CC(OO)OC(=O)C1CC(=O)OO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {8,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
3  C u0 p0 c0 {4,S} {7,S} {9,S} {13,S}
4  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {7,S} {19,D}
6  C u0 p0 c0 {2,S} {10,S} {20,D}
7  O u0 p2 c0 {3,S} {5,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {3,S} {11,S}
10 O u0 p2 c0 {6,S} {8,S}
11 O u0 p2 c0 {9,S} {21,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 O u1 p2 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {5,D}
20 O u0 p2 c0 {6,D}
21 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.4227,0.100107,-5.19109e-05,-2.93508e-09,6.82885e-12,-100497,51.4194], Tmin=(100,'K'), Tmax=(1142.44,'K')),
            NASAPolynomial(coeffs=[24.7644,0.041938,-1.95465e-05,3.86085e-09,-2.783e-13,-108668,-87.9791], Tmin=(1142.44,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 608,
    label = "CC(=O)CC(=O)C(=O)OC=O",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {13,D}
4  C u0 p0 c0 {1,S} {5,S} {14,D}
5  C u0 p0 c0 {4,S} {7,S} {15,D}
6  C u0 p0 c0 {7,S} {16,D} {17,S}
7  O u0 p2 c0 {5,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {3,D}
14 O u0 p2 c0 {4,D}
15 O u0 p2 c0 {5,D}
16 O u0 p2 c0 {6,D}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.116967,0.098339,-0.000111508,4.41622e-08,1.31958e-11,-95098.2,37.3313], Tmin=(100,'K'), Tmax=(539.96,'K')),
            NASAPolynomial(coeffs=[9.76939,0.0468416,-2.40285e-05,4.77571e-09,-3.39629e-13,-96432.3,-5.98838], Tmin=(539.96,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 609,
    label = "CC(=O)C([O])C1OC(C)OC1=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {8,S} {9,S} {13,S}
4  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {2,S} {5,S} {20,D}
7  C u0 p0 c0 {1,S} {9,S} {21,D}
8  O u0 p2 c0 {1,S} {3,S}
9  O u0 p2 c0 {3,S} {7,S}
10 H u0 p0 c0 {1,S}
11 O u1 p2 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0486057,0.0642601,3.17546e-05,-8.65093e-08,3.66274e-11,-81571.7,44.18], Tmin=(100,'K'), Tmax=(1003.48,'K')),
            NASAPolynomial(coeffs=[21.6551,0.0366063,-1.48928e-05,2.9339e-09,-2.18381e-13,-88891.1,-75.3697], Tmin=(1003.48,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 610,
    label = "CCOC(=O)C(=O)C1OCC1=O",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {6,S} {8,S} {10,S}
2  C u0 p0 c0 {4,S} {9,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {8,S} {16,S} {17,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {3,S} {18,D}
6  C u0 p0 c0 {1,S} {7,S} {19,D}
7  C u0 p0 c0 {6,S} {9,S} {20,D}
8  O u0 p2 c0 {1,S} {3,S}
9  O u0 p2 c0 {2,S} {7,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {6,D}
20 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.713914,0.0942292,-6.803e-05,2.33467e-08,-3.19233e-12,-83211,39.3282], Tmin=(100,'K'), Tmax=(1698.23,'K')),
            NASAPolynomial(coeffs=[24.0632,0.0358697,-1.6483e-05,3.11127e-09,-2.13447e-13,-91626.5,-93.329], Tmin=(1698.23,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 611,
    label = "CCOC1=C([O])C(OO)C(=O)CO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {10,S} {12,S}
2  C u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
3  C u0 p0 c0 {5,S} {9,S} {18,S} {19,S}
4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {3,S} {20,D}
6  C u0 p0 c0 {1,S} {7,D} {21,S}
7  C u0 p0 c0 {6,D} {8,S} {9,S}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {3,S} {7,S}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {10,S} {22,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 O u0 p2 c0 {5,D}
21 O u1 p2 c0 {6,S}
22 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.43138,0.116805,-6.50605e-05,-1.2675e-08,1.56911e-11,-74554,39.4417], Tmin=(100,'K'), Tmax=(1019.49,'K')),
            NASAPolynomial(coeffs=[32.9519,0.0295101,-1.24434e-05,2.49855e-09,-1.87975e-13,-84446.6,-145.079], Tmin=(1019.49,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 612,
    label = "CCOC(=O)C(=O)C(OO)C(=O)CO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {9,S} {12,S}
2  C u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
3  C u0 p0 c0 {5,S} {10,S} {18,S} {19,S}
4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {3,S} {20,D}
6  C u0 p0 c0 {1,S} {7,S} {21,D}
7  C u0 p0 c0 {6,S} {8,S} {22,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {1,S} {11,S}
10 O u0 p2 c0 {3,S} {23,S}
11 O u0 p2 c0 {9,S} {24,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 O u0 p2 c0 {5,D}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 O u1 p2 c0 {10,S}
24 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.69366,0.163773,-0.000217188,1.49496e-07,-3.59908e-11,-89626.9,53.2261], Tmin=(100,'K'), Tmax=(613.55,'K')),
            NASAPolynomial(coeffs=[15.1437,0.0683574,-3.49478e-05,6.92761e-09,-4.92019e-13,-92208.6,-27.317], Tmin=(613.55,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 613,
    label = "CCOC(=O)C(O)C[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {6,S} {17,D}
6  O u0 p2 c0 {2,S} {5,S}
7  O u0 p2 c0 {1,S} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u1 p2 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u0 p2 c0 {5,D}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.939522,0.0741906,-5.63152e-05,2.39107e-08,-4.56951e-12,-71206.1,34.5394], Tmin=(100,'K'), Tmax=(1142.76,'K')),
            NASAPolynomial(coeffs=[8.19266,0.0488023,-2.29898e-05,4.46915e-09,-3.16259e-13,-72863.8,-1.42063], Tmin=(1142.76,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 614,
    label = "CCOC(=O)C(O)COO",
    molecule = 
"""
1  O u0 p2 c0 {8,S} {10,S}
2  O u0 p2 c0 {4,S} {7,S}
3  O u0 p2 c0 {6,S} {19,S}
4  O u0 p2 c0 {2,S} {20,S}
5  O u0 p2 c0 {10,D}
6  C u0 p0 c0 {3,S} {7,S} {10,S} {11,S}
7  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
8  C u0 p0 c0 {1,S} {9,S} {12,S} {13,S}
9  C u0 p0 c0 {8,S} {16,S} {17,S} {18,S}
10 C u0 p0 c0 {1,S} {5,D} {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.284318,0.0961367,-8.34253e-05,3.82548e-08,-7.30737e-12,-89703.9,38.8269], Tmin=(100,'K'), Tmax=(1218.55,'K')),
            NASAPolynomial(coeffs=[15.2029,0.0452986,-2.08452e-05,4.01744e-09,-2.83197e-13,-93478.3,-38.9514], Tmin=(1218.55,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 615,
    label = "CCOC1=C([O])CC(=O)CO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {12,S} {13,S}
2  C u0 p0 c0 {4,S} {8,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {9,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {3,S} {19,D}
6  C u0 p0 c0 {1,S} {7,D} {20,S}
7  C u0 p0 c0 {6,D} {8,S} {9,S}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {3,S} {7,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 O u0 p2 c0 {5,D}
20 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.954457,0.0813313,3.51642e-06,-6.97992e-08,3.28562e-11,-61892.5,29.4827], Tmin=(100,'K'), Tmax=(1014.9,'K')),
            NASAPolynomial(coeffs=[28.498,0.0288356,-1.28728e-05,2.69804e-09,-2.08284e-13,-71145.4,-129.177], Tmin=(1014.9,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 616,
    label = "CCOC(=O)C1([O])CC(=O)COO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {8,S} {14,S} {15,S}
4  C u0 p0 c0 {6,S} {10,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {2,S} {4,S} {21,D}
7  C u0 p0 c0 {1,S} {8,S} {22,D}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {4,S} {9,S}
11 O u1 p2 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.96025,0.105162,-3.9302e-05,-3.22211e-08,2.04633e-11,-76553.4,41.2508], Tmin=(100,'K'), Tmax=(1040.08,'K')),
            NASAPolynomial(coeffs=[30.9366,0.0335638,-1.52463e-05,3.12651e-09,-2.35516e-13,-86367,-133.03], Tmin=(1040.08,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 617,
    label = "C=C([O])C(O)C(=O)C(=O)OCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {8,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {17,D}
5  C u0 p0 c0 {1,S} {7,D} {16,S}
6  C u0 p0 c0 {4,S} {8,S} {18,D}
7  C u0 p0 c0 {5,D} {19,S} {20,S}
8  O u0 p2 c0 {2,S} {6,S}
9  O u0 p2 c0 {1,S} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u1 p2 c0 {5,S}
17 O u0 p2 c0 {4,D}
18 O u0 p2 c0 {6,D}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.13928,0.1164,-0.000119018,6.42675e-08,-1.41842e-11,-88102.9,44.0152], Tmin=(100,'K'), Tmax=(1081.46,'K')),
            NASAPolynomial(coeffs=[17.8543,0.0461482,-2.15768e-05,4.19966e-09,-2.98329e-13,-92211,-49.105], Tmin=(1081.46,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 618,
    label = "CCOC1=C([O])C(O)C(=O)CO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {8,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {9,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {3,S} {19,D}
6  C u0 p0 c0 {1,S} {7,D} {20,S}
7  C u0 p0 c0 {6,D} {8,S} {9,S}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {3,S} {7,S}
10 O u0 p2 c0 {1,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 O u0 p2 c0 {5,D}
20 O u1 p2 c0 {6,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.68112,0.0990468,-3.12857e-05,-4.39628e-08,2.6676e-11,-83179.6,35.9844], Tmin=(100,'K'), Tmax=(990.3,'K')),
            NASAPolynomial(coeffs=[31.1014,0.0257921,-9.93547e-06,1.98775e-09,-1.52641e-13,-92573.4,-136.499], Tmin=(990.3,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 619,
    label = "CCOC(=O)C(=O)C(O)C(=O)CO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {9,S} {11,S}
2  C u0 p0 c0 {4,S} {8,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {10,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {3,S} {19,D}
6  C u0 p0 c0 {1,S} {7,S} {20,D}
7  C u0 p0 c0 {6,S} {8,S} {21,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {1,S} {23,S}
10 O u0 p2 c0 {3,S} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 O u0 p2 c0 {5,D}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
22 O u1 p2 c0 {10,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.37125,0.152094,-0.000210961,1.66946e-07,-5.44379e-11,-98234.2,51.2461], Tmin=(100,'K'), Tmax=(744.31,'K')),
            NASAPolynomial(coeffs=[14.195,0.0630556,-3.15036e-05,6.19141e-09,-4.37712e-13,-100700,-23.7828], Tmin=(744.31,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 620,
    label = "CCOC(=O)C(=O)C(O)=C([O])COO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {8,S} {12,S} {13,S}
2  C u0 p0 c0 {5,S} {9,S} {17,S} {18,S}
3  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {5,D} {6,S} {10,S}
5  C u0 p0 c0 {2,S} {4,D} {19,S}
6  C u0 p0 c0 {4,S} {7,S} {20,D}
7  C u0 p0 c0 {6,S} {8,S} {21,D}
8  O u0 p2 c0 {1,S} {7,S}
9  O u0 p2 c0 {2,S} {11,S}
10 O u0 p2 c0 {4,S} {22,S}
11 O u0 p2 c0 {9,S} {23,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 O u1 p2 c0 {5,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.89158,0.159361,-0.00020459,1.37323e-07,-3.68464e-11,-103492,48.9933], Tmin=(100,'K'), Tmax=(908.5,'K')),
            NASAPolynomial(coeffs=[21.9865,0.0498249,-2.37349e-05,4.60803e-09,-3.25411e-13,-108012,-68.6414], Tmin=(908.5,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 621,
    label = "CCOC(=O)C(=O)C1(O)OCC1=O",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {6,S} {8,S} {10,S}
2  C u0 p0 c0 {4,S} {9,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {8,S} {16,S} {17,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {3,S} {18,D}
6  C u0 p0 c0 {1,S} {7,S} {19,D}
7  C u0 p0 c0 {6,S} {9,S} {20,D}
8  O u0 p2 c0 {1,S} {3,S}
9  O u0 p2 c0 {2,S} {7,S}
10 O u0 p2 c0 {1,S} {21,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {6,D}
20 O u0 p2 c0 {7,D}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.01916,0.109797,-6.3447e-05,-1.00042e-08,1.44695e-11,-108669,43.8168], Tmin=(100,'K'), Tmax=(1009.6,'K')),
            NASAPolynomial(coeffs=[31.0925,0.0264616,-1.07284e-05,2.13049e-09,-1.60214e-13,-117794,-128.322], Tmin=(1009.6,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 622,
    label = "CCOC(=O)C(=O)C(O)(O[O])C(=O)COO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
3  C u0 p0 c0 {5,S} {9,S} {18,S} {19,S}
4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {3,S} {20,D}
6  C u0 p0 c0 {1,S} {7,S} {21,D}
7  C u0 p0 c0 {6,S} {8,S} {22,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {3,S} {12,S}
10 O u0 p2 c0 {1,S} {24,S}
11 O u0 p2 c0 {1,S} {23,S}
12 O u0 p2 c0 {9,S} {25,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 O u0 p2 c0 {5,D}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 O u1 p2 c0 {11,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.01614,0.180158,-0.000219365,1.33589e-07,-3.21059e-11,-115085,57.7429], Tmin=(100,'K'), Tmax=(1015.52,'K')),
            NASAPolynomial(coeffs=[29.7942,0.0469873,-2.26687e-05,4.46579e-09,-3.19498e-13,-121952,-105.894], Tmin=(1015.52,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 623,
    label = "CCOC(=O)C(=O)C(O)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {7,S} {8,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {5,S} {15,D}
5  C u0 p0 c0 {4,S} {6,S} {16,D}
6  O u0 p2 c0 {1,S} {5,S}
7  O u0 p2 c0 {2,S} {18,S}
8  O u0 p2 c0 {2,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {4,D}
16 O u0 p2 c0 {5,D}
17 O u1 p2 c0 {8,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.27177,0.107225,-0.000123682,5.70496e-08,5.87971e-12,-84200.5,38.5936], Tmin=(100,'K'), Tmax=(554.49,'K')),
            NASAPolynomial(coeffs=[10.3566,0.0507856,-2.57321e-05,5.08677e-09,-3.60799e-13,-85690.2,-9.2189], Tmin=(554.49,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 624,
    label = "CC(OO)OC(=O)C1OOC(=O)C1OO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {9,S} {14,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {15,S}
3  C u0 p0 c0 {4,S} {7,S} {10,S} {16,S}
4  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {2,S} {7,S} {21,D}
6  C u0 p0 c0 {1,S} {11,S} {20,D}
7  O u0 p2 c0 {3,S} {5,S}
8  O u0 p2 c0 {2,S} {11,S}
9  O u0 p2 c0 {1,S} {12,S}
10 O u0 p2 c0 {3,S} {13,S}
11 O u0 p2 c0 {6,S} {8,S}
12 O u0 p2 c0 {9,S} {22,S}
13 O u0 p2 c0 {10,S} {23,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {5,D}
22 H u0 p0 c0 {12,S}
23 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.16026,0.102944,-6.8995e-06,-7.53849e-08,3.73894e-11,-120213,55.3695], Tmin=(100,'K'), Tmax=(1008.11,'K')),
            NASAPolynomial(coeffs=[34.0743,0.0336605,-1.46437e-05,3.0311e-09,-2.33158e-13,-131304,-138.507], Tmin=(1008.11,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 625,
    label = "CC(OO)OC(=O)C(C=C([O])COO)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {7,S} {9,S} {15,S}
2  C u0 p0 c0 {4,S} {8,S} {10,S} {16,S}
3  C u0 p0 c0 {6,S} {11,S} {20,S} {21,S}
4  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {6,D} {23,S}
6  C u0 p0 c0 {3,S} {5,D} {22,S}
7  C u0 p0 c0 {1,S} {8,S} {24,D}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {1,S} {12,S}
10 O u0 p2 c0 {2,S} {13,S}
11 O u0 p2 c0 {3,S} {14,S}
12 O u0 p2 c0 {9,S} {26,S}
13 O u0 p2 c0 {10,S} {27,S}
14 O u0 p2 c0 {11,S} {25,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 O u1 p2 c0 {6,S}
23 H u0 p0 c0 {5,S}
24 O u0 p2 c0 {7,D}
25 H u0 p0 c0 {14,S}
26 H u0 p0 c0 {12,S}
27 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.51516,0.17669,-0.000211,1.34389e-07,-3.49227e-11,-96864.8,61.6114], Tmin=(100,'K'), Tmax=(927.35,'K')),
            NASAPolynomial(coeffs=[21.9585,0.0668088,-3.32596e-05,6.6071e-09,-4.73339e-13,-101589,-59.362], Tmin=(927.35,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 626,
    label = "CCOC(=O)C1([O])OOCC(=O)C1OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {10,S} {14,S}
2  C u0 p0 c0 {1,S} {7,S} {9,S} {13,S}
3  C u0 p0 c0 {5,S} {8,S} {15,S} {16,S}
4  C u0 p0 c0 {6,S} {11,S} {20,S} {21,S}
5  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {1,S} {4,S} {22,D}
7  C u0 p0 c0 {2,S} {8,S} {23,D}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {2,S} {11,S}
10 O u0 p2 c0 {1,S} {12,S}
11 O u0 p2 c0 {4,S} {9,S}
12 O u0 p2 c0 {10,S} {24,S}
13 O u1 p2 c0 {2,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 O u0 p2 c0 {6,D}
23 O u0 p2 c0 {7,D}
24 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.16053,0.125927,-5.39619e-05,-3.5662e-08,2.49313e-11,-88337.1,50.4404], Tmin=(100,'K'), Tmax=(1025.17,'K')),
            NASAPolynomial(coeffs=[38.5762,0.0309005,-1.41573e-05,2.98618e-09,-2.30731e-13,-100458,-169.335], Tmin=(1025.17,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 627,
    label = "CC(=O)CC1([O])OOC(C)OC1=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {4,S} {8,S} {10,S} {12,S}
4  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {2,S} {5,S} {21,D}
7  C u0 p0 c0 {1,S} {8,S} {22,D}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {3,S} {9,S}
11 O u1 p2 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.76215,0.0997238,-2.5811e-05,-4.46153e-08,2.43573e-11,-83171.9,41.0402], Tmin=(100,'K'), Tmax=(1038.7,'K')),
            NASAPolynomial(coeffs=[30.5196,0.0340571,-1.56779e-05,3.24224e-09,-2.45428e-13,-93041.9,-131.156], Tmin=(1038.7,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 628,
    label = "CC(=O)CC(=O)OOC(C)O[C]=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {7,S} {8,S} {11,S}
2  C u0 p0 c0 {5,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {2,S} {4,S} {20,D}
6  C u0 p0 c0 {2,S} {9,S} {21,D}
7  O u0 p2 c0 {1,S} {9,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {6,S} {7,S}
10 C u1 p0 c0 {8,S} {22,D}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {5,D}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {10,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.52332,0.118291,-0.000102291,4.42331e-08,-7.75158e-12,-93066.9,46.8773], Tmin=(100,'K'), Tmax=(1342.08,'K')),
            NASAPolynomial(coeffs=[22.6576,0.0462208,-2.17408e-05,4.22051e-09,-2.98116e-13,-99557.5,-76.8964], Tmin=(1342.08,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 629,
    label = "C[CH]OOC(=O)CC(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {2,S} {17,D}
5  C u0 p0 c0 {1,S} {7,S} {18,D}
6  C u1 p0 c0 {3,S} {8,S} {19,S}
7  O u0 p2 c0 {5,S} {8,S}
8  O u0 p2 c0 {6,S} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 O u0 p2 c0 {4,D}
18 O u0 p2 c0 {5,D}
19 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.407433,0.0916188,-7.29737e-05,2.92745e-08,-4.77211e-12,-52060,37.6748], Tmin=(100,'K'), Tmax=(1433.2,'K')),
            NASAPolynomial(coeffs=[18.7964,0.0380217,-1.68784e-05,3.18114e-09,-2.20514e-13,-57564.6,-61.8841], Tmin=(1433.2,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 630,
    label = "CCC(=O)OC(C)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {6,S} {7,S} {10,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {6,S} {17,D}
6  O u0 p2 c0 {1,S} {5,S}
7  O u0 p2 c0 {1,S} {18,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u0 p2 c0 {5,D}
18 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.496437,0.084269,-8.64227e-05,5.69571e-08,-1.68919e-11,-55882.1,32.4497], Tmin=(100,'K'), Tmax=(786.84,'K')),
            NASAPolynomial(coeffs=[6.83825,0.0520297,-2.4963e-05,4.88408e-09,-3.469e-13,-56880.1,3.37443], Tmin=(786.84,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 631,
    label = "CC1OOC(C)([O])CC(=O)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {7,S} {9,S} {11,S}
4  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
6  C u0 p0 c0 {2,S} {7,S} {20,D}
7  O u0 p2 c0 {3,S} {6,S}
8  O u0 p2 c0 {1,S} {9,S}
9  O u0 p2 c0 {3,S} {8,S}
10 O u1 p2 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.440574,0.0441258,0.000154529,-2.68941e-07,1.16531e-10,-65233.9,35.4916], Tmin=(100,'K'), Tmax=(922.53,'K')),
            NASAPolynomial(coeffs=[42.9493,-0.0055735,1.02509e-05,-2.02044e-09,1.18378e-13,-79130.5,-202.268], Tmin=(922.53,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 632,
    label = "[CH2]C(=O)OC(C)OOC(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {9,S} {17,D}
5  C u0 p0 c0 {6,S} {7,S} {18,D}
6  C u1 p0 c0 {5,S} {19,S} {20,S}
7  O u0 p2 c0 {1,S} {5,S}
8  O u0 p2 c0 {1,S} {9,S}
9  O u0 p2 c0 {4,S} {8,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 O u0 p2 c0 {4,D}
18 O u0 p2 c0 {5,D}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.960478,0.093653,-6.03184e-05,1.2406e-08,1.03859e-12,-79956,44.0147], Tmin=(100,'K'), Tmax=(1190.39,'K')),
            NASAPolynomial(coeffs=[22.1679,0.0375005,-1.67347e-05,3.2157e-09,-2.27415e-13,-86990.3,-78.0149], Tmin=(1190.39,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 633,
    label = "CC(=O)OOC(C)OC(=O)CO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {11,S}
2  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {5,S} {10,S} {15,S} {16,S}
4  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {7,S} {21,D}
6  C u0 p0 c0 {4,S} {9,S} {20,D}
7  O u0 p2 c0 {1,S} {5,S}
8  O u0 p2 c0 {1,S} {9,S}
9  O u0 p2 c0 {6,S} {8,S}
10 O u0 p2 c0 {3,S} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {5,D}
22 O u1 p2 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.57703,0.116265,-9.70291e-05,4.0062e-08,-6.66569e-12,-95978.1,48.3735], Tmin=(100,'K'), Tmax=(1413.9,'K')),
            NASAPolynomial(coeffs=[23.9635,0.0440095,-2.03728e-05,3.91772e-09,-2.74787e-13,-103200,-83.6909], Tmin=(1413.9,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 634,
    label = "CC(=O)OC(=O)CO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {13,D}
4  C u0 p0 c0 {2,S} {5,S} {12,D}
5  O u0 p2 c0 {3,S} {4,S}
6  O u0 p2 c0 {1,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {4,D}
13 O u0 p2 c0 {3,D}
14 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.896686,0.0759188,-9.09315e-05,5.44578e-08,-8.75763e-12,-62217,32.4252], Tmin=(100,'K'), Tmax=(603.71,'K')),
            NASAPolynomial(coeffs=[8.75924,0.0349711,-1.68889e-05,3.28e-09,-2.30677e-13,-63369.5,-3.2216], Tmin=(603.71,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 635,
    label = "C[C]1OCC(=O)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u1 p0 c0 {2,S} {5,S} {6,S}
4  C u0 p0 c0 {1,S} {6,S} {12,D}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {3,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.50967,0.0138836,7.49729e-05,-1.04505e-07,3.96525e-11,-40428.6,21.4303], Tmin=(100,'K'), Tmax=(979.3,'K')),
            NASAPolynomial(coeffs=[12.6293,0.0202374,-7.80307e-06,1.57115e-09,-1.21222e-13,-44697.3,-38.8543], Tmin=(979.3,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 636,
    label = "C=C([O])COOC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {10,S} {11,S}
4  C u0 p0 c0 {6,S} {12,D} {13,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {4,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u1 p2 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.733729,0.057889,-2.10124e-05,-2.06106e-08,1.3302e-11,-45832.1,29.7586], Tmin=(100,'K'), Tmax=(996.37,'K')),
            NASAPolynomial(coeffs=[18.6651,0.017154,-6.73566e-06,1.31682e-09,-9.85087e-14,-50956.6,-64.4692], Tmin=(996.37,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 637,
    label = "[O]OCC(=O)COO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {11,D}
4  O u0 p2 c0 {1,S} {6,S}
5  O u0 p2 c0 {2,S} {12,S}
6  O u0 p2 c0 {4,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 O u1 p2 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.50903,0.065698,-4.81242e-05,7.24585e-09,3.80232e-12,-25887.3,37.6448], Tmin=(100,'K'), Tmax=(1010.6,'K')),
            NASAPolynomial(coeffs=[19.013,0.014776,-5.66756e-06,1.09003e-09,-8.0462e-14,-30767,-57.46], Tmin=(1010.6,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 638,
    label = "O=C1CC(=O)C(=O)C1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  C u0 p0 c0 {1,S} {5,S} {11,D}
5  C u0 p0 c0 {2,S} {4,S} {12,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 O u0 p2 c0 {4,D}
12 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.82092,0.0370851,5.03067e-06,-3.09675e-08,1.36035e-11,-46660.6,22.6221], Tmin=(100,'K'), Tmax=(1024.54,'K')),
            NASAPolynomial(coeffs=[12.0325,0.0219495,-9.01956e-06,1.73645e-09,-1.25873e-13,-50051.1,-33.2253], Tmin=(1024.54,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 639,
    label = "[O]OCC(=O)COOC=O",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {7,S}
2  O u0 p2 c0 {1,S} {10,S}
3  O u0 p2 c0 {6,S} {8,S}
4  O u0 p2 c0 {9,D}
5  O u0 p2 c0 {10,D}
6  O u1 p2 c0 {3,S}
7  C u0 p0 c0 {1,S} {9,S} {11,S} {12,S}
8  C u0 p0 c0 {3,S} {9,S} {13,S} {14,S}
9  C u0 p0 c0 {4,D} {7,S} {8,S}
10 C u0 p0 c0 {2,S} {5,D} {15,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.420236,0.0889102,-8.40019e-05,3.82942e-08,-6.85636e-12,-54937.9,36.5348], Tmin=(100,'K'), Tmax=(1349.37,'K')),
            NASAPolynomial(coeffs=[21.8207,0.0229812,-1.07143e-05,2.08642e-09,-1.48168e-13,-60940.2,-77.4295], Tmin=(1349.37,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 640,
    label = "[O]OC(=O)C1CC(=O)CO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {3,S} {13,D}
5  C u0 p0 c0 {1,S} {7,S} {14,D}
6  O u0 p2 c0 {1,S} {3,S}
7  O u0 p2 c0 {5,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 O u0 p2 c0 {5,D}
15 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.430227,0.0662538,-3.44378e-05,-9.52015e-09,1.02792e-11,-48940.6,32.2011], Tmin=(100,'K'), Tmax=(972.5,'K')),
            NASAPolynomial(coeffs=[18.3355,0.0205566,-7.06259e-06,1.26527e-09,-9.01682e-14,-53744.8,-60.4774], Tmin=(972.5,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 641,
    label = "CCOC(=O)C1=C(O)OCC(=O)O1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {9,S} {12,S} {13,S}
2  C u0 p0 c0 {6,S} {8,S} {17,S} {18,S}
3  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {5,D} {7,S} {10,S}
5  C u0 p0 c0 {4,D} {8,S} {11,S}
6  C u0 p0 c0 {2,S} {10,S} {19,D}
7  C u0 p0 c0 {4,S} {9,S} {20,D}
8  O u0 p2 c0 {2,S} {5,S}
9  O u0 p2 c0 {1,S} {7,S}
10 O u0 p2 c0 {4,S} {6,S}
11 O u0 p2 c0 {5,S} {21,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 O u0 p2 c0 {6,D}
20 O u0 p2 c0 {7,D}
21 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.08163,0.118028,-0.000101435,4.17182e-08,-6.73823e-12,-112389,36.5973], Tmin=(100,'K'), Tmax=(1486.55,'K')),
            NASAPolynomial(coeffs=[29.8562,0.032091,-1.47221e-05,2.83126e-09,-1.98554e-13,-121885,-130.147], Tmin=(1486.55,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 642,
    label = "C=C1CCC(=O)O[CH]CO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {6,S} {8,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {7,D} {8,S}
5  C u0 p0 c0 {2,S} {9,S} {16,D}
6  C u1 p0 c0 {3,S} {9,S} {17,S}
7  C u0 p0 c0 {4,D} {18,S} {19,S}
8  O u0 p2 c0 {3,S} {4,S}
9  O u0 p2 c0 {5,S} {6,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u0 p2 c0 {5,D}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.480017,0.0515999,5.34729e-05,-1.06359e-07,4.35753e-11,-37009,28.5108], Tmin=(100,'K'), Tmax=(989.1,'K')),
            NASAPolynomial(coeffs=[20.7938,0.032336,-1.26826e-05,2.5115e-09,-1.89798e-13,-44103.6,-84.8189], Tmin=(989.1,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 643,
    label = "O=C1CC[CH]OC(=O)CC1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {4,S} {5,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {2,S} {17,D}
6  C u1 p0 c0 {4,S} {8,S} {19,S}
7  C u0 p0 c0 {3,S} {8,S} {18,D}
8  O u0 p2 c0 {6,S} {7,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u0 p2 c0 {5,D}
18 O u0 p2 c0 {7,D}
19 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.642261,0.0625992,-1.13797e-05,-1.68519e-08,7.10749e-12,-43938,29.6048], Tmin=(100,'K'), Tmax=(1238.26,'K')),
            NASAPolynomial(coeffs=[13.2003,0.0461953,-2.07788e-05,3.96751e-09,-2.77586e-13,-48900.5,-41.1439], Tmin=(1238.26,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 644,
    label = "C=COC(=O)CCC(=O)CO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {9,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {3,S} {16,D}
5  C u0 p0 c0 {2,S} {8,S} {17,D}
6  C u0 p0 c0 {7,D} {8,S} {18,S}
7  C u0 p0 c0 {6,D} {19,S} {20,S}
8  O u0 p2 c0 {5,S} {6,S}
9  O u0 p2 c0 {3,S} {21,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u0 p2 c0 {4,D}
17 O u0 p2 c0 {5,D}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 O u1 p2 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.71717,0.135349,-0.000183744,1.4023e-07,-4.37658e-11,-54969.5,42.6624], Tmin=(100,'K'), Tmax=(778.75,'K')),
            NASAPolynomial(coeffs=[14.2462,0.0533489,-2.57897e-05,5.00204e-09,-3.51225e-13,-57455.6,-30.3587], Tmin=(778.75,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 645,
    label = "O=[C]CCC(=O)CCC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {2,S} {16,D}
6  C u0 p0 c0 {3,S} {17,D} {18,S}
7  C u1 p0 c0 {4,S} {19,D}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u0 p2 c0 {5,D}
17 O u0 p2 c0 {6,D}
18 H u0 p0 c0 {6,S}
19 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.654562,0.118945,-0.000198792,1.89892e-07,-6.98168e-11,-40357.2,38.3887], Tmin=(100,'K'), Tmax=(846.63,'K')),
            NASAPolynomial(coeffs=[4.16605,0.0597271,-2.93094e-05,5.59464e-09,-3.83626e-13,-39867.4,23.6479], Tmin=(846.63,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 646,
    label = "CCOC(=O)C1OOC([O])(COO)C1OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {16,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {15,S}
3  C u0 p0 c0 {1,S} {7,S} {10,S} {17,S}
4  C u0 p0 c0 {2,S} {12,S} {20,S} {21,S}
5  C u0 p0 c0 {6,S} {8,S} {18,S} {19,S}
6  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
7  C u0 p0 c0 {3,S} {8,S} {25,D}
8  O u0 p2 c0 {5,S} {7,S}
9  O u0 p2 c0 {2,S} {10,S}
10 O u0 p2 c0 {3,S} {9,S}
11 O u0 p2 c0 {1,S} {13,S}
12 O u0 p2 c0 {4,S} {14,S}
13 O u0 p2 c0 {11,S} {26,S}
14 O u0 p2 c0 {12,S} {27,S}
15 O u1 p2 c0 {2,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 O u0 p2 c0 {7,D}
26 H u0 p0 c0 {13,S}
27 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.48519,0.165335,-0.000161662,7.93887e-08,-1.52287e-11,-87778.7,59.0824], Tmin=(100,'K'), Tmax=(1276.83,'K')),
            NASAPolynomial(coeffs=[35.5607,0.0398807,-1.42792e-05,2.43592e-09,-1.61454e-13,-98005,-143.902], Tmin=(1276.83,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 647,
    label = "[CH2]CC(=O)CCC=O",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,D}
2  O u0 p2 c0 {7,D}
3  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {7,S} {9,S} {10,S}
5  C u0 p0 c0 {6,S} {8,S} {13,S} {14,S}
6  C u0 p0 c0 {1,D} {3,S} {5,S}
7  C u0 p0 c0 {2,D} {4,S} {15,S}
8  C u1 p0 c0 {5,S} {16,S} {17,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.221683,0.0941727,-0.000143436,1.32899e-07,-4.88111e-11,-21355.4,30.7831], Tmin=(100,'K'), Tmax=(828.58,'K')),
            NASAPolynomial(coeffs=[4.60443,0.050721,-2.44147e-05,4.66258e-09,-3.21479e-13,-21316.5,15.081], Tmin=(828.58,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 648,
    label = "[O]OCCC(=O)CCC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {2,S} {16,D}
6  C u0 p0 c0 {3,S} {17,D} {18,S}
7  O u0 p2 c0 {4,S} {19,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u0 p2 c0 {5,D}
17 O u0 p2 c0 {6,D}
18 H u0 p0 c0 {6,S}
19 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.788558,0.12238,-0.000206135,1.96548e-07,-7.19849e-11,-39113.9,37.9984], Tmin=(100,'K'), Tmax=(848.84,'K')),
            NASAPolynomial(coeffs=[4.469,0.0600072,-2.94745e-05,5.62056e-09,-3.84911e-13,-38651.9,21.4741], Tmin=(848.84,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 649,
    label = "C=CC(=O)O[O]",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u0 p0 c0 {1,S} {4,S} {6,D}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 O u0 p2 c0 {2,S} {9,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.95887,0.0402908,-3.36072e-05,1.37377e-08,-2.2297e-12,-7637.73,18.3909], Tmin=(100,'K'), Tmax=(1468.69,'K')),
            NASAPolynomial(coeffs=[11.985,0.0129844,-5.7185e-06,1.07845e-09,-7.48432e-14,-10582.8,-33.8331], Tmin=(1468.69,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 650,
    label = "C=C([O])COOC(=O)C(=O)OCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {8,S} {11,S} {12,S}
2  C u0 p0 c0 {4,S} {9,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {2,S} {7,D} {18,S}
5  C u0 p0 c0 {6,S} {8,S} {20,D}
6  C u0 p0 c0 {5,S} {10,S} {19,D}
7  C u0 p0 c0 {4,D} {21,S} {22,S}
8  O u0 p2 c0 {1,S} {5,S}
9  O u0 p2 c0 {2,S} {10,S}
10 O u0 p2 c0 {6,S} {9,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 O u1 p2 c0 {4,S}
19 O u0 p2 c0 {6,D}
20 O u0 p2 c0 {5,D}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.68389,0.123792,-0.000113905,5.30427e-08,-1.00148e-11,-90623.9,46.1956], Tmin=(100,'K'), Tmax=(1254.16,'K')),
            NASAPolynomial(coeffs=[22.3285,0.0472071,-2.23067e-05,4.35236e-09,-3.09007e-13,-96646.9,-75.0883], Tmin=(1254.16,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 651,
    label = "CCOC(=O)C(=O)OOCC(=O)CO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {8,S} {12,S} {13,S}
2  C u0 p0 c0 {5,S} {9,S} {14,S} {15,S}
3  C u0 p0 c0 {5,S} {11,S} {19,S} {20,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {3,S} {21,D}
6  C u0 p0 c0 {7,S} {8,S} {23,D}
7  C u0 p0 c0 {6,S} {10,S} {22,D}
8  O u0 p2 c0 {1,S} {6,S}
9  O u0 p2 c0 {2,S} {10,S}
10 O u0 p2 c0 {7,S} {9,S}
11 O u0 p2 c0 {3,S} {24,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 O u0 p2 c0 {5,D}
22 O u0 p2 c0 {7,D}
23 O u0 p2 c0 {6,D}
24 O u1 p2 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.39684,0.149433,-0.000157604,8.69182e-08,-1.97196e-11,-99747.9,51.4062], Tmin=(100,'K'), Tmax=(1047.44,'K')),
            NASAPolynomial(coeffs=[20.804,0.060832,-3.07206e-05,6.15954e-09,-4.4412e-13,-104608,-61.5994], Tmin=(1047.44,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 652,
    label = "[O]C1CCOO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {8,S} {11,S}
4  O u0 p2 c0 {2,S} {5,S}
5  O u0 p2 c0 {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {3,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.43925,0.0247243,2.7427e-05,-5.50552e-08,2.44266e-11,-11835.3,17.8828], Tmin=(100,'K'), Tmax=(895.59,'K')),
            NASAPolynomial(coeffs=[9.67381,0.0180645,-4.3823e-06,6.04777e-10,-3.80367e-14,-14159.9,-21.9654], Tmin=(895.59,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 653,
    label = "O=C1CCOO1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,D}
4  O u0 p2 c0 {2,S} {5,S}
5  O u0 p2 c0 {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.94687,0.000123466,0.000107868,-1.41776e-07,5.42963e-11,-44715,16.7602], Tmin=(100,'K'), Tmax=(952.82,'K')),
            NASAPolynomial(coeffs=[14.118,0.0119721,-3.26713e-06,6.89847e-10,-6.13743e-14,-49510.5,-50.5879], Tmin=(952.82,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 654,
    label = "[O]OCCOOC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {11,D} {12,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {3,S} {4,S}
6  O u0 p2 c0 {2,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 H u0 p0 c0 {3,S}
13 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.635883,0.0684906,-5.99024e-05,2.57884e-08,-4.42549e-12,-42122.9,29.6778], Tmin=(100,'K'), Tmax=(1389.02,'K')),
            NASAPolynomial(coeffs=[16.5964,0.0225285,-1.02678e-05,1.96596e-09,-1.37842e-13,-46556.8,-52.5672], Tmin=(1389.02,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 655,
    label = "CCOC(=O)C(=O)OC(C=O)=C[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {6,D} {7,S} {9,S}
4  C u0 p0 c0 {5,S} {8,S} {15,D}
5  C u0 p0 c0 {4,S} {9,S} {16,D}
6  C u0 p0 c0 {3,D} {17,S} {19,S}
7  C u0 p0 c0 {3,S} {18,D} {20,S}
8  O u0 p2 c0 {1,S} {4,S}
9  O u0 p2 c0 {3,S} {5,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 O u0 p2 c0 {4,D}
16 O u0 p2 c0 {5,D}
17 O u1 p2 c0 {6,S}
18 O u0 p2 c0 {7,D}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.47726,0.12897,-0.000142636,8.08236e-08,-1.86805e-11,-102742,39.0317], Tmin=(100,'K'), Tmax=(1033.03,'K')),
            NASAPolynomial(coeffs=[19.3636,0.0482707,-2.54545e-05,5.19927e-09,-3.78641e-13,-107048,-62.1905], Tmin=(1033.03,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 656,
    label = "CCO[C]1OC(C=O)(C=O)OC1=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u1 p0 c0 {5,S} {8,S} {10,S}
5  C u0 p0 c0 {4,S} {9,S} {18,D}
6  C u0 p0 c0 {1,S} {16,D} {19,S}
7  C u0 p0 c0 {1,S} {17,D} {20,S}
8  O u0 p2 c0 {1,S} {4,S}
9  O u0 p2 c0 {1,S} {5,S}
10 O u0 p2 c0 {2,S} {4,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u0 p2 c0 {6,D}
17 O u0 p2 c0 {7,D}
18 O u0 p2 c0 {5,D}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.941673,0.081442,3.44949e-06,-7.36775e-08,3.60491e-11,-93436.8,44.5426], Tmin=(100,'K'), Tmax=(983.01,'K')),
            NASAPolynomial(coeffs=[28.6274,0.0255877,-9.69172e-06,1.94892e-09,-1.51147e-13,-102365,-113.447], Tmin=(983.01,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 657,
    label = "C[CH]OC(=O)C(=O)OC(C=O)C=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {6,S} {7,S} {8,S} {10,S}
2  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
3  C u1 p0 c0 {2,S} {9,S} {14,S}
4  C u0 p0 c0 {5,S} {8,S} {16,D}
5  C u0 p0 c0 {4,S} {9,S} {15,D}
6  C u0 p0 c0 {1,S} {17,D} {19,S}
7  C u0 p0 c0 {1,S} {18,D} {20,S}
8  O u0 p2 c0 {1,S} {4,S}
9  O u0 p2 c0 {3,S} {5,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {5,D}
16 O u0 p2 c0 {4,D}
17 O u0 p2 c0 {6,D}
18 O u0 p2 c0 {7,D}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.570905,0.110928,-0.000107273,5.54569e-08,-1.22077e-11,-94776.4,43.3523], Tmin=(100,'K'), Tmax=(1051.97,'K')),
            NASAPolynomial(coeffs=[13.8566,0.0560682,-2.9047e-05,5.88152e-09,-4.25951e-13,-97811.8,-26.9826], Tmin=(1051.97,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 658,
    label = "CCOC(=O)C(=O)OC(C=O)(C=O)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {6,S} {7,S} {8,S} {10,S}
2  C u0 p0 c0 {3,S} {9,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {5,S} {9,S} {16,D}
5  C u0 p0 c0 {4,S} {8,S} {17,D}
6  C u0 p0 c0 {1,S} {18,D} {20,S}
7  C u0 p0 c0 {1,S} {19,D} {21,S}
8  O u0 p2 c0 {1,S} {5,S}
9  O u0 p2 c0 {2,S} {4,S}
10 O u0 p2 c0 {1,S} {22,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u0 p2 c0 {4,D}
17 O u0 p2 c0 {5,D}
18 O u0 p2 c0 {6,D}
19 O u0 p2 c0 {7,D}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 O u1 p2 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.42548,0.140375,-0.00014585,7.54962e-08,-1.55782e-11,-116163,50.7305], Tmin=(100,'K'), Tmax=(1167.46,'K')),
            NASAPolynomial(coeffs=[25.9623,0.0431119,-2.0881e-05,4.13393e-09,-2.96661e-13,-122791,-90.6192], Tmin=(1167.46,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 659,
    label = "CCOC(=O)C(=O)OC(C=O)(C=O)OO",
    molecule = 
"""
1  C u0 p0 c0 {6,S} {7,S} {8,S} {10,S}
2  C u0 p0 c0 {3,S} {9,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {5,S} {9,S} {17,D}
5  C u0 p0 c0 {4,S} {8,S} {18,D}
6  C u0 p0 c0 {1,S} {19,D} {21,S}
7  C u0 p0 c0 {1,S} {20,D} {22,S}
8  O u0 p2 c0 {1,S} {5,S}
9  O u0 p2 c0 {2,S} {4,S}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {10,S} {23,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 O u0 p2 c0 {4,D}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {6,D}
20 O u0 p2 c0 {7,D}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.79689,0.145243,-0.000145558,7.16869e-08,-1.40147e-11,-134429,51.3027], Tmin=(100,'K'), Tmax=(1231.45,'K')),
            NASAPolynomial(coeffs=[28.7523,0.0427632,-2.07267e-05,4.1063e-09,-2.94663e-13,-142199,-107.471], Tmin=(1231.45,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 660,
    label = "CCOC(=O)C(=O)OC([O])(C=O)C=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {6,S} {7,S} {8,S} {10,S}
2  C u0 p0 c0 {3,S} {9,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {5,S} {8,S} {18,D}
5  C u0 p0 c0 {4,S} {9,S} {19,D}
6  C u0 p0 c0 {1,S} {16,D} {20,S}
7  C u0 p0 c0 {1,S} {17,D} {21,S}
8  O u0 p2 c0 {1,S} {4,S}
9  O u0 p2 c0 {2,S} {5,S}
10 O u1 p2 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u0 p2 c0 {6,D}
17 O u0 p2 c0 {7,D}
18 O u0 p2 c0 {4,D}
19 O u0 p2 c0 {5,D}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.04166,0.127317,-0.000125088,6.06558e-08,-1.1668e-11,-113741,48.6091], Tmin=(100,'K'), Tmax=(1252.1,'K')),
            NASAPolynomial(coeffs=[26.0309,0.0376339,-1.76477e-05,3.44964e-09,-2.45819e-13,-120771,-93.1358], Tmin=(1252.1,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 661,
    label = "CCOC(=O)C1=COCC(=O)O1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {8,S} {11,S} {12,S}
2  C u0 p0 c0 {5,S} {9,S} {16,S} {17,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {6,D} {7,S} {10,S}
5  C u0 p0 c0 {2,S} {10,S} {18,D}
6  C u0 p0 c0 {4,D} {9,S} {20,S}
7  C u0 p0 c0 {4,S} {8,S} {19,D}
8  O u0 p2 c0 {1,S} {7,S}
9  O u0 p2 c0 {2,S} {6,S}
10 O u0 p2 c0 {4,S} {5,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {7,D}
20 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.10118,0.0915072,-3.6664e-05,-2.06495e-08,1.39947e-11,-93520.4,33.2738], Tmin=(100,'K'), Tmax=(1066.21,'K')),
            NASAPolynomial(coeffs=[25.19,0.0347777,-1.58071e-05,3.17081e-09,-2.33642e-13,-101509,-106.421], Tmin=(1066.21,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 662,
    label = "CCOC(=O)[C]1COCC(=O)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {9,S} {11,S} {12,S}
2  C u0 p0 c0 {5,S} {8,S} {13,S} {19,S}
3  C u0 p0 c0 {6,S} {8,S} {17,S} {18,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  C u1 p0 c0 {2,S} {7,S} {10,S}
6  C u0 p0 c0 {3,S} {10,S} {20,D}
7  C u0 p0 c0 {5,S} {9,S} {21,D}
8  O u0 p2 c0 {2,S} {3,S}
9  O u0 p2 c0 {1,S} {7,S}
10 O u0 p2 c0 {5,S} {6,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {2,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.399854,0.0788655,-1.452e-05,-2.76743e-08,1.21721e-11,-86955.6,39.1733], Tmin=(100,'K'), Tmax=(1194.47,'K')),
            NASAPolynomial(coeffs=[20.7345,0.0471196,-2.3665e-05,4.78424e-09,-3.46652e-13,-94788.7,-78.1976], Tmin=(1194.47,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 663,
    label = "CCOC(=O)C1(O[O])COCC(=O)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {8,S} {12,S} {15,S}
3  C u0 p0 c0 {5,S} {10,S} {13,S} {14,S}
4  C u0 p0 c0 {7,S} {8,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {10,S} {22,D}
7  C u0 p0 c0 {4,S} {9,S} {21,D}
8  O u0 p2 c0 {2,S} {4,S}
9  O u0 p2 c0 {1,S} {7,S}
10 O u0 p2 c0 {3,S} {6,S}
11 O u0 p2 c0 {1,S} {23,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {7,D}
22 O u0 p2 c0 {6,D}
23 O u1 p2 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.06513,0.10468,-2.44042e-05,-5.12802e-08,2.7685e-11,-109766,43.541], Tmin=(100,'K'), Tmax=(1026.05,'K')),
            NASAPolynomial(coeffs=[31.9166,0.0354922,-1.57805e-05,3.23238e-09,-2.44567e-13,-120071,-137.51], Tmin=(1026.05,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 664,
    label = "CCOC(=O)[C]1OC(=O)COC1O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {8,S} {11,S} {14,S}
2  C u0 p0 c0 {4,S} {9,S} {12,S} {13,S}
3  C u0 p0 c0 {6,S} {8,S} {18,S} {19,S}
4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
5  C u1 p0 c0 {1,S} {7,S} {10,S}
6  C u0 p0 c0 {3,S} {10,S} {20,D}
7  C u0 p0 c0 {5,S} {9,S} {21,D}
8  O u0 p2 c0 {1,S} {3,S}
9  O u0 p2 c0 {2,S} {7,S}
10 O u0 p2 c0 {5,S} {6,S}
11 O u0 p2 c0 {1,S} {22,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.07711,0.0937049,-4.07506e-05,-7.53327e-09,6.45128e-12,-111013,44.0783], Tmin=(100,'K'), Tmax=(1246.85,'K')),
            NASAPolynomial(coeffs=[24.5236,0.0452627,-2.29997e-05,4.64435e-09,-3.35076e-13,-120016,-95.5792], Tmin=(1246.85,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 665,
    label = "CC1([O])OOCC(=O)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {4,S} {7,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {5,S} {14,D}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {2,S} {6,S}
8  O u1 p2 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.3472,0.04562,7.81594e-06,-3.34503e-08,1.24263e-11,-56108.8,24.2312], Tmin=(100,'K'), Tmax=(1176.21,'K')),
            NASAPolynomial(coeffs=[13.943,0.0341381,-1.7526e-05,3.57625e-09,-2.60552e-13,-61240.7,-47.8003], Tmin=(1176.21,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 666,
    label = "CCOC(=O)C1OOC(=O)C1OO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {9,S} {12,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {13,S}
3  C u0 p0 c0 {4,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {7,S} {20,D}
6  C u0 p0 c0 {1,S} {10,S} {19,D}
7  O u0 p2 c0 {3,S} {5,S}
8  O u0 p2 c0 {2,S} {10,S}
9  O u0 p2 c0 {1,S} {11,S}
10 O u0 p2 c0 {6,S} {8,S}
11 O u0 p2 c0 {9,S} {21,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {6,D}
20 O u0 p2 c0 {5,D}
21 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.766374,0.0706255,5.26882e-05,-1.27063e-07,5.4534e-11,-104779,46.4425], Tmin=(100,'K'), Tmax=(983.49,'K')),
            NASAPolynomial(coeffs=[29.6466,0.0299139,-1.17826e-05,2.43111e-09,-1.91098e-13,-114774,-120.179], Tmin=(983.49,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 667,
    label = "O=C1OO[CH]C1OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u1 p0 c0 {1,S} {6,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {9,D}
4  O u0 p2 c0 {1,S} {7,S}
5  O u0 p2 c0 {3,S} {6,S}
6  O u0 p2 c0 {2,S} {5,S}
7  O u0 p2 c0 {4,S} {11,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.77242,0.0224978,8.00102e-05,-1.29394e-07,5.2893e-11,-34077.9,26.1535], Tmin=(100,'K'), Tmax=(957.15,'K')),
            NASAPolynomial(coeffs=[21.1765,0.00810526,-1.96231e-06,5.06343e-10,-5.22771e-14,-40847.7,-82.5704], Tmin=(957.15,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 668,
    label = "CC(=O)OC[C]=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {11,D}
4  O u0 p2 c0 {1,S} {3,S}
5  C u1 p0 c0 {1,S} {12,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.71755,0.0439425,-2.46137e-05,5.12962e-09,-9.59721e-14,-45063.6,24.942], Tmin=(100,'K'), Tmax=(1455.93,'K')),
            NASAPolynomial(coeffs=[12.3011,0.0222221,-9.81522e-06,1.82399e-09,-1.24294e-13,-48925,-32.7709], Tmin=(1455.93,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 669,
    label = "[CH2]OC(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,D}
3  C u1 p0 c0 {4,S} {9,S} {10,S}
4  O u0 p2 c0 {2,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.32844,0.033854,-1.90647e-05,3.72985e-09,-8.06276e-14,-27231.4,16.7773], Tmin=(100,'K'), Tmax=(1662.38,'K')),
            NASAPolynomial(coeffs=[13.3191,0.0141034,-7.28421e-06,1.42812e-09,-9.88071e-14,-31810.6,-44.6144], Tmin=(1662.38,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 670,
    label = "CC(=O)OC[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {11,D}
4  O u0 p2 c0 {2,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.29065,0.0276922,1.56215e-05,-3.55047e-08,1.38962e-11,-46896.1,20.5325], Tmin=(100,'K'), Tmax=(1046.28,'K')),
            NASAPolynomial(coeffs=[9.93935,0.0218316,-9.49674e-06,1.85871e-09,-1.35025e-13,-49776.3,-22.8298], Tmin=(1046.28,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 671,
    label = "CC([O])OC(=O)C1OOC(=O)C1OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {9,S} {12,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {13,S}
3  C u0 p0 c0 {4,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {7,S} {20,D}
6  C u0 p0 c0 {1,S} {10,S} {19,D}
7  O u0 p2 c0 {3,S} {5,S}
8  O u0 p2 c0 {2,S} {10,S}
9  O u0 p2 c0 {1,S} {11,S}
10 O u0 p2 c0 {6,S} {8,S}
11 O u0 p2 c0 {9,S} {21,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 O u1 p2 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {6,D}
20 O u0 p2 c0 {5,D}
21 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.09289,0.0828939,1.34322e-05,-8.08803e-08,3.63818e-11,-101708,51.6388], Tmin=(100,'K'), Tmax=(1017.83,'K')),
            NASAPolynomial(coeffs=[28.1404,0.0353528,-1.57512e-05,3.23906e-09,-2.46078e-13,-111148,-107.048], Tmin=(1017.83,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 672,
    label = "C=COC(=O)C(=O)OC(C=O)C=O",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {8,S} {10,S}
2  C u0 p0 c0 {5,S} {8,S} {13,D}
3  C u0 p0 c0 {1,S} {11,D} {15,S}
4  C u0 p0 c0 {1,S} {12,D} {16,S}
5  C u0 p0 c0 {2,S} {9,S} {14,D}
6  C u0 p0 c0 {7,D} {9,S} {17,S}
7  C u0 p0 c0 {6,D} {18,S} {19,S}
8  O u0 p2 c0 {1,S} {2,S}
9  O u0 p2 c0 {5,S} {6,S}
10 H u0 p0 c0 {1,S}
11 O u0 p2 c0 {3,D}
12 O u0 p2 c0 {4,D}
13 O u0 p2 c0 {2,D}
14 O u0 p2 c0 {5,D}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.79001,0.111256,-0.000110663,5.65522e-08,-1.18906e-11,-103951,41.1178], Tmin=(100,'K'), Tmax=(1122.01,'K')),
            NASAPolynomial(coeffs=[17.515,0.0459987,-2.34211e-05,4.7158e-09,-3.40677e-13,-108058,-49.3004], Tmin=(1122.01,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 673,
    label = "CC(O[O])OC(=O)C(=O)OC(C=O)C=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {6,S} {7,S} {8,S} {11,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {12,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {5,S} {8,S} {17,D}
5  C u0 p0 c0 {4,S} {9,S} {16,D}
6  C u0 p0 c0 {1,S} {18,D} {20,S}
7  C u0 p0 c0 {1,S} {19,D} {21,S}
8  O u0 p2 c0 {1,S} {4,S}
9  O u0 p2 c0 {2,S} {5,S}
10 O u0 p2 c0 {2,S} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u0 p2 c0 {5,D}
17 O u0 p2 c0 {4,D}
18 O u0 p2 c0 {6,D}
19 O u0 p2 c0 {7,D}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 O u1 p2 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.69464,0.138504,-0.000173534,1.27365e-07,-3.97957e-11,-114766,51.472], Tmin=(100,'K'), Tmax=(764.88,'K')),
            NASAPolynomial(coeffs=[11.7485,0.0682009,-3.56633e-05,7.19673e-09,-5.18603e-13,-116823,-9.78027], Tmin=(764.88,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 674,
    label = "O=C1COOC(=O)O1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,D}
3  C u0 p0 c0 {4,S} {6,S} {10,D}
4  O u0 p2 c0 {2,S} {3,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {3,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {2,D}
10 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.04713,0.0880384,-9.96838e-05,5.35211e-08,-1.26717e-11,-79808.7,7.163], Tmin=(100,'K'), Tmax=(943.31,'K')),
            NASAPolynomial(coeffs=[10.5936,0.0475578,-3.53143e-05,8.02952e-09,-6.15358e-13,-81609.8,-38.3363], Tmin=(943.31,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 675,
    label = "[O]CC(OO)OC(=O)CC1OCC1=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {8,S} {12,S}
2  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
3  C u0 p0 c0 {5,S} {9,S} {10,S} {13,S}
4  C u0 p0 c0 {6,S} {8,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {4,S} {21,D}
7  C u0 p0 c0 {2,S} {9,S} {22,D}
8  O u0 p2 c0 {1,S} {4,S}
9  O u0 p2 c0 {3,S} {7,S}
10 O u0 p2 c0 {3,S} {11,S}
11 O u0 p2 c0 {10,S} {23,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 O u1 p2 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.840037,0.114933,-9.40309e-05,3.93728e-08,-6.97529e-12,-81567.4,48.2153], Tmin=(100,'K'), Tmax=(1274.07,'K')),
            NASAPolynomial(coeffs=[16.4064,0.0607872,-3.02826e-05,6.01578e-09,-4.29892e-13,-85962,-39.166], Tmin=(1274.07,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 676,
    label = "[O]C1(CCC=O)CCOO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {8,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,D} {19,S}
7  O u0 p2 c0 {1,S} {8,S}
8  O u0 p2 c0 {5,S} {7,S}
9  O u1 p2 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 O u0 p2 c0 {6,D}
19 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.281451,0.0805723,-3.38255e-05,-2.13799e-08,1.70136e-11,-32472.8,33.144], Tmin=(100,'K'), Tmax=(926.63,'K')),
            NASAPolynomial(coeffs=[19.3778,0.0305406,-9.21985e-06,1.48309e-09,-9.9021e-14,-37611.6,-68.2714], Tmin=(926.63,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 677,
    label = "C=COC(=O)C(=O)OC=COC=O",
    molecule = 
"""
1  C u0 p0 c0 {3,D} {8,S} {13,S}
2  C u0 p0 c0 {4,S} {8,S} {11,D}
3  C u0 p0 c0 {1,D} {10,S} {14,S}
4  C u0 p0 c0 {2,S} {9,S} {12,D}
5  C u0 p0 c0 {6,D} {9,S} {15,S}
6  C u0 p0 c0 {5,D} {16,S} {17,S}
7  C u0 p0 c0 {10,S} {18,D} {19,S}
8  O u0 p2 c0 {1,S} {2,S}
9  O u0 p2 c0 {4,S} {5,S}
10 O u0 p2 c0 {3,S} {7,S}
11 O u0 p2 c0 {2,D}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 O u0 p2 c0 {7,D}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.51204,0.134417,-0.0001465,7.57782e-08,-1.51918e-11,-106822,41.6302], Tmin=(100,'K'), Tmax=(1221.07,'K')),
            NASAPolynomial(coeffs=[30.8663,0.0250761,-1.2183e-05,2.44521e-09,-1.77753e-13,-114973,-126.067], Tmin=(1221.07,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 678,
    label = "O=COC(=O)C1OOC(=O)C1OO",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {10,S}
2  O u0 p2 c0 {5,S} {9,S}
3  O u0 p2 c0 {11,S} {13,S}
4  O u0 p2 c0 {1,S} {12,S}
5  O u0 p2 c0 {2,S} {17,S}
6  O u0 p2 c0 {12,D}
7  O u0 p2 c0 {11,D}
8  O u0 p2 c0 {13,D}
9  C u0 p0 c0 {2,S} {10,S} {12,S} {14,S}
10 C u0 p0 c0 {1,S} {9,S} {11,S} {15,S}
11 C u0 p0 c0 {3,S} {7,D} {10,S}
12 C u0 p0 c0 {4,S} {6,D} {9,S}
13 C u0 p0 c0 {3,S} {8,D} {16,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {10,S}
16 H u0 p0 c0 {13,S}
17 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.419141,0.066904,2.90486e-05,-9.86954e-08,4.46998e-11,-114064,46.7985], Tmin=(100,'K'), Tmax=(981.74,'K')),
            NASAPolynomial(coeffs=[29.6651,0.0173912,-6.93128e-06,1.54113e-09,-1.28659e-13,-123492,-115.718], Tmin=(981.74,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 679,
    label = "[O]C1C(=O)OOC1C(=O)OC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {13,D}
4  C u0 p0 c0 {2,S} {8,S} {12,D}
5  C u0 p0 c0 {7,S} {14,D} {15,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {3,S} {5,S}
8  O u0 p2 c0 {4,S} {6,S}
9  H u0 p0 c0 {1,S}
10 O u1 p2 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {4,D}
13 O u0 p2 c0 {3,D}
14 O u0 p2 c0 {5,D}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.526473,0.0467369,5.73401e-05,-1.19871e-07,5.13849e-11,-93384.4,43.4216], Tmin=(100,'K'), Tmax=(967.64,'K')),
            NASAPolynomial(coeffs=[26.3947,0.0131746,-4.36977e-06,1.00516e-09,-8.97265e-14,-101826,-98.276], Tmin=(967.64,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 680,
    label = "O=C1[CH]COO1",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2 C u1 p0 c0 {1,S} {3,S} {8,S}
3 C u0 p0 c0 {2,S} {5,S} {9,D}
4 O u0 p2 c0 {1,S} {5,S}
5 O u0 p2 c0 {3,S} {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.13603,-0.00502391,0.000116246,-1.50924e-07,5.79869e-11,-20678.1,18.5776], Tmin=(100,'K'), Tmax=(946.77,'K')),
            NASAPolynomial(coeffs=[14.6521,0.00772654,-1.24002e-06,3.08013e-10,-3.54522e-14,-25610.8,-50.8846], Tmin=(946.77,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 681,
    label = "[O]C12COC(C1)C(=O)OO2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {9,S}
2  C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {8,S} {15,D}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {1,S} {8,S}
8  O u0 p2 c0 {5,S} {7,S}
9  O u1 p2 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.39739,0.0219056,0.000124947,-1.83245e-07,7.17389e-11,-55540.7,23.8026], Tmin=(100,'K'), Tmax=(971.12,'K')),
            NASAPolynomial(coeffs=[23.9458,0.0180701,-6.66101e-06,1.518e-09,-1.31195e-13,-64118.7,-105.937], Tmin=(971.12,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 682,
    label = "[O]C1CC(=O)COO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {3,S} {13,D}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {3,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u1 p2 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.41494,0.0479448,-1.14602e-05,-1.22054e-08,5.24901e-12,-28951.8,21.9929], Tmin=(100,'K'), Tmax=(1307.97,'K')),
            NASAPolynomial(coeffs=[15.0365,0.0289663,-1.57036e-05,3.21367e-09,-2.31845e-13,-34455,-54.7961], Tmin=(1307.97,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 683,
    label = "CC(O[O])OC(=O)C(O)(C=O)OC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {7,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {7,S} {15,D}
5  C u0 p0 c0 {1,S} {16,D} {17,S}
6  C u0 p0 c0 {8,S} {18,D} {19,S}
7  O u0 p2 c0 {2,S} {4,S}
8  O u0 p2 c0 {1,S} {6,S}
9  O u0 p2 c0 {1,S} {21,S}
10 O u0 p2 c0 {2,S} {20,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {4,D}
16 O u0 p2 c0 {5,D}
17 H u0 p0 c0 {5,S}
18 O u0 p2 c0 {6,D}
19 H u0 p0 c0 {6,S}
20 O u1 p2 c0 {10,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.5599,0.129396,-0.000126644,5.99015e-08,-1.10365e-11,-129709,53.0884], Tmin=(100,'K'), Tmax=(1323.36,'K')),
            NASAPolynomial(coeffs=[30.7767,0.0286311,-1.24268e-05,2.3617e-09,-1.66303e-13,-138532,-117.081], Tmin=(1323.36,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 684,
    label = "CC1OOC([O])C(O)(OC=O)C(=O)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {8,S} {11,S}
2  C u0 p0 c0 {4,S} {7,S} {9,S} {12,S}
3  C u0 p0 c0 {1,S} {10,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {7,S} {18,D}
6  C u0 p0 c0 {8,S} {19,D} {20,S}
7  O u0 p2 c0 {2,S} {5,S}
8  O u0 p2 c0 {1,S} {6,S}
9  O u0 p2 c0 {2,S} {10,S}
10 O u0 p2 c0 {3,S} {9,S}
11 O u0 p2 c0 {1,S} {21,S}
12 H u0 p0 c0 {2,S}
13 O u1 p2 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {6,D}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.70962,0.0643903,0.000142506,-2.79453e-07,1.2466e-10,-124333,47.1492], Tmin=(100,'K'), Tmax=(925.76,'K')),
            NASAPolynomial(coeffs=[53.0018,-0.0141221,1.39017e-05,-2.61953e-09,1.53219e-13,-141229,-249.122], Tmin=(925.76,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 685,
    label = "CC(OOC=O)OC(=O)[C](O)OC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {12,S}
2  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
3  C u1 p0 c0 {4,S} {9,S} {11,S}
4  C u0 p0 c0 {3,S} {7,S} {16,D}
5  C u0 p0 c0 {9,S} {18,D} {20,S}
6  C u0 p0 c0 {10,S} {17,D} {19,S}
7  O u0 p2 c0 {1,S} {4,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {3,S} {5,S}
10 O u0 p2 c0 {6,S} {8,S}
11 O u0 p2 c0 {3,S} {21,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 O u0 p2 c0 {4,D}
17 O u0 p2 c0 {6,D}
18 O u0 p2 c0 {5,D}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.7774,0.116022,-9.4808e-05,3.65164e-08,-5.56438e-12,-135427,53.5341], Tmin=(100,'K'), Tmax=(1550.49,'K')),
            NASAPolynomial(coeffs=[28.9279,0.0368068,-1.81722e-05,3.565e-09,-2.51299e-13,-144949,-108.068], Tmin=(1550.49,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 686,
    label = "CC(OOC=O)OC(=O)C(=O)OC=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {11,S}
2  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {4,S} {7,S} {16,D}
4  C u0 p0 c0 {3,S} {9,S} {15,D}
5  C u0 p0 c0 {9,S} {18,D} {20,S}
6  C u0 p0 c0 {10,S} {17,D} {19,S}
7  O u0 p2 c0 {1,S} {3,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {4,S} {5,S}
10 O u0 p2 c0 {6,S} {8,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 O u0 p2 c0 {4,D}
16 O u0 p2 c0 {3,D}
17 O u0 p2 c0 {6,D}
18 O u0 p2 c0 {5,D}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.15877,0.117947,-0.000109446,4.98336e-08,-9.24385e-12,-146112,48.12], Tmin=(100,'K'), Tmax=(1261.7,'K')),
            NASAPolynomial(coeffs=[21.3448,0.0466041,-2.46288e-05,5.0172e-09,-3.63723e-13,-151790,-65.6777], Tmin=(1261.7,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 687,
    label = "CC(=O)OC(=O)[C](O)OC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u1 p0 c0 {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {6,S} {12,D}
4  C u0 p0 c0 {2,S} {6,S} {13,D}
5  C u0 p0 c0 {7,S} {14,D} {15,S}
6  O u0 p2 c0 {3,S} {4,S}
7  O u0 p2 c0 {2,S} {5,S}
8  O u0 p2 c0 {2,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 O u0 p2 c0 {3,D}
13 O u0 p2 c0 {4,D}
14 O u0 p2 c0 {5,D}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.490943,0.0851137,-9.31555e-05,5.80416e-08,-1.54662e-11,-108382,40.5991], Tmin=(100,'K'), Tmax=(885.1,'K')),
            NASAPolynomial(coeffs=[9.78842,0.0430968,-2.19498e-05,4.40987e-09,-3.17978e-13,-110028,-3.12121], Tmin=(885.1,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 688,
    label = "CC(OOC=O)OC(=O)C(O)(O[O])OC=O",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {11,S} {14,S}
2  O u0 p2 c0 {12,S} {15,S}
3  O u0 p2 c0 {6,S} {11,S}
4  O u0 p2 c0 {12,S} {23,S}
5  O u0 p2 c0 {10,S} {12,S}
6  O u0 p2 c0 {3,S} {16,S}
7  O u0 p2 c0 {14,D}
8  O u0 p2 c0 {16,D}
9  O u0 p2 c0 {15,D}
10 O u1 p2 c0 {5,S}
11 C u0 p0 c0 {1,S} {3,S} {13,S} {17,S}
12 C u0 p0 c0 {2,S} {4,S} {5,S} {14,S}
13 C u0 p0 c0 {11,S} {18,S} {19,S} {20,S}
14 C u0 p0 c0 {1,S} {7,D} {12,S}
15 C u0 p0 c0 {2,S} {9,D} {22,S}
16 C u0 p0 c0 {6,S} {8,D} {21,S}
17 H u0 p0 c0 {11,S}
18 H u0 p0 c0 {13,S}
19 H u0 p0 c0 {13,S}
20 H u0 p0 c0 {13,S}
21 H u0 p0 c0 {16,S}
22 H u0 p0 c0 {15,S}
23 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.96695,0.136275,-0.000129819,6.30393e-08,-1.25701e-11,-154931,56.8915], Tmin=(100,'K'), Tmax=(1179.57,'K')),
            NASAPolynomial(coeffs=[21.5849,0.0564101,-2.82614e-05,5.64204e-09,-4.05428e-13,-160488,-60.6224], Tmin=(1179.57,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 689,
    label = "CC(=O)OC(=O)C(O)(O[O])OC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {13,D}
4  C u0 p0 c0 {2,S} {7,S} {14,D}
5  C u0 p0 c0 {6,S} {15,D} {16,S}
6  O u0 p2 c0 {1,S} {5,S}
7  O u0 p2 c0 {3,S} {4,S}
8  O u0 p2 c0 {1,S} {18,S}
9  O u0 p2 c0 {1,S} {17,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {3,D}
14 O u0 p2 c0 {4,D}
15 O u0 p2 c0 {5,D}
16 H u0 p0 c0 {5,S}
17 O u1 p2 c0 {9,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.0366,0.121355,-0.000185101,1.60138e-07,-5.57479e-11,-127828,48.7415], Tmin=(100,'K'), Tmax=(793.97,'K')),
            NASAPolynomial(coeffs=[10.653,0.0494514,-2.46745e-05,4.79304e-09,-3.34381e-13,-129274,-2.37439], Tmin=(793.97,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 690,
    label = "CC(=O)OC(=O)C(=O)OC=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {11,D}
3  C u0 p0 c0 {4,S} {7,S} {12,D}
4  C u0 p0 c0 {3,S} {6,S} {13,D}
5  C u0 p0 c0 {7,S} {14,D} {15,S}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {3,S} {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 O u0 p2 c0 {2,D}
12 O u0 p2 c0 {3,D}
13 O u0 p2 c0 {4,D}
14 O u0 p2 c0 {5,D}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.720899,0.0874414,-7.98964e-05,-3.80445e-08,8.7092e-11,-119048,36.7963], Tmin=(100,'K'), Tmax=(475.42,'K')),
            NASAPolynomial(coeffs=[9.55992,0.0410572,-2.1841e-05,4.3544e-09,-3.07965e-13,-120205,-2.60059], Tmin=(475.42,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 691,
    label = "O=[C]OC(=O)C(=O)O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {6,S} {8,S}
2 O u0 p2 c0 {7,S} {9,S}
3 O u0 p2 c0 {7,D}
4 O u0 p2 c0 {6,D}
5 O u0 p2 c0 {8,D}
6 C u0 p0 c0 {1,S} {4,D} {7,S}
7 C u0 p0 c0 {2,S} {3,D} {6,S}
8 C u1 p0 c0 {1,S} {5,D}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.997666,0.0735166,-0.000128113,1.15793e-07,-4.10509e-11,-77040.7,25.8184], Tmin=(100,'K'), Tmax=(791.97,'K')),
            NASAPolynomial(coeffs=[8.97974,0.0229817,-1.30425e-05,2.63478e-09,-1.86736e-13,-77984.6,-8.8054], Tmin=(791.97,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 692,
    label = "O=COOC(=O)C(=O)OC=O",
    molecule = 
"""
1  O u0 p2 c0 {8,S} {10,S}
2  O u0 p2 c0 {3,S} {9,S}
3  O u0 p2 c0 {2,S} {11,S}
4  O u0 p2 c0 {9,D}
5  O u0 p2 c0 {8,D}
6  O u0 p2 c0 {11,D}
7  O u0 p2 c0 {10,D}
8  C u0 p0 c0 {1,S} {5,D} {9,S}
9  C u0 p0 c0 {2,S} {4,D} {8,S}
10 C u0 p0 c0 {1,S} {7,D} {12,S}
11 C u0 p0 c0 {3,S} {6,D} {13,S}
12 H u0 p0 c0 {10,S}
13 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.305323,0.0784914,-5.42767e-05,4.46749e-09,5.22945e-12,-127000,38.9033], Tmin=(100,'K'), Tmax=(1076.79,'K')),
            NASAPolynomial(coeffs=[24.6735,0.015601,-8.31933e-06,1.80113e-09,-1.38488e-13,-134112,-91.5018], Tmin=(1076.79,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 693,
    label = "CCOC(=O)[CH]OOC(=O)C=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {4,S} {7,S} {16,D}
4  C u1 p0 c0 {3,S} {8,S} {17,S}
5  C u0 p0 c0 {6,S} {9,S} {15,D}
6  C u0 p0 c0 {5,S} {18,D} {19,S}
7  O u0 p2 c0 {1,S} {3,S}
8  O u0 p2 c0 {4,S} {9,S}
9  O u0 p2 c0 {5,S} {8,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 O u0 p2 c0 {5,D}
16 O u0 p2 c0 {3,D}
17 H u0 p0 c0 {4,S}
18 O u0 p2 c0 {6,D}
19 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.786443,0.104581,-8.89643e-05,3.74171e-08,-6.405e-12,-86751.6,40.7439], Tmin=(100,'K'), Tmax=(1361.9,'K')),
            NASAPolynomial(coeffs=[20.2415,0.0428199,-2.09406e-05,4.11861e-09,-2.92476e-13,-92479.2,-67.1991], Tmin=(1361.9,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 694,
    label = "CCOC1([O])C(=O)OC=C1C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {8,S} {10,S}
2  C u0 p0 c0 {3,S} {8,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {4,S} {7,D}
6  C u0 p0 c0 {1,S} {9,S} {19,D}
7  C u0 p0 c0 {5,D} {9,S} {20,S}
8  O u0 p2 c0 {1,S} {2,S}
9  O u0 p2 c0 {6,S} {7,S}
10 O u1 p2 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {6,D}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.939901,0.0799898,1.06238e-05,-9.0472e-08,4.56707e-11,-57828.5,35.3461], Tmin=(100,'K'), Tmax=(941.62,'K')),
            NASAPolynomial(coeffs=[30.8863,0.0167631,-3.3051e-06,5.60824e-10,-4.9366e-14,-67012.8,-133.225], Tmin=(941.62,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 695,
    label = "CCO[C]1OC(C)=COC1=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
3  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {6,D} {9,S}
5  C u1 p0 c0 {7,S} {8,S} {9,S}
6  C u0 p0 c0 {4,D} {10,S} {20,S}
7  C u0 p0 c0 {5,S} {10,S} {19,D}
8  O u0 p2 c0 {1,S} {5,S}
9  O u0 p2 c0 {4,S} {5,S}
10 O u0 p2 c0 {6,S} {7,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 O u0 p2 c0 {7,D}
20 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.764468,0.0809711,-5.79612e-06,-5.29654e-08,2.54435e-11,-63984,31.8935], Tmin=(100,'K'), Tmax=(1032.24,'K')),
            NASAPolynomial(coeffs=[25.034,0.0342305,-1.52275e-05,3.08391e-09,-2.30694e-13,-72145.9,-107.124], Tmin=(1032.24,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 696,
    label = "CCOC1(O[O])OC(C)=COC1=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {6,S} {8,S} {9,S} {11,S}
2  C u0 p0 c0 {3,S} {8,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {7,D} {9,S}
6  C u0 p0 c0 {1,S} {10,S} {20,D}
7  C u0 p0 c0 {5,D} {10,S} {21,S}
8  O u0 p2 c0 {1,S} {2,S}
9  O u0 p2 c0 {1,S} {5,S}
10 O u0 p2 c0 {6,S} {7,S}
11 O u0 p2 c0 {1,S} {22,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {6,D}
21 H u0 p0 c0 {7,S}
22 O u1 p2 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.9521,0.11258,-7.83383e-05,1.87569e-08,7.4236e-13,-83444.5,38.1624], Tmin=(100,'K'), Tmax=(1149.47,'K')),
            NASAPolynomial(coeffs=[26.5546,0.0396732,-1.75094e-05,3.37674e-09,-2.40487e-13,-91735,-110.893], Tmin=(1149.47,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 697,
    label = "[CH2]C1OCC(=O)OOC1=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {9,S}
2  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {8,S} {13,D}
4  C u0 p0 c0 {2,S} {7,S} {12,D}
5  C u1 p0 c0 {1,S} {14,S} {15,S}
6  O u0 p2 c0 {1,S} {2,S}
7  O u0 p2 c0 {4,S} {8,S}
8  O u0 p2 c0 {3,S} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {4,D}
13 O u0 p2 c0 {3,D}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.628213,0.000483165,0.000278272,-4.1914e-07,1.7712e-10,-69357.3,33.2106], Tmin=(100,'K'), Tmax=(911.63,'K')),
            NASAPolynomial(coeffs=[53.5083,-0.0396085,2.84339e-05,-5.49113e-09,3.51066e-13,-86974.2,-260.756], Tmin=(911.63,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 698,
    label = "[O]OCC1OCC(=O)OOC1=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {9,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {6,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {8,S} {16,D}
5  C u0 p0 c0 {3,S} {7,S} {15,D}
6  O u0 p2 c0 {1,S} {3,S}
7  O u0 p2 c0 {5,S} {8,S}
8  O u0 p2 c0 {4,S} {7,S}
9  O u0 p2 c0 {2,S} {17,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {5,D}
16 O u0 p2 c0 {4,D}
17 O u1 p2 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.167184,0.0209349,0.000239941,-3.81811e-07,1.63436e-10,-86990.8,40.5365], Tmin=(100,'K'), Tmax=(914.88,'K')),
            NASAPolynomial(coeffs=[53.8954,-0.0314118,2.40523e-05,-4.63902e-09,2.92514e-13,-104584,-257.565], Tmin=(914.88,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 699,
    label = "O=C1[CH]OC(COO)C(=O)OO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {11,S}
2  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {8,S} {14,D}
4  C u1 p0 c0 {5,S} {6,S} {16,S}
5  C u0 p0 c0 {4,S} {9,S} {15,D}
6  O u0 p2 c0 {1,S} {4,S}
7  O u0 p2 c0 {2,S} {10,S}
8  O u0 p2 c0 {3,S} {9,S}
9  O u0 p2 c0 {5,S} {8,S}
10 O u0 p2 c0 {7,S} {17,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 O u0 p2 c0 {3,D}
15 O u0 p2 c0 {5,D}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.749898,0.0317414,0.000224849,-3.7672e-07,1.64092e-10,-83546,41.3152], Tmin=(100,'K'), Tmax=(913.95,'K')),
            NASAPolynomial(coeffs=[58.3835,-0.037342,2.68538e-05,-5.16437e-09,3.28028e-13,-102279,-281.997], Tmin=(913.95,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 700,
    label = "CCOC12OOC(OC1=O)[C](C)O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {7,S} {8,S} {9,S} {11,S}
2  C u0 p0 c0 {6,S} {10,S} {12,S} {15,S}
3  C u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {6,S} {19,S} {20,S} {21,S}
6  C u1 p0 c0 {2,S} {5,S} {9,S}
7  C u0 p0 c0 {1,S} {10,S} {22,D}
8  O u0 p2 c0 {1,S} {3,S}
9  O u0 p2 c0 {1,S} {6,S}
10 O u0 p2 c0 {2,S} {7,S}
11 O u0 p2 c0 {1,S} {12,S}
12 O u0 p2 c0 {2,S} {11,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.359492,0.0814408,-2.03286e-05,-1.74613e-08,7.8654e-12,-80904.1,37.6333], Tmin=(100,'K'), Tmax=(1279.9,'K')),
            NASAPolynomial(coeffs=[18.5429,0.0543823,-2.61389e-05,5.1094e-09,-3.60845e-13,-88365.1,-68.4687], Tmin=(1279.9,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 701,
    label = "CCOC12OOC(C)([CH]OC1=O)O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {6,S} {8,S} {10,S}
2  C u0 p0 c0 {7,S} {8,S} {9,S} {11,S}
3  C u0 p0 c0 {5,S} {9,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u1 p0 c0 {1,S} {12,S} {22,S}
7  C u0 p0 c0 {2,S} {12,S} {21,D}
8  O u0 p2 c0 {1,S} {2,S}
9  O u0 p2 c0 {2,S} {3,S}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {2,S} {10,S}
12 O u0 p2 c0 {6,S} {7,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.35133,0.0879785,8.07449e-06,-8.07047e-08,3.781e-11,-76994.7,35.7692], Tmin=(100,'K'), Tmax=(1002.06,'K')),
            NASAPolynomial(coeffs=[29.6139,0.033536,-1.39614e-05,2.83475e-09,-2.16218e-13,-86673,-131.01], Tmin=(1002.06,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 702,
    label = "CCO[C]1OOC(C(C)=O)OC1=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {9,S} {10,S} {14,S}
2  C u0 p0 c0 {3,S} {8,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {1,S} {4,S} {21,D}
6  C u1 p0 c0 {7,S} {8,S} {11,S}
7  C u0 p0 c0 {6,S} {9,S} {22,D}
8  O u0 p2 c0 {2,S} {6,S}
9  O u0 p2 c0 {1,S} {7,S}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {6,S} {10,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {5,D}
22 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.23486,0.0986792,-5.27734e-05,4.25024e-09,2.59181e-12,-80959,43.0304], Tmin=(100,'K'), Tmax=(1336.12,'K')),
            NASAPolynomial(coeffs=[25.9704,0.0445467,-2.26644e-05,4.52674e-09,-3.22614e-13,-90666.9,-105.226], Tmin=(1336.12,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 703,
    label = "[O]OCC(=O)OC(=O)COO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {7,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {13,D}
4  C u0 p0 c0 {2,S} {5,S} {14,D}
5  O u0 p2 c0 {3,S} {4,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {2,S} {15,S}
8  O u0 p2 c0 {6,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {3,D}
14 O u0 p2 c0 {4,D}
15 O u1 p2 c0 {7,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.923396,0.117214,-0.000181504,1.51629e-07,-5.0665e-11,-71022.7,41.6405], Tmin=(100,'K'), Tmax=(779.07,'K')),
            NASAPolynomial(coeffs=[13.2709,0.0387246,-1.95782e-05,3.82052e-09,-2.67162e-13,-73064.1,-22.2021], Tmin=(779.07,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 704,
    label = "[O]C1(COO)OOCC(=O)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {5,S} {15,D}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {3,S} {6,S}
8  O u0 p2 c0 {2,S} {9,S}
9  O u0 p2 c0 {8,S} {16,S}
10 O u1 p2 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {4,D}
16 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.306911,0.0778261,-5.20052e-05,1.49689e-08,-1.65836e-12,-66702.3,31.4433], Tmin=(100,'K'), Tmax=(2091.9,'K')),
            NASAPolynomial(coeffs=[28.734,0.0234692,-1.30282e-05,2.54725e-09,-1.73858e-13,-78595.6,-126.682], Tmin=(2091.9,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 705,
    label = "O=CC(=O)OOC(=O)[CH]COO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
2  C u1 p0 c0 {1,S} {3,S} {12,S}
3  C u0 p0 c0 {2,S} {8,S} {14,D}
4  C u0 p0 c0 {5,S} {7,S} {13,D}
5  C u0 p0 c0 {4,S} {15,D} {16,S}
6  O u0 p2 c0 {1,S} {9,S}
7  O u0 p2 c0 {4,S} {8,S}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {6,S} {17,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {4,D}
14 O u0 p2 c0 {3,D}
15 O u0 p2 c0 {5,D}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.44805,0.107273,-9.95276e-05,4.38599e-08,-7.5556e-12,-80497.9,45.7041], Tmin=(100,'K'), Tmax=(1403.54,'K')),
            NASAPolynomial(coeffs=[27.2077,0.0256043,-1.22447e-05,2.40073e-09,-1.70722e-13,-88541.7,-102.257], Tmin=(1403.54,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 706,
    label = "O=CC(=O)OOC(=O)C1CO1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {12,D}
4  C u0 p0 c0 {5,S} {8,S} {13,D}
5  C u0 p0 c0 {4,S} {14,D} {15,S}
6  O u0 p2 c0 {1,S} {2,S}
7  O u0 p2 c0 {3,S} {8,S}
8  O u0 p2 c0 {4,S} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {3,D}
13 O u0 p2 c0 {4,D}
14 O u0 p2 c0 {5,D}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.081157,0.0625722,2.80534e-05,-1.01052e-07,4.88209e-11,-91585,36.6754], Tmin=(100,'K'), Tmax=(929.64,'K')),
            NASAPolynomial(coeffs=[28.1317,0.0107599,-6.1503e-07,1.65309e-11,-9.43489e-15,-99837.3,-113.548], Tmin=(929.64,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 707,
    label = "O=C([CH]O)OOC(=O)C1CO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {13,D}
4  C u0 p0 c0 {5,S} {8,S} {14,D}
5  C u1 p0 c0 {4,S} {9,S} {15,S}
6  O u0 p2 c0 {1,S} {2,S}
7  O u0 p2 c0 {3,S} {8,S}
8  O u0 p2 c0 {4,S} {7,S}
9  O u0 p2 c0 {5,S} {16,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {3,D}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.361079,0.0683418,2.31002e-05,-1.02044e-07,5.10182e-11,-87792.2,39.2672], Tmin=(100,'K'), Tmax=(917.66,'K')),
            NASAPolynomial(coeffs=[29.5425,0.00999312,7.89419e-07,-3.38823e-10,1.84153e-14,-96312,-118.948], Tmin=(917.66,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 708,
    label = "[O]OC(O)C(=O)OOC(=O)C1CO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {9,S} {10,S} {14,S}
4  C u0 p0 c0 {1,S} {7,S} {15,D}
5  C u0 p0 c0 {3,S} {8,S} {16,D}
6  O u0 p2 c0 {1,S} {2,S}
7  O u0 p2 c0 {4,S} {8,S}
8  O u0 p2 c0 {5,S} {7,S}
9  O u0 p2 c0 {3,S} {17,S}
10 O u0 p2 c0 {3,S} {18,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {4,D}
16 O u0 p2 c0 {5,D}
17 O u1 p2 c0 {9,S}
18 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.34592,0.093928,-3.05338e-05,-4.97957e-08,3.22751e-11,-103351,48.4254], Tmin=(100,'K'), Tmax=(929.65,'K')),
            NASAPolynomial(coeffs=[30.7058,0.0164535,-3.04044e-06,4.16791e-10,-3.31223e-14,-111922,-117.913], Tmin=(929.65,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 709,
    label = "CCOC(=O)C1(OO)CO[CH]C(=O)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {8,S} {11,S}
2  C u0 p0 c0 {1,S} {10,S} {13,S} {16,S}
3  C u0 p0 c0 {4,S} {9,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {9,S} {20,D}
6  C u1 p0 c0 {7,S} {10,S} {22,S}
7  C u0 p0 c0 {6,S} {8,S} {21,D}
8  O u0 p2 c0 {1,S} {7,S}
9  O u0 p2 c0 {3,S} {5,S}
10 O u0 p2 c0 {2,S} {6,S}
11 O u0 p2 c0 {1,S} {12,S}
12 O u0 p2 c0 {11,S} {23,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {5,D}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.64416,0.115477,-3.96462e-05,-4.56812e-08,2.79641e-11,-106322,44.3045], Tmin=(100,'K'), Tmax=(1013.94,'K')),
            NASAPolynomial(coeffs=[36.2151,0.0298722,-1.3153e-05,2.74728e-09,-2.12338e-13,-117682,-160.867], Tmin=(1013.94,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 710,
    label = "CCOC(=O)C12COC(O1)C(=O)O2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {9,S} {12,S} {15,S}
3  C u0 p0 c0 {7,S} {8,S} {9,S} {16,S}
4  C u0 p0 c0 {5,S} {11,S} {13,S} {14,S}
5  C u0 p0 c0 {4,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {1,S} {11,S} {20,D}
7  C u0 p0 c0 {3,S} {10,S} {21,D}
8  O u0 p2 c0 {1,S} {3,S}
9  O u0 p2 c0 {2,S} {3,S}
10 O u0 p2 c0 {1,S} {7,S}
11 O u0 p2 c0 {4,S} {6,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.618897,0.0682242,5.32419e-05,-1.25494e-07,5.36938e-11,-127205,35.662], Tmin=(100,'K'), Tmax=(982.74,'K')),
            NASAPolynomial(coeffs=[28.7944,0.0295725,-1.14994e-05,2.36483e-09,-1.85775e-13,-136901,-125.645], Tmin=(982.74,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 711,
    label = "CCOC(=O)C1(OO)COC(O[O])C(=O)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {8,S} {14,S} {17,S}
3  C u0 p0 c0 {7,S} {8,S} {12,S} {18,S}
4  C u0 p0 c0 {5,S} {10,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {10,S} {22,D}
7  C u0 p0 c0 {3,S} {9,S} {23,D}
8  O u0 p2 c0 {2,S} {3,S}
9  O u0 p2 c0 {1,S} {7,S}
10 O u0 p2 c0 {4,S} {6,S}
11 O u0 p2 c0 {1,S} {13,S}
12 O u0 p2 c0 {3,S} {24,S}
13 O u0 p2 c0 {11,S} {25,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u0 p2 c0 {6,D}
23 O u0 p2 c0 {7,D}
24 O u1 p2 c0 {12,S}
25 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.43124,0.137734,-9.17577e-05,1.18321e-08,5.99582e-12,-126937,52.3853], Tmin=(100,'K'), Tmax=(1107.28,'K')),
            NASAPolynomial(coeffs=[35.6992,0.0402437,-1.91163e-05,3.87469e-09,-2.85517e-13,-138292,-152.528], Tmin=(1107.28,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 712,
    label = "CC1=COC2(O1)OC(C)OC2=O",
    molecule = 
"""
1  C u0 p0 c0 {6,S} {8,S} {9,S} {11,S}
2  C u0 p0 c0 {3,S} {8,S} {10,S} {12,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {4,S} {7,D} {9,S}
6  C u0 p0 c0 {1,S} {10,S} {19,D}
7  C u0 p0 c0 {5,D} {11,S} {20,S}
8  O u0 p2 c0 {1,S} {2,S}
9  O u0 p2 c0 {1,S} {5,S}
10 O u0 p2 c0 {2,S} {6,S}
11 O u0 p2 c0 {1,S} {7,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {6,D}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.449203,0.073854,9.97372e-06,-6.96803e-08,3.22638e-11,-99206,27.7354], Tmin=(100,'K'), Tmax=(994.37,'K')),
            NASAPolynomial(coeffs=[23.755,0.0327368,-1.28496e-05,2.50668e-09,-1.86814e-13,-106800,-102.882], Tmin=(994.37,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 713,
    label = "C[C]1OC2(OO)OC1C(C)OC2=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {10,S} {13,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {14,S}
3  C u0 p0 c0 {7,S} {8,S} {9,S} {11,S}
4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
6  C u1 p0 c0 {2,S} {5,S} {9,S}
7  C u0 p0 c0 {3,S} {10,S} {21,D}
8  O u0 p2 c0 {2,S} {3,S}
9  O u0 p2 c0 {3,S} {6,S}
10 O u0 p2 c0 {1,S} {7,S}
11 O u0 p2 c0 {3,S} {12,S}
12 O u0 p2 c0 {11,S} {22,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.491469,0.0932311,-5.75416e-05,1.63244e-08,-1.82898e-12,-76082.8,33.944], Tmin=(100,'K'), Tmax=(2024.24,'K')),
            NASAPolynomial(coeffs=[26.5608,0.039773,-1.7927e-05,3.27729e-09,-2.17572e-13,-87034.5,-115.644], Tmin=(2024.24,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 714,
    label = "CC1OC(=O)C2(OO)O[CH]C1(C)O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {13,S}
3  C u0 p0 c0 {7,S} {8,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
6  C u1 p0 c0 {1,S} {10,S} {21,S}
7  C u0 p0 c0 {3,S} {9,S} {20,D}
8  O u0 p2 c0 {1,S} {3,S}
9  O u0 p2 c0 {2,S} {7,S}
10 O u0 p2 c0 {3,S} {6,S}
11 O u0 p2 c0 {3,S} {12,S}
12 O u0 p2 c0 {11,S} {22,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 O u0 p2 c0 {7,D}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.37885,0.101796,-6.36107e-05,1.22647e-08,1.39389e-12,-76713.1,34.729], Tmin=(100,'K'), Tmax=(1186.16,'K')),
            NASAPolynomial(coeffs=[22.8963,0.043146,-1.87952e-05,3.57378e-09,-2.51329e-13,-84104.8,-93.4118], Tmin=(1186.16,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 715,
    label = "CC(=O)C1OC12OC(C)OC2=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {11,S}
3  C u0 p0 c0 {4,S} {9,S} {10,S} {12,S}
4  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {5,S} {19,D}
7  C u0 p0 c0 {1,S} {10,S} {20,D}
8  O u0 p2 c0 {1,S} {2,S}
9  O u0 p2 c0 {1,S} {3,S}
10 O u0 p2 c0 {3,S} {7,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u0 p2 c0 {6,D}
20 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.33256,0.065964,3.93125e-05,-1.05158e-07,4.58118e-11,-92569.5,35.1542], Tmin=(100,'K'), Tmax=(982.75,'K')),
            NASAPolynomial(coeffs=[26.4735,0.0277752,-1.06427e-05,2.15951e-09,-1.6814e-13,-101263,-111.127], Tmin=(982.75,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 716,
    label = "CC1OC(=O)C2(O1)OC2(C)C=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
6  C u0 p0 c0 {2,S} {10,S} {18,D}
7  C u0 p0 c0 {1,S} {19,D} {20,S}
8  O u0 p2 c0 {1,S} {2,S}
9  O u0 p2 c0 {2,S} {3,S}
10 O u0 p2 c0 {3,S} {6,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u0 p2 c0 {6,D}
19 O u0 p2 c0 {7,D}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.890535,0.0825361,-4.9976e-06,-6.25963e-08,3.18885e-11,-90032,32.7935], Tmin=(100,'K'), Tmax=(981.22,'K')),
            NASAPolynomial(coeffs=[27.2342,0.0268116,-9.89428e-06,1.93551e-09,-1.47314e-13,-98388.1,-116.814], Tmin=(981.22,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 717,
    label = "CCOC(=O)C1(OO)[CH]OC(OO)C(=O)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {8,S} {11,S}
2  C u0 p0 c0 {7,S} {9,S} {12,S} {17,S}
3  C u0 p0 c0 {4,S} {10,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {18,S} {19,S} {20,S}
5  C u1 p0 c0 {1,S} {9,S} {23,S}
6  C u0 p0 c0 {1,S} {10,S} {21,D}
7  C u0 p0 c0 {2,S} {8,S} {22,D}
8  O u0 p2 c0 {1,S} {7,S}
9  O u0 p2 c0 {2,S} {5,S}
10 O u0 p2 c0 {3,S} {6,S}
11 O u0 p2 c0 {1,S} {13,S}
12 O u0 p2 c0 {2,S} {14,S}
13 O u0 p2 c0 {11,S} {25,S}
14 O u0 p2 c0 {12,S} {24,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {14,S}
25 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.00317,0.148488,-0.000107052,1.78004e-08,5.9828e-12,-123493,53.1207], Tmin=(100,'K'), Tmax=(1081.01,'K')),
            NASAPolynomial(coeffs=[39.6938,0.0351051,-1.67522e-05,3.44942e-09,-2.58104e-13,-135763,-174.151], Tmin=(1081.01,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 718,
    label = "CCOC(=O)C(C=O)(OO)OC(=O)[CH]OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {8,S} {10,S}
2  C u0 p0 c0 {3,S} {9,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
4  C u0 p0 c0 {1,S} {9,S} {19,D}
5  C u0 p0 c0 {1,S} {20,D} {23,S}
6  C u0 p0 c0 {7,S} {8,S} {21,D}
7  C u1 p0 c0 {6,S} {11,S} {22,S}
8  O u0 p2 c0 {1,S} {6,S}
9  O u0 p2 c0 {2,S} {4,S}
10 O u0 p2 c0 {1,S} {12,S}
11 O u0 p2 c0 {7,S} {13,S}
12 O u0 p2 c0 {10,S} {25,S}
13 O u0 p2 c0 {11,S} {24,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 O u0 p2 c0 {4,D}
20 O u0 p2 c0 {5,D}
21 O u0 p2 c0 {6,D}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {13,S}
25 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.65396,0.163977,-0.000170431,8.77688e-08,-1.79072e-11,-122812,57.8891], Tmin=(100,'K'), Tmax=(1185.5,'K')),
            NASAPolynomial(coeffs=[31.1068,0.0466902,-2.20278e-05,4.31375e-09,-3.07998e-13,-131053,-115.726], Tmin=(1185.5,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 719,
    label = "CCOC(=O)C(C=O)(OO)OC(=O)[CH]O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {8,S} {10,S}
2  C u0 p0 c0 {3,S} {9,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {1,S} {9,S} {18,D}
5  C u0 p0 c0 {1,S} {19,D} {21,S}
6  C u0 p0 c0 {7,S} {8,S} {20,D}
7  C u1 p0 c0 {6,S} {11,S} {22,S}
8  O u0 p2 c0 {1,S} {6,S}
9  O u0 p2 c0 {2,S} {4,S}
10 O u0 p2 c0 {1,S} {12,S}
11 O u0 p2 c0 {7,S} {23,S}
12 O u0 p2 c0 {10,S} {24,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 O u0 p2 c0 {4,D}
19 O u0 p2 c0 {5,D}
20 O u0 p2 c0 {6,D}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.26801,0.150483,-0.000151363,7.51808e-08,-1.47119e-11,-131421,55.7401], Tmin=(100,'K'), Tmax=(1239.48,'K')),
            NASAPolynomial(coeffs=[30.8808,0.0402791,-1.79954e-05,3.44774e-09,-2.43508e-13,-139887,-116.34], Tmin=(1239.48,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 720,
    label = "CCOC(=O)C(C=O)(OO)OC(=O)C(O)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {7,S} {8,S} {10,S}
2  C u0 p0 c0 {4,S} {9,S} {14,S} {15,S}
3  C u0 p0 c0 {6,S} {11,S} {12,S} {16,S}
4  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {9,S} {20,D}
6  C u0 p0 c0 {3,S} {8,S} {21,D}
7  C u0 p0 c0 {1,S} {22,D} {23,S}
8  O u0 p2 c0 {1,S} {6,S}
9  O u0 p2 c0 {2,S} {5,S}
10 O u0 p2 c0 {1,S} {13,S}
11 O u0 p2 c0 {3,S} {24,S}
12 O u0 p2 c0 {3,S} {25,S}
13 O u0 p2 c0 {10,S} {26,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {5,D}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {7,S}
24 O u1 p2 c0 {11,S}
25 H u0 p0 c0 {12,S}
26 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.75425,0.170111,-0.000183864,9.96957e-08,-2.14973e-11,-147002,63.116], Tmin=(100,'K'), Tmax=(1122.29,'K')),
            NASAPolynomial(coeffs=[29.8163,0.0504606,-2.39438e-05,4.69913e-09,-3.35876e-13,-154537,-102.716], Tmin=(1122.29,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 721,
    label = "CCOC(=O)C1(C=O)OC(=O)C([O])O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {6,S} {8,S} {13,S} {17,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {10,S} {18,D}
6  C u0 p0 c0 {3,S} {9,S} {19,D}
7  C u0 p0 c0 {1,S} {20,D} {21,S}
8  O u0 p2 c0 {1,S} {3,S}
9  O u0 p2 c0 {1,S} {6,S}
10 O u0 p2 c0 {2,S} {5,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u1 p2 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {3,S}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {6,D}
20 O u0 p2 c0 {7,D}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.11541,0.0848706,3.72993e-06,-7.49985e-08,3.64282e-11,-121128,47.1744], Tmin=(100,'K'), Tmax=(985.6,'K')),
            NASAPolynomial(coeffs=[28.5365,0.0296575,-1.13578e-05,2.24996e-09,-1.71572e-13,-130136,-111.496], Tmin=(985.6,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 722,
    label = "CCOC(=O)C(=O)OC(=O)[CH]O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {4,S} {7,S} {15,D}
4  C u0 p0 c0 {3,S} {8,S} {17,D}
5  C u0 p0 c0 {6,S} {8,S} {16,D}
6  C u1 p0 c0 {5,S} {9,S} {18,S}
7  O u0 p2 c0 {1,S} {3,S}
8  O u0 p2 c0 {4,S} {5,S}
9  O u0 p2 c0 {6,S} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 O u0 p2 c0 {3,D}
16 O u0 p2 c0 {5,D}
17 O u0 p2 c0 {4,D}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.34358,0.128506,-0.000192394,1.65329e-07,-5.79674e-11,-110513,44.101], Tmin=(100,'K'), Tmax=(761.67,'K')),
            NASAPolynomial(coeffs=[11.183,0.0537203,-2.73901e-05,5.39294e-09,-3.80083e-13,-112161,-11.2086], Tmin=(761.67,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 723,
    label = "CCOC(=O)C(=O)OC(=O)C(O)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {7,S} {11,S} {12,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {13,S}
3  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {8,S} {17,D}
5  C u0 p0 c0 {6,S} {7,S} {19,D}
6  C u0 p0 c0 {5,S} {8,S} {18,D}
7  O u0 p2 c0 {1,S} {5,S}
8  O u0 p2 c0 {4,S} {6,S}
9  O u0 p2 c0 {2,S} {20,S}
10 O u0 p2 c0 {2,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 O u0 p2 c0 {4,D}
18 O u0 p2 c0 {6,D}
19 O u0 p2 c0 {5,D}
20 O u1 p2 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.34877,0.154376,-0.000247243,2.19481e-07,-7.76621e-11,-126071,53.3294], Tmin=(100,'K'), Tmax=(793.86,'K')),
            NASAPolynomial(coeffs=[12.3642,0.0601373,-3.11892e-05,6.14027e-09,-4.30869e-13,-127774,-10.2653], Tmin=(793.86,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 724,
    label = "CCOC(=O)C1(C=O)OC(=O)C(O)O1",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {6,S} {8,S} {11,S} {14,S}
3  C u0 p0 c0 {4,S} {10,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {10,S} {18,D}
6  C u0 p0 c0 {2,S} {9,S} {19,D}
7  C u0 p0 c0 {1,S} {20,D} {21,S}
8  O u0 p2 c0 {1,S} {2,S}
9  O u0 p2 c0 {1,S} {6,S}
10 O u0 p2 c0 {3,S} {5,S}
11 O u0 p2 c0 {2,S} {22,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {6,D}
20 O u0 p2 c0 {7,D}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.33147,0.0875027,8.55324e-06,-8.44624e-08,4.05573e-11,-150433,47.1694], Tmin=(100,'K'), Tmax=(981.89,'K')),
            NASAPolynomial(coeffs=[30.1749,0.0297954,-1.12079e-05,2.2278e-09,-1.71292e-13,-160025,-121.595], Tmin=(981.89,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 725,
    label = "O=COC(=O)[CH]OOC(=O)C=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {10,D}
2  C u1 p0 c0 {1,S} {7,S} {11,S}
3  C u0 p0 c0 {4,S} {8,S} {9,D}
4  C u0 p0 c0 {3,S} {12,D} {13,S}
5  C u0 p0 c0 {6,S} {14,D} {15,S}
6  O u0 p2 c0 {1,S} {5,S}
7  O u0 p2 c0 {2,S} {8,S}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {3,D}
10 O u0 p2 c0 {1,D}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
14 O u0 p2 c0 {5,D}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.269628,0.0987036,-0.000104608,5.52244e-08,-1.18038e-11,-96043.5,40.5056], Tmin=(100,'K'), Tmax=(1114.97,'K')),
            NASAPolynomial(coeffs=[17.5415,0.0348057,-1.86452e-05,3.82514e-09,-2.79075e-13,-100015,-47.3611], Tmin=(1114.97,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 726,
    label = "O=COC(=O)[CH]O",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,S} {7,S}
2  O u0 p2 c0 {6,S} {10,S}
3  O u0 p2 c0 {5,D}
4  O u0 p2 c0 {7,D}
5  C u0 p0 c0 {1,S} {3,D} {6,S}
6  C u1 p0 c0 {2,S} {5,S} {8,S}
7  C u0 p0 c0 {1,S} {4,D} {9,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {7,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.67881,0.0552109,-7.18984e-05,5.21593e-08,-1.55463e-11,-65748.3,25.5066], Tmin=(100,'K'), Tmax=(811.96,'K')),
            NASAPolynomial(coeffs=[8.36848,0.0222545,-1.1014e-05,2.16851e-09,-1.53981e-13,-66834.6,-5.37358], Tmin=(811.96,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 727,
    label = "[O]OC(O)C(=O)OC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,D}
3  C u0 p0 c0 {4,S} {9,D} {10,S}
4  O u0 p2 c0 {2,S} {3,S}
5  O u0 p2 c0 {1,S} {11,S}
6  O u0 p2 c0 {1,S} {12,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
11 O u1 p2 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.583706,0.0822803,-0.000131695,1.1407e-07,-3.93039e-11,-81302.4,35.0492], Tmin=(100,'K'), Tmax=(792.2,'K')),
            NASAPolynomial(coeffs=[9.65978,0.0284698,-1.46906e-05,2.88584e-09,-2.0221e-13,-82489.9,-5.04231], Tmin=(792.2,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 728,
    label = "[O]OCC(=O)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,D}
3  O u0 p2 c0 {2,S} {5,S}
4  O u0 p2 c0 {1,S} {9,S}
5  O u0 p2 c0 {3,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  O u1 p2 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.8039,0.073612,-0.000114809,8.93645e-08,-2.67682e-11,-34671,23.8753], Tmin=(100,'K'), Tmax=(897.23,'K')),
            NASAPolynomial(coeffs=[12.6808,0.0146146,-6.06478e-06,1.05099e-09,-6.74235e-14,-36558.8,-30.7792], Tmin=(897.23,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 729,
    label = "CC1([O])OOC(O)(OC=O)C(=O)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {7,S} {8,S} {10,S}
2  C u0 p0 c0 {3,S} {6,S} {9,S} {11,S}
3  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {6,S} {15,D}
5  C u0 p0 c0 {7,S} {16,D} {17,S}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {1,S} {5,S}
8  O u0 p2 c0 {1,S} {9,S}
9  O u0 p2 c0 {2,S} {8,S}
10 O u0 p2 c0 {1,S} {18,S}
11 O u1 p2 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {4,D}
16 O u0 p2 c0 {5,D}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.084368,0.0836021,-5.22024e-05,1.36841e-08,-1.32786e-12,-121740,38.1519], Tmin=(100,'K'), Tmax=(1963.5,'K')),
            NASAPolynomial(coeffs=[32.2597,0.025469,-1.37182e-05,2.62964e-09,-1.76561e-13,-135937,-143.521], Tmin=(1963.5,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 730,
    label = "CC(OO)OC(=O)C1OC1C(=O)COO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {8,S} {15,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {14,S}
3  C u0 p0 c0 {5,S} {9,S} {10,S} {16,S}
4  C u0 p0 c0 {6,S} {11,S} {20,S} {21,S}
5  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {1,S} {4,S} {22,D}
7  C u0 p0 c0 {2,S} {9,S} {23,D}
8  O u0 p2 c0 {1,S} {2,S}
9  O u0 p2 c0 {3,S} {7,S}
10 O u0 p2 c0 {3,S} {12,S}
11 O u0 p2 c0 {4,S} {13,S}
12 O u0 p2 c0 {10,S} {24,S}
13 O u0 p2 c0 {11,S} {25,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 O u0 p2 c0 {6,D}
23 O u0 p2 c0 {7,D}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.46268,0.14881,-0.000144604,7.08914e-08,-1.36706e-11,-101132,57.7486], Tmin=(100,'K'), Tmax=(1263.27,'K')),
            NASAPolynomial(coeffs=[30.8767,0.040078,-1.54963e-05,2.75737e-09,-1.8698e-13,-109808,-115.944], Tmin=(1263.27,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 731,
    label = "CC(OO)OC(=O)C(OO)C(O[O])C(=O)COO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {12,S} {17,S}
2  C u0 p0 c0 {1,S} {7,S} {9,S} {16,S}
3  C u0 p0 c0 {5,S} {8,S} {10,S} {18,S}
4  C u0 p0 c0 {6,S} {11,S} {22,S} {23,S}
5  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {4,S} {24,D}
7  C u0 p0 c0 {2,S} {8,S} {25,D}
8  O u0 p2 c0 {3,S} {7,S}
9  O u0 p2 c0 {2,S} {13,S}
10 O u0 p2 c0 {3,S} {14,S}
11 O u0 p2 c0 {4,S} {15,S}
12 O u0 p2 c0 {1,S} {26,S}
13 O u0 p2 c0 {9,S} {28,S}
14 O u0 p2 c0 {10,S} {29,S}
15 O u0 p2 c0 {11,S} {27,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 O u0 p2 c0 {6,D}
25 O u0 p2 c0 {7,D}
26 O u1 p2 c0 {12,S}
27 H u0 p0 c0 {15,S}
28 H u0 p0 c0 {13,S}
29 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.39776,0.197213,-0.000234028,1.44951e-07,-3.64519e-11,-107662,69.7825], Tmin=(100,'K'), Tmax=(958.09,'K')),
            NASAPolynomial(coeffs=[25.8686,0.0708456,-3.61748e-05,7.27151e-09,-5.24619e-13,-113461,-74.9377], Tmin=(958.09,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 732,
    label = "CC(OO)OC(=O)C1OC=C(COO)O1",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {9,S} {11,S} {15,S}
2  C u0 p0 c0 {6,S} {8,S} {10,S} {16,S}
3  C u0 p0 c0 {5,S} {12,S} {20,S} {21,S}
4  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {7,D} {8,S}
6  C u0 p0 c0 {2,S} {9,S} {22,D}
7  C u0 p0 c0 {5,D} {10,S} {23,S}
8  O u0 p2 c0 {2,S} {5,S}
9  O u0 p2 c0 {1,S} {6,S}
10 O u0 p2 c0 {2,S} {7,S}
11 O u0 p2 c0 {1,S} {13,S}
12 O u0 p2 c0 {3,S} {14,S}
13 O u0 p2 c0 {11,S} {24,S}
14 O u0 p2 c0 {12,S} {25,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 O u0 p2 c0 {6,D}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {13,S}
25 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.28284,0.131091,-6.66676e-05,-2.62047e-08,2.34876e-11,-113770,53.0067], Tmin=(100,'K'), Tmax=(992.89,'K')),
            NASAPolynomial(coeffs=[37.8109,0.0300875,-1.15942e-05,2.29366e-09,-1.7447e-13,-125112,-160.976], Tmin=(992.89,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 733,
    label = "CC(OO)OC(=O)C1OC=C(C[O])O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {9,S} {11,S} {13,S}
2  C u0 p0 c0 {6,S} {8,S} {10,S} {14,S}
3  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {7,D} {8,S}
6  C u0 p0 c0 {2,S} {9,S} {21,D}
7  C u0 p0 c0 {5,D} {10,S} {22,S}
8  O u0 p2 c0 {2,S} {5,S}
9  O u0 p2 c0 {1,S} {6,S}
10 O u0 p2 c0 {2,S} {7,S}
11 O u0 p2 c0 {1,S} {12,S}
12 O u0 p2 c0 {11,S} {23,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 O u1 p2 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {6,D}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.22221,0.111127,-4.66737e-05,-3.1208e-08,2.22451e-11,-95265.5,49.2998], Tmin=(100,'K'), Tmax=(1003,'K')),
            NASAPolynomial(coeffs=[31.8713,0.0317867,-1.27045e-05,2.50207e-09,-1.87415e-13,-104953,-129.483], Tmin=(1003,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 734,
    label = "CC(OO)OC(=O)C1O[C]=C(CO)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {8,S} {10,S} {14,S}
2  C u0 p0 c0 {6,S} {7,S} {9,S} {15,S}
3  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
4  C u0 p0 c0 {5,S} {12,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {7,S} {11,D}
6  C u0 p0 c0 {2,S} {8,S} {21,D}
7  O u0 p2 c0 {2,S} {5,S}
8  O u0 p2 c0 {1,S} {6,S}
9  O u0 p2 c0 {2,S} {11,S}
10 O u0 p2 c0 {1,S} {13,S}
11 C u1 p0 c0 {5,D} {9,S}
12 O u0 p2 c0 {4,S} {22,S}
13 O u0 p2 c0 {10,S} {23,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {6,D}
22 H u0 p0 c0 {12,S}
23 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.34892,0.115354,-6.04471e-05,-1.82663e-08,1.82821e-11,-93573.6,52.0213], Tmin=(100,'K'), Tmax=(998.29,'K')),
            NASAPolynomial(coeffs=[32.2132,0.0298462,-1.15667e-05,2.24934e-09,-1.67873e-13,-103114,-127.883], Tmin=(998.29,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 735,
    label = "CC(OO)OC(=O)C1OC(CO)=C(O[O])O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {9,S} {11,S} {15,S}
2  C u0 p0 c0 {7,S} {8,S} {10,S} {16,S}
3  C u0 p0 c0 {5,S} {12,S} {20,S} {21,S}
4  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {6,D} {8,S}
6  C u0 p0 c0 {5,D} {10,S} {13,S}
7  C u0 p0 c0 {2,S} {9,S} {22,D}
8  O u0 p2 c0 {2,S} {5,S}
9  O u0 p2 c0 {1,S} {7,S}
10 O u0 p2 c0 {2,S} {6,S}
11 O u0 p2 c0 {1,S} {14,S}
12 O u0 p2 c0 {3,S} {23,S}
13 O u0 p2 c0 {6,S} {24,S}
14 O u0 p2 c0 {11,S} {25,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {12,S}
24 O u1 p2 c0 {13,S}
25 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.38965,0.149929,-0.000146208,7.01625e-08,-1.32355e-11,-108026,57.2231], Tmin=(100,'K'), Tmax=(1285.9,'K')),
            NASAPolynomial(coeffs=[32.1696,0.0393156,-1.7177e-05,3.26673e-09,-2.29835e-13,-117171,-123.271], Tmin=(1285.9,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 736,
    label = "CC(OO)OC(=O)C1O[C](CO)C(=O)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {9,S} {11,S} {14,S}
2  C u0 p0 c0 {6,S} {8,S} {10,S} {15,S}
3  C u0 p0 c0 {5,S} {12,S} {19,S} {20,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u1 p0 c0 {3,S} {7,S} {8,S}
6  C u0 p0 c0 {2,S} {9,S} {21,D}
7  C u0 p0 c0 {5,S} {10,S} {22,D}
8  O u0 p2 c0 {2,S} {5,S}
9  O u0 p2 c0 {1,S} {6,S}
10 O u0 p2 c0 {2,S} {7,S}
11 O u0 p2 c0 {1,S} {13,S}
12 O u0 p2 c0 {3,S} {23,S}
13 O u0 p2 c0 {11,S} {24,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 O u0 p2 c0 {6,D}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {12,S}
24 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.55406,0.118595,-9.17744e-05,3.48685e-08,-5.38596e-12,-128064,54.0693], Tmin=(100,'K'), Tmax=(1493.18,'K')),
            NASAPolynomial(coeffs=[23.6077,0.0511917,-2.40634e-05,4.63748e-09,-3.24494e-13,-135578,-77.4092], Tmin=(1493.18,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 737,
    label = "CC(OO)OC(=O)C1OC(=O)C(=CO)O1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {9,S} {11,S} {14,S}
2  C u0 p0 c0 {5,S} {8,S} {10,S} {15,S}
3  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
4  C u0 p0 c0 {6,S} {7,D} {8,S}
5  C u0 p0 c0 {2,S} {9,S} {19,D}
6  C u0 p0 c0 {4,S} {10,S} {20,D}
7  C u0 p0 c0 {4,D} {12,S} {21,S}
8  O u0 p2 c0 {2,S} {4,S}
9  O u0 p2 c0 {1,S} {5,S}
10 O u0 p2 c0 {2,S} {6,S}
11 O u0 p2 c0 {1,S} {13,S}
12 O u0 p2 c0 {7,S} {22,S}
13 O u0 p2 c0 {11,S} {23,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 O u0 p2 c0 {5,D}
20 O u0 p2 c0 {6,D}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {12,S}
23 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.87615,0.127571,-8.66649e-05,3.88282e-09,1.1417e-11,-134401,51.4498], Tmin=(100,'K'), Tmax=(1007.36,'K')),
            NASAPolynomial(coeffs=[34.6675,0.0275985,-1.09202e-05,2.14495e-09,-1.60683e-13,-144456,-142.319], Tmin=(1007.36,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 738,
    label = "CC(OO)OC(=O)C1OC(=O)C(CO)(O[O])O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {6,S} {8,S} {12,S}
2  C u0 p0 c0 {5,S} {9,S} {11,S} {15,S}
3  C u0 p0 c0 {7,S} {8,S} {10,S} {16,S}
4  C u0 p0 c0 {1,S} {13,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {10,S} {23,D}
7  C u0 p0 c0 {3,S} {9,S} {22,D}
8  O u0 p2 c0 {1,S} {3,S}
9  O u0 p2 c0 {2,S} {7,S}
10 O u0 p2 c0 {3,S} {6,S}
11 O u0 p2 c0 {2,S} {14,S}
12 O u0 p2 c0 {1,S} {24,S}
13 O u0 p2 c0 {4,S} {25,S}
14 O u0 p2 c0 {11,S} {26,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u0 p2 c0 {7,D}
23 O u0 p2 c0 {6,D}
24 O u1 p2 c0 {12,S}
25 H u0 p0 c0 {13,S}
26 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.89931,0.150483,-0.000120633,3.55777e-08,-2.71516e-13,-148427,61.6276], Tmin=(100,'K'), Tmax=(1075.25,'K')),
            NASAPolynomial(coeffs=[36.2085,0.0385288,-1.64183e-05,3.18177e-09,-2.30238e-13,-159205,-144.792], Tmin=(1075.25,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 739,
    label = "CC([O])OC(=O)C1OC(=O)C(=CO)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {8,S} {10,S} {14,S}
2  C u0 p0 c0 {3,S} {9,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {6,S} {7,D} {8,S}
5  C u0 p0 c0 {1,S} {9,S} {18,D}
6  C u0 p0 c0 {4,S} {10,S} {19,D}
7  C u0 p0 c0 {4,D} {11,S} {20,S}
8  O u0 p2 c0 {1,S} {4,S}
9  O u0 p2 c0 {2,S} {5,S}
10 O u0 p2 c0 {1,S} {6,S}
11 O u0 p2 c0 {7,S} {21,S}
12 O u1 p2 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {6,D}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.81933,0.107645,-6.67629e-05,-1.06597e-09,1.01828e-11,-115896,47.7569], Tmin=(100,'K'), Tmax=(1024.87,'K')),
            NASAPolynomial(coeffs=[28.7868,0.0292017,-1.19768e-05,2.34098e-09,-1.72619e-13,-124323,-111.159], Tmin=(1024.87,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 740,
    label = "CC1OC(=O)C2O[C](C(=O)O2)C(O)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {8,S} {10,S} {13,S}
2  C u0 p0 c0 {5,S} {8,S} {12,S} {15,S}
3  C u0 p0 c0 {6,S} {9,S} {11,S} {14,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u1 p0 c0 {2,S} {7,S} {9,S}
6  C u0 p0 c0 {3,S} {10,S} {19,D}
7  C u0 p0 c0 {5,S} {11,S} {20,D}
8  O u0 p2 c0 {1,S} {2,S}
9  O u0 p2 c0 {3,S} {5,S}
10 O u0 p2 c0 {1,S} {6,S}
11 O u0 p2 c0 {3,S} {7,S}
12 O u0 p2 c0 {2,S} {21,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {6,D}
20 O u0 p2 c0 {7,D}
21 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.318489,0.0929184,-5.86949e-05,1.62214e-08,-1.73324e-12,-116392,41.2846], Tmin=(100,'K'), Tmax=(2149.24,'K')),
            NASAPolynomial(coeffs=[32.1873,0.0324211,-1.64726e-05,3.12456e-09,-2.09818e-13,-130364,-140.408], Tmin=(2149.24,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 741,
    label = "O=COC(=O)C1OC(=O)C(=CO)O1",
    molecule = 
"""
1  O u0 p2 c0 {8,S} {9,S}
2  O u0 p2 c0 {8,S} {11,S}
3  O u0 p2 c0 {10,S} {13,S}
4  O u0 p2 c0 {12,S} {17,S}
5  O u0 p2 c0 {10,D}
6  O u0 p2 c0 {11,D}
7  O u0 p2 c0 {13,D}
8  C u0 p0 c0 {1,S} {2,S} {10,S} {14,S}
9  C u0 p0 c0 {1,S} {11,S} {12,D}
10 C u0 p0 c0 {3,S} {5,D} {8,S}
11 C u0 p0 c0 {2,S} {6,D} {9,S}
12 C u0 p0 c0 {4,S} {9,D} {15,S}
13 C u0 p0 c0 {3,S} {7,D} {16,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {12,S}
16 H u0 p0 c0 {13,S}
17 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.11507,0.0912795,-4.97584e-05,-2.07915e-08,1.93661e-11,-128253,42.8083], Tmin=(100,'K'), Tmax=(965.68,'K')),
            NASAPolynomial(coeffs=[30.2382,0.011368,-3.23208e-06,6.61031e-10,-5.67058e-14,-136638,-119.419], Tmin=(965.68,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 742,
    label = "O=COC(=O)C1O[C](CO)C(=O)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {7,S} {8,S} {11,S}
2  C u0 p0 c0 {3,S} {10,S} {12,S} {13,S}
3  C u1 p0 c0 {2,S} {5,S} {7,S}
4  C u0 p0 c0 {1,S} {9,S} {14,D}
5  C u0 p0 c0 {3,S} {8,S} {15,D}
6  C u0 p0 c0 {9,S} {16,D} {17,S}
7  O u0 p2 c0 {1,S} {3,S}
8  O u0 p2 c0 {1,S} {5,S}
9  O u0 p2 c0 {4,S} {6,S}
10 O u0 p2 c0 {2,S} {18,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 O u0 p2 c0 {4,D}
15 O u0 p2 c0 {5,D}
16 O u0 p2 c0 {6,D}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0859937,0.0856874,-6.64875e-05,2.51591e-08,-3.84425e-12,-121903,46.4853], Tmin=(100,'K'), Tmax=(1518.2,'K')),
            NASAPolynomial(coeffs=[19.1701,0.0349549,-1.63648e-05,3.15009e-09,-2.20173e-13,-127750,-54.4549], Tmin=(1518.2,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 743,
    label = "[O]OC1(CO)OC(C(=O)OC=O)OC1=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {10,S}
2  C u0 p0 c0 {5,S} {7,S} {8,S} {13,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {14,S}
4  C u0 p0 c0 {1,S} {8,S} {16,D}
5  C u0 p0 c0 {2,S} {9,S} {15,D}
6  C u0 p0 c0 {9,S} {17,D} {18,S}
7  O u0 p2 c0 {1,S} {2,S}
8  O u0 p2 c0 {2,S} {4,S}
9  O u0 p2 c0 {5,S} {6,S}
10 O u0 p2 c0 {1,S} {19,S}
11 O u0 p2 c0 {3,S} {20,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {5,D}
16 O u0 p2 c0 {4,D}
17 O u0 p2 c0 {6,D}
18 H u0 p0 c0 {6,S}
19 O u1 p2 c0 {10,S}
20 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.0884,0.113679,-8.23293e-05,9.73631e-09,7.86333e-12,-142281,52.8027], Tmin=(100,'K'), Tmax=(1010.78,'K')),
            NASAPolynomial(coeffs=[31.1256,0.023362,-9.32427e-06,1.83492e-09,-1.37426e-13,-151096,-118.183], Tmin=(1010.78,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 744,
    label = "O=CC(OO)OC(=O)CC1OCC1=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {8,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {7,S} {9,S} {10,S} {15,S}
4  C u0 p0 c0 {5,S} {8,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {4,S} {18,D}
6  C u0 p0 c0 {2,S} {9,S} {19,D}
7  C u0 p0 c0 {3,S} {20,D} {21,S}
8  O u0 p2 c0 {1,S} {4,S}
9  O u0 p2 c0 {3,S} {6,S}
10 O u0 p2 c0 {3,S} {11,S}
11 O u0 p2 c0 {10,S} {22,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u0 p2 c0 {5,D}
19 O u0 p2 c0 {6,D}
20 O u0 p2 c0 {7,D}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.48592,0.112334,-8.81418e-05,3.31085e-08,-4.96802e-12,-99196.7,49.8964], Tmin=(100,'K'), Tmax=(1558.14,'K')),
            NASAPolynomial(coeffs=[26.2277,0.0411893,-1.96518e-05,3.80444e-09,-2.66281e-13,-107833,-96.0966], Tmin=(1558.14,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 745,
    label = "CCOC(=O)C1(O[O])OC(=O)COC1O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {8,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {10,S} {14,S} {15,S}
4  C u0 p0 c0 {7,S} {8,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {10,S} {22,D}
7  C u0 p0 c0 {4,S} {9,S} {21,D}
8  O u0 p2 c0 {2,S} {4,S}
9  O u0 p2 c0 {1,S} {7,S}
10 O u0 p2 c0 {3,S} {6,S}
11 O u0 p2 c0 {1,S} {23,S}
12 O u0 p2 c0 {2,S} {24,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {7,D}
22 O u0 p2 c0 {6,D}
23 O u1 p2 c0 {11,S}
24 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.73162,0.119492,-5.09967e-05,-3.00501e-08,2.12527e-11,-133825,48.4005], Tmin=(100,'K'), Tmax=(1037.08,'K')),
            NASAPolynomial(coeffs=[34.7107,0.0351639,-1.59327e-05,3.27492e-09,-2.47474e-13,-144822,-149.179], Tmin=(1037.08,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 746,
    label = "CCOC(=O)C1(OO)OC(=O)[CH]OC1O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {8,S} {11,S}
2  C u0 p0 c0 {1,S} {10,S} {12,S} {14,S}
3  C u0 p0 c0 {4,S} {9,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {9,S} {20,D}
6  C u1 p0 c0 {7,S} {10,S} {22,S}
7  C u0 p0 c0 {6,S} {8,S} {21,D}
8  O u0 p2 c0 {1,S} {7,S}
9  O u0 p2 c0 {3,S} {5,S}
10 O u0 p2 c0 {2,S} {6,S}
11 O u0 p2 c0 {1,S} {13,S}
12 O u0 p2 c0 {2,S} {23,S}
13 O u0 p2 c0 {11,S} {24,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {5,D}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {12,S}
24 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.30898,0.130274,-6.62125e-05,-2.44447e-08,2.151e-11,-130380,49.1577], Tmin=(100,'K'), Tmax=(1023.32,'K')),
            NASAPolynomial(coeffs=[38.972,0.0296039,-1.33384e-05,2.79745e-09,-2.15864e-13,-142416,-172.325], Tmin=(1023.32,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 747,
    label = "CCOC(=O)C12OC(=O)C(OC1O)O2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {9,S} {12,S} {13,S}
3  C u0 p0 c0 {7,S} {8,S} {9,S} {16,S}
4  C u0 p0 c0 {5,S} {11,S} {14,S} {15,S}
5  C u0 p0 c0 {4,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {1,S} {11,S} {20,D}
7  C u0 p0 c0 {3,S} {10,S} {21,D}
8  O u0 p2 c0 {1,S} {3,S}
9  O u0 p2 c0 {2,S} {3,S}
10 O u0 p2 c0 {1,S} {7,S}
11 O u0 p2 c0 {4,S} {6,S}
12 O u0 p2 c0 {2,S} {22,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.27565,0.0829367,2.69203e-05,-1.04484e-07,4.72911e-11,-151264,40.4857], Tmin=(100,'K'), Tmax=(988.5,'K')),
            NASAPolynomial(coeffs=[31.4564,0.02946,-1.17724e-05,2.4353e-09,-1.90961e-13,-161594,-136.566], Tmin=(988.5,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 748,
    label = "CCOC(=O)C1(OO)OC(=O)C(O[O])OC1O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {8,S} {12,S} {15,S}
3  C u0 p0 c0 {7,S} {8,S} {13,S} {18,S}
4  C u0 p0 c0 {5,S} {10,S} {16,S} {17,S}
5  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {10,S} {22,D}
7  C u0 p0 c0 {3,S} {9,S} {23,D}
8  O u0 p2 c0 {2,S} {3,S}
9  O u0 p2 c0 {1,S} {7,S}
10 O u0 p2 c0 {4,S} {6,S}
11 O u0 p2 c0 {1,S} {14,S}
12 O u0 p2 c0 {2,S} {25,S}
13 O u0 p2 c0 {3,S} {24,S}
14 O u0 p2 c0 {11,S} {26,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u0 p2 c0 {6,D}
23 O u0 p2 c0 {7,D}
24 O u1 p2 c0 {13,S}
25 H u0 p0 c0 {12,S}
26 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.13602,0.152939,-0.000119437,3.40483e-08,-6.71755e-13,-150994,57.386], Tmin=(100,'K'), Tmax=(1143.42,'K')),
            NASAPolynomial(coeffs=[39.0646,0.039006,-1.87688e-05,3.80338e-09,-2.79238e-13,-163304,-167.454], Tmin=(1143.42,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 749,
    label = "O=C1C=COO1",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {6,S}
2 C u0 p0 c0 {1,D} {4,S} {8,S}
3 C u0 p0 c0 {1,S} {5,S} {7,D}
4 O u0 p2 c0 {2,S} {5,S}
5 O u0 p2 c0 {3,S} {4,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {3,D}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72532,-0.0182189,0.000125766,-1.58854e-07,6.15833e-11,-22437.7,13.8736], Tmin=(100,'K'), Tmax=(933.05,'K')),
            NASAPolynomial(coeffs=[15.3098,-0.00547785,4.96181e-06,-8.59485e-10,4.484e-14,-27315.9,-55.7687], Tmin=(933.05,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 750,
    label = "[O]OC1COOC1=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,D}
4  O u0 p2 c0 {2,S} {5,S}
5  O u0 p2 c0 {3,S} {4,S}
6  O u0 p2 c0 {1,S} {11,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.02742,0.0170885,8.9272e-05,-1.36969e-07,5.54875e-11,-38228.9,25.7014], Tmin=(100,'K'), Tmax=(950.26,'K')),
            NASAPolynomial(coeffs=[20.0304,0.00789826,-1.33692e-06,3.45164e-10,-3.95413e-14,-44656.9,-76.0535], Tmin=(950.26,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 751,
    label = "O=C1C[C-]=[O+]O1",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {4,S} {8,D}
3 C u0 p1 c-1 {1,S} {5,D}
4 O u0 p2 c0 {2,S} {5,S}
5 O u0 p1 c+1 {3,D} {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.25888,0.00844173,4.02275e-05,-4.83933e-08,1.60292e-11,-202.05,25.8532], Tmin=(100,'K'), Tmax=(1071.74,'K')),
            NASAPolynomial(coeffs=[5.16996,0.0230093,-1.05324e-05,2.07335e-09,-1.49732e-13,-1857.96,10.6867], Tmin=(1071.74,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 752,
    label = "[O]C(=O)C(C=O)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,D}
3  C u0 p0 c0 {1,S} {9,D} {10,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {11,S}
6  H u0 p0 c0 {1,S}
7  O u1 p2 c0 {2,S}
8  O u0 p2 c0 {2,D}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.26718,0.0475469,-8.31161e-06,-9.1261e-08,1.01098e-10,-50881.4,24.1899], Tmin=(100,'K'), Tmax=(427.28,'K')),
            NASAPolynomial(coeffs=[4.98197,0.0363943,-1.92277e-05,3.88923e-09,-2.80331e-13,-51243.6,11.8776], Tmin=(427.28,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 753,
    label = "O=C(O)OO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {5,S} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 O u0 p2 c0 {5,D}
5 C u0 p0 c0 {1,S} {2,S} {4,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.35126,0.0467568,-5.72298e-05,3.09491e-08,-6.0655e-12,-65920.8,17.0351], Tmin=(100,'K'), Tmax=(1468.73,'K')),
            NASAPolynomial(coeffs=[16.0271,-0.00257102,2.70644e-06,-5.94946e-10,4.22654e-14,-69222.3,-55.9723], Tmin=(1468.73,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 754,
    label = "CCOC(=O)C1([O])OOC(O)C(=O)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {6,S} {8,S} {10,S} {12,S}
2  C u0 p0 c0 {4,S} {7,S} {13,S} {14,S}
3  C u0 p0 c0 {5,S} {9,S} {11,S} {15,S}
4  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {8,S} {19,D}
6  C u0 p0 c0 {1,S} {7,S} {20,D}
7  O u0 p2 c0 {2,S} {6,S}
8  O u0 p2 c0 {1,S} {5,S}
9  O u0 p2 c0 {3,S} {10,S}
10 O u0 p2 c0 {1,S} {9,S}
11 O u0 p2 c0 {3,S} {21,S}
12 O u1 p2 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {5,D}
20 O u0 p2 c0 {6,D}
21 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.13954,0.101751,-6.94128e-05,2.12346e-08,-2.53015e-12,-123759,44.9687], Tmin=(100,'K'), Tmax=(1954.08,'K')),
            NASAPolynomial(coeffs=[32.667,0.0325484,-1.62912e-05,3.11124e-09,-2.11476e-13,-136971,-140.776], Tmin=(1954.08,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 755,
    label = "CCOC(=O)C(=O)OOC(O)C([O])=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {7,S} {11,S} {12,S}
2  C u0 p0 c0 {6,S} {8,S} {10,S} {13,S}
3  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {5,S} {7,S} {18,D}
5  C u0 p0 c0 {4,S} {9,S} {20,D}
6  C u0 p0 c0 {2,S} {17,S} {19,D}
7  O u0 p2 c0 {1,S} {4,S}
8  O u0 p2 c0 {2,S} {9,S}
9  O u0 p2 c0 {5,S} {8,S}
10 O u0 p2 c0 {2,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 O u1 p2 c0 {6,S}
18 O u0 p2 c0 {4,D}
19 O u0 p2 c0 {6,D}
20 O u0 p2 c0 {5,D}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.871142,0.119464,-0.000111256,5.47613e-08,-1.15517e-11,-133244,46.1871], Tmin=(100,'K'), Tmax=(1085.71,'K')),
            NASAPolynomial(coeffs=[14.5044,0.0628172,-3.2994e-05,6.70568e-09,-4.8623e-13,-136582,-29.2556], Tmin=(1085.71,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 756,
    label = "O=CC(OO)OC(=O)C1CC(=O)OO1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {8,S} {12,S}
2  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
3  C u0 p0 c0 {6,S} {7,S} {9,S} {15,S}
4  C u0 p0 c0 {1,S} {7,S} {16,D}
5  C u0 p0 c0 {2,S} {10,S} {17,D}
6  C u0 p0 c0 {3,S} {18,D} {19,S}
7  O u0 p2 c0 {3,S} {4,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {3,S} {11,S}
10 O u0 p2 c0 {5,S} {8,S}
11 O u0 p2 c0 {9,S} {20,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 O u0 p2 c0 {4,D}
17 O u0 p2 c0 {5,D}
18 O u0 p2 c0 {6,D}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.06347,0.0861536,-8.78772e-06,-5.37817e-08,2.62295e-11,-118170,49.4635], Tmin=(100,'K'), Tmax=(1033.88,'K')),
            NASAPolynomial(coeffs=[26.6716,0.0349285,-1.58318e-05,3.22566e-09,-2.4191e-13,-126902,-99.7615], Tmin=(1033.88,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 757,
    label = "CCOC(=O)C(=O)OO[CH]O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {4,S} {6,S} {16,D}
4  C u0 p0 c0 {3,S} {7,S} {15,D}
5  C u1 p0 c0 {8,S} {9,S} {17,S}
6  O u0 p2 c0 {1,S} {3,S}
7  O u0 p2 c0 {4,S} {8,S}
8  O u0 p2 c0 {5,S} {7,S}
9  O u0 p2 c0 {5,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 O u0 p2 c0 {4,D}
16 O u0 p2 c0 {3,D}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.9672,0.110025,-0.000112006,5.72654e-08,-1.17686e-11,-90441.1,38.8367], Tmin=(100,'K'), Tmax=(1165.29,'K')),
            NASAPolynomial(coeffs=[20.2521,0.0371862,-1.8245e-05,3.62363e-09,-2.602e-13,-95386.4,-66.7796], Tmin=(1165.29,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 758,
    label = "CCOC(=O)C1CC(=O)C(O)O1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {6,S} {8,S} {10,S} {16,S}
4  C u0 p0 c0 {5,S} {9,S} {14,S} {15,S}
5  C u0 p0 c0 {4,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {2,S} {3,S} {20,D}
7  C u0 p0 c0 {1,S} {9,S} {21,D}
8  O u0 p2 c0 {1,S} {3,S}
9  O u0 p2 c0 {4,S} {7,S}
10 O u0 p2 c0 {3,S} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 O u0 p2 c0 {6,D}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.603155,0.0843717,-2.90085e-05,-1.7381e-08,1.06609e-11,-109646,43.2525], Tmin=(100,'K'), Tmax=(1100.59,'K')),
            NASAPolynomial(coeffs=[19.4108,0.0443786,-1.9131e-05,3.66926e-09,-2.61269e-13,-116035,-64.2315], Tmin=(1100.59,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 759,
    label = "O=C1O[CH]OC2(CO)OC1OC2=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {5,S} {7,S} {9,S} {12,S}
3  C u0 p0 c0 {1,S} {11,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {9,S} {16,D}
5  C u0 p0 c0 {2,S} {10,S} {15,D}
6  C u1 p0 c0 {8,S} {10,S} {17,S}
7  O u0 p2 c0 {1,S} {2,S}
8  O u0 p2 c0 {1,S} {6,S}
9  O u0 p2 c0 {2,S} {4,S}
10 O u0 p2 c0 {5,S} {6,S}
11 O u0 p2 c0 {3,S} {18,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {5,D}
16 O u0 p2 c0 {4,D}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.462988,0.0749489,-2.95247e-06,-5.42541e-08,2.60666e-11,-124922,31.2522], Tmin=(100,'K'), Tmax=(1021.29,'K')),
            NASAPolynomial(coeffs=[24.6651,0.0291147,-1.28654e-05,2.63094e-09,-1.99069e-13,-132797,-103.931], Tmin=(1021.29,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 760,
    label = "O=[C]C1OC(=O)C(CO)(OC=O)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {9,S} {11,S} {12,S}
3  C u0 p0 c0 {6,S} {8,S} {10,S} {13,S}
4  C u0 p0 c0 {1,S} {8,S} {14,D}
5  C u0 p0 c0 {7,S} {15,D} {16,S}
6  O u0 p2 c0 {1,S} {3,S}
7  O u0 p2 c0 {1,S} {5,S}
8  O u0 p2 c0 {3,S} {4,S}
9  O u0 p2 c0 {2,S} {18,S}
10 C u1 p0 c0 {3,S} {17,D}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 O u0 p2 c0 {5,D}
16 H u0 p0 c0 {5,S}
17 O u0 p2 c0 {10,D}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.660907,0.0741238,1.33185e-05,-8.40419e-08,4.01426e-11,-125154,43.1652], Tmin=(100,'K'), Tmax=(975.83,'K')),
            NASAPolynomial(coeffs=[29.409,0.0190915,-6.96359e-06,1.46348e-09,-1.19286e-13,-134271,-117.813], Tmin=(975.83,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 761,
    label = "O=COC1(CO)O[CH]OC1=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {8,S} {12,D}
4  C u1 p0 c0 {6,S} {8,S} {13,S}
5  C u0 p0 c0 {7,S} {14,D} {15,S}
6  O u0 p2 c0 {1,S} {4,S}
7  O u0 p2 c0 {1,S} {5,S}
8  O u0 p2 c0 {3,S} {4,S}
9  O u0 p2 c0 {2,S} {16,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {3,D}
13 H u0 p0 c0 {4,S}
14 O u0 p2 c0 {5,D}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.174994,0.0625586,3.009e-05,-1.03306e-07,4.88463e-11,-105792,35.2347], Tmin=(100,'K'), Tmax=(947.2,'K')),
            NASAPolynomial(coeffs=[29.8621,0.00896234,-1.03223e-06,2.41347e-10,-3.15959e-14,-114768,-125.393], Tmin=(947.2,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 762,
    label = "[O]OC(=O)C1OC(=O)C(CO)(OC=O)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {5,S} {7,S} {9,S} {14,S}
3  C u0 p0 c0 {1,S} {10,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {9,S} {15,D}
5  C u0 p0 c0 {2,S} {11,S} {16,D}
6  C u0 p0 c0 {8,S} {17,D} {18,S}
7  O u0 p2 c0 {1,S} {2,S}
8  O u0 p2 c0 {1,S} {6,S}
9  O u0 p2 c0 {2,S} {4,S}
10 O u0 p2 c0 {3,S} {19,S}
11 O u0 p2 c0 {5,S} {20,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {2,S}
15 O u0 p2 c0 {4,D}
16 O u0 p2 c0 {5,D}
17 O u0 p2 c0 {6,D}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {10,S}
20 O u1 p2 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.0929,0.110114,-6.05612e-05,-2.1375e-08,2.13649e-11,-143127,49.2384], Tmin=(100,'K'), Tmax=(964.57,'K')),
            NASAPolynomial(coeffs=[33.4353,0.0188667,-5.88059e-06,1.11286e-09,-8.71384e-14,-152590,-134.407], Tmin=(964.57,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 763,
    label = "[O]C(=O)C1OC(=O)C(CO)(OC=O)O1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {9,S} {10,S}
2  O u0 p2 c0 {10,S} {12,S}
3  O u0 p2 c0 {9,S} {14,S}
4  O u0 p2 c0 {11,S} {19,S}
5  O u0 p2 c0 {12,D}
6  O u1 p2 c0 {13,S}
7  O u0 p2 c0 {13,D}
8  O u0 p2 c0 {14,D}
9  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
10 C u0 p0 c0 {1,S} {2,S} {13,S} {15,S}
11 C u0 p0 c0 {4,S} {9,S} {16,S} {17,S}
12 C u0 p0 c0 {2,S} {5,D} {9,S}
13 C u0 p0 c0 {6,S} {7,D} {10,S}
14 C u0 p0 c0 {3,S} {8,D} {18,S}
15 H u0 p0 c0 {10,S}
16 H u0 p0 c0 {11,S}
17 H u0 p0 c0 {11,S}
18 H u0 p0 c0 {14,S}
19 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.872674,0.0815363,-3.23852e-06,-6.07783e-08,2.95507e-11,-148561,44.7258], Tmin=(100,'K'), Tmax=(1012.47,'K')),
            NASAPolynomial(coeffs=[27.1029,0.0295223,-1.28617e-05,2.63463e-09,-2.00558e-13,-157225,-105.397], Tmin=(1012.47,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 764,
    label = "[O]C12OOC(=O)C(O1)OC2(CO)OC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {8,S} {10,S} {13,S}
3  C u0 p0 c0 {5,S} {7,S} {8,S} {16,S}
4  C u0 p0 c0 {1,S} {12,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {11,S} {17,D}
6  C u0 p0 c0 {9,S} {18,D} {19,S}
7  O u0 p2 c0 {1,S} {3,S}
8  O u0 p2 c0 {2,S} {3,S}
9  O u0 p2 c0 {1,S} {6,S}
10 O u0 p2 c0 {2,S} {11,S}
11 O u0 p2 c0 {5,S} {10,S}
12 O u0 p2 c0 {4,S} {20,S}
13 O u1 p2 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {3,S}
17 O u0 p2 c0 {5,D}
18 O u0 p2 c0 {6,D}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.35825,0.0876036,4.28987e-06,-7.71589e-08,3.6475e-11,-139104,41.9256], Tmin=(100,'K'), Tmax=(1010.59,'K')),
            NASAPolynomial(coeffs=[30.9364,0.029604,-1.32633e-05,2.7907e-09,-2.1641e-13,-149197,-131.859], Tmin=(1010.59,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 765,
    label = "O=COC1(CO)OC(C(=O)OO)OC1=O",
    molecule = 
"""
1  O u0 p2 c0 {10,S} {11,S}
2  O u0 p2 c0 {10,S} {15,S}
3  O u0 p2 c0 {11,S} {13,S}
4  O u0 p2 c0 {12,S} {20,S}
5  O u0 p2 c0 {6,S} {14,S}
6  O u0 p2 c0 {5,S} {21,S}
7  O u0 p2 c0 {13,D}
8  O u0 p2 c0 {14,D}
9  O u0 p2 c0 {15,D}
10 C u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
11 C u0 p0 c0 {1,S} {3,S} {14,S} {18,S}
12 C u0 p0 c0 {4,S} {10,S} {16,S} {17,S}
13 C u0 p0 c0 {3,S} {7,D} {10,S}
14 C u0 p0 c0 {5,S} {8,D} {11,S}
15 C u0 p0 c0 {2,S} {9,D} {19,S}
16 H u0 p0 c0 {12,S}
17 H u0 p0 c0 {12,S}
18 H u0 p0 c0 {11,S}
19 H u0 p0 c0 {15,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.38079,0.113978,-5.67499e-05,-2.96279e-08,2.47257e-11,-166494,49.5133], Tmin=(100,'K'), Tmax=(969.79,'K')),
            NASAPolynomial(coeffs=[35.3045,0.020046,-6.59262e-06,1.28739e-09,-1.01758e-13,-176696,-146.052], Tmin=(969.79,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 766,
    label = "O=[C]C(CO)(OC=O)OC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {11,D} {13,S}
4  C u0 p0 c0 {6,S} {12,D} {14,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {1,S} {4,S}
7  C u1 p0 c0 {1,S} {15,D}
8  O u0 p2 c0 {2,S} {16,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 O u0 p2 c0 {7,D}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.838815,0.0895094,-6.249e-05,2.51072e-09,8.72488e-12,-106628,40.0696], Tmin=(100,'K'), Tmax=(995.93,'K')),
            NASAPolynomial(coeffs=[26.4567,0.0159995,-6.17376e-06,1.22765e-09,-9.38973e-14,-113856,-100.497], Tmin=(995.93,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 767,
    label = "O=CO[C](CO)OC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {5,S} {6,S}
3  C u0 p0 c0 {5,S} {10,D} {12,S}
4  C u0 p0 c0 {6,S} {11,D} {13,S}
5  O u0 p2 c0 {2,S} {3,S}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {1,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 O u0 p2 c0 {3,D}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.30326,0.0628864,-4.71083e-05,1.71262e-08,-2.57822e-12,-85718.2,30.7603], Tmin=(100,'K'), Tmax=(1482.45,'K')),
            NASAPolynomial(coeffs=[12.674,0.0322057,-1.60645e-05,3.1657e-09,-2.23942e-13,-89089.5,-28.5735], Tmin=(1482.45,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 768,
    label = "[O]OC(=O)C(CO)(OC=O)OC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {9,S} {12,D}
4  C u0 p0 c0 {6,S} {13,D} {15,S}
5  C u0 p0 c0 {7,S} {14,D} {16,S}
6  O u0 p2 c0 {1,S} {4,S}
7  O u0 p2 c0 {1,S} {5,S}
8  O u0 p2 c0 {2,S} {17,S}
9  O u0 p2 c0 {3,S} {18,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {3,D}
13 O u0 p2 c0 {4,D}
14 O u0 p2 c0 {5,D}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {8,S}
18 O u1 p2 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.20199,0.123536,-0.000133047,6.51641e-08,-1.11947e-11,-125240,45.756], Tmin=(100,'K'), Tmax=(1022.1,'K')),
            NASAPolynomial(coeffs=[29.7509,0.0178846,-6.46169e-06,1.1658e-09,-8.25232e-14,-132785,-114.053], Tmin=(1022.1,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 769,
    label = "O=COC(=CO)OC=O",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {5,S} {6,S}
2  C u0 p0 c0 {1,D} {7,S} {8,S}
3  C u0 p0 c0 {5,S} {9,D} {11,S}
4  C u0 p0 c0 {6,S} {10,D} {12,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {1,S} {4,S}
7  O u0 p2 c0 {2,S} {13,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.257499,0.0871837,-9.71815e-05,5.12815e-08,-1.04366e-11,-94577.8,27.9648], Tmin=(100,'K'), Tmax=(1207.78,'K')),
            NASAPolynomial(coeffs=[21.7461,0.0143109,-6.67724e-06,1.32525e-09,-9.61135e-14,-99892.9,-82.3437], Tmin=(1207.78,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 770,
    label = "O=COC(=O)CO",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {7,S}
2  O u0 p2 c0 {5,S} {11,S}
3  O u0 p2 c0 {6,D}
4  O u0 p2 c0 {7,D}
5  C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
6  C u0 p0 c0 {1,S} {3,D} {5,S}
7  C u0 p0 c0 {1,S} {4,D} {10,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.78612,0.0512878,-5.23655e-05,2.88213e-08,-6.57137e-12,-82406.4,25.3611], Tmin=(100,'K'), Tmax=(1040.66,'K')),
            NASAPolynomial(coeffs=[9.3186,0.0223351,-1.06331e-05,2.08671e-09,-1.48844e-13,-83974.2,-11.279], Tmin=(1040.66,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 771,
    label = "O=COC(=O)C(O)C=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,D}
3  C u0 p0 c0 {1,S} {9,D} {10,S}
4  C u0 p0 c0 {5,S} {11,D} {12,S}
5  O u0 p2 c0 {2,S} {4,S}
6  O u0 p2 c0 {1,S} {13,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.18271,0.0672087,-7.50249e-05,4.66242e-08,-1.2141e-11,-98245.2,33.0488], Tmin=(100,'K'), Tmax=(913.96,'K')),
            NASAPolynomial(coeffs=[9.50124,0.030801,-1.52701e-05,3.03602e-09,-2.17728e-13,-99765.7,-6.33459], Tmin=(913.96,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 772,
    label = "[O]OC(CO)(OC=O)OC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {11,D} {13,S}
4  C u0 p0 c0 {6,S} {12,D} {14,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {1,S} {4,S}
7  O u0 p2 c0 {1,S} {15,S}
8  O u0 p2 c0 {2,S} {16,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {7,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.0341497,0.0952574,-0.000121997,9.26526e-08,-2.97269e-11,-105174,38.0349], Tmin=(100,'K'), Tmax=(749.04,'K')),
            NASAPolynomial(coeffs=[9.29314,0.045817,-2.29979e-05,4.54808e-09,-3.23581e-13,-106561,-3.95967], Tmin=(749.04,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 773,
    label = "O=COC(=O)OC=CO",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {5,S} {9,S}
2  C u0 p0 c0 {1,D} {7,S} {8,S}
3  C u0 p0 c0 {5,S} {6,S} {10,D}
4  C u0 p0 c0 {6,S} {11,D} {12,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {3,S} {4,S}
7  O u0 p2 c0 {2,S} {13,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 O u0 p2 c0 {3,D}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.76676,0.0966436,-0.000110238,5.54004e-08,-1.00991e-11,-100475,36.7004], Tmin=(100,'K'), Tmax=(1583.27,'K')),
            NASAPolynomial(coeffs=[30.3358,-0.004528,4.62418e-06,-9.6998e-10,6.58947e-14,-108125,-124.984], Tmin=(1583.27,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 774,
    label = "[O]C1OOC(O)C(=O)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {11,D}
4  O u0 p2 c0 {2,S} {3,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {2,S} {5,S}
7  O u0 p2 c0 {1,S} {12,S}
8  H u0 p0 c0 {1,S}
9  O u1 p2 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.67277,0.0359064,1.7269e-06,-1.52436e-08,4.32026e-12,-77398.9,21.1541], Tmin=(100,'K'), Tmax=(1615.4,'K')),
            NASAPolynomial(coeffs=[15.7481,0.0309977,-1.92209e-05,3.92753e-09,-2.75687e-13,-85207.2,-59.2906], Tmin=(1615.4,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 775,
    label = "[O]C(=O)C(O)OOC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,D}
3  C u0 p0 c0 {6,S} {10,D} {11,S}
4  O u0 p2 c0 {1,S} {6,S}
5  O u0 p2 c0 {1,S} {12,S}
6  O u0 p2 c0 {3,S} {4,S}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {2,S}
9  O u0 p2 c0 {2,D}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.815765,0.0620043,-4.68112e-05,1.60096e-08,-2.13899e-12,-88420.5,32.3796], Tmin=(100,'K'), Tmax=(1762.21,'K')),
            NASAPolynomial(coeffs=[20.2154,0.0179701,-9.32964e-06,1.82999e-09,-1.27392e-13,-95257.8,-72.2039], Tmin=(1762.21,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 776,
    label = "C=C(CC)OC=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {6,S}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  C u0 p0 c0 {6,S} {14,D} {15,S}
6  O u0 p2 c0 {3,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 O u0 p2 c0 {5,D}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.887067,0.0590564,-3.53435e-05,6.43885e-09,8.01531e-13,-43014.2,25.2291], Tmin=(100,'K'), Tmax=(1207.72,'K')),
            NASAPolynomial(coeffs=[14.479,0.0269739,-1.15612e-05,2.17854e-09,-1.52181e-13,-47240.5,-46.8146], Tmin=(1207.72,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 777,
    label = "[O]C1OOC(=O)C(CO)(OC=O)O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {6,S} {8,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {9,S} {15,D}
5  C u0 p0 c0 {7,S} {16,D} {17,S}
6  O u0 p2 c0 {1,S} {3,S}
7  O u0 p2 c0 {1,S} {5,S}
8  O u0 p2 c0 {3,S} {9,S}
9  O u0 p2 c0 {4,S} {8,S}
10 O u0 p2 c0 {2,S} {18,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u1 p2 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {4,D}
16 O u0 p2 c0 {5,D}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.853861,0.0832033,-1.72153e-05,-3.77019e-08,1.82989e-11,-127430,38.917], Tmin=(100,'K'), Tmax=(1110.1,'K')),
            NASAPolynomial(coeffs=[26.9079,0.0336174,-1.83797e-05,3.93482e-09,-2.97253e-13,-136702,-111.918], Tmin=(1110.1,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 778,
    label = "[O]C(CO)(OC=O)C(=O)OOC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {13,D}
4  C u0 p0 c0 {6,S} {15,D} {17,S}
5  C u0 p0 c0 {9,S} {14,D} {16,S}
6  O u0 p2 c0 {1,S} {4,S}
7  O u0 p2 c0 {3,S} {9,S}
8  O u0 p2 c0 {2,S} {18,S}
9  O u0 p2 c0 {5,S} {7,S}
10 O u1 p2 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {3,D}
14 O u0 p2 c0 {5,D}
15 O u0 p2 c0 {4,D}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.81583,0.0952656,-1.28029e-05,-7.88853e-08,4.34754e-11,-136690,48.8542], Tmin=(100,'K'), Tmax=(956.56,'K')),
            NASAPolynomial(coeffs=[38.1272,0.00808677,-1.30729e-06,3.67178e-10,-4.40847e-14,-147985,-161.169], Tmin=(956.56,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 779,
    label = "O=COO[CH]O",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {3,S} {5,S} {6,S}
2 C u0 p0 c0 {4,S} {7,D} {8,S}
3 O u0 p2 c0 {1,S} {4,S}
4 O u0 p2 c0 {2,S} {3,S}
5 O u0 p2 c0 {1,S} {9,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.47541,0.0438805,-1.84182e-05,-1.72631e-08,1.19727e-11,-45650.7,22.3052], Tmin=(100,'K'), Tmax=(971.48,'K')),
            NASAPolynomial(coeffs=[17.3512,0.00586495,-1.9533e-06,4.19583e-10,-3.58258e-14,-50026,-60.4701], Tmin=(971.48,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

