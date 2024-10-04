#!/usr/bin/env python
# encoding: utf-8

name = "DEE_seeding_Danilack"
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
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
            NASAPolynomial(coeffs=[9.28251392E+00, 8.86813721E-04, 7.53440830E-05,
                        -8.89727100E-08, 3.25601682E-11, -3.39847255E+04,
                        -1.41271480E+01], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.14271655E+00, 4.02539598E-02, -1.94012566E-05,
                        4.51835180E-09, -4.12902726E-13, -3.37248726E+04,
                        6.46241861E+00], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
CH3CH2OCH2CH3
# deltaH(0) -54.44 kcal/mol
# deltaH(298) -60.95 kcal/mol
""",
)

entry(
    index = 1,
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
            NASAPolynomial(coeffs=[5.14533218E+00, 3.60511587E-02, -1.75341617E-05,
                      4.12771508E-09, -3.81180450E-13, -8.40537300E+03,
                      4.22193041E+00], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.10151189E+00, 7.25153387E-03, 5.93428486E-05,
                     -7.65874869E-08, 2.93004563E-11, -8.34493726E+03,
                     -6.35285781E+00], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
CH3CH2OCH2CH2
# deltaH(0) -4.78 kcal/mol
# deltaH(298) -10.37 kcal/mol
""",
)

entry(
    index = 2,
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
            NASAPolynomial(coeffs=[1.33504367E+01, -1.78551765E-02, 1.40110039E-04,
                     -1.67056974E-07, 6.39321480E-11, -2.64915385E+04, -2.30544087E+01], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.36460342E+00, 3.93886543E-02, -1.95882137E-05,
                      4.77628845E-09, -4.60858468E-13, -2.69745839E+04, -7.18769952E+00], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
CH3CH2OCH2CH2OO
# deltaH(0) -38.37 kcal/mol
# deltaH(298) -44.45 kcal/mol
""",
)

entry(
    index = 3,
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
            NASAPolynomial(coeffs=[1.26459249E+01, -1.99067974E-03, 9.92002874E-05,
                     -1.27649929E-07, 5.03518104E-11, -2.22473147E+04, -2.08515431E+01], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.05839559E+01, 3.58735212E-02, -1.78130433E-05,
                      4.32951106E-09, -4.16531251E-13, -2.29541944E+04, -1.72665628E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
# deltaH(0) -29.98 kcal/mol
# deltaH(298) -35.61 kcal/mol
CH3CH2OCHCH2OOH
""",
)

entry(
    index = 4,
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
            NASAPolynomial(coeffs=[1.13015923E+00, 8.26841325E-02, -7.83200988E-05,
                     2.94978920E-08, -8.79489895E-13, -2.11689993E+04, 2.21155284E+01], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.65095474E+01, 2.80826241E-02, -1.32267205E-05,
                      3.01624487E-09, -2.69100739E-13, -2.44470920E+04, -5.33920834E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
# deltaH(0) -29.24 kcal/mol
# deltaH(298) -35.35 kcal/mol
CH3CHOCH2CH2OOH
""",
)

entry(
    index = 5,
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
            NASAPolynomial(coeffs=[5.54682578E-01, 8.88023396E-02, -9.60937922E-05,
                      4.68479637E-08, -6.46166064E-12, -1.77020433E+04, 2.63284763E+01], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.70630443E+01, 2.55902872E-02, -1.11805426E-05,
                      2.37645637E-09, -1.99712235E-13, -2.10433082E+04, -5.36934702E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
# deltaH(0) -22.48 kcal/mol
# deltaH(298) -28.51 kcal/mol
CH2CH2OCH2CH2OOH
""",
)

entry(
    index = 6,
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
            NASAPolynomial(coeffs=[6.00062235E+00, 1.47218328E-02, 6.16999220E-05,
                     -9.24978978E-08, 3.84352674E-11, -3.39966252E+04, 2.69094587E+00], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.90047872E+00, 3.48640367E-02, -1.71015492E-05,
                      4.08147669E-09, -3.84696157E-13, -3.50812773E+04, -6.75464402E+00], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
# deltaH(0) -56.15 kcal/mol
# deltaH(298) -61.95 kcal/mol
c-OCH2CH(OCH2CH3)
""",
)

entry(
    index = 7,
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
            NASAPolynomial(coeffs=[5.05301908E+00, -8.27699725E-05, 1.14247751E-04,
                     -1.50953366E-07, 6.03549516E-11, -4.49993720E+04, 7.32914295E+00], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.24700651E+00, 4.00650434E-02, -2.00994152E-05,
                      4.86957306E-09, -4.62622087E-13, -4.62770974E+04, 3.18606393E+00], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
# deltaH(0) -78.22 kcal/mol
# deltaH(298) -84.97 kcal/mol
c-OCH2CH2OCH(CH3)
""",
)

entry(
    index = 8,
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
            NASAPolynomial(coeffs=[3.73621381E+00, 1.00440618E-03, 1.17383346E-04,
                     -1.55035386E-07, 6.17173044E-11, -4.09657079E+04, 1.03016903E+01], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.85976600E+00, 4.30383097E-02, -2.19850430E-05,
                      5.41491534E-09, -5.22064132E-13, -4.23147839E+04, 6.08267639E+00], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
# deltaH(0) -70.27 kcal/mol
# deltaH(298) -77.60 kcal/mol
c-OCH2CH2OCH2CH2
""",
)

entry(
    index = 9,
    label = "C4H8O",
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
            NASAPolynomial(coeffs=[  2.23228148E+00, 3.75393216E-02, 5.64663788E-06,
                    -4.00786558E-08, 2.09921892E-11,-1.96373838E+04,
                    1.55511606E+01], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[  7.33253141E+00, 3.07387159E-02, -1.49617575E-05,
                        3.55703826E-09, -3.34753766E-13, -2.11114006E+04,
                    -1.17888100E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
# deltaH(0) -29.12 kcal/mol
# deltaH(298) -34.42 kcal/mol
CH3CH2OCHCH2
""",
)

entry(
    index = 10,
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
            NASAPolynomial(coeffs=[ 8.11185681E+00, 5.61776651E-03, 6.50004312E-05,
                        -8.37877156E-08, 3.23928172E-11, -1.22475493E+04,
                        -6.62090512E+00], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[  5.45595791E+00, 3.50940214E-02, -1.67210166E-05,
                        3.85576417E-09, -3.49570726E-13, -1.24516876E+04,
                        2.08096725E+00], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
# deltaH(0) -12.63 kcal/mol
# deltaH(298) -18.19 kcal/mol
CH3CH2OCHCH3
""",
)

entry(
    index = 11,
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
            NASAPolynomial(coeffs=[  7.93762975E+00, 1.84349672E-02, 6.72761179E-05,
                    -1.04621185E-07, 4.39773349E-11, -3.13951688E+04,
                    -3.19626667E+00], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[  1.06438699E+01, 3.65552221E-02, -1.82519497E-05,
                        4.49682446E-09, -4.39101931E-13, -3.30483955E+04,
                    -2.25150931E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
# deltaH(0) -48.65 kcal/mol
# deltaH(298) -55.25 kcal/mol
CH3CH2OCH(OO)CH3
""",
)

entry(
    index = 12,
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
            NASAPolynomial(coeffs=[7.61141369E+00, 4.03556388E-02, 2.66989719E-06,
                     -3.79567008E-08, 2.03240771E-11, -2.30970070E+04, -3.37605822E+00], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.25940376E+01, 3.32983584E-02, -1.65718100E-05,
                      4.08618158E-09, -4.02441567E-13, -2.45025051E+04, -2.99493351E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
# deltaH(0) -32.15 kcal/mol
# deltaH(298) -37.91 kcal/mol
CH3CH2OCH(OOH)CH2
""",
)

entry(
    index = 13,
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
            NASAPolynomial(coeffs=[  6.94710694E+00, 3.22027910E-02, 4.73703886E-05,
                        -9.73276909E-08, 4.47517084E-11, -2.71645070E+04, -9.05755312E-01], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[   1.59814543E+01, 2.86876258E-02, -1.35657602E-05,
                        3.12593937E-09, -2.84955251E-13,-3.02352969E+04, -5.15549536E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
# deltaH(0) -40.27 kcal/mol
# deltaH(298) -46.53 kcal/mol
CH3CHOCH(OOH)CH3
""",
)

entry(
    index = 14,
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
            NASAPolynomial(coeffs=[7.66261854E+00, 3.10476096E-02, 3.65894729E-05,
                     -7.59820782E-08, 3.41728934E-11, -2.35036884E+04, -2.62337087E+00], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.37406134E+01, 3.22296539E-02, -1.59976596E-05,
                      3.89341097E-09, -3.75502431E-13, -2.57028544E+04, -3.74852137E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
# deltaH(0) -33.00 kcal/mol
# deltaH(298) -39.05 kcal/mol
CH2CH2OCH(OOH)CH3
""",
)

entry(
    index = 15,
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
            NASAPolynomial(coeffs=[4.46846425E+00, 1.31548857E-02, 7.77351941E-05,
                     -1.13874468E-07, 4.71327415E-11, -4.10547173E+04, 7.16173180E+00], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.71606421E+00, 3.76016830E-02, -1.88374665E-05,
                      4.57266173E-09, -4.36124684E-13, -4.24328382E+04, -5.20701034E+00], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
# deltaH(0) -70.36 kcal/mol
# deltaH(298) -76.81 kcal/mol
c-OCH(CH3)OCH(CH3)
""",
)

entry(
    index = 16,
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
            NASAPolynomial(coeffs=[1.00336659E+01, 2.38922280E-02, 9.89414669E-05, 
                     -1.68919876E-07, 7.55016809E-11, -4.03934263E+04, -1.07187914E+01], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.96690533E+01, 3.28299849E-02, -1.69576326E-05,
                      4.35109868E-09, -4.43338505E-13, -4.39933987E+04, -6.70366330E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
# deltaH(0) -64.21 kcal/mol
# deltaH(298) -71.07 kcal/mol
CH3CH2OCH(OO)CH2OOH
""",
)

entry(
    index = 17,
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
            NASAPolynomial(coeffs=[3.02888813E+00, 7.68509013E-02, -2.33893998E-05,
                     -5.00411048E-08, 3.33722383E-11, -4.06018775E+04, 1.78149243E+01], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.10347299E+01, 3.15206789E-02, -1.66467809E-05,
                      4.36172913E-09, -4.48833917E-13, -4.50266418E+04, -7.42851215E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
# deltaH(0) -65.69 kcal/mol
# deltaH(298) -72.68 kcal/mol
CH3CH(OO)OCH2CH2OOH
""",
)

entry(
    index = 18,
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
            NASAPolynomial(coeffs=[3.02888813E+00, 7.68509013E-02, -2.33893998E-05,
                     -5.00411048E-08, 3.33722383E-11, -4.06018775E+04, 1.78149243E+01], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.10347299E+01, 3.15206789E-02, -1.66467809E-05,
                      4.36172913E-09, -4.48833917E-13, -4.50266418E+04, -7.42851215E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
# deltaH(0) -54.93 kcal/mol
# deltaH(298) -108.96 kcal/mol
CH2(OO)CH2OCH2CH2OOH
""",
)

entry(
    index = 19,
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
            NASAPolynomial(coeffs=[7.73170243E+00, 5.02406710E-02, 1.00833672E-05,
                     -6.10352362E-08, 3.18534386E-11, -4.05810056E+04, -1.40166994E+00], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.70498950E+01, 3.63009385E-02, -1.87648661E-05,
                      4.76443078E-09, -4.76455032E-13, -4.32971922E+04, -5.12563635E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
# deltaH(0) -64.92 kcal/mol
# deltaH(298) -71.66 kcal/mol
CH3CH2OCH(OOH)CH2OO
""",
)

entry(
    index = 20,
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
            NASAPolynomial(coeffs=[8.84923940E+00, 2.07212397E-02, 1.19451342E-04,
                      -1.84973047E-07, 7.72261984E-11, -4.63643877E+04,
                      -6.82154680E+00], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.36411945E+01, 3.02220301E-02, -1.64928348E-05,
                      4.34728109E-09, -4.42698715E-13, -5.23883151E+04,
                     -9.42190065E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
# deltaH(0) -76.12 kcal/mol
# deltaH(298) -83.62 kcal/mol
CH3CH(OO)OCH(OOH)CH3
""",
)

entry(
    index = 21,
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
            NASAPolynomial(coeffs=[9.07730933E+00, 1.20414184E-02, 1.51921697E-04,
                     -2.27561632E-07, 9.55777725E-11, -4.14788554E+04, -4.61310284E+00], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.40855466E+01, 2.86122752E-02, -1.51733008E-05,
                      3.92748322E-09, -3.95439409E-13, -4.77518250E+04, -9.44794265E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
# deltaH(0) -66.68 kcal/mol
# deltaH(298) -74.12 kcal/mol
CH2(OO)CH2OCH(OOH)CH3
""",
)

entry(
    index = 22,
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
            NASAPolynomial(coeffs=[7.54412073E+00, 1.09129618E-02, 1.20648839E-04,
                     -1.65850602E-07, 6.46371697E-11, -5.83325864E+04, -1.67463223E+00], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.46068207E+01, 4.32672299E-02, -2.66276096E-05,
                      7.42260827E-09, -7.76559912E-13, -6.27158276E+04, -5.05823836E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
# deltaH(0) -102.27 kcal/mol
# deltaH(298) -108.96 kcal/mol
CH3CH(OOH)OCH2CHO
""",
)

entry(
    index = 23,
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
            NASAPolynomial(coeffs=[7.68823880E+00, 1.18750461E-02, 1.37549806E-04,
                     -2.05698085E-07, 8.58104160E-11, -5.25727404E+04, -1.27278463E+00], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.12690990E+01, 2.80909998E-02, -1.60495451E-05,
                      4.37594620E-09, -4.61077869E-13, -5.83260028E+04, -8.29591249E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
# deltaH(0) -90.93 kcal/mol
# deltaH(298) -97.18 kcal/mol
CH2(OOH)CH2OCH2CHO
""",
)

entry(
    index = 27,
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
            NASAPolynomial(coeffs=[2.01974049E+00, 6.52613710E-02, -2.36224828E-05,
                        -2.85957631E-08, 2.02700652E-11, -7.10242604E+04,
                        1.97597494E+01], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.33354866E+01, 3.78518115E-02, -2.06263385E-05, 5.29581173E-09, -5.23840446E-13, -7.39480540E+04,
                        -3.85938831E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
# deltaH(0) -128.24 kcal/mol
# deltaH(298) -134.69 kcal/mol
CH3CH(OOH)OC(O)CH3
""",
)

entry(
    index = 28,
    label = "bCOC3H7OdOOH",
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
            NASAPolynomial(coeffs=[8.62198556E+00, -6.48003541E-03, 1.64349993E-04,
                     -2.05503171E-07, 7.68906939E-11, -6.82575396E+04, -4.50620394E+00], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.41374718E+01, 4.36472786E-02, -2.65582572E-05,
                      7.44760302E-09, -7.94630416E-13, -7.29012282E+04, -4.88412825E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
# deltaH(0) -121.95 kcal/mol
# deltaH(298) -128.96 kcal/mol
CH2(OOH)CH2OC(O)CH3
""",
)

entry(
    index = 29,
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
            NASAPolynomial(coeffs=[8.59862816E+00, -2.35346530E-03, 1.06815706E-04,
                     -1.36906545E-07, 5.38046132E-11, -4.78741613E+04, -3.28950535E+00], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.82939460E+00, 4.00290186E-02, -2.01561789E-05,
                      4.66753769E-09, -4.10834557E-13, -4.85226390E+04, 3.30564218E+00], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
# deltaH(0) -83.59 kcal/mol
# deltaH(298) -88.86 kcal/mol
CH2(O)CH2OC(O)CH3
""",
)

entry(
    index = 30,
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
            NASAPolynomial(coeffs=[5.03683966E+00, 2.29276333E-02, 4.98735171E-05,
                        -8.26776333E-08, 3.49705243E-11, -5.25519348E+04,
                        9.72011689E+00], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.68769192E+00, 3.76685292E-02, -1.96137988E-05,
                        4.85873166E-09, -4.70272913E-13, -5.42067282E+04,
                        -8.90714877E+00], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
# deltaH(0) -93.28 kcal/mol
# deltaH(298) -98.84 kcal/mol
CH3CH(O)OC(O)CH3
""",
)

entry(
    index = 33,
    label = "aCHOC3H6OdO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,D} {14,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {3,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.25283476E+00, 3.66595154E-02, 5.60215024E-06,
                     -3.67079064E-08, 1.83616926E-11, -3.31429894E+04, 2.43174650E+00], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.17741615E+01, 3.05724274E-02, -1.56903851E-05,
                      3.89070451E-09, -3.78621670E-13, -3.49248502E+04, -2.78226632E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
# deltaH(0) -54.31 kcal/mol
# deltaH(298) -58.95 kcal/mol
CH2(O)CH2OCH2CHO
""",
)

entry(
    index = 34,
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
            NASAPolynomial(coeffs=[2.06037797E+00, 6.05770236E-02, -4.31726247E-05, 
                      6.17146895E-09, 4.57241637E-12, -3.91335225E+04, 1.92110800E+01], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.16161268E+01, 3.06318131E-02, -1.54749225E-05,
                      3.80485782E-09, -3.69213008E-13, -4.13692548E+04, -2.86770573E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
# deltaH(0) -66.84 kcal/mol
# deltaH(298) -71.93 kcal/mol
CH3CH(O)OCH2CHO
""",
)