#!/usr/bin/env python
# encoding: utf-8

name = "DEE_2.5"
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
            NASAPolynomial(coeffs=[3.61263,-0.00100894,2.499e-06,-1.43377e-09,2.58639e-13,-1051.1,2.6527], Tmin=(100,'K'), Tmax=(1817.02,'K')),
            NASAPolynomial(coeffs=[2.97585,0.00164148,-7.19756e-07,1.25385e-10,-7.91579e-15,-1025.81,5.53788], Tmin=(1817.02,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1,
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
    index = 2,
    label = "C4H10O",
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
            NASAPolynomial(coeffs=[3.25364,0.0388916,5.90223e-06,-3.2547e-08,1.52858e-11,-33086.4,12.3386], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.5529,0.0305738,-1.2506e-05,2.32738e-09,-1.61861e-13,-35719.8,-28.3242], Tmin=(1000,'K'), Tmax=(5000,'K')),
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
    label = "O2",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53764,-0.0012283,5.36766e-06,-4.93138e-09,1.45959e-12,-1037.99,4.67179], Tmin=(100,'K'), Tmax=(1087.7,'K')),
            NASAPolynomial(coeffs=[3.16426,0.00169456,-8.00346e-07,1.59032e-10,-1.14893e-14,-1048.44,6.08309], Tmin=(1087.7,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 4,
    label = "OH",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4858,0.00133394,-4.70032e-06,5.64365e-09,-2.06312e-12,3411.96,1.99787], Tmin=(100,'K'), Tmax=(1005.25,'K')),
            NASAPolynomial(coeffs=[2.88224,0.00103871,-2.35662e-07,1.40254e-11,6.34379e-16,3669.56,5.59059], Tmin=(1005.25,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 5,
    label = "O",
    molecule = 
"""
multiplicity 3
1 O u2 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,1.21572e-13,-1.5062e-16,6.05143e-20,-7.46776e-24,29226.7,5.11107], Tmin=(100,'K'), Tmax=(4894.38,'K')),
            NASAPolynomial(coeffs=[2.38095,9.68242e-05,-2.95308e-08,4.00288e-12,-2.03466e-16,29343.8,5.87502], Tmin=(4894.38,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 6,
    label = "H",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,1.21572e-13,-1.5062e-16,6.05143e-20,-7.46776e-24,25472.7,-0.459566], Tmin=(100,'K'), Tmax=(4894.38,'K')),
            NASAPolynomial(coeffs=[2.38095,9.68242e-05,-2.95308e-08,4.00288e-12,-2.03466e-16,25589.8,0.30439], Tmin=(4894.38,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 7,
    label = "H2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.42254,0.000286655,-4.14682e-07,4.27557e-10,-9.38141e-14,-1029.78,-3.86365], Tmin=(100,'K'), Tmax=(1962.83,'K')),
            NASAPolynomial(coeffs=[2.74225,0.000579461,1.9724e-07,-6.41169e-11,4.96057e-15,-552.074,0.413737], Tmin=(1962.83,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 8,
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
            NASAPolynomial(coeffs=[4.02958,-0.00264004,1.52237e-05,-1.71681e-08,6.26784e-12,322.677,4.84423], Tmin=(100,'K'), Tmax=(923.9,'K')),
            NASAPolynomial(coeffs=[4.15129,0.00191154,-4.11321e-07,6.35068e-11,-4.86478e-15,83.4392,3.09366], Tmin=(923.9,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 9,
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
            NASAPolynomial(coeffs=[3.72867,0.00413381,5.67483e-06,-1.01864e-08,4.28603e-12,-17696.4,5.35913], Tmin=(100,'K'), Tmax=(923.27,'K')),
            NASAPolynomial(coeffs=[4.95153,0.00354228,-1.0104e-06,1.6194e-10,-1.10208e-14,-18122.8,-1.52917], Tmin=(923.27,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 10,
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
            NASAPolynomial(coeffs=[3.65718,0.0021266,5.45839e-06,-6.6181e-09,2.46571e-12,16422.7,1.67354], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.97812,0.00579785,-1.97558e-06,3.07298e-10,-1.79174e-14,16509.5,4.72248], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
            NASAPolynomial(coeffs=[3.71181,-0.00280463,3.76551e-05,-4.73072e-08,1.86588e-11,1295.7,6.57241], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.75779,0.00744142,-2.69705e-06,4.38091e-10,-2.63537e-14,378.112,-1.9668], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
            NASAPolynomial(coeffs=[1.97339,0.0153542,-6.37315e-06,3.19931e-10,2.82194e-13,254.279,16.9194], Tmin=(200,'K'), Tmax=(1374,'K')),
            NASAPolynomial(coeffs=[6.4797,0.00744401,-2.52349e-06,3.89577e-10,-2.25182e-14,-1562.85,-8.19477], Tmin=(1374,'K'), Tmax=(5000,'K')),
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
            NASAPolynomial(coeffs=[3.90352,0.0222599,-1.0161e-05,1.7171e-09,1.88167e-14,-5096.54,8.98723], Tmin=(200,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[9.50283,0.012043,-4.09492e-06,6.33049e-10,-3.66134e-14,-7370.69,-22.1717], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
            NASAPolynomial(coeffs=[1.3273,0.0176657,-6.14927e-06,-3.01143e-10,4.38618e-13,13428.4,17.1789], Tmin=(200,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[5.88784,0.0103077,-3.46844e-06,5.32499e-10,-3.06513e-14,11506.5,-8.49652], Tmin=(1387,'K'), Tmax=(5000,'K')),
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
    index = 15,
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
            NASAPolynomial(coeffs=[3.36378,0.000265766,2.79621e-05,-3.72987e-08,1.5159e-11,34475,7.9151], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.15027,0.00754021,-2.62998e-06,4.15974e-10,-2.45408e-14,33856.6,1.72812], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
            NASAPolynomial(coeffs=[3.60373,0.027008,-2.08293e-05,8.50541e-09,-1.43846e-12,-23420.5,11.2015], Tmin=(200,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[11.2522,0.00833653,-2.89015e-06,4.52782e-10,-2.64354e-14,-26023.9,-29.637], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    label = "CH3CHO",
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
    index = 18,
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
            NASAPolynomial(coeffs=[3.96059,0.0106002,-5.25713e-06,1.01717e-09,-2.87488e-14,-17359.9,11.7807], Tmin=(200,'K'), Tmax=(1368,'K')),
            NASAPolynomial(coeffs=[7.24075,0.00463313,-1.63694e-06,2.59707e-10,-1.52965e-14,-18702.8,-6.49547], Tmin=(1368,'K'), Tmax=(5000,'K')),
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
            NASAPolynomial(coeffs=[4.30743,0.00641472,3.11397e-05,-4.33141e-08,1.72762e-11,-3402.75,5.90258], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.689,0.0131257,-4.70388e-06,7.58586e-10,-4.54133e-14,-4745.78,-9.69838], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    label = "C4H9Ob",
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
            NASAPolynomial(coeffs=[6.6946,0.00803915,8.52015e-05,-1.1891e-07,4.85794e-11,-10092.2,0.817395], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.3012,0.0289177,-1.1596e-05,2.12855e-09,-1.46595e-13,-12386.6,-24.7407], Tmin=(1000,'K'), Tmax=(5000,'K')),
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
    label = "C4H9Oa",
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
            NASAPolynomial(coeffs=[5.91586,0.0132878,6.48506e-05,-9.28704e-08,3.76846e-11,-7060.15,4.46941], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.43643,0.0291355,-1.17074e-05,2.1523e-09,-1.48402e-13,-9174.32,-19.6345], Tmin=(1000,'K'), Tmax=(5000,'K')),
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
    label = "C4H9ObOO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.76386,0.030558,3.99702e-05,-7.44018e-08,3.21226e-11,-31274.3,4.58707], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.2189,0.0312309,-1.25998e-05,2.32341e-09,-1.60566e-13,-34267.2,-38.8027], Tmin=(1000,'K'), Tmax=(5000,'K')),
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
    label = "C4H9OaOO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {3,S} {16,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.83039,0.0140264,7.29693e-05,-1.01492e-07,4.01882e-11,-24751.1,-6.80851], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.9873,0.0324217,-1.31532e-05,2.4348e-09,-1.68723e-13,-27308.6,-35.4109], Tmin=(1000,'K'), Tmax=(5000,'K')),
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
    label = "C4H8ObOOHa",
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
            NASAPolynomial(coeffs=[0.74325,0.0767615,-7.62954e-05,4.28763e-08,-1.02491e-11,-22514.6,28.6091], Tmin=(100,'K'), Tmax=(982.78,'K')),
            NASAPolynomial(coeffs=[10.0666,0.0388147,-1.83781e-05,3.58841e-09,-2.55029e-13,-24347.1,-16.2089], Tmin=(982.78,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 25,
    label = "C4H8ObOOHc",
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
            NASAPolynomial(coeffs=[6.02295,0.0428071,1.5018e-05,-5.64236e-08,2.78373e-11,-25537.9,3.45061], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.3483,0.0281952,-1.11786e-05,2.03656e-09,-1.3954e-13,-28844.7,-52.6563], Tmin=(1000,'K'), Tmax=(5000,'K')),
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
    label = "C4H8ObOOHd",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.64291,0.0793547,-8.31716e-05,4.9666e-08,-1.2563e-11,-22796.8,27.6102], Tmin=(100,'K'), Tmax=(935.24,'K')),
            NASAPolynomial(coeffs=[10.0576,0.0390893,-1.85926e-05,3.63312e-09,-2.58188e-13,-24557.8,-17.1799], Tmin=(935.24,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C4H8OaOOHb",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {2,S} {5,S} {15,S}
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
            NASAPolynomial(coeffs=[0.21277,0.0887916,-0.000111013,7.92761e-08,-2.33158e-11,-21666.6,27.5047], Tmin=(100,'K'), Tmax=(822.91,'K')),
            NASAPolynomial(coeffs=[10.7992,0.0373323,-1.72118e-05,3.28373e-09,-2.29062e-13,-23409,-21.5054], Tmin=(822.91,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C4H8OaOOHc",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {3,S} {5,S} {15,S}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.04809,0.04262,1.04522e-05,-4.61843e-08,2.24966e-11,-19913.5,7.99617], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.385,0.0300271,-1.20373e-05,2.20997e-09,-1.52257e-13,-23026.3,-43.1328], Tmin=(1000,'K'), Tmax=(5000,'K')),
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
    label = "C4H8OaOOHd",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
4  C u1 p0 c0 {3,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.284598,0.0879946,-0.000115872,9.14925e-08,-3.01633e-11,-17925.7,28.4275], Tmin=(100,'K'), Tmax=(743.46,'K')),
            NASAPolynomial(coeffs=[8.95625,0.0407135,-1.92159e-05,3.68866e-09,-2.57414e-13,-19197.8,-10.7213], Tmin=(743.46,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C4H8OcyOab",
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
            NASAPolynomial(coeffs=[1.58594,0.0468381,-1.20062e-05,-2.01104e-08,1.30851e-11,-34069.3,19.8548], Tmin=(100,'K'), Tmax=(874.33,'K')),
            NASAPolynomial(coeffs=[10.4724,0.0251384,-7.29775e-06,1.09526e-09,-6.8258e-14,-36347.7,-25.9672], Tmin=(874.33,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C4H8OcyOac",
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
            NASAPolynomial(coeffs=[2.10515,0.0265836,4.85567e-05,-9.74379e-08,4.64288e-11,-44636.9,15.4379], Tmin=(100,'K'), Tmax=(849.29,'K')),
            NASAPolynomial(coeffs=[15.4781,0.00772913,3.91654e-06,-1.21612e-09,9.53704e-14,-48500,-56.264], Tmin=(849.29,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C4H8OcyOad",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {5,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {2,S} {3,S}
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
            NASAPolynomial(coeffs=[2.26767,0.0282568,4.78932e-05,-9.34956e-08,4.56146e-11,-40698.1,12.2425], Tmin=(100,'K'), Tmax=(796.38,'K')),
            NASAPolynomial(coeffs=[10.2632,0.0211489,-9.7262e-07,-4.74812e-10,5.36628e-14,-43019.7,-31.0912], Tmin=(796.38,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C4H8OaOOHbOO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {2,S} {8,S}
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
            NASAPolynomial(coeffs=[-0.656503,0.111239,-0.000160177,1.34446e-07,-4.61814e-11,-40542.9,35.8467], Tmin=(100,'K'), Tmax=(774.34,'K')),
            NASAPolynomial(coeffs=[10.197,0.0478949,-2.33703e-05,4.52367e-09,-3.1598e-13,-42005.5,-12.3302], Tmin=(774.34,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C4H8OaOOHcOO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {7,S} {9,S}
2  C u0 p0 c0 {3,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {3,S} {8,S}
7  O u0 p2 c0 {1,S} {17,S}
8  O u0 p2 c0 {6,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u1 p2 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.64148,0.0376816,5.64308e-05,-1.08943e-07,4.85443e-11,-38897.5,6.91938], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[19.0448,0.0322665,-1.32606e-05,2.47669e-09,-1.72714e-13,-43474.5,-63.4598], Tmin=(1000,'K'), Tmax=(5000,'K')),
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
    label = "C4H8OaOOHdOO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {4,S} {5,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {7,S} {15,S} {16,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {3,S} {8,S}
7  O u0 p2 c0 {4,S} {17,S}
8  O u0 p2 c0 {6,S} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u1 p2 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.812111,0.117331,-0.000183058,1.61789e-07,-5.65654e-11,-35680.5,35.9462], Tmin=(100,'K'), Tmax=(828.8,'K')),
            NASAPolynomial(coeffs=[9.06353,0.04956,-2.40106e-05,4.58195e-09,-3.15348e-13,-36626.9,-5.6772], Tmin=(828.8,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C4H8ObOOHaOO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {9,S}
2  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {3,S} {17,S}
8  O u0 p2 c0 {6,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u1 p2 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.656503,0.111239,-0.000160177,1.34446e-07,-4.61814e-11,-40542.9,35.8467], Tmin=(100,'K'), Tmax=(774.34,'K')),
            NASAPolynomial(coeffs=[10.197,0.0478949,-2.33703e-05,4.52367e-09,-3.1598e-13,-42005.5,-12.3302], Tmin=(774.34,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C4H8ObOOHcOO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {9,S}
2  C u0 p0 c0 {4,S} {5,S} {7,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {2,S} {17,S}
8  O u0 p2 c0 {6,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
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
            NASAPolynomial(coeffs=[5.01456,0.0515034,2.22133e-05,-7.43584e-08,3.60402e-11,-47022.4,11.0917], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[19.3674,0.0318377,-1.3058e-05,2.4356e-09,-1.69694e-13,-51741.8,-67.2984], Tmin=(1000,'K'), Tmax=(5000,'K')),
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
    label = "C4H8ObOOHdOO",
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
            NASAPolynomial(coeffs=[-0.656503,0.111239,-0.000160177,1.34446e-07,-4.61814e-11,-40542.9,35.8467], Tmin=(100,'K'), Tmax=(774.34,'K')),
            NASAPolynomial(coeffs=[10.197,0.0478949,-2.33703e-05,4.52367e-09,-3.1598e-13,-42005.5,-12.3302], Tmin=(774.34,'K'), Tmax=(5000,'K')),
        ],
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
    label = "bC4H7OcdOOH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
4  C u1 p0 c0 {3,S} {5,S} {16,S}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {2,S} {9,S}
8  O u0 p2 c0 {6,S} {17,S}
9  O u0 p2 c0 {7,S} {18,S}
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
            NASAPolynomial(coeffs=[-1.05984,0.119677,-0.000165653,1.24824e-07,-3.80638e-11,-37105.7,35.9975], Tmin=(100,'K'), Tmax=(798.98,'K')),
            NASAPolynomial(coeffs=[14.337,0.042598,-2.09519e-05,4.09195e-09,-2.88432e-13,-39566.1,-34.8288], Tmin=(798.98,'K'), Tmax=(5000,'K')),
        ],
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
    label = "bC4H7OacOOH",
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
            NASAPolynomial(coeffs=[-1.05984,0.119677,-0.000165653,1.24824e-07,-3.80638e-11,-37105.7,35.9975], Tmin=(100,'K'), Tmax=(798.98,'K')),
            NASAPolynomial(coeffs=[14.337,0.042598,-2.09519e-05,4.09195e-09,-2.88432e-13,-39566.1,-34.8288], Tmin=(798.98,'K'), Tmax=(5000,'K')),
        ],
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
    label = "bC4H7OadOOH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {7,S} {14,S} {15,S}
4  C u1 p0 c0 {3,S} {5,S} {16,S}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {2,S} {8,S}
7  O u0 p2 c0 {3,S} {9,S}
8  O u0 p2 c0 {6,S} {17,S}
9  O u0 p2 c0 {7,S} {18,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.3651,0.127758,-0.000196686,1.64784e-07,-5.49282e-11,-32236.9,36.6202], Tmin=(100,'K'), Tmax=(810.15,'K')),
            NASAPolynomial(coeffs=[13.4646,0.0437857,-2.13023e-05,4.07923e-09,-2.81748e-13,-34286.9,-29.6246], Tmin=(810.15,'K'), Tmax=(5000,'K')),
        ],
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
    label = "bCOC3H7OcOOH",
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
            NASAPolynomial(coeffs=[0.99585,0.0662477,-4.58354e-05,1.55425e-08,-2.16919e-12,-71119.7,28.535], Tmin=(100,'K'), Tmax=(1600.73,'K')),
            NASAPolynomial(coeffs=[13.8941,0.034017,-1.5633e-05,2.96395e-09,-2.04703e-13,-75249,-39.7596], Tmin=(1600.73,'K'), Tmax=(5000,'K')),
        ],
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
    label = "aCHOC3H6OcOOH",
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
            NASAPolynomial(coeffs=[0.709111,0.0768995,-7.04245e-05,3.46011e-08,-7.17062e-12,-56255.4,28.9375], Tmin=(100,'K'), Tmax=(1120.79,'K')),
            NASAPolynomial(coeffs=[11.6181,0.0379666,-1.83196e-05,3.60846e-09,-2.57587e-13,-58700.8,-24.9363], Tmin=(1120.79,'K'), Tmax=(5000,'K')),
        ],
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
    label = "aCHOC3H6OdOOH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {14,D} {15,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.511442,0.0832492,-9.32598e-05,6.09609e-08,-1.6944e-11,-51390.7,29.2051], Tmin=(100,'K'), Tmax=(855.47,'K')),
            NASAPolynomial(coeffs=[9.43302,0.0415304,-2.01034e-05,3.9456e-09,-2.80645e-13,-52917.1,-12.443], Tmin=(855.47,'K'), Tmax=(5000,'K')),
        ],
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
    label = "bCOC3H7OdOOH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {5,S} {15,D}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {4,D}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.1568,0.0684053,-5.44191e-05,2.42488e-08,-4.80997e-12,-66270,27.5176], Tmin=(100,'K'), Tmax=(1119.71,'K')),
            NASAPolynomial(coeffs=[8.27565,0.042974,-2.03501e-05,3.96422e-09,-2.80938e-13,-67864.2,-7.63159], Tmin=(1119.71,'K'), Tmax=(5000,'K')),
        ],
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
    label = "aCHOC3H6OcO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {13,D} {14,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u1 p2 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.57807,0.0590211,-5.70597e-05,3.76909e-08,-1.18641e-11,-37742.1,25.9308], Tmin=(100,'K'), Tmax=(726.55,'K')),
            NASAPolynomial(coeffs=[4.80357,0.0412641,-2.0401e-05,4.0553e-09,-2.9089e-13,-38210.8,11.3998], Tmin=(726.55,'K'), Tmax=(5000,'K')),
        ],
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
    label = "aCHOC3H6OdO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {13,D} {14,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.23119,0.0677102,-9.08479e-05,8.22732e-08,-3.12507e-11,-32871.6,26.6958], Tmin=(100,'K'), Tmax=(776.91,'K')),
            NASAPolynomial(coeffs=[4.0885,0.0421538,-2.05663e-05,3.99638e-09,-2.80218e-13,-32988.3,15.7386], Tmin=(776.91,'K'), Tmax=(5000,'K')),
        ],
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
    label = "bCOC3H7OcO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {5,S} {14,D}
5  O u0 p2 c0 {1,S} {4,S}
6  O u1 p2 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.11294,0.0453201,-2.13549e-05,3.56523e-09,-9.96709e-14,-52616.5,24.6494], Tmin=(100,'K'), Tmax=(2060.92,'K')),
            NASAPolynomial(coeffs=[18.647,0.0213634,-9.83866e-06,1.75498e-09,-1.12383e-13,-61158.9,-71.2654], Tmin=(2060.92,'K'), Tmax=(5000,'K')),
        ],
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
    label = "bCOC3H7OdO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {5,S} {14,D}
5  O u0 p2 c0 {1,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.70238,0.0435241,-2.00949e-05,3.48986e-09,-1.7695e-13,-47789.6,22.0043], Tmin=(100,'K'), Tmax=(2492.7,'K')),
            NASAPolynomial(coeffs=[27.567,0.0117916,-5.91442e-06,1.01176e-09,-6.02424e-14,-62723,-125.753], Tmin=(2492.7,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C4H8ObOOHcyOac",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {6,S} {9,S}
2  C u0 p0 c0 {3,S} {5,S} {7,S} {10,S}
3  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {3,S}
7  O u0 p2 c0 {2,S} {8,S}
8  O u0 p2 c0 {7,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.74231,0.0760332,-7.14096e-05,3.42435e-08,-6.05447e-12,-60006.8,28.8927], Tmin=(100,'K'), Tmax=(1692.29,'K')),
            NASAPolynomial(coeffs=[16.8778,0.0153093,-6.77179e-07,-2.82007e-10,2.99572e-14,-63238.9,-57.313], Tmin=(1692.29,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C4H8OcOOHcyOab",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {4,S} {5,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {3,S}
7  O u0 p2 c0 {2,S} {8,S}
8  O u0 p2 c0 {7,S} {16,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.0573219,0.080874,-7.82512e-05,4.1255e-08,-8.71982e-12,-49497.4,29.2569], Tmin=(100,'K'), Tmax=(1149.68,'K')),
            NASAPolynomial(coeffs=[15.1065,0.0285144,-9.93688e-06,1.6414e-09,-1.05762e-13,-52957.7,-45.4458], Tmin=(1149.68,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C4H8OdOOHcyOab",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
3  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {7,S} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {1,S} {2,S}
7  O u0 p2 c0 {4,S} {8,S}
8  O u0 p2 c0 {7,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.112405,0.0844208,-9.20351e-05,5.67227e-08,-1.41146e-11,-44644,28.6053], Tmin=(100,'K'), Tmax=(979.03,'K')),
            NASAPolynomial(coeffs=[12.964,0.0319124,-1.1584e-05,1.9389e-09,-1.25058e-13,-47160.4,-33.1236], Tmin=(979.03,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C4H9OaO",
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
            NASAPolynomial(coeffs=[1.40432,0.0640878,-8.12509e-05,7.52228e-08,-2.92515e-11,-24869.2,23.8654], Tmin=(100,'K'), Tmax=(796.77,'K')),
            NASAPolynomial(coeffs=[2.33309,0.0459408,-2.17018e-05,4.15723e-09,-2.89052e-13,-24589.2,22.2816], Tmin=(796.77,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C4H9ObO",
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
            NASAPolynomial(coeffs=[2.58322,0.0471075,-2.38345e-05,5.1328e-09,-4.18851e-13,-29782.1,19.9883], Tmin=(100,'K'), Tmax=(2745.42,'K')),
            NASAPolynomial(coeffs=[19.9808,0.0217603,-9.98597e-06,1.77008e-09,-1.12646e-13,-39335.1,-81.516], Tmin=(2745.42,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 55,
    label = "C4H8OcyObc",
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
            NASAPolynomial(coeffs=[1.99162,0.0286689,4.15863e-05,-6.92548e-08,2.64936e-11,-39011.2,17.9803], Tmin=(100,'K'), Tmax=(1016,'K')),
            NASAPolynomial(coeffs=[12.256,0.0263176,-1.11333e-05,2.20923e-09,-1.63758e-13,-43061.3,-41.3694], Tmin=(1016,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 56,
    label = "CH3COOH",
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
    index = 57,
    label = "C2H5OH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {9,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {1,S}
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
    index = 58,
    label = "C2H4",
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
            NASAPolynomial(coeffs=[3.9592,-0.00757051,5.7099e-05,-6.91588e-08,2.69884e-11,5089.78,4.0973], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.99183,0.0104834,-3.71721e-06,5.94628e-10,-3.5363e-14,4268.66,-0.269082], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 59,
    label = "R52C3H7OE",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C u1 p0 c0 {1,S} {10,S} {11,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.31053,0.0331583,-1.80389e-05,4.71443e-09,-4.91778e-13,-5677.73,15.9897], Tmin=(100,'K'), Tmax=(2164.2,'K')),
            NASAPolynomial(coeffs=[11.7279,0.0157526,-5.97504e-06,9.98217e-10,-6.24933e-14,-9753.91,-36.7141], Tmin=(2164.2,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 60,
    label = "CH2O",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.79372,-0.00990833,3.7322e-05,-3.79285e-08,1.31773e-11,-14379.2,0.602798], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.16953,0.00619321,-2.25056e-06,3.65976e-10,-2.20149e-14,-14548.7,6.04208], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 61,
    label = "H2O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99882,-0.000554834,2.76775e-06,-1.55666e-09,3.02332e-13,-30274.6,-0.0308952], Tmin=(100,'K'), Tmax=(1281.43,'K')),
            NASAPolynomial(coeffs=[3.19561,0.0019524,-1.67116e-07,-2.97943e-11,4.45143e-15,-30068.7,4.04333], Tmin=(1281.43,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 62,
    label = "CH4",
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
            NASAPolynomial(coeffs=[5.14911,-0.0136622,4.91454e-05,-4.84247e-08,1.66603e-11,-10246.6,-4.63849], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.65326,0.0100263,-3.31661e-06,5.36483e-10,-3.14697e-14,-10009.6,9.90506], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 63,
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
            NASAPolynomial(coeffs=[5.65851,-0.0162983,6.91938e-05,-7.58373e-08,2.80428e-11,-25612,-0.897331], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.52727,0.0103179,-3.62893e-06,5.77448e-10,-3.42183e-14,-26002.9,5.16759], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 64,
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
            NASAPolynomial(coeffs=[4.47834,-0.0013507,2.78485e-05,-3.64869e-08,1.47907e-11,-3500.73,3.30913], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.09314,0.00594761,-2.06497e-06,3.23008e-10,-1.88126e-14,-4034.1,-1.84691], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 65,
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
            NASAPolynomial(coeffs=[4.23755,-0.00332075,1.4003e-05,-1.3424e-08,4.37416e-12,3872.41,3.30835], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.92002,0.00252279,-6.71004e-07,1.05616e-10,-7.43798e-15,3653.43,3.58077], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 66,
    label = "PC2H4OH",
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
            NASAPolynomial(coeffs=[4.47893,0.00759782,2.81795e-05,-4.26953e-08,1.78879e-11,-4714.46,6.38921], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.02825,0.0120038,-4.21306e-06,6.69471e-10,-3.96372e-14,-5924.93,-9.40356], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    label = "SC2H4OH",
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
            NASAPolynomial(coeffs=[4.22283,0.00512175,3.48387e-05,-4.91944e-08,2.01184e-11,-8205.04,8.01676], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.35842,0.0124356,-4.33097e-06,6.8453e-10,-4.03713e-14,-9379,-6.05106], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 68,
    label = "CH3CO",
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
    index = 69,
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
            NASAPolynomial(coeffs=[2.79503,0.0101099,1.61751e-05,-3.10303e-08,1.39436e-11,162.945,12.3647], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.53928,0.00780239,-2.76414e-06,4.42099e-10,-2.62954e-14,-1188.59,-8.72091], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 70,
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
            NASAPolynomial(coeffs=[4.29143,-0.00550155,5.99438e-05,-7.08466e-08,2.68686e-11,-11522.2,2.66679], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.04666,0.0153539,-5.47039e-06,8.77827e-10,-5.23168e-14,-12447.3,-0.968698], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 71,
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
            NASAPolynomial(coeffs=[0.621688,0.0804141,-8.66776e-05,5.83327e-08,-1.71405e-11,-43385.7,26.5975], Tmin=(100,'K'), Tmax=(804.48,'K')),
            NASAPolynomial(coeffs=[7.67952,0.0453213,-2.12444e-05,4.10839e-09,-2.89681e-13,-44521.3,-5.91694], Tmin=(804.48,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 72,
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
            NASAPolynomial(coeffs=[0.882922,0.0732984,-6.1069e-05,2.81897e-08,-5.64289e-12,-48253.1,26.1029], Tmin=(100,'K'), Tmax=(1135.12,'K')),
            NASAPolynomial(coeffs=[9.80771,0.0418492,-1.95111e-05,3.7827e-09,-2.67542e-13,-50279.3,-18.0853], Tmin=(1135.12,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 73,
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
            NASAPolynomial(coeffs=[1.37441,0.0249116,-1.74309e-05,6.248e-09,-9.09517e-13,-27233,18.1405], Tmin=(200,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[8.5406,0.00832951,-2.84722e-06,4.41927e-10,-2.56373e-14,-29729.1,-20.3884], Tmin=(1395,'K'), Tmax=(5000,'K')),
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
    index = 74,
    label = "CH3O2H",
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
            NASAPolynomial(coeffs=[2.90541,0.0174995,5.28244e-06,-2.52827e-08,1.34368e-11,-16889.5,11.3742], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.76538,0.008615,-2.98007e-06,4.68638e-10,-2.75339e-14,-18298,-14.3993], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 75,
    label = "C2H5O2H",
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
            NASAPolynomial(coeffs=[1.83755,0.0338054,-2.37548e-05,9.31975e-09,-1.58003e-12,-21581.4,18.0978], Tmin=(200,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[10.4824,0.013478,-4.62179e-06,7.18619e-10,-4.17307e-14,-24657.8,-28.4294], Tmin=(1390,'K'), Tmax=(5000,'K')),
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
    index = 76,
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
            NASAPolynomial(coeffs=[-1.29466,0.0444936,-4.26577e-05,2.07392e-08,-3.96829e-12,-11827.6,36.0779], Tmin=(200,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[11.1808,0.00914479,-3.1509e-06,4.91944e-10,-2.86639e-14,-15579,-28.7893], Tmin=(1393,'K'), Tmax=(5000,'K')),
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
    index = 77,
    label = "HO2CH2CHO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {7,D} {8,S}
3 O u0 p2 c0 {1,S} {4,S}
4 O u0 p2 c0 {3,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.32769,0.0521619,-4.97328e-05,2.31272e-08,-4.20788e-12,-29060.9,36.186], Tmin=(200,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[15.1555,0.0075724,-2.72693e-06,4.38217e-10,-2.60434e-14,-34142,-50.1255], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 78,
    label = "CH3CO3H",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {8,D}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {3,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 O u0 p2 c0 {2,D}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.24136,0.0337964,-2.53887e-05,9.67584e-09,-1.49266e-12,-42467.8,17.0668], Tmin=(200,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[12.506,0.0094779,-3.30402e-06,5.19631e-10,-3.04234e-14,-45985.7,-37.9196], Tmin=(1391,'K'), Tmax=(5000,'K')),
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
    index = 79,
    label = "EVE",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,D} {5,S} {11,S}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
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

entry(
    index = 80,
    label = "C2H5OC2H4OH-B",
    molecule = 
"""
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
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.30068,0.0635307,-5.60532e-05,3.10801e-08,-7.7681e-12,-52008.3,23.393], Tmin=(100,'K'), Tmax=(919.05,'K')),
            NASAPolynomial(coeffs=[6.67438,0.0401437,-1.78845e-05,3.3944e-09,-2.37367e-13,-52996.1,-2.07858], Tmin=(919.05,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C2H5OCH2CHO",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {13,D} {14,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.57623,0.0507918,-3.23445e-05,1.02055e-08,-1.31997e-12,-40799.2,21.8972], Tmin=(100,'K'), Tmax=(1727.66,'K')),
            NASAPolynomial(coeffs=[12.1268,0.0263645,-1.1136e-05,2.0216e-09,-1.35732e-13,-44444.7,-34.7719], Tmin=(1727.66,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C2H5OC2H4OH-A",
    molecule = 
"""
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
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.31365,0.0594192,-4.11686e-05,1.5004e-08,-2.31946e-12,-56865.5,23.7816], Tmin=(100,'K'), Tmax=(1440.14,'K')),
            NASAPolynomial(coeffs=[10.4875,0.0339387,-1.46289e-05,2.71833e-09,-1.86738e-13,-59507.8,-23.8231], Tmin=(1440.14,'K'), Tmax=(5000,'K')),
        ],
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
    label = "EA",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {5,S} {14,D}
5  O u0 p2 c0 {1,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87017,0.039781,-5.70252e-06,-1.19381e-08,4.97591e-12,-55662.3,21.4943], Tmin=(100,'K'), Tmax=(1194.01,'K')),
            NASAPolynomial(coeffs=[8.70975,0.0313593,-1.33274e-05,2.48366e-09,-1.719e-13,-58328.6,-17.0413], Tmin=(1194.01,'K'), Tmax=(5000,'K')),
        ],
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
            NASAPolynomial(coeffs=[4.68826,-0.00414872,2.55066e-05,-2.84474e-08,1.04423e-11,-16986.7,4.28426], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.14394,0.00559739,-1.99794e-06,3.16179e-10,-1.85614e-14,-17246,5.07779], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 85,
    label = "C2H4O2H",
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
            NASAPolynomial(coeffs=[2.75788,0.0288272,-2.08302e-05,8.47401e-09,-1.48618e-12,3001.54,15.9922], Tmin=(200,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[10.0591,0.0113379,-3.89403e-06,6.06091e-10,-3.52212e-14,424.049,-23.2087], Tmin=(1389,'K'), Tmax=(5000,'K')),
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
    index = 86,
    label = "CH2O2H",
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
            NASAPolynomial(coeffs=[2.88976,0.0209466,-1.75191e-05,7.2782e-09,-1.18912e-12,6123.91,12.3802], Tmin=(200,'K'), Tmax=(1410,'K')),
            NASAPolynomial(coeffs=[9.24698,0.00460846,-1.53501e-06,2.34435e-10,-1.34573e-14,4115.3,-21.1503], Tmin=(1410,'K'), Tmax=(5000,'K')),
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
    index = 87,
    label = "C2H3OOH",
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
            NASAPolynomial(coeffs=[1.35644,0.0337002,-2.75989e-05,1.14223e-08,-1.89489e-12,-5499.97,19.8354], Tmin=(200,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[11.575,0.00809909,-2.81809e-06,4.42698e-10,-2.58998e-14,-8848.53,-34.3859], Tmin=(1397,'K'), Tmax=(5000,'K')),
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
    index = 88,
    label = "C2OC2KETB-A",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,D} {15,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.814704,0.076673,-7.47816e-05,4.18849e-08,-1.01903e-11,-57995.3,29.2735], Tmin=(100,'K'), Tmax=(954.67,'K')),
            NASAPolynomial(coeffs=[9.03633,0.0422252,-2.06568e-05,4.08866e-09,-2.92679e-13,-59565.1,-10.0098], Tmin=(954.67,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C2OC2KETA-B",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,S} {15,D}
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
15 O u0 p2 c0 {4,D}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.915075,0.0702848,-5.45195e-05,2.20686e-08,-3.77705e-12,-64506,27.6353], Tmin=(100,'K'), Tmax=(1320.99,'K')),
            NASAPolynomial(coeffs=[11.6996,0.0376292,-1.7439e-05,3.35525e-09,-2.35544e-13,-67355.2,-27.3963], Tmin=(1320.99,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C2H5OCHO",
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
            NASAPolynomial(coeffs=[2.4914,0.0261855,8.77766e-06,-2.29349e-08,8.50601e-12,-48965,16.9475], Tmin=(100,'K'), Tmax=(1107.17,'K')),
            NASAPolynomial(coeffs=[7.64059,0.0239688,-1.04197e-05,1.99228e-09,-1.41065e-13,-51109.5,-12.9542], Tmin=(1107.17,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C2H5OCO",
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
            NASAPolynomial(coeffs=[2.23009,0.033073,-1.39885e-05,-4.15594e-09,3.53821e-12,-25180.8,17.5155], Tmin=(100,'K'), Tmax=(1061.29,'K')),
            NASAPolynomial(coeffs=[9.58315,0.0166206,-6.65161e-06,1.23343e-09,-8.65183e-14,-27375.7,-21.384], Tmin=(1061.29,'K'), Tmax=(5000,'K')),
        ],
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
    label = "AA",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {12,D}
4  C u0 p0 c0 {2,S} {5,S} {13,D}
5  O u0 p2 c0 {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {3,D}
13 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.05612,0.0446241,-2.78409e-05,8.67158e-09,-1.13487e-12,-71665.9,24.0242], Tmin=(100,'K'), Tmax=(1638.67,'K')),
            NASAPolynomial(coeffs=[9.14186,0.0273279,-1.20085e-05,2.23046e-09,-1.52198e-13,-73988.2,-13.66], Tmin=(1638.67,'K'), Tmax=(5000,'K')),
        ],
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
    label = "CC(O)OCCO",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {11,D}
4  C u0 p0 c0 {1,S} {12,D} {13,S}
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
            NASAPolynomial(coeffs=[1.67612,0.0436135,-1.58213e-05,-4.62397e-09,3.10693e-12,-63663.7,24.4018], Tmin=(100,'K'), Tmax=(1218.62,'K')),
            NASAPolynomial(coeffs=[10.8396,0.0269609,-1.1849e-05,2.24344e-09,-1.56578e-13,-66893.9,-25.7085], Tmin=(1218.62,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C4O-AO2H-1O2H-B",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {4,S} {5,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {2,S} {15,S} {16,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {9,S}
7  O u0 p2 c0 {2,S} {8,S}
8  O u0 p2 c0 {7,S} {17,S}
9  O u0 p2 c0 {6,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.495903,0.107131,-0.000128558,8.45206e-08,-2.29621e-11,-37954.9,36.9899], Tmin=(100,'K'), Tmax=(883.8,'K')),
            NASAPolynomial(coeffs=[13.322,0.0445971,-2.24321e-05,4.47362e-09,-3.20967e-13,-40397.5,-27.9677], Tmin=(883.8,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 95,
    label = "C4O-BO2H-AO2H1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {12,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {10,S}
7  O u0 p2 c0 {3,S} {9,S}
8  O u0 p2 c0 {2,S} {18,S}
9  O u0 p2 c0 {7,S} {19,S}
10 O u0 p2 c0 {6,S} {20,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u1 p2 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.95854,0.14253,-0.000216552,1.828e-07,-6.24324e-11,-55980.7,44.4417], Tmin=(100,'K'), Tmax=(762.58,'K')),
            NASAPolynomial(coeffs=[13.7886,0.0530601,-2.70485e-05,5.31656e-09,-3.74034e-13,-58182.6,-25.951], Tmin=(762.58,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C4O-BO2H-1O2HAO2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {11,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {12,S}
3  C u0 p0 c0 {2,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {9,S}
7  O u0 p2 c0 {3,S} {10,S}
8  O u0 p2 c0 {2,S} {18,S}
9  O u0 p2 c0 {6,S} {19,S}
10 O u0 p2 c0 {7,S} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u1 p2 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.95854,0.14253,-0.000216552,1.828e-07,-6.24324e-11,-55980.7,44.4417], Tmin=(100,'K'), Tmax=(762.58,'K')),
            NASAPolynomial(coeffs=[13.7886,0.0530601,-2.70485e-05,5.31656e-09,-3.74034e-13,-58182.6,-25.951], Tmin=(762.58,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C4O-BO2H-2O2HAO2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {8,S} {11,S}
2  C u0 p0 c0 {4,S} {5,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {7,S} {16,S} {17,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {3,S} {9,S}
7  O u0 p2 c0 {4,S} {10,S}
8  O u0 p2 c0 {1,S} {18,S}
9  O u0 p2 c0 {6,S} {19,S}
10 O u0 p2 c0 {7,S} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u1 p2 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.13024,0.148829,-0.000240239,2.11289e-07,-7.3339e-11,-51117.6,44.5977], Tmin=(100,'K'), Tmax=(815.9,'K')),
            NASAPolynomial(coeffs=[12.713,0.0546202,-2.76254e-05,5.35937e-09,-3.72086e-13,-52826.1,-19.6194], Tmin=(815.9,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C4O-AO2H-1O2HBO2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {7,S} {12,S}
2  C u0 p0 c0 {4,S} {5,S} {6,S} {11,S}
3  C u0 p0 c0 {1,S} {8,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {2,S} {9,S}
7  O u0 p2 c0 {1,S} {10,S}
8  O u0 p2 c0 {3,S} {18,S}
9  O u0 p2 c0 {6,S} {19,S}
10 O u0 p2 c0 {7,S} {20,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u1 p2 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.95854,0.14253,-0.000216552,1.828e-07,-6.24324e-11,-55980.7,44.4417], Tmin=(100,'K'), Tmax=(762.58,'K')),
            NASAPolynomial(coeffs=[13.7886,0.0530601,-2.70485e-05,5.31656e-09,-3.74034e-13,-58182.6,-25.951], Tmin=(762.58,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C2OC2KETA-B-1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {5,S} {16,D}
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
16 O u0 p2 c0 {4,D}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.172103,0.0987251,-9.95813e-05,5.40109e-08,-1.22812e-11,-79952.3,35.4828], Tmin=(100,'K'), Tmax=(1034.2,'K')),
            NASAPolynomial(coeffs=[13.5015,0.0458389,-2.28748e-05,4.56379e-09,-3.28108e-13,-82780.5,-30.944], Tmin=(1034.2,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C2OC2KET1-A-B",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {5,S} {16,D}
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
16 O u0 p2 c0 {4,D}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.104651,0.098897,-0.000106528,6.5031e-08,-1.693e-11,-81709.1,35.9887], Tmin=(100,'K'), Tmax=(905.95,'K')),
            NASAPolynomial(coeffs=[11.0608,0.0496006,-2.49103e-05,4.97248e-09,-3.57304e-13,-83732.2,-16.7758], Tmin=(905.95,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C2OC2KET2-A-B",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {15,D} {16,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {1,S} {9,S}
7  O u0 p2 c0 {2,S} {8,S}
8  O u0 p2 c0 {7,S} {17,S}
9  O u0 p2 c0 {6,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {4,D}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.764991,0.114156,-0.00014786,1.06287e-07,-3.15184e-11,-66829.6,37.713], Tmin=(100,'K'), Tmax=(814.06,'K')),
            NASAPolynomial(coeffs=[12.9263,0.0468816,-2.38972e-05,4.7673e-09,-3.41184e-13,-69058.7,-25.5227], Tmin=(814.06,'K'), Tmax=(5000,'K')),
        ],
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
    label = "OCH2CHO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {7,S}
3 O u1 p2 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.12785,0.00667998,1.00125e-05,-1.06888e-08,2.76653e-12,-12821.7,-0.809763], Tmin=(200,'K'), Tmax=(1468,'K')),
            NASAPolynomial(coeffs=[9.83473,0.00777896,-2.78175e-06,4.44912e-10,-2.6353e-14,-15074,-24.1645], Tmin=(1468,'K'), Tmax=(5000,'K')),
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
    index = 103,
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
            NASAPolynomial(coeffs=[3.83464,0.00329079,5.05228e-05,-6.66251e-08,2.63707e-11,788.717,7.53408], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.0387,0.0162964,-5.82131e-06,9.35937e-10,-5.58603e-14,-741.715,-8.43826], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 104,
    label = "C2H3OH",
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
            NASAPolynomial(coeffs=[-0.127972,0.0338506,-3.30645e-05,1.64859e-08,-3.19935e-12,-15991.5,23.0439], Tmin=(200,'K'), Tmax=(1410,'K')),
            NASAPolynomial(coeffs=[8.32598,0.00803387,-2.63928e-06,3.98411e-10,-2.26551e-14,-18322.1,-20.208], Tmin=(1410,'K'), Tmax=(5000,'K')),
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
    index = 105,
    label = "CH2CH2OH-2O2",
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
            NASAPolynomial(coeffs=[7.0401,0.0159564,2.21097e-06,-7.05197e-09,2.08266e-12,-22452.4,-1.75362], Tmin=(200,'K'), Tmax=(1506,'K')),
            NASAPolynomial(coeffs=[12.7504,0.0111514,-3.83474e-06,5.98156e-10,-3.48372e-14,-25277.1,-35.4318], Tmin=(1506,'K'), Tmax=(5000,'K')),
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
    index = 106,
    label = "CH2CH2O-2OOH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  O u0 p2 c0 {1,S} {4,S}
4  O u0 p2 c0 {3,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  O u1 p2 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.03473,0.050251,-7.86992e-05,7.68024e-08,-2.9424e-11,-14271.1,19.1962], Tmin=(100,'K'), Tmax=(824.52,'K')),
            NASAPolynomial(coeffs=[2.92969,0.0306151,-1.51532e-05,2.92544e-09,-2.02872e-13,-13898.8,18.2038], Tmin=(824.52,'K'), Tmax=(5000,'K')),
        ],
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
    label = "CH2CHOH-2OOH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u1 p0 c0 {1,S} {4,S} {8,S}
3  O u0 p2 c0 {1,S} {5,S}
4  O u0 p2 c0 {2,S} {9,S}
5  O u0 p2 c0 {3,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.44246,0.0612316,-9.55821e-05,8.08552e-08,-2.68511e-11,-19709,20.0129], Tmin=(100,'K'), Tmax=(846.73,'K')),
            NASAPolynomial(coeffs=[8.19724,0.0210744,-9.8326e-06,1.83796e-09,-1.24708e-13,-20557.2,-9.70536], Tmin=(846.73,'K'), Tmax=(5000,'K')),
        ],
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
    label = "CY(CCO)OH",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 O u0 p2 c0 {1,S} {2,S}
4 O u0 p2 c0 {1,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.99496,0.0147545,2.68649e-05,-5.45533e-08,2.6667e-11,-32097.9,11.6357], Tmin=(100,'K'), Tmax=(823.13,'K')),
            NASAPolynomial(coeffs=[9.62022,0.0054469,2.11765e-06,-7.29544e-10,5.99152e-14,-33964,-23.7477], Tmin=(823.13,'K'), Tmax=(5000,'K')),
        ],
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
    label = "CH2CO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.81423,0.0199009,-2.21416e-05,1.45029e-08,-3.98877e-12,-7053.95,13.6079], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.35869,0.00695642,-2.64803e-06,4.65068e-10,-3.08642e-14,-7902.94,-3.98526], Tmin=(1000,'K'), Tmax=(5000,'K')),
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
    index = 110,
    label = "CH3CHOH-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  O u0 p2 c0 {1,S} {9,S}
4  O u0 p2 c0 {1,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u1 p2 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.18811,0.042071,-4.32161e-05,2.58453e-08,-6.53761e-12,-27995.2,19.0096], Tmin=(100,'K'), Tmax=(938.29,'K')),
            NASAPolynomial(coeffs=[7.15875,0.0208805,-9.33935e-06,1.77516e-09,-1.24219e-13,-28928,-4.65417], Tmin=(938.29,'K'), Tmax=(5000,'K')),
        ],
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
    label = "CH3COHOOH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {5,S}
4  O u0 p2 c0 {2,S} {9,S}
5  O u0 p2 c0 {3,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.01765,0.0457412,-4.66873e-05,2.58116e-08,-5.91171e-12,-21585.5,19.5498], Tmin=(100,'K'), Tmax=(1036.97,'K')),
            NASAPolynomial(coeffs=[8.70272,0.0199541,-9.38554e-06,1.83018e-09,-1.30072e-13,-22971.9,-12.9445], Tmin=(1036.97,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C2H4O-1OOH",
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
    index = 113,
    label = "CH2CHOH-1OOH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u1 p0 c0 {1,S} {7,S} {8,S}
3  O u0 p2 c0 {1,S} {5,S}
4  O u0 p2 c0 {1,S} {9,S}
5  O u0 p2 c0 {3,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.86375,0.0483508,-5.16563e-05,2.91724e-08,-6.69132e-12,-20531,21.4081], Tmin=(100,'K'), Tmax=(1047.31,'K')),
            NASAPolynomial(coeffs=[9.776,0.0181317,-8.37566e-06,1.62229e-09,-1.14969e-13,-22188.3,-17.1298], Tmin=(1047.31,'K'), Tmax=(5000,'K')),
        ],
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
    label = "Ar",
    molecule = 
"""
1 Ar u0 p4 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,1.21572e-13,-1.5062e-16,6.05143e-20,-7.46776e-24,-745,4.3663], Tmin=(100,'K'), Tmax=(4894.38,'K')),
            NASAPolynomial(coeffs=[2.38095,9.68242e-05,-2.95308e-08,4.00288e-12,-2.03466e-16,-627.909,5.13026], Tmin=(4894.38,'K'), Tmax=(5000,'K')),
        ],
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
    label = "He",
    molecule = 
"""
1 He u0 p1 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,1.21572e-13,-1.5062e-16,6.05143e-20,-7.46776e-24,-745,0.914222], Tmin=(100,'K'), Tmax=(4894.38,'K')),
            NASAPolynomial(coeffs=[2.38095,9.68242e-05,-2.95308e-08,4.00288e-12,-2.03466e-16,-627.909,1.67818], Tmin=(4894.38,'K'), Tmax=(5000,'K')),
        ],
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
            NASAPolynomial(coeffs=[3.71758,0.00127391,2.17347e-06,-3.48858e-09,1.65209e-12,45872.4,1.75298], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.14632,0.00303671,-9.96474e-07,1.50484e-10,-8.57336e-15,46041.3,4.72342], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 117,
    label = "CO",
    molecule = 
"""
1 O u0 p1 c+1 {2,T}
2 C u0 p1 c-1 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5971,-0.00102424,2.83336e-06,-1.75825e-09,3.42587e-13,-14343.2,3.45822], Tmin=(100,'K'), Tmax=(1669.93,'K')),
            NASAPolynomial(coeffs=[2.92795,0.00181931,-8.3531e-07,1.51269e-10,-9.88874e-15,-14292.7,6.51158], Tmin=(1669.93,'K'), Tmax=(5000,'K')),
        ],
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
            NASAPolynomial(coeffs=[0.80868,0.0233616,-3.55172e-05,2.80153e-08,-8.50075e-12,26429,13.9397], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.65878,0.00488397,-1.60829e-06,2.46975e-10,-1.38606e-14,25759.4,-3.99838], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 119,
    label = "CO2",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.2779,0.00275789,7.12764e-06,-1.07852e-08,4.14215e-12,-48475.6,5.97858], Tmin=(100,'K'), Tmax=(988.19,'K')),
            NASAPolynomial(coeffs=[4.55073,0.00290725,-1.14641e-06,2.25793e-10,-1.69522e-14,-48986,-1.45674], Tmin=(988.19,'K'), Tmax=(5000,'K')),
        ],
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
            NASAPolynomial(coeffs=[2.42465,0.0219706,-1.68706e-05,6.25612e-09,-9.11646e-13,-35482.8,17.5028], Tmin=(200,'K'), Tmax=(1378,'K')),
            NASAPolynomial(coeffs=[9.87504,0.00464664,-1.67231e-06,2.68624e-10,-1.59595e-14,-38050.2,-22.4939], Tmin=(1378,'K'), Tmax=(5000,'K')),
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
    index = 121,
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
            NASAPolynomial(coeffs=[4.11183,0.00753851,3.77337e-06,-5.38746e-09,1.45616e-12,-22802.3,7.46807], Tmin=(200,'K'), Tmax=(1452,'K')),
            NASAPolynomial(coeffs=[6.39522,0.00743673,-2.50422e-06,3.8488e-10,-2.21779e-14,-24110.9,-6.63866], Tmin=(1452,'K'), Tmax=(5000,'K')),
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
    index = 122,
    label = "HOCHO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89836,-0.00355878,3.55205e-05,-4.385e-08,1.71078e-11,-46770.6,7.34954], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.61383,0.00644964,-2.29083e-06,3.6716e-10,-2.18737e-14,-47514.8,0.847884], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 123,
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
            NASAPolynomial(coeffs=[0.446349,0.036305,-3.26131e-05,1.37051e-08,-2.20873e-12,-14197.3,27.296], Tmin=(200,'K'), Tmax=(1418,'K')),
            NASAPolynomial(coeffs=[12.9622,0.00421949,-1.54275e-06,2.50413e-10,-1.49856e-14,-18132.6,-38.7016], Tmin=(1418,'K'), Tmax=(5000,'K')),
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
    index = 124,
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
            NASAPolynomial(coeffs=[2.82069,0.0247857,-1.66186e-05,4.79633e-09,-4.28088e-13,-22207.7,17.06], Tmin=(200,'K'), Tmax=(1377,'K')),
            NASAPolynomial(coeffs=[11.6406,0.00572826,-2.05362e-06,3.29071e-10,-1.95188e-14,-25350.6,-30.7332], Tmin=(1377,'K'), Tmax=(5000,'K')),
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
    index = 125,
    label = "C2H4O1-2",
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
    index = 126,
    label = "HO2CH2CO",
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
            NASAPolynomial(coeffs=[2.22682,0.0356781,-3.26402e-05,1.47652e-08,-2.64794e-12,-11873.5,19.1581], Tmin=(200,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[10.4146,0.011268,-5.17495e-06,1.00333e-09,-6.68166e-14,-14095.6,-22.7894], Tmin=(1386,'K'), Tmax=(5000,'K')),
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
    index = 127,
    label = "HCCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 C u1 p0 c0 {3,D} {4,S}
3 C u0 p0 c0 {1,D} {2,D}
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
    index = 128,
    label = "CHOCHO",
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
            NASAPolynomial(coeffs=[1.88105,0.0236386,-1.83443e-05,6.84843e-09,-9.92734e-13,-26928,15.9155], Tmin=(200,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[9.75439,0.00497646,-1.7441e-06,2.75587e-10,-1.6197e-14,-29583.3,-26.1878], Tmin=(1386,'K'), Tmax=(5000,'K')),
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
    index = 129,
    label = "C3H6O1-2",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
4  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.42807,0.00625177,6.13196e-05,-8.60387e-08,3.51371e-11,-12844.7,10.4245], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.01491,0.017392,-6.26028e-06,1.01188e-09,-6.06239e-14,-15198.1,-18.828], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 130,
    label = "C4H8O2-3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {7,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.98701,0.0632679,-5.20856e-05,2.24064e-08,-3.95417e-12,-17195.7,36.692], Tmin=(200,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[15.8264,0.0164401,-5.8068e-06,9.21146e-10,-5.42511e-14,-23533.5,-63.4845], Tmin=(1384,'K'), Tmax=(5000,'K')),
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
    index = 131,
    label = "NC3H7CHO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,D} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.30068,0.00500213,8.1222e-05,-1.07816e-07,4.25781e-11,-27119.8,4.93593], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.2351,0.0232201,-8.46144e-06,1.3759e-09,-8.27046e-14,-30034.6,-28.2583], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 132,
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
            NASAPolynomial(coeffs=[2.92208,0.00762454,3.29884e-06,-1.07135e-08,5.11587e-12,-23028.2,11.2926], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.39206,0.00411221,-1.48195e-06,2.39875e-10,-1.43903e-14,-23860.7,-2.23529], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 133,
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
    index = 134,
    label = "[CH2]C[O]",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u1 p0 c0 {2,S} {6,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57173,0.0102135,5.90957e-06,-7.99912e-09,2.07091e-12,22733,11.7516], Tmin=(100,'K'), Tmax=(1490.81,'K')),
            NASAPolynomial(coeffs=[4.7406,0.0150206,-6.91944e-06,1.31186e-09,-8.98291e-14,21501.8,2.68523], Tmin=(1490.81,'K'), Tmax=(5000,'K')),
        ],
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
    label = "[CH2]C(=O)O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,D}
2 C u1 p0 c0 {1,S} {5,S} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 O u0 p2 c0 {1,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.92689,0.0179294,4.49451e-06,-1.67266e-08,6.86775e-12,-29754.3,12.035], Tmin=(100,'K'), Tmax=(1057.99,'K')),
            NASAPolynomial(coeffs=[7.9836,0.0118142,-5.27089e-06,1.04332e-09,-7.61682e-14,-31552,-16.0851], Tmin=(1057.99,'K'), Tmax=(5000,'K')),
        ],
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
    label = "[CH2]C([O])=O",
    molecule = 
"""
multiplicity 3
1 C u1 p0 c0 {2,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 O u1 p2 c0 {2,S}
4 O u0 p2 c0 {2,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60873,0.0103835,4.16403e-06,-6.72686e-09,1.73622e-12,-973.928,12.8424], Tmin=(100,'K'), Tmax=(1564.29,'K')),
            NASAPolynomial(coeffs=[5.70757,0.0133435,-6.659e-06,1.28861e-09,-8.86352e-14,-2649.36,-1.4788], Tmin=(1564.29,'K'), Tmax=(5000,'K')),
        ],
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
    label = "[CH2]O[O]",
    molecule = 
"""
multiplicity 3
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.92061,0.0189601,-2.08419e-05,1.10972e-08,-2.15338e-12,24926,11.4734], Tmin=(100,'K'), Tmax=(1506.16,'K')),
            NASAPolynomial(coeffs=[8.03882,0.0013555,6.86097e-07,-2.00094e-10,1.53444e-14,23839.3,-13.8046], Tmin=(1506.16,'K'), Tmax=(5000,'K')),
        ],
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
            NASAPolynomial(coeffs=[2.15507,0.0316121,-7.88183e-06,-1.61007e-08,8.92088e-12,-19671.6,15.8772], Tmin=(100,'K'), Tmax=(1013.67,'K')),
            NASAPolynomial(coeffs=[12.9804,0.00893267,-3.97259e-06,8.29144e-10,-6.39519e-14,-22895.8,-41.5735], Tmin=(1013.67,'K'), Tmax=(5000,'K')),
        ],
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
    index = 140,
    label = "[CH2]OCC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,D} {8,S}
3  C u1 p0 c0 {4,S} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  O u0 p2 c0 {2,D}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.28484,0.0325728,-1.57335e-05,-5.45967e-10,1.92281e-12,-13722.2,19.2133], Tmin=(100,'K'), Tmax=(1108.69,'K')),
            NASAPolynomial(coeffs=[8.91549,0.0173719,-6.96736e-06,1.27826e-09,-8.84902e-14,-15728.5,-15.8773], Tmin=(1108.69,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C[CH]OCC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {2,S} {5,S} {11,S}
4  C u0 p0 c0 {1,S} {12,D} {13,S}
5  O u0 p2 c0 {1,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.3106,0.057454,-5.07255e-05,2.37466e-08,-4.54729e-12,-19085.9,22.2944], Tmin=(100,'K'), Tmax=(1237.21,'K')),
            NASAPolynomial(coeffs=[11.6582,0.0239992,-1.01647e-05,1.89049e-09,-1.3087e-13,-21646.4,-29.8295], Tmin=(1237.21,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C[CH]OC(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u1 p0 c0 {2,S} {5,S} {13,S}
4  C u0 p0 c0 {1,S} {5,S} {12,D}
5  O u0 p2 c0 {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.61977,0.0437289,-1.33725e-05,-9.84825e-09,5.53773e-12,-32824.8,22.9963], Tmin=(100,'K'), Tmax=(1115.21,'K')),
            NASAPolynomial(coeffs=[11.4779,0.0250924,-1.07982e-05,2.05875e-09,-1.45718e-13,-36063.5,-30.3009], Tmin=(1115.21,'K'), Tmax=(5000,'K')),
        ],
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
    label = "O=C(O)COO",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {6,S} {9,S}
3  O u0 p2 c0 {1,S} {10,S}
4  O u0 p2 c0 {6,D}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6  C u0 p0 c0 {2,S} {4,D} {5,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.85186,0.0456117,-3.78629e-05,1.56235e-08,-2.61369e-12,-62143.3,19.8082], Tmin=(100,'K'), Tmax=(1398.5,'K')),
            NASAPolynomial(coeffs=[11.4054,0.0182868,-8.55482e-06,1.65231e-09,-1.16169e-13,-64815.5,-29.4862], Tmin=(1398.5,'K'), Tmax=(5000,'K')),
        ],
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
    label = "CC(=O)O[C]=O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {8,D}
3 O u0 p2 c0 {2,S} {4,S}
4 C u1 p0 c0 {3,S} {9,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 O u0 p2 c0 {2,D}
9 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.28559,0.0406005,-4.65138e-05,3.12301e-08,-8.85009e-12,-41327.5,20.2311], Tmin=(100,'K'), Tmax=(843.53,'K')),
            NASAPolynomial(coeffs=[6.70115,0.019661,-9.27646e-06,1.79886e-09,-1.27014e-13,-42072.4,-0.319797], Tmin=(843.53,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C=COC(C)OO",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {6,S}
2  O u0 p2 c0 {3,S} {4,S}
3  O u0 p2 c0 {2,S} {15,S}
4  C u0 p0 c0 {1,S} {2,S} {5,S} {8,S}
5  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
6  C u0 p0 c0 {1,S} {7,D} {12,S}
7  C u0 p0 c0 {6,D} {13,S} {14,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.155399,0.0700051,-3.71897e-05,-1.25338e-08,1.24804e-11,-37642,26.4042], Tmin=(100,'K'), Tmax=(973.04,'K')),
            NASAPolynomial(coeffs=[21.4459,0.0159313,-5.39349e-06,1.0085e-09,-7.55539e-14,-43368.7,-83.8645], Tmin=(973.04,'K'), Tmax=(5000,'K')),
        ],
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
    label = "CC([O])OC(=O)COO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {5,S} {15,D}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  O u1 p2 c0 {1,S}
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
            NASAPolynomial(coeffs=[0.678257,0.0811053,-8.72446e-05,5.84847e-08,-1.75282e-11,-61438.3,32.5395], Tmin=(100,'K'), Tmax=(779.61,'K')),
            NASAPolynomial(coeffs=[7.02269,0.0485539,-2.46152e-05,4.92916e-09,-3.54597e-13,-62427.5,3.51073], Tmin=(779.61,'K'), Tmax=(5000,'K')),
        ],
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
    label = "CC(=O)OC([O])COO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {5,S} {15,D}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  O u1 p2 c0 {1,S}
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
            NASAPolynomial(coeffs=[0.491636,0.084901,-0.000110075,9.53244e-08,-3.59045e-11,-63184.6,33.9175], Tmin=(100,'K'), Tmax=(715.98,'K')),
            NASAPolynomial(coeffs=[5.59968,0.0504521,-2.55183e-05,5.06002e-09,-3.60087e-13,-63764.5,12.0389], Tmin=(715.98,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C[C]C",
    molecule = 
"""
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3 C u0 p1 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.92363,0.0210869,-1.82385e-06,-5.35961e-09,1.86099e-12,37101.5,19.8374], Tmin=(100,'K'), Tmax=(1330.24,'K')),
            NASAPolynomial(coeffs=[5.20763,0.0205523,-8.36245e-06,1.49635e-09,-1.00129e-13,35933.5,6.06055], Tmin=(1330.24,'K'), Tmax=(5000,'K')),
        ],
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
    label = "[CH2]C([O])O",
    molecule = 
"""
multiplicity 3
1 O u0 p2 c0 {3,S} {8,S}
2 O u1 p2 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 C u1 p0 c0 {3,S} {6,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.66053,0.0330664,-4.66701e-05,4.29244e-08,-1.61007e-11,-2301.52,17.279], Tmin=(100,'K'), Tmax=(804.57,'K')),
            NASAPolynomial(coeffs=[3.9817,0.0198208,-9.52726e-06,1.83295e-09,-1.27455e-13,-2297.99,12.5355], Tmin=(804.57,'K'), Tmax=(5000,'K')),
        ],
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
    label = "[CH2]OC1CO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u1 p0 c0 {5,S} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {2,S}
5  O u0 p2 c0 {1,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.52031,0.0404321,-3.3206e-05,1.52488e-08,-2.66167e-12,-6949.06,19.0539], Tmin=(100,'K'), Tmax=(1706.44,'K')),
            NASAPolynomial(coeffs=[8.83544,0.0143568,-2.43712e-06,1.621e-10,-2.22621e-15,-8145.7,-16.3377], Tmin=(1706.44,'K'), Tmax=(5000,'K')),
        ],
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
    label = "CC1O[CH]CO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u1 p0 c0 {2,S} {6,S} {13,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.310893,0.0582318,-5.61061e-05,2.76823e-08,-4.82089e-12,-22828.6,23.5818], Tmin=(100,'K'), Tmax=(1839.24,'K')),
            NASAPolynomial(coeffs=[9.30593,0.0121363,2.02362e-06,-8.31633e-10,6.66783e-14,-22107.1,-17.0955], Tmin=(1839.24,'K'), Tmax=(5000,'K')),
        ],
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
    index = 153,
    label = "CC1OCC([O])O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {6,S} {8,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {3,S}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {3,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.8124,0.0385561,9.75507e-06,-5.07913e-08,2.75102e-11,-41567.9,19.814], Tmin=(100,'K'), Tmax=(844.36,'K')),
            NASAPolynomial(coeffs=[13.3006,0.0142828,-6.83916e-07,-2.60762e-10,2.82801e-14,-44582.7,-40.0306], Tmin=(844.36,'K'), Tmax=(5000,'K')),
        ],
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
    label = "O=CCOC=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,D} {8,S}
3  C u0 p0 c0 {4,S} {9,D} {10,S}
4  O u0 p2 c0 {1,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  O u0 p2 c0 {2,D}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.30187,0.029977,-1.25334e-06,-1.56614e-08,6.62598e-12,-56966.6,19.838], Tmin=(100,'K'), Tmax=(1119.04,'K')),
            NASAPolynomial(coeffs=[9.63762,0.0197748,-9.05078e-06,1.77651e-09,-1.27688e-13,-59611.4,-20.8593], Tmin=(1119.04,'K'), Tmax=(5000,'K')),
        ],
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
    index = 156,
    label = "[O]C[O]",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u1 p2 c0 {1,S}
3 O u1 p2 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.67715,-0.00771638,2.71171e-05,-1.79271e-08,3.39819e-12,6337.74,0.967287], Tmin=(100,'K'), Tmax=(1894.84,'K')),
            NASAPolynomial(coeffs=[6.52031,0.0150023,-1.02613e-05,2.04716e-09,-1.37412e-13,1620.19,-15.2446], Tmin=(1894.84,'K'), Tmax=(5000,'K')),
        ],
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
    label = "O=[C]C=O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {4,D}
3 C u0 p0 c0 {1,D} {4,S} {5,S}
4 C u1 p0 c0 {2,D} {3,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.25386,0.0154074,-1.14326e-05,4.29105e-09,-6.587e-13,-9058.53,11.1539], Tmin=(100,'K'), Tmax=(1504.28,'K')),
            NASAPolynomial(coeffs=[6.43153,0.00695779,-3.00696e-06,5.56992e-10,-3.81281e-14,-10014.6,-5.474], Tmin=(1504.28,'K'), Tmax=(5000,'K')),
        ],
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
    label = "O=[C]CC=O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,D}
2 O u0 p2 c0 {5,D}
3 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,D} {3,S} {8,S}
5 C u1 p0 c0 {2,D} {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.34837,0.0397445,-5.8374e-05,4.99593e-08,-1.71206e-11,-13513.9,16.8709], Tmin=(100,'K'), Tmax=(829.99,'K')),
            NASAPolynomial(coeffs=[5.81588,0.0174819,-8.10677e-06,1.52464e-09,-1.04311e-13,-13898.3,1.9403], Tmin=(829.99,'K'), Tmax=(5000,'K')),
        ],
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
    label = "C=COC(C)[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,D} {5,S} {11,S}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u1 p2 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.21425,0.0500689,-1.73272e-05,-1.73107e-08,1.11138e-11,-19137.3,22.7032], Tmin=(100,'K'), Tmax=(989.55,'K')),
            NASAPolynomial(coeffs=[15.4818,0.0176695,-6.52518e-06,1.2218e-09,-8.88934e-14,-23198.3,-52.2318], Tmin=(989.55,'K'), Tmax=(5000,'K')),
        ],
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
    label = "[O]C(=O)C=O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,D}
2 C u0 p0 c0 {1,S} {5,D} {6,S}
3 O u1 p2 c0 {1,S}
4 O u0 p2 c0 {1,D}
5 O u0 p2 c0 {2,D}
6 H u0 p0 c0 {2,S}
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
    index = 161,
    label = "CC([O])OC=O",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {6,S}
2  O u1 p2 c0 {4,S}
3  O u0 p2 c0 {6,D}
4  C u0 p0 c0 {1,S} {2,S} {5,S} {7,S}
5  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {1,S} {3,D} {11,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.52315,0.034012,-1.40072e-05,6.95839e-10,4.07466e-13,-45909.5,20.8741], Tmin=(100,'K'), Tmax=(1809.57,'K')),
            NASAPolynomial(coeffs=[13.0454,0.0196792,-9.52561e-06,1.77074e-09,-1.17643e-13,-51179.1,-40.1683], Tmin=(1809.57,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 162,
    label = "C=COC=O",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 C u0 p0 c0 {4,S} {8,D} {9,S}
4 O u0 p2 c0 {1,S} {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 O u0 p2 c0 {3,D}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.26822,0.0274098,8.9621e-06,-3.49175e-08,1.60198e-11,-35312.1,15.3426], Tmin=(100,'K'), Tmax=(975.34,'K')),
            NASAPolynomial(coeffs=[12.8621,0.0097387,-3.50257e-06,6.98088e-10,-5.44447e-14,-38604.6,-41.7875], Tmin=(975.34,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 163,
    label = "O=COC1CO1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {5,S} {9,D} {10,S}
4  O u0 p2 c0 {1,S} {2,S}
5  O u0 p2 c0 {1,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.44076,0.0245733,2.39615e-05,-5.22222e-08,2.37004e-11,-50242.8,17.3249], Tmin=(100,'K'), Tmax=(896.08,'K')),
            NASAPolynomial(coeffs=[10.4654,0.0147784,-3.20883e-06,4.04554e-10,-2.49017e-14,-52725.9,-26.3394], Tmin=(896.08,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 164,
    label = "CC(O[O])OC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,D} {11,S}
4  O u0 p2 c0 {1,S} {3,S}
5  O u0 p2 c0 {1,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {3,S}
12 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.90357,0.0487633,-3.49692e-05,1.24893e-08,-1.87161e-12,-46152.7,23.7225], Tmin=(100,'K'), Tmax=(1472.82,'K')),
            NASAPolynomial(coeffs=[9.88888,0.0270763,-1.28822e-05,2.49176e-09,-1.74627e-13,-48504.9,-17.8938], Tmin=(1472.82,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 165,
    label = "O=CCC=O",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {9,S}
3 C u0 p0 c0 {1,S} {7,D} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 O u0 p2 c0 {3,D}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.60725,0.0276497,-1.51511e-05,3.74761e-09,-3.45659e-13,-32764.1,16.6664], Tmin=(100,'K'), Tmax=(1863.44,'K')),
            NASAPolynomial(coeffs=[10.4165,0.0132386,-5.44405e-06,9.52139e-10,-6.14904e-14,-36082.9,-26.9651], Tmin=(1863.44,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 166,
    label = "[O]C[C]=O",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,D}
3 O u1 p2 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.01457,0.0123696,2.06311e-05,-3.93787e-08,1.66634e-11,7969.01,14.0081], Tmin=(100,'K'), Tmax=(965.91,'K')),
            NASAPolynomial(coeffs=[10.9319,0.00281309,-6.04149e-07,1.77118e-10,-1.91393e-14,5355.84,-29.5235], Tmin=(965.91,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 167,
    label = "O=CCOCC=O",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,D} {12,S}
4  C u0 p0 c0 {2,S} {11,D} {13,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.45439,0.0538398,-4.00534e-05,1.4876e-08,-2.25843e-12,-48803.8,23.8486], Tmin=(100,'K'), Tmax=(1512.62,'K')),
            NASAPolynomial(coeffs=[12.523,0.0245702,-1.10284e-05,2.08379e-09,-1.44216e-13,-52152.3,-34.1319], Tmin=(1512.62,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 168,
    label = "CC1OCC(O[O])O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {3,S} {5,S} {7,S} {9,S}
3  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {3,S}
7  O u0 p2 c0 {2,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.231879,0.0697684,-6.77813e-05,3.40668e-08,-6.29372e-12,-41747.6,27.8033], Tmin=(100,'K'), Tmax=(1628,'K')),
            NASAPolynomial(coeffs=[15.0415,0.0142957,-1.34931e-07,-4.05562e-10,3.97549e-14,-44342.4,-46.0212], Tmin=(1628,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 169,
    label = "CC(OO)OC=O",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {7,S}
2  O u0 p2 c0 {3,S} {5,S}
3  O u0 p2 c0 {2,S} {13,S}
4  O u0 p2 c0 {7,D}
5  C u0 p0 c0 {1,S} {2,S} {6,S} {8,S}
6  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
7  C u0 p0 c0 {1,S} {4,D} {12,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.39088,0.055087,-3.88673e-05,1.30025e-08,-1.74928e-12,-64412.1,24.8165], Tmin=(100,'K'), Tmax=(1694.25,'K')),
            NASAPolynomial(coeffs=[14.5779,0.0239532,-1.1303e-05,2.1563e-09,-1.48826e-13,-68880.5,-45.7561], Tmin=(1694.25,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 170,
    label = "CC([O])OC1CO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {1,S} {2,S}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.27961,0.0589903,-5.15129e-05,2.7523e-08,-6.2687e-12,-30999.7,24.9713], Tmin=(100,'K'), Tmax=(1039.21,'K')),
            NASAPolynomial(coeffs=[8.43654,0.0314428,-1.17508e-05,2.01515e-09,-1.32364e-13,-32487.2,-9.83201], Tmin=(1039.21,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 171,
    label = "[O]CCOC1CO1",
    molecule = 
"""
multiplicity 2
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
12 O u1 p2 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.1739,0.0644592,-7.21202e-05,5.19503e-08,-1.55242e-11,-26139.4,24.8945], Tmin=(100,'K'), Tmax=(916.65,'K')),
            NASAPolynomial(coeffs=[6.93201,0.0337648,-1.27811e-05,2.16756e-09,-1.39668e-13,-26961.1,-1.10799], Tmin=(916.65,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 172,
    label = "O=[C]CC(=O)O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {4,S} {7,D}
3 C u1 p0 c0 {1,S} {8,D}
4 O u0 p2 c0 {2,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 O u0 p2 c0 {3,D}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.93063,0.0490671,-6.82891e-05,5.53036e-08,-1.84288e-11,-45453.6,19.6804], Tmin=(100,'K'), Tmax=(761.43,'K')),
            NASAPolynomial(coeffs=[7.04734,0.0208311,-9.99251e-06,1.92265e-09,-1.34032e-13,-46193.5,-3.35196], Tmin=(761.43,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 173,
    label = "CC(OC=O)OC=O",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {7,S}
2  O u0 p2 c0 {5,S} {8,S}
3  O u0 p2 c0 {7,D}
4  O u0 p2 c0 {8,D}
5  C u0 p0 c0 {1,S} {2,S} {6,S} {9,S}
6  C u0 p0 c0 {5,S} {10,S} {11,S} {12,S}
7  C u0 p0 c0 {1,S} {3,D} {14,S}
8  C u0 p0 c0 {2,S} {4,D} {13,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.29202,0.0502001,-1.66412e-05,-7.87818e-09,4.37723e-12,-91169,27.4422], Tmin=(100,'K'), Tmax=(1237.63,'K')),
            NASAPolynomial(coeffs=[13.3044,0.0297521,-1.41299e-05,2.76604e-09,-1.96283e-13,-95549.7,-38.7571], Tmin=(1237.63,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 174,
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
    index = 175,
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
    index = 176,
    label = "[O]CC(=O)O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,D}
3 O u0 p2 c0 {2,S} {8,S}
4 O u1 p2 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.53281,0.0284229,-1.94174e-05,6.58114e-09,-8.99582e-13,-41451.6,17.3916], Tmin=(100,'K'), Tmax=(1695.18,'K')),
            NASAPolynomial(coeffs=[9.47929,0.0120315,-4.91305e-06,8.76885e-10,-5.83219e-14,-43806.6,-19.7873], Tmin=(1695.18,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 177,
    label = "[O]OCC(=O)O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {4,S} {7,D}
3 O u0 p2 c0 {1,S} {8,S}
4 O u0 p2 c0 {2,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 O u1 p2 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.23253,0.0406211,-3.76985e-05,1.88584e-08,-3.95525e-12,-43877.7,19.2042], Tmin=(100,'K'), Tmax=(1115.41,'K')),
            NASAPolynomial(coeffs=[8.16048,0.0193628,-9.11063e-06,1.77181e-09,-1.25607e-13,-45200.1,-10.0422], Tmin=(1115.41,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 178,
    label = "O=COC=O",
    molecule = 
"""
1 C u0 p0 c0 {3,S} {4,D} {6,S}
2 C u0 p0 c0 {3,S} {5,D} {7,S}
3 O u0 p2 c0 {1,S} {2,S}
4 O u0 p2 c0 {1,D}
5 O u0 p2 c0 {2,D}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.83834,0.0223427,-1.38973e-05,3.49318e-09,-2.4455e-13,-58250,16.6203], Tmin=(100,'K'), Tmax=(1522.36,'K')),
            NASAPolynomial(coeffs=[9.19089,0.00916685,-4.37887e-06,8.41795e-10,-5.8246e-14,-60591.6,-18.0348], Tmin=(1522.36,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 179,
    label = "O=CC(=O)O",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,D}
2 C u0 p0 c0 {1,S} {5,D} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 O u0 p2 c0 {1,D}
5 O u0 p2 c0 {2,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
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
    index = 180,
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
    index = 181,
    label = "CC1OC1=O",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {4,S} {9,D}
4 O u0 p2 c0 {1,S} {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.21816,-0.00506665,0.000108587,-1.41984e-07,5.51326e-11,-25635.5,14.3097], Tmin=(100,'K'), Tmax=(937.61,'K')),
            NASAPolynomial(coeffs=[14.0287,0.00579699,4.43973e-08,1.26355e-11,-1.2226e-14,-30167.4,-50.5053], Tmin=(937.61,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 182,
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
    index = 183,
    label = "[O]OC=C=O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 C u0 p0 c0 {1,D} {6,D}
4 H u0 p0 c0 {1,S}
5 O u1 p2 c0 {2,S}
6 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.53916,0.0349114,-5.07387e-05,3.64952e-08,-9.52285e-12,7713.97,15.2203], Tmin=(100,'K'), Tmax=(668.13,'K')),
            NASAPolynomial(coeffs=[7.4976,0.00982574,-4.74667e-06,9.08496e-10,-6.2882e-14,6948.72,-7.47001], Tmin=(668.13,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 184,
    label = "[O]C(O)C(=O)O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {4,S} {7,D}
3 O u0 p2 c0 {1,S} {8,S}
4 O u0 p2 c0 {2,S} {9,S}
5 O u1 p2 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33987,0.0389387,-3.73434e-05,1.97973e-08,-4.44795e-12,-67266.3,21.9419], Tmin=(100,'K'), Tmax=(1041.04,'K')),
            NASAPolynomial(coeffs=[7.41282,0.0194469,-9.25856e-06,1.81235e-09,-1.28988e-13,-68322.6,-2.73625], Tmin=(1041.04,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 185,
    label = "[O]OCOC1CO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {5,S} {6,S} {10,S} {11,S}
4  O u0 p2 c0 {1,S} {2,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {3,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.752177,0.0716884,-7.33573e-05,3.60235e-08,-6.35481e-12,-25651.6,29.869], Tmin=(100,'K'), Tmax=(1734.64,'K')),
            NASAPolynomial(coeffs=[17.1623,0.00721117,2.43174e-06,-8.0362e-10,6.24404e-14,-28381.2,-56.3786], Tmin=(1734.64,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 186,
    label = "CC1OC=CO1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,D} {5,S} {11,S}
4  C u0 p0 c0 {3,D} {6,S} {12,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {1,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.89776,0.00490909,0.000157398,-2.36438e-07,9.92402e-11,-39526.9,15.2835], Tmin=(100,'K'), Tmax=(914.36,'K')),
            NASAPolynomial(coeffs=[30.8245,-0.0142525,1.26732e-05,-2.48032e-09,1.55906e-13,-49305.7,-146.228], Tmin=(914.36,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 187,
    label = "[O]CC(=O)OO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {8,D}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {3,S} {9,S}
5 O u1 p2 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 O u0 p2 c0 {2,D}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.42765,0.0577065,-8.40605e-05,6.15975e-08,-1.73692e-11,-32259.1,20.8951], Tmin=(100,'K'), Tmax=(937.3,'K')),
            NASAPolynomial(coeffs=[11.4958,0.0112111,-4.00454e-06,6.39839e-10,-3.89914e-14,-33991.5,-26.1989], Tmin=(937.3,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 188,
    label = "O=CC(=O)OO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {5,D}
2 C u0 p0 c0 {1,S} {6,D} {7,S}
3 O u0 p2 c0 {1,S} {4,S}
4 O u0 p2 c0 {3,S} {8,S}
5 O u0 p2 c0 {1,D}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.56722,0.0563211,-8.61289e-05,6.62451e-08,-1.98882e-11,-48706.3,17.7879], Tmin=(100,'K'), Tmax=(822.19,'K')),
            NASAPolynomial(coeffs=[10.6202,0.0122759,-5.7697e-06,1.08378e-09,-7.39873e-14,-50194.9,-24.1148], Tmin=(822.19,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 189,
    label = "CC1OC1C=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {7,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {11,D} {12,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.17643,0.0246691,4.8287e-05,-8.94931e-08,4.0049e-11,-26387.3,19.0013], Tmin=(100,'K'), Tmax=(887.62,'K')),
            NASAPolynomial(coeffs=[14.3152,0.0116347,-1.01047e-07,-2.63719e-10,2.18028e-14,-30183.7,-47.3603], Tmin=(887.62,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 190,
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
    index = 191,
    label = "[CH2]OC(C)OC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {5,S} {12,S} {13,S}
4  C u0 p0 c0 {6,S} {11,D} {14,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {1,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.31427,0.0551219,-3.61404e-05,1.11655e-08,-1.37741e-12,-47917.1,26.4669], Tmin=(100,'K'), Tmax=(1845.06,'K')),
            NASAPolynomial(coeffs=[15.7198,0.0238916,-1.07509e-05,1.99164e-09,-1.34391e-13,-53232.9,-51.8553], Tmin=(1845.06,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 192,
    label = "CC(OC=O)OCO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {6,S} {14,D} {15,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {1,S} {4,S}
7  O u0 p2 c0 {3,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.200001,0.0779118,-4.88714e-05,-5.8186e-10,7.53707e-12,-66653.3,34.5299], Tmin=(100,'K'), Tmax=(1014.2,'K')),
            NASAPolynomial(coeffs=[21.8258,0.0207441,-8.24983e-06,1.59268e-09,-1.17053e-13,-72648.6,-79.5731], Tmin=(1014.2,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 193,
    label = "CC(OC=O)OC[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {6,S} {14,D} {15,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {1,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u1 p2 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.724813,0.0618253,-3.57861e-05,5.67372e-09,8.99769e-13,-66223.3,30.1878], Tmin=(100,'K'), Tmax=(1283.17,'K')),
            NASAPolynomial(coeffs=[16.1713,0.0279858,-1.29583e-05,2.50553e-09,-1.76403e-13,-71365.7,-52.7751], Tmin=(1283.17,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 194,
    label = "OOCOC1[CH]O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {5,S} {11,S}
4  O u0 p2 c0 {1,S} {2,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {12,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.48041,0.0818363,-8.7889e-05,4.34576e-08,-7.65805e-12,-21805.5,31.9344], Tmin=(100,'K'), Tmax=(1735.08,'K')),
            NASAPolynomial(coeffs=[21.0415,0.0024532,4.47994e-06,-1.15513e-09,8.43481e-14,-25487.3,-77.2193], Tmin=(1735.08,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 195,
    label = "O=C([CH]O)OO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {6,D}
2 C u1 p0 c0 {1,S} {4,S} {7,S}
3 O u0 p2 c0 {1,S} {5,S}
4 O u0 p2 c0 {2,S} {8,S}
5 O u0 p2 c0 {3,S} {9,S}
6 O u0 p2 c0 {1,D}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.19977,0.0631799,-9.5151e-05,7.08816e-08,-2.02379e-11,-44909.8,20.6898], Tmin=(100,'K'), Tmax=(931.08,'K')),
            NASAPolynomial(coeffs=[12.349,0.0109531,-4.03798e-06,6.49965e-10,-3.95563e-14,-46798.3,-31.2948], Tmin=(931.08,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 196,
    label = "[O]C=COCOO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {3,D} {4,S} {9,S}
3  C u0 p0 c0 {2,D} {10,S} {11,S}
4  O u0 p2 c0 {1,S} {2,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 O u1 p2 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.0287936,0.0549814,3.39677e-05,-1.22559e-07,6.21923e-11,-40206.9,25.0516], Tmin=(100,'K'), Tmax=(906.61,'K')),
            NASAPolynomial(coeffs=[36.4337,-0.0192734,1.39314e-05,-2.7511e-09,1.80676e-13,-50357.3,-166.587], Tmin=(906.61,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 197,
    label = "O=COC(=O)COO",
    molecule = 
"""
1  O u0 p2 c0 {7,S} {8,S}
2  O u0 p2 c0 {3,S} {6,S}
3  O u0 p2 c0 {2,S} {12,S}
4  O u0 p2 c0 {7,D}
5  O u0 p2 c0 {8,D}
6  C u0 p0 c0 {2,S} {7,S} {9,S} {10,S}
7  C u0 p0 c0 {1,S} {4,D} {6,S}
8  C u0 p0 c0 {1,S} {5,D} {11,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {8,S}
12 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.18754,0.0671483,-7.907e-05,5.04919e-08,-1.33295e-11,-73787.2,28.2823], Tmin=(100,'K'), Tmax=(907.39,'K')),
            NASAPolynomial(coeffs=[10.0849,0.0279275,-1.42357e-05,2.85859e-09,-2.05994e-13,-75401.9,-13.7776], Tmin=(907.39,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 198,
    label = "O=CC1OCO1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,D} {10,S}
4  O u0 p2 c0 {1,S} {2,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.38751,0.00895596,9.61326e-05,-1.43406e-07,5.84352e-11,-43246.7,18.4666], Tmin=(100,'K'), Tmax=(939.83,'K')),
            NASAPolynomial(coeffs=[20.4173,-9.88332e-05,2.56112e-06,-4.0437e-10,1.26077e-14,-49624.7,-83.3001], Tmin=(939.83,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 199,
    label = "[O]OC(C=O)OCOO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {7,S} {8,S}
2  O u0 p2 c0 {4,S} {8,S}
3  O u0 p2 c0 {6,S} {7,S}
4  O u0 p2 c0 {2,S} {14,S}
5  O u0 p2 c0 {9,D}
6  O u1 p2 c0 {3,S}
7  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
8  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
9  C u0 p0 c0 {5,D} {7,S} {13,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {8,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.523302,0.0902763,-9.88445e-05,5.16598e-08,-1.03843e-11,-49622.9,35.657], Tmin=(100,'K'), Tmax=(1226.6,'K')),
            NASAPolynomial(coeffs=[22.8099,0.014186,-5.79456e-06,1.08668e-09,-7.68062e-14,-55347,-81.6781], Tmin=(1226.6,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 200,
    label = "O=C(O)[CH]O",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {4,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {5,D}
3 O u0 p2 c0 {2,S} {7,S}
4 O u0 p2 c0 {1,S} {8,S}
5 O u0 p2 c0 {2,D}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
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
    index = 201,
    label = "[O]C(O)[C]=O",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {7,S}
3 C u1 p0 c0 {1,S} {6,D}
4 O u1 p2 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {3,D}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.66623,0.0317027,-4.3309e-05,3.49109e-08,-1.16695e-11,-16721,20.1364], Tmin=(100,'K'), Tmax=(741.14,'K')),
            NASAPolynomial(coeffs=[5.8665,0.0140352,-6.75154e-06,1.30728e-09,-9.16246e-14,-17184.5,5.7288], Tmin=(741.14,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 202,
    label = "[O]C([O])=CO",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 O u1 p2 c0 {2,S}
6 O u1 p2 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.641377,0.049514,-5.71631e-05,2.85305e-08,-5.01908e-12,-29883.6,19.7649], Tmin=(100,'K'), Tmax=(1733.83,'K')),
            NASAPolynomial(coeffs=[16.4065,-0.0042557,4.40766e-06,-9.31585e-10,6.35993e-14,-32735.2,-57.427], Tmin=(1733.83,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 203,
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
    index = 204,
    label = "O=C(O)C(O)OO",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {6,S}
2  O u0 p2 c0 {6,S} {9,S}
3  O u0 p2 c0 {7,S} {10,S}
4  O u0 p2 c0 {1,S} {11,S}
5  O u0 p2 c0 {7,D}
6  C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
7  C u0 p0 c0 {3,S} {5,D} {6,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.56353,0.057086,-5.84658e-05,3.15299e-08,-7.04105e-12,-87953.5,24.7132], Tmin=(100,'K'), Tmax=(1058.76,'K')),
            NASAPolynomial(coeffs=[10.1882,0.0245018,-1.23018e-05,2.46179e-09,-1.7731e-13,-89779.8,-17.3883], Tmin=(1058.76,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 205,
    label = "O=C(O)C(=O)O",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {5,D}
2 C u0 p0 c0 {1,S} {4,S} {6,D}
3 O u0 p2 c0 {1,S} {7,S}
4 O u0 p2 c0 {2,S} {8,S}
5 O u0 p2 c0 {1,D}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.55079,0.0359585,-2.85219e-05,1.08202e-08,-1.71415e-12,-89058.5,14.8488], Tmin=(100,'K'), Tmax=(1398.07,'K')),
            NASAPolynomial(coeffs=[8.53138,0.0188476,-1.01636e-05,2.06616e-09,-1.48772e-13,-90730.7,-16.0082], Tmin=(1398.07,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 206,
    label = "C1OO1",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54047,-0.0177442,0.000131418,-1.83784e-07,7.77289e-11,-1973.83,7.10167], Tmin=(100,'K'), Tmax=(885.26,'K')),
            NASAPolynomial(coeffs=[21.1789,-0.0237533,1.67397e-05,-3.39203e-09,2.31179e-13,-7984.16,-92.152], Tmin=(885.26,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 207,
    label = "O=C1OC1O",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {6,D}
3 O u0 p2 c0 {1,S} {2,S}
4 O u0 p2 c0 {1,S} {7,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.19579,0.0027947,6.26394e-05,-8.72778e-08,3.45225e-11,-45439.1,14.0728], Tmin=(100,'K'), Tmax=(942.2,'K')),
            NASAPolynomial(coeffs=[11.7684,0.00438688,-3.70279e-07,9.55716e-11,-1.4567e-14,-48740.6,-35.7223], Tmin=(942.2,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

