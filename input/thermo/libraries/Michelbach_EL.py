#!/usr/bin/env python
# encoding: utf-8

name = "Michelbach_EL"
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
    label = "CCOC(=O)CCC(C)=O",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {10,S}
2  O u0 p2 c0 {9,D}
3  O u0 p2 c0 {10,D}
4  C u0 p0 c0 {5,S} {9,S} {13,S} {14,S}
5  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
7  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
8  C u0 p0 c0 {9,S} {20,S} {21,S} {22,S}
9  C u0 p0 c0 {2,D} {4,S} {8,S}
10 C u0 p0 c0 {1,S} {3,D} {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
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
    index = 1,
    label = "[CH2]C(=O)CCC(=O)OCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {7,S} {18,D}
6  C u0 p0 c0 {2,S} {8,S} {19,D}
7  C u1 p0 c0 {5,S} {20,S} {21,S}
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
    index = 2,
    label = "CCOC(=O)C[CH]C(C)=O",
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
    index = 3,
    label = "CCOC(=O)[CH]CC(C)=O",
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
    index = 4,
    label = "C[CH]OC(=O)CCC(C)=O",
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
    index = 5,
    label = "[CH2]COC(=O)CCC(C)=O",
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
    index = 6,
    label = "CC(=O)CCC(=O)O",
    molecule = 
"""
1  O u0 p2 c0 {8,S} {16,S}
2  O u0 p2 c0 {7,D}
3  O u0 p2 c0 {8,D}
4  C u0 p0 c0 {5,S} {7,S} {9,S} {10,S}
5  C u0 p0 c0 {4,S} {8,S} {11,S} {12,S}
6  C u0 p0 c0 {7,S} {13,S} {14,S} {15,S}
7  C u0 p0 c0 {2,D} {4,S} {6,S}
8  C u0 p0 c0 {1,S} {3,D} {5,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {1,S}
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
    index = 7,
    label = "CC(=O)CCC([O])=O",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {7,D}
2  O u1 p2 c0 {8,S}
3  O u0 p2 c0 {8,D}
4  C u0 p0 c0 {5,S} {7,S} {9,S} {10,S}
5  C u0 p0 c0 {4,S} {8,S} {11,S} {12,S}
6  C u0 p0 c0 {7,S} {13,S} {14,S} {15,S}
7  C u0 p0 c0 {1,D} {4,S} {6,S}
8  C u0 p0 c0 {2,S} {3,D} {5,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
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
    index = 8,
    label = "CCOC(=O)CC[C]=O",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,S} {8,S}
2  O u0 p2 c0 {8,D}
3  O u0 p2 c0 {9,D}
4  C u0 p0 c0 {6,S} {8,S} {10,S} {11,S}
5  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {9,S} {14,S} {15,S}
7  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
8  C u0 p0 c0 {1,S} {2,D} {4,S}
9  C u1 p0 c0 {3,D} {6,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
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
    index = 9,
    label = "[CH2]C(=O)OCC",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {5,D}
3  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
4  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
5  C u0 p0 c0 {1,S} {2,D} {6,S}
6  C u1 p0 c0 {5,S} {12,S} {13,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
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

