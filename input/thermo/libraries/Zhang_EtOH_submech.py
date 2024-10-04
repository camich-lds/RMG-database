#!/usr/bin/env python
# encoding: utf-8

name = "Zhang_EtOH_submech"
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
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
            NASAPolynomial(coeffs=[0.215806,0.0295228,-1.68271e-05,4.49485e-09,-4.02452e-13,-29485.2,24.5725], Tmin=(300,'K'), Tmax=(1402,'K')),
            NASAPolynomial(coeffs=[8.14484,0.0128314,-4.29053e-06,6.55972e-10,-3.76507e-14,-32400.6,-18.6241], Tmin=(1402,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1,
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
            NASAPolynomial(coeffs=[2.90354,0.0177257,-2.69625e-06,-3.45831e-09,1.25225e-12,-3289.3,11.3546], Tmin=(300,'K'), Tmax=(1467,'K')),
            NASAPolynomial(coeffs=[8.19121,0.0110392,-3.75271e-06,5.80276e-10,-3.35735e-14,-5668.47,-19.0131], Tmin=(1467,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2,
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
            NASAPolynomial(coeffs=[2.5948,0.0227101,-1.39474e-05,4.70096e-09,-6.90044e-13,-4914.87,14.3241], Tmin=(300,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[8.0675,0.0106144,-3.57999e-06,5.50364e-10,-3.17052e-14,-6927.48,-15.3833], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 3,
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
            NASAPolynomial(coeffs=[1.46281,0.0239194,-1.30667e-05,3.10615e-09,-1.85896e-13,-8007.9,19.2547], Tmin=(300,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[8.15007,0.0102549,-3.40138e-06,5.1751e-10,-2.96129e-14,-10501.4,-17.3135], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 4,
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
            NASAPolynomial(coeffs=[7.0401,0.0159564,2.21097e-06,-7.05197e-09,2.08266e-12,-22452.4,-1.75362], Tmin=(300,'K'), Tmax=(1506,'K')),
            NASAPolynomial(coeffs=[12.7504,0.0111514,-3.83474e-06,5.98156e-10,-3.48372e-14,-25277.1,-35.4318], Tmin=(1506,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 5,
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
            NASAPolynomial(coeffs=[4.07328,0.0292132,-1.52828e-05,2.63255e-09,1.52348e-13,-13414.8,11.0932], Tmin=(300,'K'), Tmax=(1489,'K')),
            NASAPolynomial(coeffs=[13.3404,0.0109745,-3.74672e-06,5.8125e-10,-3.3714e-14,-16896.3,-39.7564], Tmin=(1489,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 6,
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
            NASAPolynomial(coeffs=[2.33734,0.042034,-3.82429e-05,1.7892e-08,-3.3207e-12,-17530.3,19.3825], Tmin=(300,'K'), Tmax=(1404,'K')),
            NASAPolynomial(coeffs=[13.774,0.0101573,-3.45547e-06,5.34494e-10,-3.09294e-14,-20989.8,-40.2145], Tmin=(1404,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 7,
    label = "CY(CCO)OH",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {3,S} {8,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.478581,0.0333964,-2.36033e-05,8.04822e-09,-1.05069e-12,-30907,28.1885], Tmin=(300,'K'), Tmax=(1649,'K')),
            NASAPolynomial(coeffs=[9.02424,0.0104465,-3.612e-06,5.6803e-10,-3.33387e-14,-33908,-22.2436], Tmin=(1649,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 8,
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
            NASAPolynomial(coeffs=[0.765239,0.0418978,-3.44242e-05,1.46381e-08,-2.50529e-12,-27229.2,26.3505], Tmin=(300,'K'), Tmax=(1405,'K')),
            NASAPolynomial(coeffs=[12.5016,0.0114979,-3.88395e-06,5.98041e-10,-3.45006e-14,-30976.1,-35.5712], Tmin=(1405,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 9,
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
            NASAPolynomial(coeffs=[1.94095,0.0409617,-3.50724e-05,1.58513e-08,-2.90496e-12,-17871.8,18.4802], Tmin=(300,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[13.1124,0.0113613,-3.91861e-06,6.1175e-10,-3.56278e-14,-21449.1,-40.3551], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 10,
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
            NASAPolynomial(coeffs=[4.62867,0.0255848,-1.1935e-05,1.85831e-09,1.22915e-13,-25163.3,10.7862], Tmin=(300,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[11.3626,0.0128096,-4.22991e-06,6.41336e-10,-3.65999e-14,-27778.4,-26.3951], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 11,
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
            NASAPolynomial(coeffs=[1.87394,0.0453102,-4.09182e-05,1.84737e-08,-3.29201e-12,-19508.3,20.0877], Tmin=(300,'K'), Tmax=(1403,'K')),
            NASAPolynomial(coeffs=[15.3465,0.00910986,-3.15993e-06,4.95378e-10,-2.89408e-14,-23673.3,-50.5231], Tmin=(1403,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

