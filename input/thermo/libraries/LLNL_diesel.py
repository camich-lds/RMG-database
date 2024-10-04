#!/usr/bin/env python
# encoding: utf-8

name = "LLNL_diesel"
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
    label = "CC1=CC=C(C)C=C1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {5,B} {8,B}
4  C u0 p0 c0 {2,S} {6,B} {7,B}
5  C u0 p0 c0 {3,B} {6,B} {15,S}
6  C u0 p0 c0 {4,B} {5,B} {16,S}
7  C u0 p0 c0 {4,B} {8,B} {17,S}
8  C u0 p0 c0 {3,B} {7,B} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.00111,0.0740464,-4.5947e-05,1.38104e-08,-1.58639e-12,-94.4588,40.5388], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[18.9495,0.0273272,-9.45728e-06,1.48002e-09,-8.63505e-14,-8187.79,-78.9916], Tmin=(1386,'K'), Tmax=(5000,'K')),
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
    label = "CCCCCCCCCCCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {8,S} {27,S} {28,S}
8  C u0 p0 c0 {7,S} {10,S} {29,S} {30,S}
9  C u0 p0 c0 {1,S} {11,S} {13,S} {14,S}
10 C u0 p0 c0 {8,S} {12,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 C u0 p0 c0 {10,S} {36,S} {37,S} {38,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.62182,0.147238,-9.4397e-05,3.07441e-08,-4.03602e-12,-40065.4,50.0995], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[38.5095,0.056355,-1.91493e-05,2.96025e-09,-1.71244e-13,-54884.3,-172.671], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    label = "Cc1cc[c]cc1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {11,S}
4  C u0 p0 c0 {2,B} {6,B} {12,S}
5  C u0 p0 c0 {3,B} {7,B} {13,S}
6  C u0 p0 c0 {4,B} {7,B} {14,S}
7  C u1 p0 c0 {5,B} {6,B}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.53984,0.0611194,-3.16055e-05,1.04281e-09,2.86557e-12,34181.7,43.0769], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.5915,0.0224187,-7.13697e-06,1.08735e-09,-6.49369e-14,28819.5,-48.0783], Tmin=(1000,'K'), Tmax=(5000,'K')),
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
    label = "[CH2]c1ccc(C)cc1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,B} {5,B}
3  C u0 p0 c0 {6,B} {7,B} {8,S}
4  C u0 p0 c0 {2,B} {6,B} {13,S}
5  C u0 p0 c0 {2,B} {7,B} {14,S}
6  C u0 p0 c0 {3,B} {4,B} {12,S}
7  C u0 p0 c0 {3,B} {5,B} {15,S}
8  C u1 p0 c0 {3,S} {16,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.44083,0.0750205,-5.20941e-05,1.84357e-08,-2.67709e-12,18311.6,35.5997], Tmin=(298,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[20.1614,0.0241711,-8.46243e-06,1.33456e-09,-7.82792e-14,10221,-86.5598], Tmin=(1385,'K'), Tmax=(5000,'K')),
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
    label = "Cc1[c]cc(C)cc1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,B} {7,B}
4  C u0 p0 c0 {2,S} {6,B} {8,B}
5  C u0 p0 c0 {3,B} {6,B} {16,S}
6  C u0 p0 c0 {4,B} {5,B} {15,S}
7  C u0 p0 c0 {3,B} {8,B} {17,S}
8  C u1 p0 c0 {4,B} {7,B}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.07492,0.0702221,-4.70582e-05,1.63788e-08,-2.36671e-12,30453.7,37.462], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[17.7731,0.0256909,-8.87033e-06,1.38581e-09,-8.07516e-14,23318.2,-69.8837], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    label = "CC1=CC=CC=C1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {11,S}
4  C u0 p0 c0 {2,B} {7,B} {15,S}
5  C u0 p0 c0 {3,B} {6,B} {12,S}
6  C u0 p0 c0 {5,B} {7,B} {13,S}
7  C u0 p0 c0 {4,B} {6,B} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.08982,0.0686477,-4.74717e-05,1.67001e-08,-2.39578e-12,4499.38,43.4583], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[16.3092,0.0225332,-7.84282e-06,1.23201e-09,-7.20675e-14,-2758.04,-66.676], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    label = "[O]CC1=CC=CC=C1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {11,S}
4  C u0 p0 c0 {2,B} {7,B} {15,S}
5  C u0 p0 c0 {3,B} {6,B} {12,S}
6  C u0 p0 c0 {5,B} {7,B} {13,S}
7  C u0 p0 c0 {4,B} {6,B} {14,S}
8  O u1 p2 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.77737,0.0751049,-5.68533e-05,2.1829e-08,-3.38134e-12,12623.4,51.0429], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[17.8843,0.0209012,-7.21833e-06,1.1284e-09,-6.57955e-14,4931.83,-70.1305], Tmin=(1392,'K'), Tmax=(5000,'K')),
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
    label = "OCC1=CC=CC=C1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {11,S}
4  C u0 p0 c0 {2,B} {7,B} {15,S}
5  C u0 p0 c0 {3,B} {6,B} {12,S}
6  C u0 p0 c0 {5,B} {7,B} {13,S}
7  C u0 p0 c0 {4,B} {6,B} {14,S}
8  O u0 p2 c0 {1,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.04501,0.0757966,-5.64778e-05,2.15225e-08,-3.32437e-12,-13778.4,47.4803], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[18.3336,0.0224114,-7.68818e-06,1.19642e-09,-6.95416e-14,-21397.1,-72.2445], Tmin=(1393,'K'), Tmax=(5000,'K')),
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
    label = "[O]OCC1=CC=CC=C1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {5,B} {6,B}
5  C u0 p0 c0 {4,B} {7,B} {12,S}
6  C u0 p0 c0 {4,B} {9,B} {16,S}
7  C u0 p0 c0 {5,B} {8,B} {13,S}
8  C u0 p0 c0 {7,B} {9,B} {14,S}
9  C u0 p0 c0 {6,B} {8,B} {15,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.77864,0.0829485,-6.64288e-05,2.69505e-08,-4.41845e-12,12560.3,47.327], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[21.8946,0.0202701,-7.14525e-06,1.13209e-09,-6.66221e-14,3932.73,-89.5685], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    label = "OOCC1=CC=CC=C1",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {17,S}
3  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {5,B} {6,B}
5  C u0 p0 c0 {4,B} {7,B} {12,S}
6  C u0 p0 c0 {4,B} {9,B} {16,S}
7  C u0 p0 c0 {5,B} {8,B} {13,S}
8  C u0 p0 c0 {7,B} {9,B} {14,S}
9  C u0 p0 c0 {6,B} {8,B} {15,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.39515,0.0845307,-6.70634e-05,2.72113e-08,-4.4829e-12,-5787.31,45.7079], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[22.1951,0.0219901,-7.70453e-06,1.21574e-09,-7.13427e-14,-14396.7,-90.7484], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    label = "CC1=CC=C([O])C=C1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {12,S}
4  C u0 p0 c0 {2,B} {7,B} {15,S}
5  C u0 p0 c0 {3,B} {6,B} {13,S}
6  C u0 p0 c0 {5,B} {7,B} {11,S}
7  C u0 p0 c0 {4,B} {6,B} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 O u1 p2 c0 {6,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.03964,0.0739909,-5.15945e-05,1.20373e-08,1.4321e-12,225.708,45.3169], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.32623,0.0370921,-1.3737e-05,2.32847e-09,-1.49702e-13,-1566.36,-4.68621], Tmin=(1000,'K'), Tmax=(5000,'K')),
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
    label = "CC1=CC=C(O)C=C1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,B} {5,B}
3  C u0 p0 c0 {6,B} {7,B} {8,S}
4  C u0 p0 c0 {2,B} {6,B} {12,S}
5  C u0 p0 c0 {2,B} {7,B} {15,S}
6  C u0 p0 c0 {3,B} {4,B} {13,S}
7  C u0 p0 c0 {3,B} {5,B} {14,S}
8  O u0 p2 c0 {3,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.8386,0.07713,-5.33551e-05,1.2949e-08,1.09766e-12,-17273.9,43.5757], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.93692,0.0457992,-1.89178e-05,3.46244e-09,-2.34982e-13,-18225,7.47181], Tmin=(1000,'K'), Tmax=(5000,'K')),
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
    label = "Cc1ccc(CO[O])cc1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {7,B} {8,B}
4  C u0 p0 c0 {2,S} {5,B} {6,B}
5  C u0 p0 c0 {4,B} {7,B} {16,S}
6  C u0 p0 c0 {4,B} {8,B} {17,S}
7  C u0 p0 c0 {3,B} {5,B} {15,S}
8  C u0 p0 c0 {3,B} {6,B} {18,S}
9  O u0 p2 c0 {1,S} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 O u1 p2 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.282984,0.0755295,-4.79147e-05,1.4811e-08,-1.79585e-12,6664.25,32.7362], Tmin=(298,'K'), Tmax=(1381,'K')),
            NASAPolynomial(coeffs=[22.9655,0.0261982,-9.19916e-06,1.45359e-09,-8.53776e-14,-1962.41,-93.984], Tmin=(1381,'K'), Tmax=(5000,'K')),
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
    label = "Cc1ccc(C)c(O[O])c1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {5,B} {8,B}
4  C u0 p0 c0 {1,S} {6,B} {7,B}
5  C u0 p0 c0 {3,B} {6,B} {9,S}
6  C u0 p0 c0 {4,B} {5,B} {18,S}
7  C u0 p0 c0 {4,B} {8,B} {16,S}
8  C u0 p0 c0 {3,B} {7,B} {17,S}
9  O u0 p2 c0 {5,S} {19,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {6,S}
19 O u1 p2 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.289488,0.0801774,-5.767e-05,2.13527e-08,-3.243e-12,6231.58,31.59], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[23.3499,0.0252937,-8.75775e-06,1.37109e-09,-8.00203e-14,-2027.87,-95.5172], Tmin=(1388,'K'), Tmax=(5000,'K')),
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
    label = "Cc1ccc(C)c([O])c1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {5,B} {8,B}
4  C u0 p0 c0 {1,S} {6,B} {7,B}
5  C u0 p0 c0 {3,B} {6,B} {15,S}
6  C u0 p0 c0 {4,B} {5,B} {18,S}
7  C u0 p0 c0 {4,B} {8,B} {16,S}
8  C u0 p0 c0 {3,B} {7,B} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 O u1 p2 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.19831,0.0738252,-4.72443e-05,1.46487e-08,-1.75801e-12,-4487.43,35.034], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[21.5356,0.0251599,-8.81158e-06,1.38996e-09,-8.15443e-14,-12845.7,-88.671], Tmin=(1383,'K'), Tmax=(5000,'K')),
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
    label = "Cc1ccc(COO)cc1",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {20,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {6,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {8,B} {9,B}
6  C u0 p0 c0 {4,S} {7,B} {10,B}
7  C u0 p0 c0 {6,B} {8,B} {16,S}
8  C u0 p0 c0 {5,B} {7,B} {17,S}
9  C u0 p0 c0 {5,B} {10,B} {18,S}
10 C u0 p0 c0 {6,B} {9,B} {19,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.06987,0.0838088,-5.57145e-05,1.81805e-08,-2.33992e-12,-10215.9,35.6479], Tmin=(298,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[24.8705,0.0270785,-9.49239e-06,1.49832e-09,-8.79417e-14,-19615.5,-105.05], Tmin=(1384,'K'), Tmax=(5000,'K')),
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
    label = "Cc1ccc(C[O])cc1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {6,B} {7,B}
4  C u0 p0 c0 {2,S} {5,B} {8,B}
5  C u0 p0 c0 {4,B} {6,B} {15,S}
6  C u0 p0 c0 {3,B} {5,B} {16,S}
7  C u0 p0 c0 {3,B} {8,B} {17,S}
8  C u0 p0 c0 {4,B} {7,B} {18,S}
9  O u1 p2 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.89639,0.0744241,-4.69073e-05,1.40045e-08,-1.55079e-12,8374.71,38.3903], Tmin=(298,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[21.1703,0.0253464,-8.84887e-06,1.393e-09,-8.1609e-14,-101.622,-87.1745], Tmin=(1384,'K'), Tmax=(5000,'K')),
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
    label = "Cc1ccc(C=O)cc1",
    molecule = 
"""
1  O u0 p2 c0 {9,D}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {5,B} {6,B}
4  C u0 p0 c0 {7,B} {8,B} {9,S}
5  C u0 p0 c0 {3,B} {7,B} {13,S}
6  C u0 p0 c0 {3,B} {8,B} {16,S}
7  C u0 p0 c0 {4,B} {5,B} {14,S}
8  C u0 p0 c0 {4,B} {6,B} {15,S}
9  C u0 p0 c0 {1,D} {4,S} {17,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.76001,0.0748976,-5.20135e-05,1.76317e-08,-2.3173e-12,-10878.7,35.595], Tmin=(298,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[21.5356,0.022103,-7.56077e-06,1.17506e-09,-6.82595e-14,-19027.5,-89.9224], Tmin=(1385,'K'), Tmax=(5000,'K')),
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
    label = "Cc1ccc([C]=O)cc1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {9,D}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {5,B} {6,B}
4  C u0 p0 c0 {7,B} {8,B} {9,S}
5  C u0 p0 c0 {3,B} {7,B} {13,S}
6  C u0 p0 c0 {3,B} {8,B} {16,S}
7  C u0 p0 c0 {4,B} {5,B} {14,S}
8  C u0 p0 c0 {4,B} {6,B} {15,S}
9  C u1 p0 c0 {1,D} {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.530171,0.0703241,-5.16125e-05,1.9191e-08,-2.86547e-12,6515.72,29.2215], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[20.3485,0.0208606,-7.0979e-06,1.09876e-09,-6.3638e-14,-594.289,-82.5465], Tmin=(1393,'K'), Tmax=(5000,'K')),
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
    label = "[C]1=CC=CC=C1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {8,S}
2  C u0 p0 c0 {1,B} {5,B} {7,S}
3  C u0 p0 c0 {1,B} {4,B} {9,S}
4  C u0 p0 c0 {3,B} {6,B} {10,S}
5  C u0 p0 c0 {2,B} {6,B} {11,S}
6  C u1 p0 c0 {4,B} {5,B}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.210307,0.0204746,5.89743e-05,-1.01534e-07,4.47106e-11,39546.9,25.291], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.8445,0.0173212,-6.29233e-06,1.0237e-09,-6.16217e-14,35559.8,-35.3735], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 20,
    label = "C1=CC=CC=C1",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {6,B} {7,S}
2  C u0 p0 c0 {1,B} {3,B} {8,S}
3  C u0 p0 c0 {2,B} {4,B} {9,S}
4  C u0 p0 c0 {3,B} {5,B} {10,S}
5  C u0 p0 c0 {4,B} {6,B} {11,S}
6  C u0 p0 c0 {1,B} {5,B} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.18689,0.0630511,-4.82875e-05,1.89015e-08,-3.01017e-12,9099.5,45.0745], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[13.8673,0.0174152,-6.08384e-06,9.58141e-10,-5.61503e-14,2599.89,-56.8525], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 21,
    label = "Cc1ccc(C)c(O)c1",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {19,S}
2  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {6,B} {9,B}
5  C u0 p0 c0 {2,S} {7,B} {8,B}
6  C u0 p0 c0 {1,S} {4,B} {7,B}
7  C u0 p0 c0 {5,B} {6,B} {18,S}
8  C u0 p0 c0 {5,B} {9,B} {16,S}
9  C u0 p0 c0 {4,B} {8,B} {17,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.86444,0.0814756,-5.72869e-05,2.05832e-08,-3.00395e-12,-21863.8,36.2905], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[21.84,0.0267301,-9.19246e-06,1.43255e-09,-8.33371e-14,-30139,-91.2069], Tmin=(1394,'K'), Tmax=(5000,'K')),
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
    label = "[O]c1ccccc1",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,B} {7,B}
3  C u0 p0 c0 {2,B} {4,B} {8,S}
4  C u0 p0 c0 {3,B} {5,B} {9,S}
5  C u0 p0 c0 {4,B} {6,B} {10,S}
6  C u0 p0 c0 {5,B} {7,B} {11,S}
7  C u0 p0 c0 {2,B} {6,B} {12,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.56102,0.0698936,-6.18066e-05,2.76045e-08,-4.8941e-12,4836.71,45.507], Tmin=(298,'K'), Tmax=(1401,'K')),
            NASAPolynomial(coeffs=[15.9513,0.0152837,-5.26839e-06,8.22485e-10,-4.79123e-14,-1567.83,-62.2003], Tmin=(1401,'K'), Tmax=(5000,'K')),
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
    label = "Oc1ccccc1",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {13,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {8,S}
4  C u0 p0 c0 {2,B} {7,B} {12,S}
5  C u0 p0 c0 {3,B} {6,B} {9,S}
6  C u0 p0 c0 {5,B} {7,B} {10,S}
7  C u0 p0 c0 {4,B} {6,B} {11,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.48631,0.0722846,-6.19804e-05,2.67795e-08,-4.60013e-12,-12601.3,44.3728], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[17.1525,0.0160439,-5.46326e-06,8.46545e-10,-4.9076e-14,-19463.3,-69.6842], Tmin=(1397,'K'), Tmax=(5000,'K')),
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
    label = "[CH2]CCCCCCCCCCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {8,S} {27,S} {28,S}
8  C u0 p0 c0 {7,S} {10,S} {29,S} {30,S}
9  C u0 p0 c0 {1,S} {11,S} {13,S} {14,S}
10 C u0 p0 c0 {8,S} {12,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 C u1 p0 c0 {10,S} {36,S} {37,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.85029,0.142671,-9.18917e-05,3.00883e-08,-3.97454e-12,-15453,49.3702], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[38.0922,0.0542108,-1.84206e-05,2.84762e-09,-1.64732e-13,-29819.4,-166.883], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    label = "C[CH]CCCCCCCCCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {9,S} {27,S} {28,S}
8  C u0 p0 c0 {1,S} {10,S} {13,S} {14,S}
9  C u0 p0 c0 {7,S} {12,S} {29,S} {30,S}
10 C u0 p0 c0 {8,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {12,S} {34,S} {35,S} {36,S}
12 C u1 p0 c0 {9,S} {11,S} {37,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.36787,0.137355,-8.24076e-05,2.36422e-08,-2.47436e-12,-16766.1,48.3522], Tmin=(298,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[37.9688,0.0538719,-1.82171e-05,2.80775e-09,-1.62108e-13,-31214.5,-165.806], Tmin=(1385,'K'), Tmax=(5000,'K')),
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
    label = "CC[CH]CCCCCCCCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {8,S} {25,S} {26,S}
7  C u0 p0 c0 {1,S} {10,S} {13,S} {14,S}
8  C u0 p0 c0 {6,S} {12,S} {27,S} {28,S}
9  C u0 p0 c0 {11,S} {12,S} {29,S} {30,S}
10 C u0 p0 c0 {7,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u1 p0 c0 {8,S} {9,S} {37,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.36787,0.137355,-8.24076e-05,2.36422e-08,-2.47436e-12,-16766.1,48.3522], Tmin=(298,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[37.9688,0.0538719,-1.82171e-05,2.80775e-09,-1.62108e-13,-31214.5,-165.806], Tmin=(1385,'K'), Tmax=(5000,'K')),
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
    index = 27,
    label = "CCC[CH]CCCCCCCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {8,S} {23,S} {24,S}
6  C u0 p0 c0 {1,S} {10,S} {13,S} {14,S}
7  C u0 p0 c0 {9,S} {11,S} {25,S} {26,S}
8  C u0 p0 c0 {5,S} {12,S} {27,S} {28,S}
9  C u0 p0 c0 {7,S} {12,S} {29,S} {30,S}
10 C u0 p0 c0 {6,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {7,S} {34,S} {35,S} {36,S}
12 C u1 p0 c0 {8,S} {9,S} {37,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.36787,0.137355,-8.24076e-05,2.36422e-08,-2.47436e-12,-16766.1,48.3522], Tmin=(298,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[37.9688,0.0538719,-1.82171e-05,2.80775e-09,-1.62108e-13,-31214.5,-165.806], Tmin=(1385,'K'), Tmax=(5000,'K')),
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
    index = 28,
    label = "CCCC[CH]CCCCCCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {8,S} {21,S} {22,S}
5  C u0 p0 c0 {7,S} {9,S} {23,S} {24,S}
6  C u0 p0 c0 {1,S} {10,S} {13,S} {14,S}
7  C u0 p0 c0 {5,S} {11,S} {25,S} {26,S}
8  C u0 p0 c0 {4,S} {12,S} {27,S} {28,S}
9  C u0 p0 c0 {5,S} {12,S} {29,S} {30,S}
10 C u0 p0 c0 {6,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {7,S} {34,S} {35,S} {36,S}
12 C u1 p0 c0 {8,S} {9,S} {37,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.36787,0.137355,-8.24076e-05,2.36422e-08,-2.47436e-12,-16766.1,48.3522], Tmin=(298,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[37.9688,0.0538719,-1.82171e-05,2.80775e-09,-1.62108e-13,-31214.5,-165.806], Tmin=(1385,'K'), Tmax=(5000,'K')),
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
    index = 29,
    label = "CCCCC[CH]CCCCCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {4,S} {17,S} {18,S}
3  C u0 p0 c0 {5,S} {7,S} {23,S} {24,S}
4  C u0 p0 c0 {2,S} {8,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {9,S} {21,S} {22,S}
6  C u0 p0 c0 {1,S} {10,S} {13,S} {14,S}
7  C u0 p0 c0 {3,S} {11,S} {25,S} {26,S}
8  C u0 p0 c0 {4,S} {12,S} {27,S} {28,S}
9  C u0 p0 c0 {5,S} {12,S} {29,S} {30,S}
10 C u0 p0 c0 {6,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {7,S} {34,S} {35,S} {36,S}
12 C u1 p0 c0 {8,S} {9,S} {37,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.36787,0.137355,-8.24076e-05,2.36422e-08,-2.47436e-12,-16766.1,48.3522], Tmin=(298,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[37.9688,0.0538719,-1.82171e-05,2.80775e-09,-1.62108e-13,-31214.5,-165.806], Tmin=(1385,'K'), Tmax=(5000,'K')),
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
    index = 30,
    label = "[CH2]CCCCCCCCCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {8,S} {24,S} {25,S}
7  C u0 p0 c0 {1,S} {9,S} {12,S} {13,S}
8  C u0 p0 c0 {6,S} {10,S} {26,S} {27,S}
9  C u0 p0 c0 {7,S} {11,S} {28,S} {29,S}
10 C u0 p0 c0 {8,S} {30,S} {31,S} {32,S}
11 C u1 p0 c0 {9,S} {33,S} {34,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.5823,0.130324,-8.35408e-05,2.72126e-08,-3.5753e-12,-12571.3,46.4373], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[34.8306,0.0498968,-1.69602e-05,2.62239e-09,-1.51722e-13,-25696.4,-150.794], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 31,
    label = "[CH2]CCCCCCCCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {7,S} {21,S} {22,S}
6  C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {5,S} {9,S} {23,S} {24,S}
8  C u0 p0 c0 {6,S} {10,S} {25,S} {26,S}
9  C u0 p0 c0 {7,S} {27,S} {28,S} {29,S}
10 C u1 p0 c0 {8,S} {30,S} {31,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.31358,0.117973,-7.51843e-05,2.43331e-08,-3.17523e-12,-9689.68,43.501], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[31.5697,0.0455818,-1.54995e-05,2.39711e-09,-1.3871e-13,-21573.8,-134.709], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 32,
    label = "[CH2]CCCCCCCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {4,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {6,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {4,S} {8,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {9,S} {22,S} {23,S}
8  C u0 p0 c0 {6,S} {24,S} {25,S} {26,S}
9  C u1 p0 c0 {7,S} {27,S} {28,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.04387,0.105617,-6.682e-05,2.14486e-08,-2.77404e-12,-6808.19,40.5603], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[28.3098,0.0412657,-1.40383e-05,2.17175e-09,-1.25692e-13,-17451.6,-118.63], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 33,
    label = "[CH2]CC",
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
            NASAPolynomial(coeffs=[0.474365,0.031919,-1.7191e-05,4.45928e-09,-4.36675e-13,10631.5,23.2671], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[8.88635,0.0152273,-5.21906e-06,8.11259e-10,-4.71028e-14,7346.72,-23.0728], Tmin=(1386,'K'), Tmax=(5000,'K')),
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
    index = 34,
    label = "[CH2]CCCCCCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {8,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  C u1 p0 c0 {6,S} {24,S} {25,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.772759,0.093255,-5.84447e-05,1.8557e-08,-2.37127e-12,-3926.9,37.6131], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[25.051,0.036948,-1.25765e-05,1.94628e-09,-1.12669e-13,-13330.1,-102.557], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 35,
    label = "[CH2]CCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {12,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.320731,0.0434654,-2.40585e-05,6.28245e-09,-5.80113e-13,7714.91,25.7301], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[12.078,0.0196265,-6.71302e-06,1.04206e-09,-6.04469e-14,3225.5,-38.7719], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 36,
    label = "[CH2]CCCCCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  C u1 p0 c0 {5,S} {21,S} {22,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.49957,0.0808826,-5.00533e-05,1.56549e-08,-1.96616e-12,-1045.9,34.6564], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[21.7941,0.032628,-1.11138e-05,1.72067e-09,-9.96367e-14,-9209.38,-86.4954], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 37,
    label = "[CH2]CCCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u1 p0 c0 {3,S} {15,S} {16,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.994216,0.0599861,-3.78319e-05,1.21311e-08,-1.57043e-12,4976.98,33.5998], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[15.4992,0.0238273,-8.13845e-06,1.26221e-09,-7.3173e-14,-1009.89,-55.8564], Tmin=(1396,'K'), Tmax=(5000,'K')),
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
    index = 38,
    label = "[CH2]CCCCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u1 p0 c0 {4,S} {18,S} {19,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.204871,0.0683801,-4.14448e-05,1.26156e-08,-1.5312e-12,1832.8,31.6075], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[18.5385,0.0283108,-9.65307e-06,1.49548e-09,-8.66336e-14,-5092.99,-70.4491], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 39,
    label = "C=CC",
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
            NASAPolynomial(coeffs=[0.394615,0.0289108,-1.54887e-05,3.88814e-09,-3.3789e-13,1177.6,21.9004], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[8.01596,0.0137024,-4.6625e-06,7.21254e-10,-4.1737e-14,-1767.49,-20.0161], Tmin=(1388,'K'), Tmax=(5000,'K')),
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
    index = 40,
    label = "C=CCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.833377,0.0454141,-2.97609e-05,1.03518e-08,-1.51976e-12,-1491.62,29.4328], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[11.3457,0.0180843,-6.17277e-06,9.56926e-10,-5.54586e-14,-5886.59,-36.4627], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 41,
    label = "C=CCCCCCCCCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {7,S} {22,S} {23,S}
6  C u0 p0 c0 {1,S} {8,S} {12,S} {13,S}
7  C u0 p0 c0 {5,S} {9,S} {24,S} {25,S}
8  C u0 p0 c0 {6,S} {10,S} {26,S} {27,S}
9  C u0 p0 c0 {7,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {8,S} {11,D} {31,S}
11 C u0 p0 c0 {10,D} {32,S} {33,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.69654,0.13165,-8.77957e-05,3.01468e-08,-4.22584e-12,-21752.6,49.988], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[34.1377,0.0483102,-1.64025e-05,2.53434e-09,-1.46557e-13,-34817.1,-148.798], Tmin=(1392,'K'), Tmax=(5000,'K')),
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
    index = 42,
    label = "C=CCCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {14,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.06223,0.0574218,-3.74487e-05,1.27365e-08,-1.7961e-12,-4465.47,32.274], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[14.5852,0.0224072,-7.63348e-06,1.18189e-09,-6.84385e-14,-10089.8,-52.3684], Tmin=(1392,'K'), Tmax=(5000,'K')),
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
    index = 43,
    label = "C=CCCCCCCCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {6,S} {19,S} {20,S}
5  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {8,S} {21,S} {22,S}
7  C u0 p0 c0 {5,S} {9,S} {23,S} {24,S}
8  C u0 p0 c0 {6,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {7,S} {10,D} {28,S}
10 C u0 p0 c0 {9,D} {29,S} {30,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {10,S}
30 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.42902,0.119306,-7.94489e-05,2.72737e-08,-3.82718e-12,-18870.8,47.0571], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[30.8754,0.0439972,-1.49426e-05,2.30918e-09,-1.33551e-13,-30693.7,-132.705], Tmin=(1392,'K'), Tmax=(5000,'K')),
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
    index = 44,
    label = "C=CCCCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {6,D} {16,S}
6  C u0 p0 c0 {5,D} {17,S} {18,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.35275,0.0698655,-4.59408e-05,1.56967e-08,-2.21296e-12,-7343.69,35.3121], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[17.8338,0.0267378,-9.10037e-06,1.4082e-09,-8.15124e-14,-14206.3,-68.3819], Tmin=(1392,'K'), Tmax=(5000,'K')),
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
    index = 45,
    label = "C=CCCCCCCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {5,S} {16,S} {17,S}
4  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {7,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {8,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {6,S} {9,D} {25,S}
9  C u0 p0 c0 {8,D} {26,S} {27,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.16108,0.106958,-7.10973e-05,2.43971e-08,-3.42772e-12,-15989.1,44.1245], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[27.6142,0.0396825,-1.34819e-05,2.0839e-09,-1.20539e-13,-26570.9,-116.619], Tmin=(1392,'K'), Tmax=(5000,'K')),
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
    index = 46,
    label = "C=CCCCCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {7,D} {19,S}
7  C u0 p0 c0 {6,D} {20,S} {21,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.67721,0.0824612,-5.46504e-05,1.87862e-08,-2.65738e-12,-10216.9,38.5068], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[21.0898,0.0310608,-1.05645e-05,1.63406e-09,-9.45598e-14,-18326,-84.4391], Tmin=(1392,'K'), Tmax=(5000,'K')),
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
    index = 47,
    label = "C=CCCCCCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {8,D} {22,S}
8  C u0 p0 c0 {7,D} {23,S} {24,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.89227,0.0946066,-6.27386e-05,2.15158e-08,-3.02719e-12,-13107.5,41.1879], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[24.354,0.0353666,-1.20208e-05,1.85855e-09,-1.07522e-13,-22448.6,-100.538], Tmin=(1392,'K'), Tmax=(5000,'K')),
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
    index = 48,
    label = "[CH2]C=C",
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
            NASAPolynomial(coeffs=[-0.529132,0.0334559,-2.53401e-05,1.02866e-08,-1.73258e-12,19494.1,24.6172], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[8.45884,0.0112695,-3.83793e-06,5.94059e-10,-3.43918e-14,16468.3,-23.2704], Tmin=(1397,'K'), Tmax=(5000,'K')),
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
    index = 49,
    label = "[CH]=CCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u1 p0 c0 {3,D} {11,S}
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
            NASAPolynomial(coeffs=[0.119943,0.0415804,-2.89254e-05,1.08175e-08,-1.70622e-12,28039.1,25.8582], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[11.2162,0.0156658,-5.34225e-06,8.27633e-10,-4.79429e-14,24140.4,-33.8119], Tmin=(1393,'K'), Tmax=(5000,'K')),
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
    index = 50,
    label = "[CH2]CCC=C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u1 p0 c0 {2,S} {11,S} {12,S}
5  C u0 p0 c0 {3,D} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.300352,0.052903,-3.502e-05,1.2128e-08,-1.7446e-12,20148.2,30.8939], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[14.1604,0.020271,-6.90765e-06,1.06973e-09,-6.1953e-14,14979.5,-47.2301], Tmin=(1392,'K'), Tmax=(5000,'K')),
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
    index = 51,
    label = "[CH2]CCCC=C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {6,D} {13,S}
5  C u1 p0 c0 {3,S} {14,S} {15,S}
6  C u0 p0 c0 {4,D} {16,S} {17,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.617485,0.0654674,-4.36872e-05,1.51937e-08,-2.18414e-12,17273.9,34.0545], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[17.413,0.0245984,-8.37353e-06,1.29588e-09,-7.50183e-14,10861.4,-63.267], Tmin=(1392,'K'), Tmax=(5000,'K')),
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
    index = 52,
    label = "[CH2]CCCCC=C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {7,D} {16,S}
6  C u1 p0 c0 {4,S} {17,S} {18,S}
7  C u0 p0 c0 {5,D} {19,S} {20,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.856744,0.0777196,-5.19282e-05,1.80146e-08,-2.57342e-12,14241,36.8477], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[20.6754,0.0289092,-9.83223e-06,1.5208e-09,-8.80072e-14,6593.6,-79.3565], Tmin=(1392,'K'), Tmax=(5000,'K')),
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
    index = 53,
    label = "[CH2]C=CCCCCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {7,D} {20,S}
7  C u0 p0 c0 {6,D} {8,S} {21,S}
8  C u1 p0 c0 {7,S} {22,S} {23,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.06768,0.0852583,-5.12152e-05,1.47537e-08,-1.5614e-12,8905.62,40.8246], Tmin=(298,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[23.3543,0.0334309,-1.13091e-05,1.7435e-09,-1.00683e-13,-71.287,-92.1461], Tmin=(1385,'K'), Tmax=(5000,'K')),
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
    index = 54,
    label = "CCCCCCCCCCCCO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {6,S} {24,S} {25,S}
6  C u0 p0 c0 {5,S} {7,S} {26,S} {27,S}
7  C u0 p0 c0 {6,S} {8,S} {28,S} {29,S}
8  C u0 p0 c0 {7,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {1,S} {11,S} {14,S} {15,S}
10 C u0 p0 c0 {8,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {13,S} {34,S} {35,S}
12 C u0 p0 c0 {10,S} {36,S} {37,S} {38,S}
13 O u0 p2 c0 {11,S} {39,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 O u1 p2 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.58304,0.142768,-8.97642e-05,2.902e-08,-3.87986e-12,-35013.1,37.2785], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[41.2071,0.0569826,-1.96259e-05,3.06096e-09,-1.78149e-13,-49620.9,-178.214], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    label = "CCCCCCCCCCC(C)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {11,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {5,S} {7,S} {23,S} {24,S}
7  C u0 p0 c0 {6,S} {8,S} {25,S} {26,S}
8  C u0 p0 c0 {7,S} {9,S} {27,S} {28,S}
9  C u0 p0 c0 {8,S} {10,S} {29,S} {30,S}
10 C u0 p0 c0 {9,S} {12,S} {31,S} {32,S}
11 C u0 p0 c0 {1,S} {33,S} {34,S} {35,S}
12 C u0 p0 c0 {10,S} {36,S} {37,S} {38,S}
13 O u0 p2 c0 {1,S} {39,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 O u1 p2 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.719001,0.147857,-9.76141e-05,3.37768e-08,-4.89238e-12,-36662.6,39.5787], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[41.5594,0.0565862,-1.94674e-05,3.03392e-09,-1.76481e-13,-51418.8,-181.492], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 56,
    label = "CCCCCCCCCC(CC)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {8,S} {27,S} {28,S}
8  C u0 p0 c0 {7,S} {10,S} {29,S} {30,S}
9  C u0 p0 c0 {1,S} {11,S} {15,S} {16,S}
10 C u0 p0 c0 {8,S} {12,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 C u0 p0 c0 {10,S} {36,S} {37,S} {38,S}
13 O u0 p2 c0 {1,S} {39,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 O u1 p2 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.719001,0.147857,-9.76141e-05,3.37768e-08,-4.89238e-12,-36662.6,39.5787], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[41.5594,0.0565862,-1.94674e-05,3.03392e-09,-1.76481e-13,-51418.8,-181.492], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    label = "CCCCCCCCC(CCC)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {9,S} {17,S} {18,S}
3  C u0 p0 c0 {1,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {8,S} {27,S} {28,S}
8  C u0 p0 c0 {7,S} {10,S} {29,S} {30,S}
9  C u0 p0 c0 {2,S} {11,S} {15,S} {16,S}
10 C u0 p0 c0 {8,S} {12,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 C u0 p0 c0 {10,S} {36,S} {37,S} {38,S}
13 O u0 p2 c0 {1,S} {39,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 O u1 p2 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.719001,0.147857,-9.76141e-05,3.37768e-08,-4.89238e-12,-36662.6,39.5787], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[41.5594,0.0565862,-1.94674e-05,3.03392e-09,-1.76481e-13,-51418.8,-181.492], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 58,
    label = "CCCCCCCC(CCCC)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {4,S} {19,S} {20,S}
3  C u0 p0 c0 {1,S} {5,S} {21,S} {22,S}
4  C u0 p0 c0 {2,S} {9,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {8,S} {27,S} {28,S}
8  C u0 p0 c0 {7,S} {10,S} {29,S} {30,S}
9  C u0 p0 c0 {4,S} {11,S} {15,S} {16,S}
10 C u0 p0 c0 {8,S} {12,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 C u0 p0 c0 {10,S} {36,S} {37,S} {38,S}
13 O u0 p2 c0 {1,S} {39,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 O u1 p2 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.719001,0.147857,-9.76141e-05,3.37768e-08,-4.89238e-12,-36662.6,39.5787], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[41.5594,0.0565862,-1.94674e-05,3.03392e-09,-1.76481e-13,-51418.8,-181.492], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 59,
    label = "CCCCCCC(CCCCC)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {5,S} {21,S} {22,S}
3  C u0 p0 c0 {1,S} {6,S} {23,S} {24,S}
4  C u0 p0 c0 {5,S} {9,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
6  C u0 p0 c0 {3,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {8,S} {27,S} {28,S}
8  C u0 p0 c0 {7,S} {10,S} {29,S} {30,S}
9  C u0 p0 c0 {4,S} {11,S} {15,S} {16,S}
10 C u0 p0 c0 {8,S} {12,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 C u0 p0 c0 {10,S} {36,S} {37,S} {38,S}
13 O u0 p2 c0 {1,S} {39,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 O u1 p2 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.719001,0.147857,-9.76141e-05,3.37768e-08,-4.89238e-12,-36662.6,39.5787], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[41.5594,0.0565862,-1.94674e-05,3.03392e-09,-1.76481e-13,-51418.8,-181.492], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 60,
    label = "CCCCCCCCCCCC[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {8,S} {27,S} {28,S}
8  C u0 p0 c0 {7,S} {10,S} {29,S} {30,S}
9  C u0 p0 c0 {1,S} {11,S} {13,S} {14,S}
10 C u0 p0 c0 {8,S} {12,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {33,S} {37,S} {38,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 O u1 p2 c0 {12,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.27096,0.146875,-9.5524e-05,3.20177e-08,-4.42534e-12,-32311.6,47.8653], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[39.9249,0.055792,-1.91826e-05,2.98851e-09,-1.73804e-13,-47245.5,-175.397], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    label = "CCCCCCCCCCC(C)[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {6,S} {24,S} {25,S}
6  C u0 p0 c0 {5,S} {7,S} {26,S} {27,S}
7  C u0 p0 c0 {6,S} {8,S} {28,S} {29,S}
8  C u0 p0 c0 {7,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {1,S} {11,S} {14,S} {15,S}
10 C u0 p0 c0 {8,S} {12,S} {13,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 C u0 p0 c0 {10,S} {36,S} {37,S} {38,S}
13 O u1 p2 c0 {10,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.18061,0.152934,-0.000104579,3.7164e-08,-5.4477e-12,-34438.6,50.594], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[40.761,0.0547295,-1.874e-05,2.91167e-09,-1.69021e-13,-49612.8,-180.861], Tmin=(1393,'K'), Tmax=(5000,'K')),
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
    index = 62,
    label = "CCCCCCCCCC([O])CC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {6,S} {24,S} {25,S}
6  C u0 p0 c0 {5,S} {7,S} {26,S} {27,S}
7  C u0 p0 c0 {6,S} {8,S} {28,S} {29,S}
8  C u0 p0 c0 {7,S} {10,S} {13,S} {30,S}
9  C u0 p0 c0 {1,S} {11,S} {14,S} {15,S}
10 C u0 p0 c0 {8,S} {12,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 C u0 p0 c0 {10,S} {36,S} {37,S} {38,S}
13 O u1 p2 c0 {8,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.18061,0.152934,-0.000104579,3.7164e-08,-5.4477e-12,-34438.6,50.594], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[40.761,0.0547295,-1.874e-05,2.91167e-09,-1.69021e-13,-49612.8,-180.861], Tmin=(1393,'K'), Tmax=(5000,'K')),
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
    index = 63,
    label = "CCCCCCCCC([O])CCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {6,S} {24,S} {25,S}
6  C u0 p0 c0 {5,S} {7,S} {26,S} {27,S}
7  C u0 p0 c0 {6,S} {8,S} {13,S} {28,S}
8  C u0 p0 c0 {7,S} {10,S} {29,S} {30,S}
9  C u0 p0 c0 {1,S} {11,S} {14,S} {15,S}
10 C u0 p0 c0 {8,S} {12,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 C u0 p0 c0 {10,S} {36,S} {37,S} {38,S}
13 O u1 p2 c0 {7,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.18061,0.152934,-0.000104579,3.7164e-08,-5.4477e-12,-34438.6,50.594], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[40.761,0.0547295,-1.874e-05,2.91167e-09,-1.69021e-13,-49612.8,-180.861], Tmin=(1393,'K'), Tmax=(5000,'K')),
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
    index = 64,
    label = "CCCCCCCC([O])CCCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {6,S} {24,S} {25,S}
6  C u0 p0 c0 {5,S} {7,S} {13,S} {26,S}
7  C u0 p0 c0 {6,S} {8,S} {27,S} {28,S}
8  C u0 p0 c0 {7,S} {10,S} {29,S} {30,S}
9  C u0 p0 c0 {1,S} {11,S} {14,S} {15,S}
10 C u0 p0 c0 {8,S} {12,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 C u0 p0 c0 {10,S} {36,S} {37,S} {38,S}
13 O u1 p2 c0 {6,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.18061,0.152934,-0.000104579,3.7164e-08,-5.4477e-12,-34438.6,50.594], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[40.761,0.0547295,-1.874e-05,2.91167e-09,-1.69021e-13,-49612.8,-180.861], Tmin=(1393,'K'), Tmax=(5000,'K')),
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
    label = "CCCCCCC([O])CCCCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {6,S} {13,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {8,S} {27,S} {28,S}
8  C u0 p0 c0 {7,S} {10,S} {29,S} {30,S}
9  C u0 p0 c0 {1,S} {11,S} {14,S} {15,S}
10 C u0 p0 c0 {8,S} {12,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 C u0 p0 c0 {10,S} {36,S} {37,S} {38,S}
13 O u1 p2 c0 {5,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.18061,0.152934,-0.000104579,3.7164e-08,-5.4477e-12,-34438.6,50.594], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[40.761,0.0547295,-1.874e-05,2.91167e-09,-1.69021e-13,-49612.8,-180.861], Tmin=(1393,'K'), Tmax=(5000,'K')),
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
    index = 66,
    label = "CCCCCCCCCC[CH]COO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {17,S} {18,S}
2  C u0 p0 c0 {1,S} {3,S} {19,S} {20,S}
3  C u0 p0 c0 {2,S} {4,S} {21,S} {22,S}
4  C u0 p0 c0 {3,S} {5,S} {23,S} {24,S}
5  C u0 p0 c0 {4,S} {6,S} {25,S} {26,S}
6  C u0 p0 c0 {5,S} {7,S} {27,S} {28,S}
7  C u0 p0 c0 {6,S} {9,S} {29,S} {30,S}
8  C u0 p0 c0 {1,S} {11,S} {15,S} {16,S}
9  C u0 p0 c0 {7,S} {12,S} {31,S} {32,S}
10 C u0 p0 c0 {12,S} {13,S} {36,S} {37,S}
11 C u0 p0 c0 {8,S} {33,S} {34,S} {35,S}
12 C u1 p0 c0 {9,S} {10,S} {38,S}
13 O u0 p2 c0 {10,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {6,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {7,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {10,S}
37 H u0 p0 c0 {10,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.42078,0.144039,-8.95664e-05,2.73266e-08,-3.21226e-12,-28502.6,40.642], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[42.7762,0.0547964,-1.86936e-05,2.89771e-09,-1.67953e-13,-43580.1,-184.041], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 67,
    label = "CCCCCCCCC[CH]CCOO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {17,S} {18,S}
2  C u0 p0 c0 {1,S} {3,S} {19,S} {20,S}
3  C u0 p0 c0 {2,S} {4,S} {21,S} {22,S}
4  C u0 p0 c0 {3,S} {5,S} {23,S} {24,S}
5  C u0 p0 c0 {4,S} {6,S} {25,S} {26,S}
6  C u0 p0 c0 {5,S} {8,S} {27,S} {28,S}
7  C u0 p0 c0 {1,S} {11,S} {15,S} {16,S}
8  C u0 p0 c0 {6,S} {12,S} {29,S} {30,S}
9  C u0 p0 c0 {10,S} {12,S} {31,S} {32,S}
10 C u0 p0 c0 {9,S} {13,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {10,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {6,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.42078,0.144039,-8.95664e-05,2.73266e-08,-3.21226e-12,-28502.6,40.642], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[42.7762,0.0547964,-1.86936e-05,2.89771e-09,-1.67953e-13,-43580.1,-184.041], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 68,
    label = "CCCCCCCC[CH]CCCOO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {17,S} {18,S}
2  C u0 p0 c0 {1,S} {3,S} {19,S} {20,S}
3  C u0 p0 c0 {2,S} {4,S} {21,S} {22,S}
4  C u0 p0 c0 {3,S} {5,S} {23,S} {24,S}
5  C u0 p0 c0 {4,S} {8,S} {25,S} {26,S}
6  C u0 p0 c0 {1,S} {11,S} {15,S} {16,S}
7  C u0 p0 c0 {9,S} {10,S} {27,S} {28,S}
8  C u0 p0 c0 {5,S} {12,S} {29,S} {30,S}
9  C u0 p0 c0 {7,S} {12,S} {31,S} {32,S}
10 C u0 p0 c0 {7,S} {13,S} {33,S} {34,S}
11 C u0 p0 c0 {6,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {10,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.42078,0.144039,-8.95664e-05,2.73266e-08,-3.21226e-12,-28502.6,40.642], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[42.7762,0.0547964,-1.86936e-05,2.89771e-09,-1.67953e-13,-43580.1,-184.041], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 69,
    label = "CCCCCCC[CH]CCCCOO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {17,S} {18,S}
2  C u0 p0 c0 {1,S} {3,S} {19,S} {20,S}
3  C u0 p0 c0 {2,S} {4,S} {21,S} {22,S}
4  C u0 p0 c0 {3,S} {8,S} {23,S} {24,S}
5  C u0 p0 c0 {6,S} {9,S} {25,S} {26,S}
6  C u0 p0 c0 {5,S} {10,S} {27,S} {28,S}
7  C u0 p0 c0 {1,S} {11,S} {15,S} {16,S}
8  C u0 p0 c0 {4,S} {12,S} {29,S} {30,S}
9  C u0 p0 c0 {5,S} {12,S} {31,S} {32,S}
10 C u0 p0 c0 {6,S} {13,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {10,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {6,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.42078,0.144039,-8.95664e-05,2.73266e-08,-3.21226e-12,-28502.6,40.642], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[42.7762,0.0547964,-1.86936e-05,2.89771e-09,-1.67953e-13,-43580.1,-184.041], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 70,
    label = "[CH2]C(CCCCCCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {10,S} {17,S} {18,S}
2  C u0 p0 c0 {1,S} {3,S} {19,S} {20,S}
3  C u0 p0 c0 {2,S} {4,S} {21,S} {22,S}
4  C u0 p0 c0 {3,S} {5,S} {23,S} {24,S}
5  C u0 p0 c0 {4,S} {6,S} {25,S} {26,S}
6  C u0 p0 c0 {5,S} {7,S} {27,S} {28,S}
7  C u0 p0 c0 {6,S} {8,S} {29,S} {30,S}
8  C u0 p0 c0 {7,S} {9,S} {31,S} {32,S}
9  C u0 p0 c0 {8,S} {12,S} {13,S} {33,S}
10 C u0 p0 c0 {1,S} {11,S} {15,S} {16,S}
11 C u0 p0 c0 {10,S} {34,S} {35,S} {36,S}
12 C u1 p0 c0 {9,S} {37,S} {38,S}
13 O u0 p2 c0 {9,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {10,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {6,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {7,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {8,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.591698,0.15202,-0.000103496,3.67769e-08,-5.42226e-12,-28912.3,41.599], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[43.1031,0.0551988,-1.89732e-05,2.95525e-09,-1.71842e-13,-44019.1,-187.753], Tmin=(1393,'K'), Tmax=(5000,'K')),
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
    index = 71,
    label = "CCCCCCCCC[CH]C(C)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {17,S} {18,S}
2  C u0 p0 c0 {1,S} {3,S} {19,S} {20,S}
3  C u0 p0 c0 {2,S} {4,S} {21,S} {22,S}
4  C u0 p0 c0 {3,S} {5,S} {23,S} {24,S}
5  C u0 p0 c0 {4,S} {6,S} {25,S} {26,S}
6  C u0 p0 c0 {5,S} {9,S} {27,S} {28,S}
7  C u0 p0 c0 {11,S} {12,S} {13,S} {29,S}
8  C u0 p0 c0 {1,S} {10,S} {15,S} {16,S}
9  C u0 p0 c0 {6,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {8,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {7,S} {9,S} {38,S}
13 O u0 p2 c0 {7,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {6,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 72,
    label = "CCCCCCCC[CH]CC(C)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {8,S} {10,S} {13,S} {15,S}
2  C u0 p0 c0 {3,S} {7,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {6,S} {24,S} {25,S}
6  C u0 p0 c0 {5,S} {9,S} {26,S} {27,S}
7  C u0 p0 c0 {2,S} {11,S} {16,S} {17,S}
8  C u0 p0 c0 {1,S} {12,S} {30,S} {31,S}
9  C u0 p0 c0 {6,S} {12,S} {28,S} {29,S}
10 C u0 p0 c0 {1,S} {35,S} {36,S} {37,S}
11 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {10,S}
36 H u0 p0 c0 {10,S}
37 H u0 p0 c0 {10,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 73,
    label = "CCCCCCC[CH]CCC(C)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {10,S} {13,S} {15,S}
2  C u0 p0 c0 {3,S} {7,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {6,S} {22,S} {23,S}
5  C u0 p0 c0 {1,S} {9,S} {26,S} {27,S}
6  C u0 p0 c0 {4,S} {8,S} {24,S} {25,S}
7  C u0 p0 c0 {2,S} {11,S} {16,S} {17,S}
8  C u0 p0 c0 {6,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {5,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {1,S} {35,S} {36,S} {37,S}
11 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {5,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {10,S}
36 H u0 p0 c0 {10,S}
37 H u0 p0 c0 {10,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 74,
    label = "CCCCCC[CH]CCCC(C)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {10,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {6,S} {26,S} {27,S}
3  C u0 p0 c0 {4,S} {7,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {8,S} {22,S} {23,S}
6  C u0 p0 c0 {2,S} {9,S} {24,S} {25,S}
7  C u0 p0 c0 {3,S} {11,S} {16,S} {17,S}
8  C u0 p0 c0 {5,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {6,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {1,S} {35,S} {36,S} {37,S}
11 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {2,S}
27 H u0 p0 c0 {2,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {10,S}
36 H u0 p0 c0 {10,S}
37 H u0 p0 c0 {10,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 75,
    label = "[CH2]CC(CCCCCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {10,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {8,S} {30,S} {31,S}
3  C u0 p0 c0 {4,S} {9,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {6,S} {8,S} {26,S} {27,S}
8  C u0 p0 c0 {2,S} {7,S} {28,S} {29,S}
9  C u0 p0 c0 {3,S} {11,S} {16,S} {17,S}
10 C u0 p0 c0 {1,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u1 p0 c0 {10,S} {37,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {2,S}
31 H u0 p0 c0 {2,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.591698,0.15202,-0.000103496,3.67769e-08,-5.42226e-12,-28912.3,41.599], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[43.1031,0.0551988,-1.89732e-05,2.95525e-09,-1.71842e-13,-44019.1,-187.753], Tmin=(1393,'K'), Tmax=(5000,'K')),
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
    index = 76,
    label = "C[CH]C(CCCCCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {8,S} {12,S} {13,S} {31,S}
2  C u0 p0 c0 {3,S} {9,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {8,S} {27,S} {28,S}
8  C u0 p0 c0 {1,S} {7,S} {29,S} {30,S}
9  C u0 p0 c0 {2,S} {10,S} {15,S} {16,S}
10 C u0 p0 c0 {9,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {12,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {1,S} {11,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {1,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 77,
    label = "CCCCCCCC[CH]C(CC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {8,S} {12,S} {13,S} {27,S}
2  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {9,S} {25,S} {26,S}
7  C u0 p0 c0 {2,S} {10,S} {15,S} {16,S}
8  C u0 p0 c0 {1,S} {11,S} {28,S} {29,S}
9  C u0 p0 c0 {6,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {8,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {1,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {1,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 78,
    label = "CCCCCCC[CH]CC(CC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {6,S} {8,S} {13,S} {15,S}
2  C u0 p0 c0 {3,S} {7,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {9,S} {24,S} {25,S}
6  C u0 p0 c0 {1,S} {11,S} {26,S} {27,S}
7  C u0 p0 c0 {2,S} {10,S} {16,S} {17,S}
8  C u0 p0 c0 {1,S} {12,S} {30,S} {31,S}
9  C u0 p0 c0 {5,S} {12,S} {28,S} {29,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {6,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 79,
    label = "CCCCCC[CH]CCC(CC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {6,S} {13,S} {15,S}
2  C u0 p0 c0 {3,S} {7,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {5,S} {20,S} {21,S}
4  C u0 p0 c0 {1,S} {9,S} {24,S} {25,S}
5  C u0 p0 c0 {3,S} {8,S} {22,S} {23,S}
6  C u0 p0 c0 {1,S} {11,S} {26,S} {27,S}
7  C u0 p0 c0 {2,S} {10,S} {16,S} {17,S}
8  C u0 p0 c0 {5,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {4,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {6,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 80,
    label = "CCCCC[CH]CCCC(CC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {5,S} {24,S} {25,S}
3  C u0 p0 c0 {4,S} {7,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {8,S} {20,S} {21,S}
5  C u0 p0 c0 {2,S} {9,S} {22,S} {23,S}
6  C u0 p0 c0 {1,S} {11,S} {26,S} {27,S}
7  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
8  C u0 p0 c0 {4,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {5,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {6,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {2,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 81,
    label = "[CH2]CCC(CCCCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {7,S} {28,S} {29,S}
3  C u0 p0 c0 {4,S} {9,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {2,S} {6,S} {26,S} {27,S}
8  C u0 p0 c0 {1,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {3,S} {11,S} {16,S} {17,S}
10 C u0 p0 c0 {8,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u1 p0 c0 {10,S} {37,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {2,S}
29 H u0 p0 c0 {2,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.591698,0.15202,-0.000103496,3.67769e-08,-5.42226e-12,-28912.3,41.599], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[43.1031,0.0551988,-1.89732e-05,2.95525e-09,-1.71842e-13,-44019.1,-187.753], Tmin=(1393,'K'), Tmax=(5000,'K')),
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
    index = 82,
    label = "C[CH]CC(CCCCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {7,S} {28,S} {29,S}
3  C u0 p0 c0 {4,S} {8,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {2,S} {6,S} {26,S} {27,S}
8  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
9  C u0 p0 c0 {1,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {8,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {12,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {9,S} {11,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {2,S}
29 H u0 p0 c0 {2,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 83,
    label = "CC[CH]C(CCCCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {7,S} {12,S} {13,S} {29,S}
2  C u0 p0 c0 {3,S} {8,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {1,S} {6,S} {27,S} {28,S}
8  C u0 p0 c0 {2,S} {10,S} {15,S} {16,S}
9  C u0 p0 c0 {11,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {8,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {9,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {1,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {1,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 84,
    label = "CCCCCCC[CH]C(CCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {12,S} {13,S} {25,S}
2  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {6,S} {21,S} {22,S}
5  C u0 p0 c0 {1,S} {8,S} {26,S} {27,S}
6  C u0 p0 c0 {4,S} {9,S} {23,S} {24,S}
7  C u0 p0 c0 {2,S} {10,S} {15,S} {16,S}
8  C u0 p0 c0 {5,S} {11,S} {28,S} {29,S}
9  C u0 p0 c0 {6,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {8,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {1,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {1,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {5,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 85,
    label = "CCCCCC[CH]CC(CCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {7,S} {24,S} {25,S}
3  C u0 p0 c0 {4,S} {6,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {9,S} {22,S} {23,S}
6  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {2,S} {11,S} {26,S} {27,S}
8  C u0 p0 c0 {1,S} {12,S} {30,S} {31,S}
9  C u0 p0 c0 {5,S} {12,S} {28,S} {29,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {2,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 86,
    label = "CCCCC[CH]CCC(CCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {7,S} {24,S} {25,S}
3  C u0 p0 c0 {5,S} {6,S} {18,S} {19,S}
4  C u0 p0 c0 {1,S} {9,S} {22,S} {23,S}
5  C u0 p0 c0 {3,S} {8,S} {20,S} {21,S}
6  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {2,S} {11,S} {26,S} {27,S}
8  C u0 p0 c0 {5,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {4,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {2,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 87,
    label = "CCCC[CH]CCCC(CCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {5,S} {22,S} {23,S}
3  C u0 p0 c0 {1,S} {7,S} {24,S} {25,S}
4  C u0 p0 c0 {6,S} {8,S} {18,S} {19,S}
5  C u0 p0 c0 {2,S} {9,S} {20,S} {21,S}
6  C u0 p0 c0 {4,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {3,S} {11,S} {26,S} {27,S}
8  C u0 p0 c0 {4,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {5,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 88,
    label = "[CH2]CCCC(CCCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {7,S} {26,S} {27,S}
3  C u0 p0 c0 {1,S} {8,S} {28,S} {29,S}
4  C u0 p0 c0 {5,S} {9,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {20,S} {21,S}
6  C u0 p0 c0 {5,S} {7,S} {22,S} {23,S}
7  C u0 p0 c0 {2,S} {6,S} {24,S} {25,S}
8  C u0 p0 c0 {3,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {4,S} {11,S} {16,S} {17,S}
10 C u0 p0 c0 {8,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u1 p0 c0 {10,S} {37,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {2,S}
27 H u0 p0 c0 {2,S}
28 H u0 p0 c0 {3,S}
29 H u0 p0 c0 {3,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.591698,0.15202,-0.000103496,3.67769e-08,-5.42226e-12,-28912.3,41.599], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[43.1031,0.0551988,-1.89732e-05,2.95525e-09,-1.71842e-13,-44019.1,-187.753], Tmin=(1393,'K'), Tmax=(5000,'K')),
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
    index = 89,
    label = "C[CH]CCC(CCCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {6,S} {26,S} {27,S}
3  C u0 p0 c0 {4,S} {8,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {2,S} {5,S} {24,S} {25,S}
7  C u0 p0 c0 {1,S} {9,S} {28,S} {29,S}
8  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
9  C u0 p0 c0 {7,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {8,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {12,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {9,S} {11,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {2,S}
27 H u0 p0 c0 {2,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 90,
    label = "CC[CH]CC(CCCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {6,S} {26,S} {27,S}
3  C u0 p0 c0 {4,S} {7,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {2,S} {5,S} {24,S} {25,S}
7  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
8  C u0 p0 c0 {1,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {11,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {9,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {2,S}
27 H u0 p0 c0 {2,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 91,
    label = "CCC[CH]C(CCCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {6,S} {12,S} {13,S} {27,S}
2  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {1,S} {5,S} {25,S} {26,S}
7  C u0 p0 c0 {2,S} {10,S} {15,S} {16,S}
8  C u0 p0 c0 {9,S} {11,S} {28,S} {29,S}
9  C u0 p0 c0 {8,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {8,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {1,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {1,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 92,
    label = "CCCCCC[CH]C(CCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {12,S} {13,S} {23,S}
2  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {6,S} {19,S} {20,S}
4  C u0 p0 c0 {1,S} {5,S} {24,S} {25,S}
5  C u0 p0 c0 {4,S} {8,S} {26,S} {27,S}
6  C u0 p0 c0 {3,S} {9,S} {21,S} {22,S}
7  C u0 p0 c0 {2,S} {10,S} {15,S} {16,S}
8  C u0 p0 c0 {5,S} {11,S} {28,S} {29,S}
9  C u0 p0 c0 {6,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {8,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {1,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {1,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {5,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 93,
    label = "CCCCC[CH]CC(CCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {4,S} {22,S} {23,S}
3  C u0 p0 c0 {5,S} {6,S} {18,S} {19,S}
4  C u0 p0 c0 {2,S} {7,S} {24,S} {25,S}
5  C u0 p0 c0 {3,S} {9,S} {20,S} {21,S}
6  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {4,S} {11,S} {26,S} {27,S}
8  C u0 p0 c0 {1,S} {12,S} {30,S} {31,S}
9  C u0 p0 c0 {5,S} {12,S} {28,S} {29,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 94,
    label = "CCCC[CH]CCC(CCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {4,S} {22,S} {23,S}
3  C u0 p0 c0 {1,S} {9,S} {20,S} {21,S}
4  C u0 p0 c0 {2,S} {7,S} {24,S} {25,S}
5  C u0 p0 c0 {6,S} {8,S} {18,S} {19,S}
6  C u0 p0 c0 {5,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {4,S} {11,S} {26,S} {27,S}
8  C u0 p0 c0 {5,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {3,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 95,
    label = "CCC[CH]CCCC(CCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {5,S} {20,S} {21,S}
3  C u0 p0 c0 {1,S} {4,S} {22,S} {23,S}
4  C u0 p0 c0 {3,S} {6,S} {24,S} {25,S}
5  C u0 p0 c0 {2,S} {9,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {11,S} {26,S} {27,S}
7  C u0 p0 c0 {8,S} {10,S} {16,S} {17,S}
8  C u0 p0 c0 {7,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {5,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {6,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 96,
    label = "C[CH]CCCC(CCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {6,S} {24,S} {25,S}
3  C u0 p0 c0 {1,S} {7,S} {26,S} {27,S}
4  C u0 p0 c0 {5,S} {8,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {20,S} {21,S}
6  C u0 p0 c0 {2,S} {5,S} {22,S} {23,S}
7  C u0 p0 c0 {3,S} {9,S} {28,S} {29,S}
8  C u0 p0 c0 {4,S} {10,S} {16,S} {17,S}
9  C u0 p0 c0 {7,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {8,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {12,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {9,S} {11,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {2,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {3,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 97,
    label = "CC[CH]CCC(CCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {5,S} {24,S} {25,S}
3  C u0 p0 c0 {4,S} {7,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {2,S} {4,S} {22,S} {23,S}
6  C u0 p0 c0 {1,S} {8,S} {26,S} {27,S}
7  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
8  C u0 p0 c0 {6,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {11,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {9,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {2,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 98,
    label = "CCC[CH]CC(CCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {5,S} {24,S} {25,S}
3  C u0 p0 c0 {4,S} {6,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {2,S} {4,S} {22,S} {23,S}
6  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {9,S} {11,S} {26,S} {27,S}
8  C u0 p0 c0 {1,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {7,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {2,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 99,
    label = "CCCC[CH]C(CCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {12,S} {13,S} {25,S}
2  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {1,S} {4,S} {23,S} {24,S}
6  C u0 p0 c0 {8,S} {9,S} {26,S} {27,S}
7  C u0 p0 c0 {2,S} {10,S} {15,S} {16,S}
8  C u0 p0 c0 {6,S} {11,S} {28,S} {29,S}
9  C u0 p0 c0 {6,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {8,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {1,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {1,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 100,
    label = "CCCCC[CH]C(CCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {12,S} {13,S} {21,S}
2  C u0 p0 c0 {6,S} {7,S} {17,S} {18,S}
3  C u0 p0 c0 {1,S} {4,S} {22,S} {23,S}
4  C u0 p0 c0 {3,S} {5,S} {24,S} {25,S}
5  C u0 p0 c0 {4,S} {8,S} {26,S} {27,S}
6  C u0 p0 c0 {2,S} {9,S} {19,S} {20,S}
7  C u0 p0 c0 {2,S} {10,S} {15,S} {16,S}
8  C u0 p0 c0 {5,S} {11,S} {28,S} {29,S}
9  C u0 p0 c0 {6,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {8,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {1,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {1,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {5,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 101,
    label = "CCCC[CH]CC(CCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {20,S} {21,S}
3  C u0 p0 c0 {2,S} {4,S} {22,S} {23,S}
4  C u0 p0 c0 {3,S} {7,S} {24,S} {25,S}
5  C u0 p0 c0 {6,S} {9,S} {18,S} {19,S}
6  C u0 p0 c0 {5,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {4,S} {11,S} {26,S} {27,S}
8  C u0 p0 c0 {1,S} {12,S} {30,S} {31,S}
9  C u0 p0 c0 {5,S} {12,S} {28,S} {29,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 102,
    label = "CCC[CH]CCC(CCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {4,S} {20,S} {21,S}
3  C u0 p0 c0 {1,S} {9,S} {18,S} {19,S}
4  C u0 p0 c0 {2,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {6,S} {24,S} {25,S}
6  C u0 p0 c0 {5,S} {11,S} {26,S} {27,S}
7  C u0 p0 c0 {8,S} {10,S} {16,S} {17,S}
8  C u0 p0 c0 {7,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {3,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {6,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 103,
    label = "CC[CH]CCCC(CCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {6,S} {18,S} {19,S}
3  C u0 p0 c0 {1,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {7,S} {24,S} {25,S}
6  C u0 p0 c0 {2,S} {8,S} {16,S} {17,S}
7  C u0 p0 c0 {5,S} {10,S} {26,S} {27,S}
8  C u0 p0 c0 {6,S} {12,S} {30,S} {31,S}
9  C u0 p0 c0 {11,S} {12,S} {28,S} {29,S}
10 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
11 C u0 p0 c0 {9,S} {32,S} {33,S} {34,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {10,S}
36 H u0 p0 c0 {10,S}
37 H u0 p0 c0 {10,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.543431,0.14916,-9.74342e-05,3.20767e-08,-4.22023e-12,-30149.3,43.0098], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1479,0.0543644,-1.85191e-05,2.86784e-09,-1.66108e-13,-45385.9,-187.427], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 104,
    label = "C=CCCCCCCCCCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {9,S} {27,S} {28,S}
8  C u0 p0 c0 {1,S} {10,S} {13,S} {14,S}
9  C u0 p0 c0 {7,S} {11,S} {29,S} {30,S}
10 C u0 p0 c0 {8,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {12,D} {34,S}
12 C u0 p0 c0 {11,D} {35,S} {36,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.96343,0.143992,-9.61384e-05,3.30174e-08,-4.62398e-12,-24634.5,52.9159], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[37.4002,0.0526231,-1.78624e-05,2.7595e-09,-1.59562e-13,-38940.6,-164.893], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 105,
    label = "CC=CCCCCCCCCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {8,S} {25,S} {26,S}
7  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
8  C u0 p0 c0 {6,S} {11,S} {27,S} {28,S}
9  C u0 p0 c0 {7,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {12,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {8,S} {12,D} {35,S}
12 C u0 p0 c0 {10,S} {11,D} {36,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.43875,0.140513,-9.10033e-05,3.00309e-08,-4.0079e-12,-26155.7,50.7457], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[36.9269,0.053053,-1.80167e-05,2.78417e-09,-1.61023e-13,-40285.6,-162.284], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 106,
    label = "CCC=CCCCCCCCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {7,S} {23,S} {24,S}
6  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
7  C u0 p0 c0 {5,S} {11,S} {25,S} {26,S}
8  C u0 p0 c0 {10,S} {12,S} {27,S} {28,S}
9  C u0 p0 c0 {6,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {8,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {12,D} {35,S}
12 C u0 p0 c0 {8,S} {11,D} {36,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.39231,0.144505,-9.65459e-05,3.33095e-08,-4.7082e-12,-25920.5,54.9907], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[36.9736,0.0531279,-1.80659e-05,2.79414e-09,-1.61691e-13,-40249.4,-162.866], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 107,
    label = "CCCC=CCCCCCCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {7,S} {21,S} {22,S}
5  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
6  C u0 p0 c0 {8,S} {10,S} {23,S} {24,S}
7  C u0 p0 c0 {4,S} {11,S} {25,S} {26,S}
8  C u0 p0 c0 {6,S} {12,S} {27,S} {28,S}
9  C u0 p0 c0 {5,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {12,D} {35,S}
12 C u0 p0 c0 {8,S} {11,D} {36,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.39231,0.144505,-9.65459e-05,3.33095e-08,-4.7082e-12,-25920.5,54.9907], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[36.9736,0.0531279,-1.80659e-05,2.79414e-09,-1.61691e-13,-40249.4,-162.866], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 108,
    label = "CCCCC=CCCCCCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {7,S} {19,S} {20,S}
4  C u0 p0 c0 {6,S} {8,S} {21,S} {22,S}
5  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
6  C u0 p0 c0 {4,S} {10,S} {23,S} {24,S}
7  C u0 p0 c0 {3,S} {11,S} {25,S} {26,S}
8  C u0 p0 c0 {4,S} {12,S} {27,S} {28,S}
9  C u0 p0 c0 {5,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {12,D} {35,S}
12 C u0 p0 c0 {8,S} {11,D} {36,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.39231,0.144505,-9.65459e-05,3.33095e-08,-4.7082e-12,-25920.5,54.9907], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[36.9736,0.0531279,-1.80659e-05,2.79414e-09,-1.61691e-13,-40249.4,-162.866], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 109,
    label = "CCCCCC=CCCCCC",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {15,S} {16,S}
2  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
3  C u0 p0 c0 {1,S} {7,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {8,S} {19,S} {20,S}
5  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
6  C u0 p0 c0 {2,S} {10,S} {23,S} {24,S}
7  C u0 p0 c0 {3,S} {11,S} {25,S} {26,S}
8  C u0 p0 c0 {4,S} {12,S} {27,S} {28,S}
9  C u0 p0 c0 {5,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {12,D} {35,S}
12 C u0 p0 c0 {8,S} {11,D} {36,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.39231,0.144505,-9.65459e-05,3.33095e-08,-4.7082e-12,-25920.5,54.9907], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[36.9736,0.0531279,-1.80659e-05,2.79414e-09,-1.61691e-13,-40249.4,-162.866], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 110,
    label = "CCCCCCCCCCCCOO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {10,S} {17,S} {18,S}
2  C u0 p0 c0 {1,S} {3,S} {19,S} {20,S}
3  C u0 p0 c0 {2,S} {4,S} {21,S} {22,S}
4  C u0 p0 c0 {3,S} {5,S} {23,S} {24,S}
5  C u0 p0 c0 {4,S} {6,S} {25,S} {26,S}
6  C u0 p0 c0 {5,S} {7,S} {27,S} {28,S}
7  C u0 p0 c0 {6,S} {8,S} {29,S} {30,S}
8  C u0 p0 c0 {7,S} {9,S} {31,S} {32,S}
9  C u0 p0 c0 {8,S} {11,S} {33,S} {34,S}
10 C u0 p0 c0 {1,S} {12,S} {15,S} {16,S}
11 C u0 p0 c0 {9,S} {13,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {11,S} {14,S}
14 O u0 p2 c0 {13,S} {40,S}
15 H u0 p0 c0 {10,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {6,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {7,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {8,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {9,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.720522,0.151371,-9.79917e-05,3.25886e-08,-4.45366e-12,-51881.7,40.5418], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[43.1639,0.0577457,-1.98632e-05,3.09541e-09,-1.80054e-13,-67282.6,-189.546], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 111,
    label = "CCCCCCCCCCC(C)OO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {11,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {9,S} {32,S} {33,S}
3  C u0 p0 c0 {4,S} {10,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {6,S} {8,S} {26,S} {27,S}
8  C u0 p0 c0 {7,S} {9,S} {28,S} {29,S}
9  C u0 p0 c0 {2,S} {8,S} {30,S} {31,S}
10 C u0 p0 c0 {3,S} {12,S} {16,S} {17,S}
11 C u0 p0 c0 {1,S} {37,S} {38,S} {39,S}
12 C u0 p0 c0 {10,S} {34,S} {35,S} {36,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {40,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {2,S}
33 H u0 p0 c0 {2,S}
34 H u0 p0 c0 {12,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {11,S}
39 H u0 p0 c0 {11,S}
40 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.157577,0.15651,-0.000105904,3.73775e-08,-5.47228e-12,-53528.7,42.9098], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[43.5212,0.0573414,-1.97012e-05,3.06776e-09,-1.78348e-13,-69083,-192.853], Tmin=(1393,'K'), Tmax=(5000,'K')),
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
    index = 112,
    label = "CCCCCCCCCC(CC)OO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {8,S} {30,S} {31,S}
3  C u0 p0 c0 {4,S} {10,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {6,S} {8,S} {26,S} {27,S}
8  C u0 p0 c0 {2,S} {7,S} {28,S} {29,S}
9  C u0 p0 c0 {1,S} {12,S} {32,S} {33,S}
10 C u0 p0 c0 {3,S} {11,S} {16,S} {17,S}
11 C u0 p0 c0 {10,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {9,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {40,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {2,S}
31 H u0 p0 c0 {2,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.157577,0.15651,-0.000105904,3.73775e-08,-5.47228e-12,-53528.7,42.9098], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[43.5212,0.0573414,-1.97012e-05,3.06776e-09,-1.78348e-13,-69083,-192.853], Tmin=(1393,'K'), Tmax=(5000,'K')),
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
    index = 113,
    label = "CCCCCCCCC(CCC)OO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {8,S} {28,S} {29,S}
3  C u0 p0 c0 {1,S} {10,S} {30,S} {31,S}
4  C u0 p0 c0 {5,S} {9,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {20,S} {21,S}
6  C u0 p0 c0 {5,S} {7,S} {22,S} {23,S}
7  C u0 p0 c0 {6,S} {8,S} {24,S} {25,S}
8  C u0 p0 c0 {2,S} {7,S} {26,S} {27,S}
9  C u0 p0 c0 {4,S} {11,S} {16,S} {17,S}
10 C u0 p0 c0 {3,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {40,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {2,S}
29 H u0 p0 c0 {2,S}
30 H u0 p0 c0 {3,S}
31 H u0 p0 c0 {3,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.157577,0.15651,-0.000105904,3.73775e-08,-5.47228e-12,-53528.7,42.9098], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[43.5212,0.0573414,-1.97012e-05,3.06776e-09,-1.78348e-13,-69083,-192.853], Tmin=(1393,'K'), Tmax=(5000,'K')),
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
    index = 114,
    label = "CCCCCCCC(CCCC)OO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {7,S} {26,S} {27,S}
3  C u0 p0 c0 {1,S} {8,S} {28,S} {29,S}
4  C u0 p0 c0 {5,S} {9,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {20,S} {21,S}
6  C u0 p0 c0 {5,S} {7,S} {22,S} {23,S}
7  C u0 p0 c0 {2,S} {6,S} {24,S} {25,S}
8  C u0 p0 c0 {3,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {4,S} {11,S} {16,S} {17,S}
10 C u0 p0 c0 {8,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {40,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {2,S}
27 H u0 p0 c0 {2,S}
28 H u0 p0 c0 {3,S}
29 H u0 p0 c0 {3,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.157577,0.15651,-0.000105904,3.73775e-08,-5.47228e-12,-53528.7,42.9098], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[43.5212,0.0573414,-1.97012e-05,3.06776e-09,-1.78348e-13,-69083,-192.853], Tmin=(1393,'K'), Tmax=(5000,'K')),
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
    index = 115,
    label = "CCCCCCC(CCCCC)OO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {6,S} {24,S} {25,S}
3  C u0 p0 c0 {1,S} {7,S} {26,S} {27,S}
4  C u0 p0 c0 {5,S} {9,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {20,S} {21,S}
6  C u0 p0 c0 {2,S} {5,S} {22,S} {23,S}
7  C u0 p0 c0 {3,S} {8,S} {28,S} {29,S}
8  C u0 p0 c0 {7,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {4,S} {11,S} {16,S} {17,S}
10 C u0 p0 c0 {8,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {40,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {2,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {3,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.157577,0.15651,-0.000105904,3.73775e-08,-5.47228e-12,-53528.7,42.9098], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[43.5212,0.0573414,-1.97012e-05,3.06776e-09,-1.78348e-13,-69083,-192.853], Tmin=(1393,'K'), Tmax=(5000,'K')),
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
    index = 116,
    label = "CCCCCCCCCCC1CO1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {11,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {9,S} {31,S} {32,S}
3  C u0 p0 c0 {4,S} {10,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {5,S} {7,S} {23,S} {24,S}
7  C u0 p0 c0 {6,S} {8,S} {25,S} {26,S}
8  C u0 p0 c0 {7,S} {9,S} {27,S} {28,S}
9  C u0 p0 c0 {2,S} {8,S} {29,S} {30,S}
10 C u0 p0 c0 {3,S} {12,S} {15,S} {16,S}
11 C u0 p0 c0 {1,S} {13,S} {33,S} {34,S}
12 C u0 p0 c0 {10,S} {35,S} {36,S} {37,S}
13 O u0 p2 c0 {1,S} {11,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {10,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {2,S}
32 H u0 p0 c0 {2,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.29776,0.15574,-0.000109307,4.02923e-08,-6.17232e-12,-38088.5,59.5378], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[39.2369,0.0547043,-1.88121e-05,2.9311e-09,-1.70475e-13,-53368.2,-174.663], Tmin=(1394,'K'), Tmax=(5000,'K')),
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
    index = 117,
    label = "CCCCCCCCCC1OC1C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {11,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {9,S} {30,S} {31,S}
4  C u0 p0 c0 {5,S} {10,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {20,S} {21,S}
6  C u0 p0 c0 {5,S} {7,S} {22,S} {23,S}
7  C u0 p0 c0 {6,S} {8,S} {24,S} {25,S}
8  C u0 p0 c0 {7,S} {9,S} {26,S} {27,S}
9  C u0 p0 c0 {3,S} {8,S} {28,S} {29,S}
10 C u0 p0 c0 {4,S} {12,S} {16,S} {17,S}
11 C u0 p0 c0 {2,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {10,S} {32,S} {33,S} {34,S}
13 O u0 p2 c0 {1,S} {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {3,S}
31 H u0 p0 c0 {3,S}
32 H u0 p0 c0 {12,S}
33 H u0 p0 c0 {12,S}
34 H u0 p0 c0 {12,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.15651,0.160827,-0.000115426,4.32184e-08,-6.67484e-12,-40209.3,62.844], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[40.4607,0.0537349,-1.84948e-05,2.88345e-09,-1.67781e-13,-56044.8,-182.038], Tmin=(1395,'K'), Tmax=(5000,'K')),
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
    index = 118,
    label = "CCCCCCCCC1OC1CC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {15,S}
3  C u0 p0 c0 {2,S} {8,S} {30,S} {31,S}
4  C u0 p0 c0 {5,S} {10,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {20,S} {21,S}
6  C u0 p0 c0 {5,S} {7,S} {22,S} {23,S}
7  C u0 p0 c0 {6,S} {8,S} {24,S} {25,S}
8  C u0 p0 c0 {3,S} {7,S} {26,S} {27,S}
9  C u0 p0 c0 {1,S} {12,S} {28,S} {29,S}
10 C u0 p0 c0 {4,S} {11,S} {16,S} {17,S}
11 C u0 p0 c0 {10,S} {32,S} {33,S} {34,S}
12 C u0 p0 c0 {9,S} {35,S} {36,S} {37,S}
13 O u0 p2 c0 {1,S} {2,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {3,S}
31 H u0 p0 c0 {3,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.15651,0.160827,-0.000115426,4.32184e-08,-6.67484e-12,-40209.3,62.844], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[40.4607,0.0537349,-1.84948e-05,2.88345e-09,-1.67781e-13,-56044.8,-182.038], Tmin=(1395,'K'), Tmax=(5000,'K')),
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
    index = 119,
    label = "CCCCCCCC1OC1CCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {15,S}
3  C u0 p0 c0 {1,S} {8,S} {26,S} {27,S}
4  C u0 p0 c0 {2,S} {10,S} {28,S} {29,S}
5  C u0 p0 c0 {6,S} {9,S} {18,S} {19,S}
6  C u0 p0 c0 {5,S} {7,S} {20,S} {21,S}
7  C u0 p0 c0 {6,S} {8,S} {22,S} {23,S}
8  C u0 p0 c0 {3,S} {7,S} {24,S} {25,S}
9  C u0 p0 c0 {5,S} {11,S} {16,S} {17,S}
10 C u0 p0 c0 {4,S} {12,S} {30,S} {31,S}
11 C u0 p0 c0 {9,S} {32,S} {33,S} {34,S}
12 C u0 p0 c0 {10,S} {35,S} {36,S} {37,S}
13 O u0 p2 c0 {1,S} {2,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {3,S}
28 H u0 p0 c0 {4,S}
29 H u0 p0 c0 {4,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.15651,0.160827,-0.000115426,4.32184e-08,-6.67484e-12,-40209.3,62.844], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[40.4607,0.0537349,-1.84948e-05,2.88345e-09,-1.67781e-13,-56044.8,-182.038], Tmin=(1395,'K'), Tmax=(5000,'K')),
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
    index = 120,
    label = "CCCCCCC1OC1CCCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {15,S}
3  C u0 p0 c0 {1,S} {7,S} {24,S} {25,S}
4  C u0 p0 c0 {2,S} {8,S} {26,S} {27,S}
5  C u0 p0 c0 {6,S} {9,S} {18,S} {19,S}
6  C u0 p0 c0 {5,S} {7,S} {20,S} {21,S}
7  C u0 p0 c0 {3,S} {6,S} {22,S} {23,S}
8  C u0 p0 c0 {4,S} {10,S} {28,S} {29,S}
9  C u0 p0 c0 {5,S} {11,S} {16,S} {17,S}
10 C u0 p0 c0 {8,S} {12,S} {30,S} {31,S}
11 C u0 p0 c0 {9,S} {32,S} {33,S} {34,S}
12 C u0 p0 c0 {10,S} {35,S} {36,S} {37,S}
13 O u0 p2 c0 {1,S} {2,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {4,S}
27 H u0 p0 c0 {4,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.15651,0.160827,-0.000115426,4.32184e-08,-6.67484e-12,-40209.3,62.844], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[40.4607,0.0537349,-1.84948e-05,2.88345e-09,-1.67781e-13,-56044.8,-182.038], Tmin=(1395,'K'), Tmax=(5000,'K')),
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
    index = 121,
    label = "CCCCCC1OC1CCCCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {15,S}
3  C u0 p0 c0 {1,S} {6,S} {22,S} {23,S}
4  C u0 p0 c0 {2,S} {7,S} {24,S} {25,S}
5  C u0 p0 c0 {6,S} {9,S} {18,S} {19,S}
6  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
7  C u0 p0 c0 {4,S} {8,S} {26,S} {27,S}
8  C u0 p0 c0 {7,S} {10,S} {28,S} {29,S}
9  C u0 p0 c0 {5,S} {11,S} {16,S} {17,S}
10 C u0 p0 c0 {8,S} {12,S} {30,S} {31,S}
11 C u0 p0 c0 {9,S} {32,S} {33,S} {34,S}
12 C u0 p0 c0 {10,S} {35,S} {36,S} {37,S}
13 O u0 p2 c0 {1,S} {2,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.15651,0.160827,-0.000115426,4.32184e-08,-6.67484e-12,-40209.3,62.844], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[40.4607,0.0537349,-1.84948e-05,2.88345e-09,-1.67781e-13,-56044.8,-182.038], Tmin=(1395,'K'), Tmax=(5000,'K')),
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
    index = 122,
    label = "CCCCCCCCCC1CCO1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {8,S} {29,S} {30,S}
3  C u0 p0 c0 {4,S} {10,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {5,S} {7,S} {23,S} {24,S}
7  C u0 p0 c0 {6,S} {8,S} {25,S} {26,S}
8  C u0 p0 c0 {2,S} {7,S} {27,S} {28,S}
9  C u0 p0 c0 {1,S} {11,S} {31,S} {32,S}
10 C u0 p0 c0 {3,S} {12,S} {15,S} {16,S}
11 C u0 p0 c0 {9,S} {13,S} {33,S} {34,S}
12 C u0 p0 c0 {10,S} {35,S} {36,S} {37,S}
13 O u0 p2 c0 {1,S} {11,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {10,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {2,S}
30 H u0 p0 c0 {2,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.95564,0.158032,-0.000109347,3.92877e-08,-5.8291e-12,-38569.6,67.0371], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[38.9551,0.0551362,-1.90052e-05,2.96596e-09,-1.727e-13,-54440.4,-174.998], Tmin=(1393,'K'), Tmax=(5000,'K')),
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
    index = 123,
    label = "CCCCCCCCC1OCC1C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {10,S} {11,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {15,S}
3  C u0 p0 c0 {2,S} {8,S} {28,S} {29,S}
4  C u0 p0 c0 {5,S} {9,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {20,S} {21,S}
6  C u0 p0 c0 {5,S} {7,S} {22,S} {23,S}
7  C u0 p0 c0 {6,S} {8,S} {24,S} {25,S}
8  C u0 p0 c0 {3,S} {7,S} {26,S} {27,S}
9  C u0 p0 c0 {4,S} {12,S} {16,S} {17,S}
10 C u0 p0 c0 {1,S} {13,S} {30,S} {31,S}
11 C u0 p0 c0 {1,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {9,S} {32,S} {33,S} {34,S}
13 O u0 p2 c0 {2,S} {10,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {3,S}
29 H u0 p0 c0 {3,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {12,S}
33 H u0 p0 c0 {12,S}
34 H u0 p0 c0 {12,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.81408,0.16847,-0.000125041,4.89353e-08,-7.94259e-12,-40558.1,74.8131], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[39.8039,0.0546226,-1.88739e-05,2.95022e-09,-1.71976e-13,-56954.9,-180.202], Tmin=(1393,'K'), Tmax=(5000,'K')),
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
    index = 124,
    label = "CCCCCCCC1OCC1CC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {10,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {15,S}
3  C u0 p0 c0 {2,S} {7,S} {26,S} {27,S}
4  C u0 p0 c0 {5,S} {9,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {20,S} {21,S}
6  C u0 p0 c0 {5,S} {7,S} {22,S} {23,S}
7  C u0 p0 c0 {3,S} {6,S} {24,S} {25,S}
8  C u0 p0 c0 {1,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {4,S} {11,S} {16,S} {17,S}
10 C u0 p0 c0 {1,S} {13,S} {30,S} {31,S}
11 C u0 p0 c0 {9,S} {32,S} {33,S} {34,S}
12 C u0 p0 c0 {8,S} {35,S} {36,S} {37,S}
13 O u0 p2 c0 {2,S} {10,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {3,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.81408,0.16847,-0.000125041,4.89353e-08,-7.94259e-12,-40558.1,74.8131], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[39.8039,0.0546226,-1.88739e-05,2.95022e-09,-1.71976e-13,-56954.9,-180.202], Tmin=(1393,'K'), Tmax=(5000,'K')),
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
    index = 125,
    label = "CCCCCCC1OCC1CCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {14,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {15,S}
3  C u0 p0 c0 {1,S} {9,S} {26,S} {27,S}
4  C u0 p0 c0 {2,S} {7,S} {24,S} {25,S}
5  C u0 p0 c0 {6,S} {8,S} {18,S} {19,S}
6  C u0 p0 c0 {5,S} {7,S} {20,S} {21,S}
7  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
8  C u0 p0 c0 {5,S} {11,S} {16,S} {17,S}
9  C u0 p0 c0 {3,S} {12,S} {28,S} {29,S}
10 C u0 p0 c0 {1,S} {13,S} {30,S} {31,S}
11 C u0 p0 c0 {8,S} {32,S} {33,S} {34,S}
12 C u0 p0 c0 {9,S} {35,S} {36,S} {37,S}
13 O u0 p2 c0 {2,S} {10,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {3,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.81408,0.16847,-0.000125041,4.89353e-08,-7.94259e-12,-40558.1,74.8131], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[39.8039,0.0546226,-1.88739e-05,2.95022e-09,-1.71976e-13,-56954.9,-180.202], Tmin=(1393,'K'), Tmax=(5000,'K')),
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
    index = 126,
    label = "CCCCCC1OCC1CCCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {14,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {15,S}
3  C u0 p0 c0 {1,S} {7,S} {24,S} {25,S}
4  C u0 p0 c0 {2,S} {6,S} {22,S} {23,S}
5  C u0 p0 c0 {6,S} {8,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {5,S} {20,S} {21,S}
7  C u0 p0 c0 {3,S} {9,S} {26,S} {27,S}
8  C u0 p0 c0 {5,S} {11,S} {16,S} {17,S}
9  C u0 p0 c0 {7,S} {12,S} {28,S} {29,S}
10 C u0 p0 c0 {1,S} {13,S} {30,S} {31,S}
11 C u0 p0 c0 {8,S} {32,S} {33,S} {34,S}
12 C u0 p0 c0 {9,S} {35,S} {36,S} {37,S}
13 O u0 p2 c0 {2,S} {10,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.81408,0.16847,-0.000125041,4.89353e-08,-7.94259e-12,-40558.1,74.8131], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[39.8039,0.0546226,-1.88739e-05,2.95022e-09,-1.71976e-13,-56954.9,-180.202], Tmin=(1393,'K'), Tmax=(5000,'K')),
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
    index = 127,
    label = "CCCCCCCCC1CCCO1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {8,S} {27,S} {28,S}
3  C u0 p0 c0 {1,S} {9,S} {29,S} {30,S}
4  C u0 p0 c0 {5,S} {10,S} {17,S} {18,S}
5  C u0 p0 c0 {4,S} {6,S} {19,S} {20,S}
6  C u0 p0 c0 {5,S} {7,S} {21,S} {22,S}
7  C u0 p0 c0 {6,S} {8,S} {23,S} {24,S}
8  C u0 p0 c0 {2,S} {7,S} {25,S} {26,S}
9  C u0 p0 c0 {3,S} {11,S} {31,S} {32,S}
10 C u0 p0 c0 {4,S} {12,S} {15,S} {16,S}
11 C u0 p0 c0 {9,S} {13,S} {33,S} {34,S}
12 C u0 p0 c0 {10,S} {35,S} {36,S} {37,S}
13 O u0 p2 c0 {1,S} {11,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {10,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {2,S}
28 H u0 p0 c0 {2,S}
29 H u0 p0 c0 {3,S}
30 H u0 p0 c0 {3,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.78099,0.161601,-0.000111365,3.95061e-08,-5.7546e-12,-48247.1,75.4392], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[38.854,0.0554503,-1.91657e-05,2.99655e-09,-1.74709e-13,-64778.5,-176.105], Tmin=(1392,'K'), Tmax=(5000,'K')),
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
    index = 128,
    label = "CCCCCCCC1OCCC1C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {11,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {15,S}
3  C u0 p0 c0 {2,S} {8,S} {26,S} {27,S}
4  C u0 p0 c0 {1,S} {10,S} {28,S} {29,S}
5  C u0 p0 c0 {6,S} {9,S} {18,S} {19,S}
6  C u0 p0 c0 {5,S} {7,S} {20,S} {21,S}
7  C u0 p0 c0 {6,S} {8,S} {22,S} {23,S}
8  C u0 p0 c0 {3,S} {7,S} {24,S} {25,S}
9  C u0 p0 c0 {5,S} {12,S} {16,S} {17,S}
10 C u0 p0 c0 {4,S} {13,S} {30,S} {31,S}
11 C u0 p0 c0 {1,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {9,S} {32,S} {33,S} {34,S}
13 O u0 p2 c0 {2,S} {10,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {3,S}
28 H u0 p0 c0 {4,S}
29 H u0 p0 c0 {4,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {12,S}
33 H u0 p0 c0 {12,S}
34 H u0 p0 c0 {12,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-9.72414,0.17266,-0.000128074,4.98189e-08,-8.02148e-12,-50230.3,83.5521], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[39.7731,0.0548992,-1.90264e-05,2.98013e-09,-1.73968e-13,-67319.7,-181.713], Tmin=(1392,'K'), Tmax=(5000,'K')),
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
    index = 129,
    label = "CCCCCCC1OCCC1CC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {8,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {15,S}
3  C u0 p0 c0 {2,S} {7,S} {24,S} {25,S}
4  C u0 p0 c0 {1,S} {10,S} {26,S} {27,S}
5  C u0 p0 c0 {6,S} {9,S} {18,S} {19,S}
6  C u0 p0 c0 {5,S} {7,S} {20,S} {21,S}
7  C u0 p0 c0 {3,S} {6,S} {22,S} {23,S}
8  C u0 p0 c0 {1,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {5,S} {11,S} {16,S} {17,S}
10 C u0 p0 c0 {4,S} {13,S} {30,S} {31,S}
11 C u0 p0 c0 {9,S} {32,S} {33,S} {34,S}
12 C u0 p0 c0 {8,S} {35,S} {36,S} {37,S}
13 O u0 p2 c0 {2,S} {10,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {4,S}
27 H u0 p0 c0 {4,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-9.72414,0.17266,-0.000128074,4.98189e-08,-8.02148e-12,-50230.3,83.5521], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[39.7731,0.0548992,-1.90264e-05,2.98013e-09,-1.73968e-13,-67319.7,-181.713], Tmin=(1392,'K'), Tmax=(5000,'K')),
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
    index = 130,
    label = "CCCCCC1OCCC1CCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {14,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {15,S}
3  C u0 p0 c0 {1,S} {9,S} {26,S} {27,S}
4  C u0 p0 c0 {2,S} {7,S} {22,S} {23,S}
5  C u0 p0 c0 {1,S} {10,S} {24,S} {25,S}
6  C u0 p0 c0 {7,S} {8,S} {18,S} {19,S}
7  C u0 p0 c0 {4,S} {6,S} {20,S} {21,S}
8  C u0 p0 c0 {6,S} {11,S} {16,S} {17,S}
9  C u0 p0 c0 {3,S} {12,S} {28,S} {29,S}
10 C u0 p0 c0 {5,S} {13,S} {30,S} {31,S}
11 C u0 p0 c0 {8,S} {32,S} {33,S} {34,S}
12 C u0 p0 c0 {9,S} {35,S} {36,S} {37,S}
13 O u0 p2 c0 {2,S} {10,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {3,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-9.72414,0.17266,-0.000128074,4.98189e-08,-8.02148e-12,-50230.3,83.5521], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[39.7731,0.0548992,-1.90264e-05,2.98013e-09,-1.73968e-13,-67319.7,-181.713], Tmin=(1392,'K'), Tmax=(5000,'K')),
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
    index = 131,
    label = "CCCCC1CCOC1CCCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {14,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {15,S}
3  C u0 p0 c0 {1,S} {7,S} {24,S} {25,S}
4  C u0 p0 c0 {2,S} {6,S} {20,S} {21,S}
5  C u0 p0 c0 {1,S} {10,S} {22,S} {23,S}
6  C u0 p0 c0 {4,S} {8,S} {18,S} {19,S}
7  C u0 p0 c0 {3,S} {9,S} {26,S} {27,S}
8  C u0 p0 c0 {6,S} {11,S} {16,S} {17,S}
9  C u0 p0 c0 {7,S} {12,S} {28,S} {29,S}
10 C u0 p0 c0 {5,S} {13,S} {30,S} {31,S}
11 C u0 p0 c0 {8,S} {32,S} {33,S} {34,S}
12 C u0 p0 c0 {9,S} {35,S} {36,S} {37,S}
13 O u0 p2 c0 {2,S} {10,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-9.72414,0.17266,-0.000128074,4.98189e-08,-8.02148e-12,-50230.3,83.5521], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[39.7731,0.0548992,-1.90264e-05,2.98013e-09,-1.73968e-13,-67319.7,-181.713], Tmin=(1392,'K'), Tmax=(5000,'K')),
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
    index = 132,
    label = "CCCCCCCC1CCCCO1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {7,S} {25,S} {26,S}
3  C u0 p0 c0 {1,S} {8,S} {27,S} {28,S}
4  C u0 p0 c0 {5,S} {10,S} {17,S} {18,S}
5  C u0 p0 c0 {4,S} {6,S} {19,S} {20,S}
6  C u0 p0 c0 {5,S} {7,S} {21,S} {22,S}
7  C u0 p0 c0 {2,S} {6,S} {23,S} {24,S}
8  C u0 p0 c0 {3,S} {9,S} {29,S} {30,S}
9  C u0 p0 c0 {8,S} {11,S} {31,S} {32,S}
10 C u0 p0 c0 {4,S} {12,S} {15,S} {16,S}
11 C u0 p0 c0 {9,S} {13,S} {33,S} {34,S}
12 C u0 p0 c0 {10,S} {35,S} {36,S} {37,S}
13 O u0 p2 c0 {1,S} {11,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {10,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {2,S}
26 H u0 p0 c0 {2,S}
27 H u0 p0 c0 {3,S}
28 H u0 p0 c0 {3,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-8.87088,0.165815,-0.000114726,4.06035e-08,-5.89399e-12,-50225.8,75.8319], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[40.1706,0.0549321,-1.91228e-05,3.00427e-09,-1.7575e-13,-67703.9,-188.991], Tmin=(1388,'K'), Tmax=(5000,'K')),
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
    index = 133,
    label = "CCCCCCC1OCCCC1C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {11,S} {14,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {15,S}
3  C u0 p0 c0 {1,S} {8,S} {28,S} {29,S}
4  C u0 p0 c0 {2,S} {7,S} {24,S} {25,S}
5  C u0 p0 c0 {6,S} {9,S} {18,S} {19,S}
6  C u0 p0 c0 {5,S} {7,S} {20,S} {21,S}
7  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
8  C u0 p0 c0 {3,S} {10,S} {26,S} {27,S}
9  C u0 p0 c0 {5,S} {12,S} {16,S} {17,S}
10 C u0 p0 c0 {8,S} {13,S} {30,S} {31,S}
11 C u0 p0 c0 {1,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {9,S} {32,S} {33,S} {34,S}
13 O u0 p2 c0 {2,S} {10,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {3,S}
29 H u0 p0 c0 {3,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {12,S}
33 H u0 p0 c0 {12,S}
34 H u0 p0 c0 {12,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-10.5409,0.175784,-0.000129888,4.99034e-08,-7.919e-12,-52253.7,82.6535], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[41.0846,0.0542617,-1.89153e-05,2.97437e-09,-1.74111e-13,-70201.1,-194.47], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 134,
    label = "CCCCCC1OCCCC1CC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {14,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {15,S}
3  C u0 p0 c0 {1,S} {8,S} {26,S} {27,S}
4  C u0 p0 c0 {2,S} {6,S} {22,S} {23,S}
5  C u0 p0 c0 {6,S} {9,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {5,S} {20,S} {21,S}
7  C u0 p0 c0 {1,S} {12,S} {28,S} {29,S}
8  C u0 p0 c0 {3,S} {10,S} {24,S} {25,S}
9  C u0 p0 c0 {5,S} {11,S} {16,S} {17,S}
10 C u0 p0 c0 {8,S} {13,S} {30,S} {31,S}
11 C u0 p0 c0 {9,S} {32,S} {33,S} {34,S}
12 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
13 O u0 p2 c0 {2,S} {10,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {3,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-10.5409,0.175784,-0.000129888,4.99034e-08,-7.919e-12,-52253.7,82.6535], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[41.0846,0.0542617,-1.89153e-05,2.97437e-09,-1.74111e-13,-70201.1,-194.47], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 135,
    label = "CCCCC1OCCCC1CCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {14,S}
2  C u0 p0 c0 {1,S} {5,S} {13,S} {15,S}
3  C u0 p0 c0 {1,S} {7,S} {24,S} {25,S}
4  C u0 p0 c0 {1,S} {9,S} {26,S} {27,S}
5  C u0 p0 c0 {2,S} {6,S} {20,S} {21,S}
6  C u0 p0 c0 {5,S} {8,S} {18,S} {19,S}
7  C u0 p0 c0 {3,S} {10,S} {22,S} {23,S}
8  C u0 p0 c0 {6,S} {11,S} {16,S} {17,S}
9  C u0 p0 c0 {4,S} {12,S} {28,S} {29,S}
10 C u0 p0 c0 {7,S} {13,S} {30,S} {31,S}
11 C u0 p0 c0 {8,S} {32,S} {33,S} {34,S}
12 C u0 p0 c0 {9,S} {35,S} {36,S} {37,S}
13 O u0 p2 c0 {2,S} {10,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {4,S}
27 H u0 p0 c0 {4,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-10.5409,0.175784,-0.000129888,4.99034e-08,-7.919e-12,-52253.7,82.6535], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[41.0846,0.0542617,-1.89153e-05,2.97437e-09,-1.74111e-13,-70201.1,-194.47], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 136,
    label = "CCCCCCCCCC=O",
    molecule = 
"""
1  O u0 p2 c0 {11,D}
2  C u0 p0 c0 {3,S} {8,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {4,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {5,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {20,S} {21,S}
6  C u0 p0 c0 {5,S} {7,S} {22,S} {23,S}
7  C u0 p0 c0 {6,S} {9,S} {24,S} {25,S}
8  C u0 p0 c0 {2,S} {10,S} {12,S} {13,S}
9  C u0 p0 c0 {7,S} {11,S} {26,S} {27,S}
10 C u0 p0 c0 {8,S} {28,S} {29,S} {30,S}
11 C u0 p0 c0 {1,D} {9,S} {31,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {10,S}
29 H u0 p0 c0 {10,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.582223,0.114923,-7.28776e-05,2.37837e-08,-3.20082e-12,-44446.6,35.2424], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[32.469,0.0453285,-1.55213e-05,2.41159e-09,-1.39992e-13,-56114.1,-137.921], Tmin=(1388,'K'), Tmax=(5000,'K')),
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
    index = 137,
    label = "CCCCCCCCC=O",
    molecule = 
"""
1  O u0 p2 c0 {10,D}
2  C u0 p0 c0 {3,S} {7,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {5,S} {17,S} {18,S}
5  C u0 p0 c0 {4,S} {6,S} {19,S} {20,S}
6  C u0 p0 c0 {5,S} {8,S} {21,S} {22,S}
7  C u0 p0 c0 {2,S} {9,S} {11,S} {12,S}
8  C u0 p0 c0 {6,S} {10,S} {23,S} {24,S}
9  C u0 p0 c0 {7,S} {25,S} {26,S} {27,S}
10 C u0 p0 c0 {1,D} {8,S} {28,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.756488,0.102972,-6.49911e-05,2.10892e-08,-2.82096e-12,-41550.8,32.7444], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[29.316,0.0408274,-1.39769e-05,2.17134e-09,-1.26034e-13,-52023.5,-122.423], Tmin=(1387,'K'), Tmax=(5000,'K')),
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
    index = 138,
    label = "CCCCCCCC=O",
    molecule = 
"""
1  O u0 p2 c0 {9,D}
2  C u0 p0 c0 {3,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {5,S} {16,S} {17,S}
5  C u0 p0 c0 {4,S} {7,S} {18,S} {19,S}
6  C u0 p0 c0 {2,S} {8,S} {10,S} {11,S}
7  C u0 p0 c0 {5,S} {9,S} {20,S} {21,S}
8  C u0 p0 c0 {6,S} {22,S} {23,S} {24,S}
9  C u0 p0 c0 {1,D} {7,S} {25,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.96685,0.0908064,-5.6771e-05,1.81651e-08,-2.38497e-12,-38658.7,30.0919], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[26.1609,0.0362859,-1.24097e-05,1.92662e-09,-1.11781e-13,-47926,-106.895], Tmin=(1386,'K'), Tmax=(5000,'K')),
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
    index = 139,
    label = "CCCCCCC=O",
    molecule = 
"""
1  O u0 p2 c0 {8,D}
2  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {7,S} {9,S} {10,S}
6  C u0 p0 c0 {4,S} {8,S} {17,S} {18,S}
7  C u0 p0 c0 {5,S} {19,S} {20,S} {21,S}
8  C u0 p0 c0 {1,D} {6,S} {22,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.16727,0.0787064,-4.86434e-05,1.53023e-08,-1.96405e-12,-35765.9,27.48], Tmin=(298,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[23.0173,0.0317488,-1.08472e-05,1.68297e-09,-9.76032e-14,-43836.2,-91.4417], Tmin=(1385,'K'), Tmax=(5000,'K')),
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
    index = 140,
    label = "CCCCCCCCCCC(O[O])COO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {11,S} {14,S} {16,S}
2  C u0 p0 c0 {1,S} {9,S} {33,S} {34,S}
3  C u0 p0 c0 {4,S} {10,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {8,S} {27,S} {28,S}
8  C u0 p0 c0 {7,S} {9,S} {29,S} {30,S}
9  C u0 p0 c0 {2,S} {8,S} {31,S} {32,S}
10 C u0 p0 c0 {3,S} {12,S} {17,S} {18,S}
11 C u0 p0 c0 {1,S} {13,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {11,S} {15,S}
14 O u0 p2 c0 {1,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {2,S}
34 H u0 p0 c0 {2,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.14842,0.153205,-9.6423e-05,2.94571e-08,-3.45152e-12,-48291.6,34.0093], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[48.7897,0.0552856,-1.91573e-05,3.00051e-09,-1.75161e-13,-65016.6,-214.208], Tmin=(1388,'K'), Tmax=(5000,'K')),
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
    index = 141,
    label = "CCCCCCCCCC(O[O])CCOO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {14,S} {16,S}
2  C u0 p0 c0 {1,S} {8,S} {31,S} {32,S}
3  C u0 p0 c0 {4,S} {10,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {8,S} {27,S} {28,S}
8  C u0 p0 c0 {2,S} {7,S} {29,S} {30,S}
9  C u0 p0 c0 {1,S} {11,S} {33,S} {34,S}
10 C u0 p0 c0 {3,S} {12,S} {17,S} {18,S}
11 C u0 p0 c0 {9,S} {13,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {11,S} {15,S}
14 O u0 p2 c0 {1,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {2,S}
32 H u0 p0 c0 {2,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {9,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.14842,0.153205,-9.6423e-05,2.94571e-08,-3.45152e-12,-48291.6,34.0093], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[48.7897,0.0552856,-1.91573e-05,3.00051e-09,-1.75161e-13,-65016.6,-214.208], Tmin=(1388,'K'), Tmax=(5000,'K')),
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
    index = 142,
    label = "CCCCCCCCC(O[O])CCCOO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {14,S} {16,S}
2  C u0 p0 c0 {1,S} {8,S} {29,S} {30,S}
3  C u0 p0 c0 {1,S} {9,S} {31,S} {32,S}
4  C u0 p0 c0 {5,S} {10,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {5,S} {7,S} {23,S} {24,S}
7  C u0 p0 c0 {6,S} {8,S} {25,S} {26,S}
8  C u0 p0 c0 {2,S} {7,S} {27,S} {28,S}
9  C u0 p0 c0 {3,S} {11,S} {33,S} {34,S}
10 C u0 p0 c0 {4,S} {12,S} {17,S} {18,S}
11 C u0 p0 c0 {9,S} {13,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {11,S} {15,S}
14 O u0 p2 c0 {1,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {2,S}
30 H u0 p0 c0 {2,S}
31 H u0 p0 c0 {3,S}
32 H u0 p0 c0 {3,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {9,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.14842,0.153205,-9.6423e-05,2.94571e-08,-3.45152e-12,-48291.6,34.0093], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[48.7897,0.0552856,-1.91573e-05,3.00051e-09,-1.75161e-13,-65016.6,-214.208], Tmin=(1388,'K'), Tmax=(5000,'K')),
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
    index = 143,
    label = "CCCCCCCC(O[O])CCCCOO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {14,S} {16,S}
2  C u0 p0 c0 {1,S} {7,S} {27,S} {28,S}
3  C u0 p0 c0 {1,S} {8,S} {29,S} {30,S}
4  C u0 p0 c0 {5,S} {10,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {5,S} {7,S} {23,S} {24,S}
7  C u0 p0 c0 {2,S} {6,S} {25,S} {26,S}
8  C u0 p0 c0 {3,S} {9,S} {31,S} {32,S}
9  C u0 p0 c0 {8,S} {11,S} {33,S} {34,S}
10 C u0 p0 c0 {4,S} {12,S} {17,S} {18,S}
11 C u0 p0 c0 {9,S} {13,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {11,S} {15,S}
14 O u0 p2 c0 {1,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {2,S}
28 H u0 p0 c0 {2,S}
29 H u0 p0 c0 {3,S}
30 H u0 p0 c0 {3,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {8,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {9,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.14842,0.153205,-9.6423e-05,2.94571e-08,-3.45152e-12,-48291.6,34.0093], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[48.7897,0.0552856,-1.91573e-05,3.00051e-09,-1.75161e-13,-65016.6,-214.208], Tmin=(1388,'K'), Tmax=(5000,'K')),
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
    index = 144,
    label = "C(O[O])C(CCCCCCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {11,S} {13,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {8,S} {27,S} {28,S}
8  C u0 p0 c0 {7,S} {9,S} {29,S} {30,S}
9  C u0 p0 c0 {8,S} {10,S} {31,S} {32,S}
10 C u0 p0 c0 {9,S} {12,S} {33,S} {34,S}
11 C u0 p0 c0 {1,S} {14,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {11,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.14842,0.153205,-9.6423e-05,2.94571e-08,-3.45152e-12,-48291.6,34.0093], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[48.7897,0.0552856,-1.91573e-05,3.00051e-09,-1.75161e-13,-65016.6,-214.208], Tmin=(1388,'K'), Tmax=(5000,'K')),
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
    index = 145,
    label = "CCCCCCCCCC(O[O])C(C)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {14,S} {16,S}
2  C u0 p0 c0 {1,S} {11,S} {13,S} {17,S}
3  C u0 p0 c0 {1,S} {9,S} {32,S} {33,S}
4  C u0 p0 c0 {5,S} {10,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {6,S} {8,S} {26,S} {27,S}
8  C u0 p0 c0 {7,S} {9,S} {28,S} {29,S}
9  C u0 p0 c0 {3,S} {8,S} {30,S} {31,S}
10 C u0 p0 c0 {4,S} {12,S} {18,S} {19,S}
11 C u0 p0 c0 {2,S} {37,S} {38,S} {39,S}
12 C u0 p0 c0 {10,S} {34,S} {35,S} {36,S}
13 O u0 p2 c0 {2,S} {15,S}
14 O u0 p2 c0 {1,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {3,S}
33 H u0 p0 c0 {3,S}
34 H u0 p0 c0 {12,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {11,S}
39 H u0 p0 c0 {11,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 146,
    label = "CCCCCCCCC(O[O])CC(C)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {14,S} {16,S}
2  C u0 p0 c0 {3,S} {11,S} {13,S} {17,S}
3  C u0 p0 c0 {1,S} {2,S} {32,S} {33,S}
4  C u0 p0 c0 {1,S} {9,S} {30,S} {31,S}
5  C u0 p0 c0 {6,S} {10,S} {20,S} {21,S}
6  C u0 p0 c0 {5,S} {7,S} {22,S} {23,S}
7  C u0 p0 c0 {6,S} {8,S} {24,S} {25,S}
8  C u0 p0 c0 {7,S} {9,S} {26,S} {27,S}
9  C u0 p0 c0 {4,S} {8,S} {28,S} {29,S}
10 C u0 p0 c0 {5,S} {12,S} {18,S} {19,S}
11 C u0 p0 c0 {2,S} {37,S} {38,S} {39,S}
12 C u0 p0 c0 {10,S} {34,S} {35,S} {36,S}
13 O u0 p2 c0 {2,S} {15,S}
14 O u0 p2 c0 {1,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {4,S}
31 H u0 p0 c0 {4,S}
32 H u0 p0 c0 {3,S}
33 H u0 p0 c0 {3,S}
34 H u0 p0 c0 {12,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {11,S}
39 H u0 p0 c0 {11,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 147,
    label = "CCCCCCCC(O[O])CCC(C)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {14,S} {16,S}
2  C u0 p0 c0 {5,S} {11,S} {13,S} {17,S}
3  C u0 p0 c0 {1,S} {9,S} {28,S} {29,S}
4  C u0 p0 c0 {1,S} {5,S} {30,S} {31,S}
5  C u0 p0 c0 {2,S} {4,S} {32,S} {33,S}
6  C u0 p0 c0 {7,S} {10,S} {20,S} {21,S}
7  C u0 p0 c0 {6,S} {8,S} {22,S} {23,S}
8  C u0 p0 c0 {7,S} {9,S} {24,S} {25,S}
9  C u0 p0 c0 {3,S} {8,S} {26,S} {27,S}
10 C u0 p0 c0 {6,S} {12,S} {18,S} {19,S}
11 C u0 p0 c0 {2,S} {37,S} {38,S} {39,S}
12 C u0 p0 c0 {10,S} {34,S} {35,S} {36,S}
13 O u0 p2 c0 {2,S} {15,S}
14 O u0 p2 c0 {1,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {3,S}
29 H u0 p0 c0 {3,S}
30 H u0 p0 c0 {4,S}
31 H u0 p0 c0 {4,S}
32 H u0 p0 c0 {5,S}
33 H u0 p0 c0 {5,S}
34 H u0 p0 c0 {12,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {11,S}
39 H u0 p0 c0 {11,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 148,
    label = "CCCCCCC(O[O])CCCC(C)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {14,S} {16,S}
2  C u0 p0 c0 {5,S} {11,S} {13,S} {17,S}
3  C u0 p0 c0 {1,S} {8,S} {26,S} {27,S}
4  C u0 p0 c0 {1,S} {9,S} {28,S} {29,S}
5  C u0 p0 c0 {2,S} {9,S} {32,S} {33,S}
6  C u0 p0 c0 {7,S} {10,S} {20,S} {21,S}
7  C u0 p0 c0 {6,S} {8,S} {22,S} {23,S}
8  C u0 p0 c0 {3,S} {7,S} {24,S} {25,S}
9  C u0 p0 c0 {4,S} {5,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {12,S} {18,S} {19,S}
11 C u0 p0 c0 {2,S} {37,S} {38,S} {39,S}
12 C u0 p0 c0 {10,S} {34,S} {35,S} {36,S}
13 O u0 p2 c0 {2,S} {15,S}
14 O u0 p2 c0 {1,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {3,S}
28 H u0 p0 c0 {4,S}
29 H u0 p0 c0 {4,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {5,S}
33 H u0 p0 c0 {5,S}
34 H u0 p0 c0 {12,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {11,S}
39 H u0 p0 c0 {11,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 149,
    label = "C(O[O])CC(CCCCCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {13,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {19,S} {20,S}
3  C u0 p0 c0 {2,S} {4,S} {21,S} {22,S}
4  C u0 p0 c0 {3,S} {5,S} {23,S} {24,S}
5  C u0 p0 c0 {4,S} {6,S} {25,S} {26,S}
6  C u0 p0 c0 {5,S} {7,S} {27,S} {28,S}
7  C u0 p0 c0 {6,S} {8,S} {29,S} {30,S}
8  C u0 p0 c0 {7,S} {10,S} {31,S} {32,S}
9  C u0 p0 c0 {1,S} {11,S} {17,S} {18,S}
10 C u0 p0 c0 {8,S} {12,S} {33,S} {34,S}
11 C u0 p0 c0 {9,S} {14,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {11,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {6,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {7,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {8,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.14842,0.153205,-9.6423e-05,2.94571e-08,-3.45152e-12,-48291.6,34.0093], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[48.7897,0.0552856,-1.91573e-05,3.00051e-09,-1.75161e-13,-65016.6,-214.208], Tmin=(1388,'K'), Tmax=(5000,'K')),
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
    index = 150,
    label = "CC(O[O])C(CCCCCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {17,S}
2  C u0 p0 c0 {1,S} {11,S} {14,S} {16,S}
3  C u0 p0 c0 {1,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {6,S} {8,S} {26,S} {27,S}
8  C u0 p0 c0 {7,S} {9,S} {28,S} {29,S}
9  C u0 p0 c0 {8,S} {10,S} {30,S} {31,S}
10 C u0 p0 c0 {9,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {2,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 151,
    label = "CCCCCCCCC(O[O])C(CC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {13,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {16,S}
3  C u0 p0 c0 {2,S} {8,S} {30,S} {31,S}
4  C u0 p0 c0 {5,S} {10,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {6,S} {8,S} {26,S} {27,S}
8  C u0 p0 c0 {3,S} {7,S} {28,S} {29,S}
9  C u0 p0 c0 {1,S} {12,S} {32,S} {33,S}
10 C u0 p0 c0 {4,S} {11,S} {18,S} {19,S}
11 C u0 p0 c0 {10,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {9,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {3,S}
31 H u0 p0 c0 {3,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 152,
    label = "CCCCCCCC(O[O])CC(CC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {9,S} {13,S} {17,S}
2  C u0 p0 c0 {3,S} {4,S} {14,S} {16,S}
3  C u0 p0 c0 {1,S} {2,S} {30,S} {31,S}
4  C u0 p0 c0 {2,S} {8,S} {28,S} {29,S}
5  C u0 p0 c0 {6,S} {10,S} {20,S} {21,S}
6  C u0 p0 c0 {5,S} {7,S} {22,S} {23,S}
7  C u0 p0 c0 {6,S} {8,S} {24,S} {25,S}
8  C u0 p0 c0 {4,S} {7,S} {26,S} {27,S}
9  C u0 p0 c0 {1,S} {12,S} {32,S} {33,S}
10 C u0 p0 c0 {5,S} {11,S} {18,S} {19,S}
11 C u0 p0 c0 {10,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {9,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {4,S}
29 H u0 p0 c0 {4,S}
30 H u0 p0 c0 {3,S}
31 H u0 p0 c0 {3,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 153,
    label = "CCCCCCC(O[O])CCC(CC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {9,S} {13,S} {17,S}
2  C u0 p0 c0 {3,S} {4,S} {14,S} {16,S}
3  C u0 p0 c0 {2,S} {8,S} {26,S} {27,S}
4  C u0 p0 c0 {2,S} {5,S} {28,S} {29,S}
5  C u0 p0 c0 {1,S} {4,S} {30,S} {31,S}
6  C u0 p0 c0 {7,S} {10,S} {20,S} {21,S}
7  C u0 p0 c0 {6,S} {8,S} {22,S} {23,S}
8  C u0 p0 c0 {3,S} {7,S} {24,S} {25,S}
9  C u0 p0 c0 {1,S} {12,S} {32,S} {33,S}
10 C u0 p0 c0 {6,S} {11,S} {18,S} {19,S}
11 C u0 p0 c0 {10,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {9,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {3,S}
28 H u0 p0 c0 {4,S}
29 H u0 p0 c0 {4,S}
30 H u0 p0 c0 {5,S}
31 H u0 p0 c0 {5,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 154,
    label = "CCCCCC(O[O])CCCC(CC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {9,S} {13,S} {17,S}
2  C u0 p0 c0 {3,S} {4,S} {14,S} {16,S}
3  C u0 p0 c0 {2,S} {7,S} {24,S} {25,S}
4  C u0 p0 c0 {2,S} {8,S} {26,S} {27,S}
5  C u0 p0 c0 {1,S} {8,S} {30,S} {31,S}
6  C u0 p0 c0 {7,S} {10,S} {20,S} {21,S}
7  C u0 p0 c0 {3,S} {6,S} {22,S} {23,S}
8  C u0 p0 c0 {4,S} {5,S} {28,S} {29,S}
9  C u0 p0 c0 {1,S} {12,S} {32,S} {33,S}
10 C u0 p0 c0 {6,S} {11,S} {18,S} {19,S}
11 C u0 p0 c0 {10,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {9,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {4,S}
27 H u0 p0 c0 {4,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {5,S}
31 H u0 p0 c0 {5,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 155,
    label = "C(O[O])CCC(CCCCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {16,S}
2  C u0 p0 c0 {1,S} {9,S} {19,S} {20,S}
3  C u0 p0 c0 {1,S} {4,S} {21,S} {22,S}
4  C u0 p0 c0 {3,S} {5,S} {23,S} {24,S}
5  C u0 p0 c0 {4,S} {6,S} {25,S} {26,S}
6  C u0 p0 c0 {5,S} {7,S} {27,S} {28,S}
7  C u0 p0 c0 {6,S} {8,S} {29,S} {30,S}
8  C u0 p0 c0 {7,S} {10,S} {31,S} {32,S}
9  C u0 p0 c0 {2,S} {11,S} {17,S} {18,S}
10 C u0 p0 c0 {8,S} {12,S} {33,S} {34,S}
11 C u0 p0 c0 {9,S} {14,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {11,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {6,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {7,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {8,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.14842,0.153205,-9.6423e-05,2.94571e-08,-3.45152e-12,-48291.6,34.0093], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[48.7897,0.0552856,-1.91573e-05,3.00051e-09,-1.75161e-13,-65016.6,-214.208], Tmin=(1388,'K'), Tmax=(5000,'K')),
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
    index = 156,
    label = "CC(O[O])CC(CCCCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {13,S} {17,S}
2  C u0 p0 c0 {3,S} {11,S} {14,S} {16,S}
3  C u0 p0 c0 {1,S} {2,S} {18,S} {19,S}
4  C u0 p0 c0 {1,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {6,S} {8,S} {26,S} {27,S}
8  C u0 p0 c0 {7,S} {9,S} {28,S} {29,S}
9  C u0 p0 c0 {8,S} {10,S} {30,S} {31,S}
10 C u0 p0 c0 {9,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {2,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 157,
    label = "CCC(O[O])C(CCCCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {17,S}
2  C u0 p0 c0 {1,S} {9,S} {14,S} {16,S}
3  C u0 p0 c0 {1,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {6,S} {24,S} {25,S}
6  C u0 p0 c0 {5,S} {7,S} {26,S} {27,S}
7  C u0 p0 c0 {6,S} {8,S} {28,S} {29,S}
8  C u0 p0 c0 {7,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {2,S} {11,S} {18,S} {19,S}
10 C u0 p0 c0 {8,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 158,
    label = "CCCCCCCC(O[O])C(CCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {13,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {16,S}
3  C u0 p0 c0 {2,S} {8,S} {28,S} {29,S}
4  C u0 p0 c0 {1,S} {10,S} {30,S} {31,S}
5  C u0 p0 c0 {6,S} {9,S} {20,S} {21,S}
6  C u0 p0 c0 {5,S} {7,S} {22,S} {23,S}
7  C u0 p0 c0 {6,S} {8,S} {24,S} {25,S}
8  C u0 p0 c0 {3,S} {7,S} {26,S} {27,S}
9  C u0 p0 c0 {5,S} {11,S} {18,S} {19,S}
10 C u0 p0 c0 {4,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {3,S}
29 H u0 p0 c0 {3,S}
30 H u0 p0 c0 {4,S}
31 H u0 p0 c0 {4,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 159,
    label = "CCCCCCC(O[O])CC(CCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {13,S} {17,S}
2  C u0 p0 c0 {3,S} {4,S} {14,S} {16,S}
3  C u0 p0 c0 {1,S} {2,S} {28,S} {29,S}
4  C u0 p0 c0 {2,S} {8,S} {26,S} {27,S}
5  C u0 p0 c0 {1,S} {10,S} {30,S} {31,S}
6  C u0 p0 c0 {7,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {6,S} {8,S} {22,S} {23,S}
8  C u0 p0 c0 {4,S} {7,S} {24,S} {25,S}
9  C u0 p0 c0 {6,S} {11,S} {18,S} {19,S}
10 C u0 p0 c0 {5,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {4,S}
27 H u0 p0 c0 {4,S}
28 H u0 p0 c0 {3,S}
29 H u0 p0 c0 {3,S}
30 H u0 p0 c0 {5,S}
31 H u0 p0 c0 {5,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 160,
    label = "CCCCCC(O[O])CCC(CCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {13,S} {17,S}
2  C u0 p0 c0 {3,S} {4,S} {14,S} {16,S}
3  C u0 p0 c0 {2,S} {8,S} {24,S} {25,S}
4  C u0 p0 c0 {2,S} {5,S} {26,S} {27,S}
5  C u0 p0 c0 {1,S} {4,S} {28,S} {29,S}
6  C u0 p0 c0 {1,S} {10,S} {30,S} {31,S}
7  C u0 p0 c0 {8,S} {9,S} {20,S} {21,S}
8  C u0 p0 c0 {3,S} {7,S} {22,S} {23,S}
9  C u0 p0 c0 {7,S} {11,S} {18,S} {19,S}
10 C u0 p0 c0 {6,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {4,S}
27 H u0 p0 c0 {4,S}
28 H u0 p0 c0 {5,S}
29 H u0 p0 c0 {5,S}
30 H u0 p0 c0 {6,S}
31 H u0 p0 c0 {6,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 161,
    label = "CCCCC(O[O])CCCC(CCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {13,S} {17,S}
2  C u0 p0 c0 {3,S} {4,S} {14,S} {16,S}
3  C u0 p0 c0 {2,S} {7,S} {22,S} {23,S}
4  C u0 p0 c0 {2,S} {8,S} {24,S} {25,S}
5  C u0 p0 c0 {1,S} {8,S} {28,S} {29,S}
6  C u0 p0 c0 {1,S} {10,S} {30,S} {31,S}
7  C u0 p0 c0 {3,S} {9,S} {20,S} {21,S}
8  C u0 p0 c0 {4,S} {5,S} {26,S} {27,S}
9  C u0 p0 c0 {7,S} {11,S} {18,S} {19,S}
10 C u0 p0 c0 {6,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {5,S}
29 H u0 p0 c0 {5,S}
30 H u0 p0 c0 {6,S}
31 H u0 p0 c0 {6,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 162,
    label = "C(O[O])CCCC(CCCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {16,S}
2  C u0 p0 c0 {1,S} {4,S} {21,S} {22,S}
3  C u0 p0 c0 {1,S} {5,S} {23,S} {24,S}
4  C u0 p0 c0 {2,S} {9,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {6,S} {25,S} {26,S}
6  C u0 p0 c0 {5,S} {7,S} {27,S} {28,S}
7  C u0 p0 c0 {6,S} {8,S} {29,S} {30,S}
8  C u0 p0 c0 {7,S} {10,S} {31,S} {32,S}
9  C u0 p0 c0 {4,S} {11,S} {17,S} {18,S}
10 C u0 p0 c0 {8,S} {12,S} {33,S} {34,S}
11 C u0 p0 c0 {9,S} {14,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {11,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {6,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {7,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {8,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.14842,0.153205,-9.6423e-05,2.94571e-08,-3.45152e-12,-48291.6,34.0093], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[48.7897,0.0552856,-1.91573e-05,3.00051e-09,-1.75161e-13,-65016.6,-214.208], Tmin=(1388,'K'), Tmax=(5000,'K')),
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
    index = 163,
    label = "CC(O[O])CCC(CCCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {13,S} {17,S}
2  C u0 p0 c0 {3,S} {11,S} {14,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {1,S} {3,S} {20,S} {21,S}
5  C u0 p0 c0 {1,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {6,S} {8,S} {26,S} {27,S}
8  C u0 p0 c0 {7,S} {9,S} {28,S} {29,S}
9  C u0 p0 c0 {8,S} {10,S} {30,S} {31,S}
10 C u0 p0 c0 {9,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {2,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 164,
    label = "CCC(O[O])CC(CCCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {13,S} {17,S}
2  C u0 p0 c0 {3,S} {9,S} {14,S} {16,S}
3  C u0 p0 c0 {1,S} {2,S} {20,S} {21,S}
4  C u0 p0 c0 {1,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {6,S} {24,S} {25,S}
6  C u0 p0 c0 {5,S} {7,S} {26,S} {27,S}
7  C u0 p0 c0 {6,S} {8,S} {28,S} {29,S}
8  C u0 p0 c0 {7,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {2,S} {11,S} {18,S} {19,S}
10 C u0 p0 c0 {8,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 165,
    label = "CCCC(O[O])C(CCCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {13,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {16,S}
3  C u0 p0 c0 {2,S} {9,S} {20,S} {21,S}
4  C u0 p0 c0 {1,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {6,S} {24,S} {25,S}
6  C u0 p0 c0 {5,S} {7,S} {26,S} {27,S}
7  C u0 p0 c0 {6,S} {8,S} {28,S} {29,S}
8  C u0 p0 c0 {7,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {3,S} {11,S} {18,S} {19,S}
10 C u0 p0 c0 {8,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 166,
    label = "CCCCCCC(O[O])C(CCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {13,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {16,S}
3  C u0 p0 c0 {2,S} {7,S} {26,S} {27,S}
4  C u0 p0 c0 {1,S} {8,S} {28,S} {29,S}
5  C u0 p0 c0 {6,S} {9,S} {20,S} {21,S}
6  C u0 p0 c0 {5,S} {7,S} {22,S} {23,S}
7  C u0 p0 c0 {3,S} {6,S} {24,S} {25,S}
8  C u0 p0 c0 {4,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {5,S} {11,S} {18,S} {19,S}
10 C u0 p0 c0 {8,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {3,S}
28 H u0 p0 c0 {4,S}
29 H u0 p0 c0 {4,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 167,
    label = "CCCCCC(O[O])CC(CCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {13,S} {17,S}
2  C u0 p0 c0 {3,S} {4,S} {14,S} {16,S}
3  C u0 p0 c0 {1,S} {2,S} {26,S} {27,S}
4  C u0 p0 c0 {2,S} {7,S} {24,S} {25,S}
5  C u0 p0 c0 {1,S} {8,S} {28,S} {29,S}
6  C u0 p0 c0 {7,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
8  C u0 p0 c0 {5,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {6,S} {11,S} {18,S} {19,S}
10 C u0 p0 c0 {8,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {3,S}
28 H u0 p0 c0 {5,S}
29 H u0 p0 c0 {5,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 168,
    label = "CCCCC(O[O])CCC(CCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {13,S} {17,S}
2  C u0 p0 c0 {3,S} {4,S} {14,S} {16,S}
3  C u0 p0 c0 {2,S} {7,S} {22,S} {23,S}
4  C u0 p0 c0 {2,S} {5,S} {24,S} {25,S}
5  C u0 p0 c0 {1,S} {4,S} {26,S} {27,S}
6  C u0 p0 c0 {1,S} {8,S} {28,S} {29,S}
7  C u0 p0 c0 {3,S} {9,S} {20,S} {21,S}
8  C u0 p0 c0 {6,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {7,S} {11,S} {18,S} {19,S}
10 C u0 p0 c0 {8,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {5,S}
28 H u0 p0 c0 {6,S}
29 H u0 p0 c0 {6,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 169,
    label = "CCCC(O[O])CCCC(CCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {13,S} {17,S}
2  C u0 p0 c0 {3,S} {4,S} {14,S} {16,S}
3  C u0 p0 c0 {2,S} {9,S} {20,S} {21,S}
4  C u0 p0 c0 {2,S} {7,S} {22,S} {23,S}
5  C u0 p0 c0 {1,S} {7,S} {26,S} {27,S}
6  C u0 p0 c0 {1,S} {8,S} {28,S} {29,S}
7  C u0 p0 c0 {4,S} {5,S} {24,S} {25,S}
8  C u0 p0 c0 {6,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {3,S} {11,S} {18,S} {19,S}
10 C u0 p0 c0 {8,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {5,S}
28 H u0 p0 c0 {6,S}
29 H u0 p0 c0 {6,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 170,
    label = "CC(O[O])CCCC(CCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {13,S} {17,S}
2  C u0 p0 c0 {3,S} {11,S} {14,S} {16,S}
3  C u0 p0 c0 {2,S} {6,S} {18,S} {19,S}
4  C u0 p0 c0 {1,S} {6,S} {22,S} {23,S}
5  C u0 p0 c0 {1,S} {7,S} {24,S} {25,S}
6  C u0 p0 c0 {3,S} {4,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {8,S} {26,S} {27,S}
8  C u0 p0 c0 {7,S} {9,S} {28,S} {29,S}
9  C u0 p0 c0 {8,S} {10,S} {30,S} {31,S}
10 C u0 p0 c0 {9,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {2,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 171,
    label = "CCC(O[O])CCC(CCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {13,S} {17,S}
2  C u0 p0 c0 {3,S} {9,S} {14,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {1,S} {3,S} {22,S} {23,S}
5  C u0 p0 c0 {1,S} {6,S} {24,S} {25,S}
6  C u0 p0 c0 {5,S} {7,S} {26,S} {27,S}
7  C u0 p0 c0 {6,S} {8,S} {28,S} {29,S}
8  C u0 p0 c0 {7,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {2,S} {11,S} {18,S} {19,S}
10 C u0 p0 c0 {8,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 172,
    label = "CCCC(O[O])CC(CCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {13,S} {17,S}
2  C u0 p0 c0 {3,S} {4,S} {14,S} {16,S}
3  C u0 p0 c0 {1,S} {2,S} {22,S} {23,S}
4  C u0 p0 c0 {2,S} {9,S} {20,S} {21,S}
5  C u0 p0 c0 {1,S} {6,S} {24,S} {25,S}
6  C u0 p0 c0 {5,S} {7,S} {26,S} {27,S}
7  C u0 p0 c0 {6,S} {8,S} {28,S} {29,S}
8  C u0 p0 c0 {7,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {4,S} {11,S} {18,S} {19,S}
10 C u0 p0 c0 {8,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 173,
    label = "CCCCC(O[O])C(CCCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {13,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {16,S}
3  C u0 p0 c0 {2,S} {5,S} {22,S} {23,S}
4  C u0 p0 c0 {1,S} {6,S} {24,S} {25,S}
5  C u0 p0 c0 {3,S} {9,S} {20,S} {21,S}
6  C u0 p0 c0 {4,S} {7,S} {26,S} {27,S}
7  C u0 p0 c0 {6,S} {8,S} {28,S} {29,S}
8  C u0 p0 c0 {7,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {5,S} {11,S} {18,S} {19,S}
10 C u0 p0 c0 {8,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 174,
    label = "CCCCCC(O[O])C(CCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {13,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {16,S}
3  C u0 p0 c0 {2,S} {6,S} {24,S} {25,S}
4  C u0 p0 c0 {1,S} {7,S} {26,S} {27,S}
5  C u0 p0 c0 {6,S} {9,S} {20,S} {21,S}
6  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
7  C u0 p0 c0 {4,S} {8,S} {28,S} {29,S}
8  C u0 p0 c0 {7,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {5,S} {11,S} {18,S} {19,S}
10 C u0 p0 c0 {8,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {4,S}
27 H u0 p0 c0 {4,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 175,
    label = "CCCCC(O[O])CC(CCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {13,S} {17,S}
2  C u0 p0 c0 {3,S} {4,S} {14,S} {16,S}
3  C u0 p0 c0 {1,S} {2,S} {24,S} {25,S}
4  C u0 p0 c0 {2,S} {6,S} {22,S} {23,S}
5  C u0 p0 c0 {1,S} {7,S} {26,S} {27,S}
6  C u0 p0 c0 {4,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {8,S} {28,S} {29,S}
8  C u0 p0 c0 {7,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {6,S} {11,S} {18,S} {19,S}
10 C u0 p0 c0 {8,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {5,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 176,
    label = "CCCC(O[O])CCC(CCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {13,S} {17,S}
2  C u0 p0 c0 {3,S} {4,S} {14,S} {16,S}
3  C u0 p0 c0 {2,S} {9,S} {20,S} {21,S}
4  C u0 p0 c0 {2,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {1,S} {4,S} {24,S} {25,S}
6  C u0 p0 c0 {1,S} {7,S} {26,S} {27,S}
7  C u0 p0 c0 {6,S} {8,S} {28,S} {29,S}
8  C u0 p0 c0 {7,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {3,S} {11,S} {18,S} {19,S}
10 C u0 p0 c0 {8,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 177,
    label = "CCC(O[O])CCCC(CCCCC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {13,S} {17,S}
2  C u0 p0 c0 {3,S} {9,S} {14,S} {16,S}
3  C u0 p0 c0 {2,S} {6,S} {20,S} {21,S}
4  C u0 p0 c0 {1,S} {6,S} {24,S} {25,S}
5  C u0 p0 c0 {1,S} {7,S} {26,S} {27,S}
6  C u0 p0 c0 {3,S} {4,S} {22,S} {23,S}
7  C u0 p0 c0 {5,S} {8,S} {28,S} {29,S}
8  C u0 p0 c0 {7,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {2,S} {11,S} {18,S} {19,S}
10 C u0 p0 c0 {8,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {5,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33639,0.15807,-0.000103826,3.38978e-08,-4.39025e-12,-49949.9,36.0628], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[49.2017,0.0548624,-1.89949e-05,2.97345e-09,-1.73516e-13,-66846.7,-217.849], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 178,
    label = "CCCCCCCCCCC(C=O)OO",
    molecule = 
"""
1  C u0 p0 c0 {8,S} {9,S} {32,S} {33,S}
2  C u0 p0 c0 {3,S} {10,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {6,S} {24,S} {25,S}
6  C u0 p0 c0 {5,S} {7,S} {26,S} {27,S}
7  C u0 p0 c0 {6,S} {8,S} {28,S} {29,S}
8  C u0 p0 c0 {1,S} {7,S} {30,S} {31,S}
9  C u0 p0 c0 {1,S} {12,S} {13,S} {15,S}
10 C u0 p0 c0 {2,S} {11,S} {16,S} {17,S}
11 C u0 p0 c0 {10,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {9,S} {37,D} {38,S}
13 O u0 p2 c0 {9,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {1,S}
33 H u0 p0 c0 {1,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 O u0 p2 c0 {12,D}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.325555,0.161211,-0.000116345,4.37404e-08,-6.77236e-12,-62137.7,45.7846], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[45.5899,0.0531251,-1.82692e-05,2.84677e-09,-1.6559e-13,-78033.7,-200.572], Tmin=(1394,'K'), Tmax=(5000,'K')),
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
    index = 179,
    label = "CCCCCCCCCC(CC=O)OO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {10,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {8,S} {30,S} {31,S}
3  C u0 p0 c0 {4,S} {9,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {6,S} {8,S} {26,S} {27,S}
8  C u0 p0 c0 {2,S} {7,S} {28,S} {29,S}
9  C u0 p0 c0 {3,S} {11,S} {16,S} {17,S}
10 C u0 p0 c0 {1,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,D} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {2,S}
31 H u0 p0 c0 {2,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 O u0 p2 c0 {12,D}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.0932,0.150718,-0.000103321,3.70083e-08,-5.50514e-12,-63612.1,35.1537], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[44.4327,0.0540311,-1.85637e-05,2.89079e-09,-1.68071e-13,-78633.5,-193.183], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 180,
    label = "CCCCCCCCC(CCC=O)OO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {7,S} {28,S} {29,S}
3  C u0 p0 c0 {4,S} {9,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {2,S} {6,S} {26,S} {27,S}
8  C u0 p0 c0 {1,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {3,S} {11,S} {16,S} {17,S}
10 C u0 p0 c0 {8,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,D} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {2,S}
29 H u0 p0 c0 {2,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 O u0 p2 c0 {12,D}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.0932,0.150718,-0.000103321,3.70083e-08,-5.50514e-12,-63612.1,35.1537], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[44.4327,0.0540311,-1.85637e-05,2.89079e-09,-1.68071e-13,-78633.5,-193.183], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 181,
    label = "CCCCCCCC(CCCC=O)OO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {7,S} {26,S} {27,S}
3  C u0 p0 c0 {1,S} {8,S} {28,S} {29,S}
4  C u0 p0 c0 {5,S} {9,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {20,S} {21,S}
6  C u0 p0 c0 {5,S} {7,S} {22,S} {23,S}
7  C u0 p0 c0 {2,S} {6,S} {24,S} {25,S}
8  C u0 p0 c0 {3,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {4,S} {11,S} {16,S} {17,S}
10 C u0 p0 c0 {8,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,D} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {2,S}
27 H u0 p0 c0 {2,S}
28 H u0 p0 c0 {3,S}
29 H u0 p0 c0 {3,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 O u0 p2 c0 {12,D}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.0932,0.150718,-0.000103321,3.70083e-08,-5.50514e-12,-63612.1,35.1537], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[44.4327,0.0540311,-1.85637e-05,2.89079e-09,-1.68071e-13,-78633.5,-193.183], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 182,
    label = "CCCCCCCCCCC(=O)COO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {17,S} {18,S}
2  C u0 p0 c0 {1,S} {3,S} {19,S} {20,S}
3  C u0 p0 c0 {2,S} {4,S} {21,S} {22,S}
4  C u0 p0 c0 {3,S} {5,S} {23,S} {24,S}
5  C u0 p0 c0 {4,S} {6,S} {25,S} {26,S}
6  C u0 p0 c0 {5,S} {7,S} {27,S} {28,S}
7  C u0 p0 c0 {6,S} {9,S} {29,S} {30,S}
8  C u0 p0 c0 {1,S} {11,S} {15,S} {16,S}
9  C u0 p0 c0 {7,S} {12,S} {31,S} {32,S}
10 C u0 p0 c0 {12,S} {13,S} {36,S} {37,S}
11 C u0 p0 c0 {8,S} {33,S} {34,S} {35,S}
12 C u0 p0 c0 {9,S} {10,S} {38,D}
13 O u0 p2 c0 {10,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {6,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {7,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {10,S}
37 H u0 p0 c0 {10,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.549007,0.162096,-0.000118994,4.61133e-08,-7.41762e-12,-63706.9,48.1302], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[44.9392,0.0537234,-1.84844e-05,2.88119e-09,-1.67624e-13,-79396.6,-195.595], Tmin=(1393,'K'), Tmax=(5000,'K')),
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
    index = 183,
    label = "CCCCCCCCCC(OO)C(=O)C",
    molecule = 
"""
1  C u0 p0 c0 {8,S} {12,S} {13,S} {31,S}
2  C u0 p0 c0 {3,S} {9,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {8,S} {27,S} {28,S}
8  C u0 p0 c0 {1,S} {7,S} {29,S} {30,S}
9  C u0 p0 c0 {2,S} {10,S} {15,S} {16,S}
10 C u0 p0 c0 {9,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {12,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {1,S} {11,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {1,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.594225,0.162754,-0.000119881,4.6616e-08,-7.52441e-12,-66045.9,46.5307], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[45.1725,0.0536022,-1.84597e-05,2.87913e-09,-1.67577e-13,-81825.5,-198.655], Tmin=(1392,'K'), Tmax=(5000,'K')),
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
    index = 184,
    label = "CCCCCCCCC(OO)CC(=O)C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {7,S} {28,S} {29,S}
3  C u0 p0 c0 {4,S} {8,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {2,S} {6,S} {26,S} {27,S}
8  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
9  C u0 p0 c0 {1,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {8,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {12,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {9,S} {11,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {2,S}
29 H u0 p0 c0 {2,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87259,0.152046,-0.000106553,3.96809e-08,-6.20833e-12,-67527.4,35.6781], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[44.0352,0.0544376,-1.87186e-05,2.91644e-09,-1.69623e-13,-82425,-191.356], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 185,
    label = "CCCCCCCC(OO)CCC(=O)C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {6,S} {26,S} {27,S}
3  C u0 p0 c0 {4,S} {8,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {2,S} {5,S} {24,S} {25,S}
7  C u0 p0 c0 {1,S} {9,S} {28,S} {29,S}
8  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
9  C u0 p0 c0 {7,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {8,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {12,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {9,S} {11,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {2,S}
27 H u0 p0 c0 {2,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87259,0.152046,-0.000106553,3.96809e-08,-6.20833e-12,-67527.4,35.6781], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[44.0352,0.0544376,-1.87186e-05,2.91644e-09,-1.69623e-13,-82425,-191.356], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 186,
    label = "CCCCCCC(OO)CCCC(=O)C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {6,S} {24,S} {25,S}
3  C u0 p0 c0 {1,S} {7,S} {26,S} {27,S}
4  C u0 p0 c0 {5,S} {8,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {20,S} {21,S}
6  C u0 p0 c0 {2,S} {5,S} {22,S} {23,S}
7  C u0 p0 c0 {3,S} {9,S} {28,S} {29,S}
8  C u0 p0 c0 {4,S} {10,S} {16,S} {17,S}
9  C u0 p0 c0 {7,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {8,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {12,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {9,S} {11,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {2,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {3,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87259,0.152046,-0.000106553,3.96809e-08,-6.20833e-12,-67527.4,35.6781], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[44.0352,0.0544376,-1.87186e-05,2.91644e-09,-1.69623e-13,-82425,-191.356], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 187,
    label = "CCCCCCCCCC(=O)CCOO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {17,S} {18,S}
2  C u0 p0 c0 {1,S} {3,S} {19,S} {20,S}
3  C u0 p0 c0 {2,S} {4,S} {21,S} {22,S}
4  C u0 p0 c0 {3,S} {5,S} {23,S} {24,S}
5  C u0 p0 c0 {4,S} {6,S} {25,S} {26,S}
6  C u0 p0 c0 {5,S} {8,S} {27,S} {28,S}
7  C u0 p0 c0 {1,S} {11,S} {15,S} {16,S}
8  C u0 p0 c0 {6,S} {12,S} {29,S} {30,S}
9  C u0 p0 c0 {10,S} {12,S} {31,S} {32,S}
10 C u0 p0 c0 {9,S} {13,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {10,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {6,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.7522,0.146907,-9.86405e-05,3.48918e-08,-5.18985e-12,-65880.8,33.3015], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[43.6808,0.0548418,-1.8881e-05,2.94421e-09,-1.71338e-13,-80626.1,-188.066], Tmin=(1388,'K'), Tmax=(5000,'K')),
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
    index = 188,
    label = "CCCCCCCCCC(=O)C(OO)C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {17,S} {18,S}
2  C u0 p0 c0 {1,S} {3,S} {19,S} {20,S}
3  C u0 p0 c0 {2,S} {4,S} {21,S} {22,S}
4  C u0 p0 c0 {3,S} {5,S} {23,S} {24,S}
5  C u0 p0 c0 {4,S} {6,S} {25,S} {26,S}
6  C u0 p0 c0 {5,S} {9,S} {27,S} {28,S}
7  C u0 p0 c0 {11,S} {12,S} {13,S} {29,S}
8  C u0 p0 c0 {1,S} {10,S} {15,S} {16,S}
9  C u0 p0 c0 {6,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {8,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {7,S} {9,S} {38,D}
13 O u0 p2 c0 {7,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {6,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.594225,0.162754,-0.000119881,4.6616e-08,-7.52441e-12,-66045.9,46.5307], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[45.1725,0.0536022,-1.84597e-05,2.87913e-09,-1.67577e-13,-81825.5,-198.655], Tmin=(1392,'K'), Tmax=(5000,'K')),
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
    index = 189,
    label = "CCCCCCCCC(OO)C(=O)CC",
    molecule = 
"""
1  C u0 p0 c0 {7,S} {12,S} {13,S} {29,S}
2  C u0 p0 c0 {3,S} {8,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {1,S} {6,S} {27,S} {28,S}
8  C u0 p0 c0 {2,S} {10,S} {15,S} {16,S}
9  C u0 p0 c0 {11,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {8,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {9,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {1,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {1,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.594225,0.162754,-0.000119881,4.6616e-08,-7.52441e-12,-66045.9,46.5307], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[45.1725,0.0536022,-1.84597e-05,2.87913e-09,-1.67577e-13,-81825.5,-198.655], Tmin=(1392,'K'), Tmax=(5000,'K')),
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
    index = 190,
    label = "CCCCCCCC(OO)CC(=O)CC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {6,S} {26,S} {27,S}
3  C u0 p0 c0 {4,S} {7,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {2,S} {5,S} {24,S} {25,S}
7  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
8  C u0 p0 c0 {1,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {11,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {9,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {2,S}
27 H u0 p0 c0 {2,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87259,0.152046,-0.000106553,3.96809e-08,-6.20833e-12,-67527.4,35.6781], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[44.0352,0.0544376,-1.87186e-05,2.91644e-09,-1.69623e-13,-82425,-191.356], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 191,
    label = "CCCCCCC(OO)CCC(=O)CC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {5,S} {24,S} {25,S}
3  C u0 p0 c0 {4,S} {7,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {2,S} {4,S} {22,S} {23,S}
6  C u0 p0 c0 {1,S} {8,S} {26,S} {27,S}
7  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
8  C u0 p0 c0 {6,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {11,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {9,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {2,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87259,0.152046,-0.000106553,3.96809e-08,-6.20833e-12,-67527.4,35.6781], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[44.0352,0.0544376,-1.87186e-05,2.91644e-09,-1.69623e-13,-82425,-191.356], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 192,
    label = "CCCCCC(OO)CCCC(=O)CC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {5,S} {22,S} {23,S}
3  C u0 p0 c0 {1,S} {6,S} {24,S} {25,S}
4  C u0 p0 c0 {5,S} {7,S} {18,S} {19,S}
5  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
6  C u0 p0 c0 {3,S} {8,S} {26,S} {27,S}
7  C u0 p0 c0 {4,S} {10,S} {16,S} {17,S}
8  C u0 p0 c0 {6,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {11,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {9,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87259,0.152046,-0.000106553,3.96809e-08,-6.20833e-12,-67527.4,35.6781], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[44.0352,0.0544376,-1.87186e-05,2.91644e-09,-1.69623e-13,-82425,-191.356], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 193,
    label = "CCCCCCCCC(=O)CCCOO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {17,S} {18,S}
2  C u0 p0 c0 {1,S} {3,S} {19,S} {20,S}
3  C u0 p0 c0 {2,S} {4,S} {21,S} {22,S}
4  C u0 p0 c0 {3,S} {5,S} {23,S} {24,S}
5  C u0 p0 c0 {4,S} {8,S} {25,S} {26,S}
6  C u0 p0 c0 {1,S} {11,S} {15,S} {16,S}
7  C u0 p0 c0 {9,S} {10,S} {27,S} {28,S}
8  C u0 p0 c0 {5,S} {12,S} {29,S} {30,S}
9  C u0 p0 c0 {7,S} {12,S} {31,S} {32,S}
10 C u0 p0 c0 {7,S} {13,S} {33,S} {34,S}
11 C u0 p0 c0 {6,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {10,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.7522,0.146907,-9.86405e-05,3.48918e-08,-5.18985e-12,-65880.8,33.3015], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[43.6808,0.0548418,-1.8881e-05,2.94421e-09,-1.71338e-13,-80626.1,-188.066], Tmin=(1388,'K'), Tmax=(5000,'K')),
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
    index = 194,
    label = "CCCCCCCCC(=O)CC(OO)C",
    molecule = 
"""
1  C u0 p0 c0 {8,S} {10,S} {13,S} {15,S}
2  C u0 p0 c0 {3,S} {7,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {6,S} {24,S} {25,S}
6  C u0 p0 c0 {5,S} {9,S} {26,S} {27,S}
7  C u0 p0 c0 {2,S} {11,S} {16,S} {17,S}
8  C u0 p0 c0 {1,S} {12,S} {30,S} {31,S}
9  C u0 p0 c0 {6,S} {12,S} {28,S} {29,S}
10 C u0 p0 c0 {1,S} {35,S} {36,S} {37,S}
11 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {10,S}
36 H u0 p0 c0 {10,S}
37 H u0 p0 c0 {10,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87259,0.152046,-0.000106553,3.96809e-08,-6.20833e-12,-67527.4,35.6781], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[44.0352,0.0544376,-1.87186e-05,2.91644e-09,-1.69623e-13,-82425,-191.356], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 195,
    label = "CCCCCCCCC(=O)C(OO)CC",
    molecule = 
"""
1  C u0 p0 c0 {8,S} {12,S} {13,S} {27,S}
2  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {9,S} {25,S} {26,S}
7  C u0 p0 c0 {2,S} {10,S} {15,S} {16,S}
8  C u0 p0 c0 {1,S} {11,S} {28,S} {29,S}
9  C u0 p0 c0 {6,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {8,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {1,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {1,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.594225,0.162754,-0.000119881,4.6616e-08,-7.52441e-12,-66045.9,46.5307], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[45.1725,0.0536022,-1.84597e-05,2.87913e-09,-1.67577e-13,-81825.5,-198.655], Tmin=(1392,'K'), Tmax=(5000,'K')),
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
    index = 196,
    label = "CCCCCCCC(OO)C(=O)CCC",
    molecule = 
"""
1  C u0 p0 c0 {6,S} {12,S} {13,S} {27,S}
2  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {1,S} {5,S} {25,S} {26,S}
7  C u0 p0 c0 {2,S} {10,S} {15,S} {16,S}
8  C u0 p0 c0 {9,S} {11,S} {28,S} {29,S}
9  C u0 p0 c0 {8,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {8,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {1,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {1,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.594225,0.162754,-0.000119881,4.6616e-08,-7.52441e-12,-66045.9,46.5307], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[45.1725,0.0536022,-1.84597e-05,2.87913e-09,-1.67577e-13,-81825.5,-198.655], Tmin=(1392,'K'), Tmax=(5000,'K')),
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
    index = 197,
    label = "CCCCCCC(OO)CC(=O)CCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {5,S} {24,S} {25,S}
3  C u0 p0 c0 {4,S} {6,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {2,S} {4,S} {22,S} {23,S}
6  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {9,S} {11,S} {26,S} {27,S}
8  C u0 p0 c0 {1,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {7,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {2,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87259,0.152046,-0.000106553,3.96809e-08,-6.20833e-12,-67527.4,35.6781], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[44.0352,0.0544376,-1.87186e-05,2.91644e-09,-1.69623e-13,-82425,-191.356], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 198,
    label = "CCCCCC(OO)CCC(=O)CCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {4,S} {22,S} {23,S}
3  C u0 p0 c0 {4,S} {6,S} {18,S} {19,S}
4  C u0 p0 c0 {2,S} {3,S} {20,S} {21,S}
5  C u0 p0 c0 {1,S} {8,S} {24,S} {25,S}
6  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {9,S} {11,S} {26,S} {27,S}
8  C u0 p0 c0 {5,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {7,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87259,0.152046,-0.000106553,3.96809e-08,-6.20833e-12,-67527.4,35.6781], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[44.0352,0.0544376,-1.87186e-05,2.91644e-09,-1.69623e-13,-82425,-191.356], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 199,
    label = "CCCCC(OO)CCCC(=O)CCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {4,S} {20,S} {21,S}
3  C u0 p0 c0 {1,S} {5,S} {22,S} {23,S}
4  C u0 p0 c0 {2,S} {6,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {8,S} {24,S} {25,S}
6  C u0 p0 c0 {4,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {9,S} {11,S} {26,S} {27,S}
8  C u0 p0 c0 {5,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {7,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87259,0.152046,-0.000106553,3.96809e-08,-6.20833e-12,-67527.4,35.6781], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[44.0352,0.0544376,-1.87186e-05,2.91644e-09,-1.69623e-13,-82425,-191.356], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 200,
    label = "CCCCCCCC(=O)CCCCOO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {17,S} {18,S}
2  C u0 p0 c0 {1,S} {3,S} {19,S} {20,S}
3  C u0 p0 c0 {2,S} {4,S} {21,S} {22,S}
4  C u0 p0 c0 {3,S} {8,S} {23,S} {24,S}
5  C u0 p0 c0 {6,S} {9,S} {25,S} {26,S}
6  C u0 p0 c0 {5,S} {10,S} {27,S} {28,S}
7  C u0 p0 c0 {1,S} {11,S} {15,S} {16,S}
8  C u0 p0 c0 {4,S} {12,S} {29,S} {30,S}
9  C u0 p0 c0 {5,S} {12,S} {31,S} {32,S}
10 C u0 p0 c0 {6,S} {13,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {10,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {6,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.7522,0.146907,-9.86405e-05,3.48918e-08,-5.18985e-12,-65880.8,33.3015], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[43.6808,0.0548418,-1.8881e-05,2.94421e-09,-1.71338e-13,-80626.1,-188.066], Tmin=(1388,'K'), Tmax=(5000,'K')),
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
    index = 201,
    label = "CCCCCCCC(=O)CCC(OO)C",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {10,S} {13,S} {15,S}
2  C u0 p0 c0 {3,S} {7,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {6,S} {22,S} {23,S}
5  C u0 p0 c0 {1,S} {9,S} {26,S} {27,S}
6  C u0 p0 c0 {4,S} {8,S} {24,S} {25,S}
7  C u0 p0 c0 {2,S} {11,S} {16,S} {17,S}
8  C u0 p0 c0 {6,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {5,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {1,S} {35,S} {36,S} {37,S}
11 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {5,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {10,S}
36 H u0 p0 c0 {10,S}
37 H u0 p0 c0 {10,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87259,0.152046,-0.000106553,3.96809e-08,-6.20833e-12,-67527.4,35.6781], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[44.0352,0.0544376,-1.87186e-05,2.91644e-09,-1.69623e-13,-82425,-191.356], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 202,
    label = "CCCCCCCC(=O)CC(OO)CC",
    molecule = 
"""
1  C u0 p0 c0 {6,S} {8,S} {13,S} {15,S}
2  C u0 p0 c0 {3,S} {7,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {9,S} {24,S} {25,S}
6  C u0 p0 c0 {1,S} {11,S} {26,S} {27,S}
7  C u0 p0 c0 {2,S} {10,S} {16,S} {17,S}
8  C u0 p0 c0 {1,S} {12,S} {30,S} {31,S}
9  C u0 p0 c0 {5,S} {12,S} {28,S} {29,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {6,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87259,0.152046,-0.000106553,3.96809e-08,-6.20833e-12,-67527.4,35.6781], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[44.0352,0.0544376,-1.87186e-05,2.91644e-09,-1.69623e-13,-82425,-191.356], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 203,
    label = "CCCCCCCC(=O)C(OO)CCC",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {12,S} {13,S} {25,S}
2  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {6,S} {21,S} {22,S}
5  C u0 p0 c0 {1,S} {8,S} {26,S} {27,S}
6  C u0 p0 c0 {4,S} {9,S} {23,S} {24,S}
7  C u0 p0 c0 {2,S} {10,S} {15,S} {16,S}
8  C u0 p0 c0 {5,S} {11,S} {28,S} {29,S}
9  C u0 p0 c0 {6,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {8,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {1,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {1,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {5,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.594225,0.162754,-0.000119881,4.6616e-08,-7.52441e-12,-66045.9,46.5307], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[45.1725,0.0536022,-1.84597e-05,2.87913e-09,-1.67577e-13,-81825.5,-198.655], Tmin=(1392,'K'), Tmax=(5000,'K')),
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
    index = 204,
    label = "CCCCCCC(OO)C(=O)CCCC",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {12,S} {13,S} {25,S}
2  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {1,S} {4,S} {23,S} {24,S}
6  C u0 p0 c0 {8,S} {9,S} {26,S} {27,S}
7  C u0 p0 c0 {2,S} {10,S} {15,S} {16,S}
8  C u0 p0 c0 {6,S} {11,S} {28,S} {29,S}
9  C u0 p0 c0 {6,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {8,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {1,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {1,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.594225,0.162754,-0.000119881,4.6616e-08,-7.52441e-12,-66045.9,46.5307], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[45.1725,0.0536022,-1.84597e-05,2.87913e-09,-1.67577e-13,-81825.5,-198.655], Tmin=(1392,'K'), Tmax=(5000,'K')),
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
    index = 205,
    label = "CCCCCC(OO)CC(=O)CCCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {4,S} {22,S} {23,S}
3  C u0 p0 c0 {4,S} {6,S} {18,S} {19,S}
4  C u0 p0 c0 {2,S} {3,S} {20,S} {21,S}
5  C u0 p0 c0 {7,S} {9,S} {24,S} {25,S}
6  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {5,S} {11,S} {26,S} {27,S}
8  C u0 p0 c0 {1,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {5,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87259,0.152046,-0.000106553,3.96809e-08,-6.20833e-12,-67527.4,35.6781], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[44.0352,0.0544376,-1.87186e-05,2.91644e-09,-1.69623e-13,-82425,-191.356], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 206,
    label = "CCCCC(OO)CCC(=O)CCCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {20,S} {21,S}
3  C u0 p0 c0 {2,S} {6,S} {18,S} {19,S}
4  C u0 p0 c0 {1,S} {8,S} {22,S} {23,S}
5  C u0 p0 c0 {7,S} {9,S} {24,S} {25,S}
6  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {5,S} {11,S} {26,S} {27,S}
8  C u0 p0 c0 {4,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {5,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87259,0.152046,-0.000106553,3.96809e-08,-6.20833e-12,-67527.4,35.6781], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[44.0352,0.0544376,-1.87186e-05,2.91644e-09,-1.69623e-13,-82425,-191.356], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 207,
    label = "CCCC(OO)CCCC(=O)CCCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {6,S} {18,S} {19,S}
3  C u0 p0 c0 {1,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {8,S} {22,S} {23,S}
5  C u0 p0 c0 {7,S} {9,S} {24,S} {25,S}
6  C u0 p0 c0 {2,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {5,S} {11,S} {26,S} {27,S}
8  C u0 p0 c0 {4,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {5,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87259,0.152046,-0.000106553,3.96809e-08,-6.20833e-12,-67527.4,35.6781], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[44.0352,0.0544376,-1.87186e-05,2.91644e-09,-1.69623e-13,-82425,-191.356], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 208,
    label = "CCCCCCC(=O)CCCC(OO)C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {10,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {6,S} {26,S} {27,S}
3  C u0 p0 c0 {4,S} {7,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {8,S} {22,S} {23,S}
6  C u0 p0 c0 {2,S} {9,S} {24,S} {25,S}
7  C u0 p0 c0 {3,S} {11,S} {16,S} {17,S}
8  C u0 p0 c0 {5,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {6,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {1,S} {35,S} {36,S} {37,S}
11 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {2,S}
27 H u0 p0 c0 {2,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {10,S}
36 H u0 p0 c0 {10,S}
37 H u0 p0 c0 {10,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87259,0.152046,-0.000106553,3.96809e-08,-6.20833e-12,-67527.4,35.6781], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[44.0352,0.0544376,-1.87186e-05,2.91644e-09,-1.69623e-13,-82425,-191.356], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 209,
    label = "CCCCCCC(=O)CCC(OO)CC",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {6,S} {13,S} {15,S}
2  C u0 p0 c0 {3,S} {7,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {5,S} {20,S} {21,S}
4  C u0 p0 c0 {1,S} {9,S} {24,S} {25,S}
5  C u0 p0 c0 {3,S} {8,S} {22,S} {23,S}
6  C u0 p0 c0 {1,S} {11,S} {26,S} {27,S}
7  C u0 p0 c0 {2,S} {10,S} {16,S} {17,S}
8  C u0 p0 c0 {5,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {4,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {6,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87259,0.152046,-0.000106553,3.96809e-08,-6.20833e-12,-67527.4,35.6781], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[44.0352,0.0544376,-1.87186e-05,2.91644e-09,-1.69623e-13,-82425,-191.356], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 210,
    label = "CCCCCCC(=O)CC(OO)CCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {7,S} {24,S} {25,S}
3  C u0 p0 c0 {4,S} {6,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {9,S} {22,S} {23,S}
6  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {2,S} {11,S} {26,S} {27,S}
8  C u0 p0 c0 {1,S} {12,S} {30,S} {31,S}
9  C u0 p0 c0 {5,S} {12,S} {28,S} {29,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {2,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87259,0.152046,-0.000106553,3.96809e-08,-6.20833e-12,-67527.4,35.6781], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[44.0352,0.0544376,-1.87186e-05,2.91644e-09,-1.69623e-13,-82425,-191.356], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 211,
    label = "CCCCCCC(=O)C(OO)CCCC",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {12,S} {13,S} {23,S}
2  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {6,S} {19,S} {20,S}
4  C u0 p0 c0 {1,S} {5,S} {24,S} {25,S}
5  C u0 p0 c0 {4,S} {8,S} {26,S} {27,S}
6  C u0 p0 c0 {3,S} {9,S} {21,S} {22,S}
7  C u0 p0 c0 {2,S} {10,S} {15,S} {16,S}
8  C u0 p0 c0 {5,S} {11,S} {28,S} {29,S}
9  C u0 p0 c0 {6,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {8,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {1,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {1,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {5,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.594225,0.162754,-0.000119881,4.6616e-08,-7.52441e-12,-66045.9,46.5307], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[45.1725,0.0536022,-1.84597e-05,2.87913e-09,-1.67577e-13,-81825.5,-198.655], Tmin=(1392,'K'), Tmax=(5000,'K')),
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
    index = 212,
    label = "CCCCCC(OO)C(=O)CCCCC",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {12,S} {13,S} {23,S}
2  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {1,S} {3,S} {21,S} {22,S}
5  C u0 p0 c0 {6,S} {8,S} {26,S} {27,S}
6  C u0 p0 c0 {5,S} {9,S} {24,S} {25,S}
7  C u0 p0 c0 {2,S} {10,S} {15,S} {16,S}
8  C u0 p0 c0 {5,S} {11,S} {28,S} {29,S}
9  C u0 p0 c0 {6,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {8,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {1,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {1,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {5,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.594225,0.162754,-0.000119881,4.6616e-08,-7.52441e-12,-66045.9,46.5307], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[45.1725,0.0536022,-1.84597e-05,2.87913e-09,-1.67577e-13,-81825.5,-198.655], Tmin=(1392,'K'), Tmax=(5000,'K')),
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
    index = 213,
    label = "CCCCC(OO)CC(=O)CCCCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {20,S} {21,S}
3  C u0 p0 c0 {2,S} {6,S} {18,S} {19,S}
4  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
5  C u0 p0 c0 {4,S} {9,S} {22,S} {23,S}
6  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {4,S} {11,S} {26,S} {27,S}
8  C u0 p0 c0 {1,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {5,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87259,0.152046,-0.000106553,3.96809e-08,-6.20833e-12,-67527.4,35.6781], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[44.0352,0.0544376,-1.87186e-05,2.91644e-09,-1.69623e-13,-82425,-191.356], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 214,
    label = "CCCC(OO)CCC(=O)CCCCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {6,S} {18,S} {19,S}
3  C u0 p0 c0 {1,S} {8,S} {20,S} {21,S}
4  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
5  C u0 p0 c0 {4,S} {9,S} {22,S} {23,S}
6  C u0 p0 c0 {2,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {4,S} {11,S} {26,S} {27,S}
8  C u0 p0 c0 {3,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {5,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87259,0.152046,-0.000106553,3.96809e-08,-6.20833e-12,-67527.4,35.6781], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[44.0352,0.0544376,-1.87186e-05,2.91644e-09,-1.69623e-13,-82425,-191.356], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 215,
    label = "CCC(OO)CCCC(=O)CCCCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {4,S} {18,S} {19,S}
3  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
4  C u0 p0 c0 {2,S} {8,S} {20,S} {21,S}
5  C u0 p0 c0 {3,S} {9,S} {22,S} {23,S}
6  C u0 p0 c0 {1,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {3,S} {11,S} {26,S} {27,S}
8  C u0 p0 c0 {4,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {5,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87259,0.152046,-0.000106553,3.96809e-08,-6.20833e-12,-67527.4,35.6781], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[44.0352,0.0544376,-1.87186e-05,2.91644e-09,-1.69623e-13,-82425,-191.356], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

