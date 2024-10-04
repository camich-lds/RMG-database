#!/usr/bin/env python
# encoding: utf-8

name = "Ghosh_EL"
shortDesc = ""
longDesc = """
Manik Kumer Ghosh, Mícheál Séamus Howard, Yingjia Zhang, Khalil Djebbi, Gianluca Capriolo, Aamir Farooq, Henry J. Curran, Stephen Dooley,
The combustion kinetics of the lignocellulosic biofuel, ethyl levulinate,
Combustion and Flame,
Volume 193,
2018,
Pages 157-169,
https://doi.org/10.1016/j.combustflame.2018.02.028.
"""
entry(
    index = 0,
    label = "EL",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {10,S}
2  O u0 p2 c0 {9,D}
3  O u0 p2 c0 {10,D}
4  C u0 p0 c0 {5,S} {9,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {10,S} {13,S} {14,S}
6  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
7  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
8  C u0 p0 c0 {9,S} {20,S} {21,S} {22,S}
9  C u0 p0 c0 {2,D} {4,S} {8,S}
10 C u0 p0 c0 {1,S} {3,D} {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
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
    label = "EL1J",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {7,D} {18,S}
6  C u0 p0 c0 {2,S} {8,S} {19,D}
7  C u0 p0 c0 {5,D} {20,S} {21,S}
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
18 O u1 p2 c0 {5,S}
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
    label = "EL3J",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {7,S} {11,S} {12,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {6,D} {20,S}
6  C u0 p0 c0 {4,S} {5,D} {19,S}
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
19 O u1 p2 c0 {6,S}
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
            NASAPolynomial(coeffs=[-3.57328,0.106131,-8.97042e-05,3.87046e-08,-6.71428e-12,-57336.2,52.3946], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[26.3217,0.0282819,-1.07074e-05,1.86592e-09,-1.18112e-13,-66867.9,-105.239], Tmin=(1393,'K'), Tmax=(5000,'K')),
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
            NASAPolynomial(coeffs=[-4.07291,0.113374,-0.000104917,4.97538e-08,-9.27668e-12,-55633.9,54.657], Tmin=(298,'K'), Tmax=(1405,'K')),
            NASAPolynomial(coeffs=[26.0058,0.0268924,-8.68913e-06,1.29807e-09,-7.33156e-14,-64371.6,-100.987], Tmin=(1405,'K'), Tmax=(5000,'K')),
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
    index = 6,
    label = "ELCOJ",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,S} {8,S}
2  O u0 p2 c0 {8,D}
3  O u0 p2 c0 {9,D}
4  C u0 p0 c0 {5,S} {8,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {9,S} {12,S} {13,S}
6  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
7  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
8  C u0 p0 c0 {1,S} {2,D} {4,S}
9  C u1 p0 c0 {3,D} {5,S}
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
    index = 7,
    label = "CH3COCH2CH2COJ",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,D}
2  O u0 p2 c0 {7,D}
3  C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {7,S} {10,S} {11,S}
5  C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
6  C u0 p0 c0 {1,D} {3,S} {5,S}
7  C u1 p0 c0 {2,D} {4,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01831,0.045044,-2.81199e-05,8.71054e-09,-9.49266e-13,-26320.2,14.4174], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[20.8272,0.0143618,-8.55021e-06,3.22963e-09,-3.14616e-13,-33146.6,-79.2029], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    label = "C5H8O3",
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
    index = 9,
    label = "CH3COCH2CHCO",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  O u0 p2 c0 {7,D}
3  C u0 p0 c0 {5,S} {6,S} {8,S} {9,S}
4  C u0 p0 c0 {5,S} {10,S} {11,S} {12,S}
5  C u0 p0 c0 {1,D} {3,S} {4,S}
6  C u0 p0 c0 {3,S} {7,D} {13,S}
7  C u0 p0 c0 {2,D} {6,D}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.16344,0.0438809,-2.82126e-05,8.68755e-09,-9.55691e-13,-31187.6,10.8817], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[18.7955,0.0174586,-1.1407e-05,3.8673e-09,-3.58946e-13,-37200.4,-70.7868], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 10,
    label = "EF",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {5,D}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
4  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
5  C u0 p0 c0 {1,S} {2,D} {11,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.44296,0.00762357,2.67908e-05,-2.46164e-08,6.09316e-12,-49814.8,-6.81274], Tmin=(298,'K'), Tmax=(1478,'K')),
            NASAPolynomial(coeffs=[12.6152,0.0163875,-5.83402e-06,9.30327e-10,-5.49919e-14,-53724.7,-42.0403], Tmin=(1478,'K'), Tmax=(5000,'K')),
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
    index = 11,
    label = "EFP",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u1 p0 c0 {1,S} {7,S} {8,S}
3  C u0 p0 c0 {4,S} {9,D} {10,S}
4  O u0 p2 c0 {1,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.14444,0.0459778,-3.56327e-05,1.41627e-08,-2.27601e-12,-23815.1,35.5386], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[12.447,0.0127063,-4.28646e-06,6.60171e-10,-3.8114e-14,-28347.8,-36.8588], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 12,
    label = "EFF",
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
            NASAPolynomial(coeffs=[1.8544,0.0344694,-1.75356e-05,2.49608e-09,3.52506e-13,-25991.5,19.1289], Tmin=(298,'K'), Tmax=(1548,'K')),
            NASAPolynomial(coeffs=[13.5065,0.0120804,-4.13118e-06,6.42255e-10,-3.73273e-14,-30423.6,-45.0028], Tmin=(1548,'K'), Tmax=(5000,'K')),
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
    index = 13,
    label = "EFS",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u1 p0 c0 {1,S} {4,S} {8,S}
3  C u0 p0 c0 {4,S} {9,D} {10,S}
4  O u0 p2 c0 {2,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.00672091,0.044989,-3.15149e-05,1.01006e-08,-1.1486e-12,-24253.9,26.6239], Tmin=(298,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[15.2046,0.0108565,-3.75677e-06,5.88753e-10,-3.4411e-14,-29533.8,-55.2601], Tmin=(1384,'K'), Tmax=(5000,'K')),
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
    index = 14,
    label = "COJCH2CH2CO2H",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,S} {12,S}
2  O u0 p2 c0 {6,D}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {5,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {1,S} {2,D} {4,S}
7  C u1 p0 c0 {3,D} {5,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94533,0.043697,-3.43022e-05,1.41356e-08,-2.3804e-12,-50985.2,13.4816], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[15.8435,0.013813,-4.99536e-06,8.54957e-10,-5.38741e-14,-54910.1,-49.6815], Tmin=(1393,'K'), Tmax=(5000,'K')),
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
    index = 15,
    label = "COCHCH2CO2CH2CH3",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {7,S}
2  O u0 p2 c0 {7,D}
3  O u0 p2 c0 {9,D}
4  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {7,S} {8,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
7  C u0 p0 c0 {1,S} {2,D} {5,S}
8  C u0 p0 c0 {5,S} {9,D} {17,S}
9  C u0 p0 c0 {3,D} {8,D}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.221136,0.081372,-6.9485e-05,3.01694e-08,-5.25545e-12,-59935.2,29.9283], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[23.0696,0.0214039,-8.21139e-06,1.44043e-09,-9.13528e-14,-67162.7,-90.3664], Tmin=(1393,'K'), Tmax=(5000,'K')),
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
    index = 16,
    label = "C5H7O3-OJ",
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
    index = 17,
    label = "C5H7O3-2J",
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
            NASAPolynomial(coeffs=[2.36577,0.0617886,-4.90522e-05,2.03456e-08,-3.43962e-12,-55170.6,21.2532], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[19.7043,0.0182792,-6.43662e-06,1.05927e-09,-6.46522e-14,-60892.1,-70.802], Tmin=(1392,'K'), Tmax=(5000,'K')),
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
    index = 18,
    label = "C5H7O3-3J",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u1 p0 c0 {1,S} {4,S} {13,S}
4  C u0 p0 c0 {2,S} {3,S} {12,D}
5  C u0 p0 c0 {1,S} {6,S} {14,D}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {5,D}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.32278,0.0582789,-4.45721e-05,1.80672e-08,-3.00975e-12,-56416,20.8499], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[18.3176,0.0187708,-6.47289e-06,1.0567e-09,-6.4426e-14,-61770.2,-64.3159], Tmin=(1392,'K'), Tmax=(5000,'K')),
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
    index = 19,
    label = "C5H7O3-5J",
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
            NASAPolynomial(coeffs=[3.36695,0.0582348,-4.60906e-05,1.90907e-08,-3.22549e-12,-54348.5,16.4523], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[19.2581,0.0181566,-6.62471e-06,1.14195e-09,-7.23052e-14,-59571.4,-67.8454], Tmin=(1394,'K'), Tmax=(5000,'K')),
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
    index = 20,
    label = "EE2J",
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

