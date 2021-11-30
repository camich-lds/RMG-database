#!/usr/bin/env python
# encoding: utf-8

name = "CO_Disproportionation/groups"
shortDesc = ""
longDesc = """
This family describes reactions of the sort:
Y_rad + [CH]=O <=> Y_H + [C-]#[O+]

atom labels:

  R_rad   +        [CH]=O        <=>     RH     +    [C-]#[O+]

R_rad(*1) + H(*4)C_rad(*3)=O(*2) <=> R(*1)H(*4) + [C-](*3)#[O+](*2)
"""

template(reactants=["Root"], products=["Y_H", "CO_CS"], ownReverse=False)

reverse = "CO_Addition"
reversible = True

reactantNum = 2
productNum = 2

autoGenerated = True

recipe(actions=[
    ['FORM_BOND', '*1', 1, '*4'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['LOSE_PAIR', '*2', '1'],
    ['GAIN_PAIR', '*3', '1'],
    ['CHANGE_BOND', '*2', 1, '*3'],
    ['LOSE_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 0,
    label = "Root",
    group = 
"""
1 *3 C       u1         p0 c0 {2,S} {3,D}
2 *4 H       u0         p0 c0 {1,S}
3 *2 [O,S2d] u0         p2 c0 {1,D}
4 *1 R       u[1,2,3,4]
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "Root_4R->N",
    group = 
"""
1 *3 C u1         p0 c0 r0 {2,S} {3,D}
2 *4 H u0         p0 c0 r0 {1,S}
3 *2 O u0         p2 c0 r0 {1,D}
4 *1 N u[1,2,3,4] r0
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "Root_N-4R->N",
    group = 
"""
1 *3 C                        u1         p0 c0 {2,S} {3,D}
2 *4 H                        u0         p0 c0 {1,S}
3 *2 O                        u0         p2 c0 {1,D}
4 *1 [S,C,P,Si,F,H,I,Br,Cl,O] u[1,2,3,4]
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "Root_N-4R->N_4BrCClFHIOPSSi->H",
    group = 
"""
1 *3 C u1         p0 c0 {2,S} {3,D}
2 *4 H u0         p0 c0 {1,S}
3 *2 O u0         p2 c0 {1,D}
4 *1 H u[1,2,3,4]
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H",
    group = 
"""
1 *3 C     u1         p0 c0 {2,S} {3,D}
2 *4 H     u0         p0 c0 {1,S}
3 *2 O     u0         p2 c0 {1,D}
4 *1 [C,O] u[1,2,3,4]
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R",
    group = 
"""
1 *3 C     u1         p0 c0 {2,S} {3,D}
2 *4 H     u0         p0 c0 {1,S}
3 *2 O     u0         p2 c0 {1,D}
4 *1 [C,O] u[1,2,3,4] {5,[S,D,T,B]}
5    R!H   ux         {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C",
    group = 
"""
1 *3 C     u1         p0 c0 {2,S} {3,D}
2 *4 H     u0         p0 c0 {1,S}
3 *2 O     u0         p2 c0 {1,D}
4 *1 [C,O] u[1,2,3,4] {5,[S,D,T,B]}
5    C     ux         {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Ext-4CO-R",
    group = 
"""
1 *3 C     u1         p0 c0 r0 {2,S} {3,D}
2 *4 H     u0         p0 c0 r0 {1,S}
3 *2 O     u0         p2 c0 r0 {1,D}
4 *1 [C,O] u[1,2,3,4] r0 {5,[S,D,T,B]} {6,[S,D,T,B]}
5    C     u0         {4,[S,D,T,B]}
6    R!H   ux         {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO",
    group = 
"""
1 *3 C     u1         p0 c0 {2,S} {3,D}
2 *4 H     u0         p0 c0 {1,S}
3 *2 O     u0         p2 c0 {1,D}
4 *1 [C,O] u[1,2,3,4] {5,S}
5    C     ux         {4,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->C",
    group = 
"""
1 *3 C u1         p0 c0 {2,S} {3,D}
2 *4 H u0         p0 c0 {1,S}
3 *2 O u0         p2 c0 {1,D}
4 *1 C u[1,2,3,4] {5,S}
5    C ux         {4,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->C_Ext-5C-R",
    group = 
"""
1 *3 C   u1         p0 c0 {2,S} {3,D}
2 *4 H   u0         p0 c0 {1,S}
3 *2 O   u0         p2 c0 {1,D}
4 *1 C   u[1,2,3,4] {5,S}
5    C   ux         {4,S} {6,[S,D,T,B]}
6    R!H ux         {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_N-4CO->C",
    group = 
"""
1 *3 C u1 p0 c0 r0 {2,S} {3,D}
2 *4 H u0 p0 c0 r0 {1,S}
3 *2 O u0 p2 c0 r0 {1,D}
4 *1 O u1 r0 {5,S}
5    C u0 r0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_N-Sp-5C-4CO",
    group = 
"""
1 *3 C     u1         p0 c0 {2,S} {3,D}
2 *4 H     u0         p0 c0 {1,S}
3 *2 O     u0         p2 c0 {1,D}
4 *1 [C,O] u[1,2,3,4] {5,D}
5    C     ux         {4,D}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C",
    group = 
"""
1 *3 C                      u1         p0 c0 {2,S} {3,D}
2 *4 H                      u0         p0 c0 {1,S}
3 *2 O                      u0         p2 c0 {1,D}
4 *1 [C,O]                  u[1,2,3,4] {5,[S,D,T,B]}
5    [S,N,P,Si,F,I,Br,Cl,O] ux         {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->N",
    group = 
"""
1 *3 C     u1         p0 c0 r0 {2,S} {3,D}
2 *4 H     u0         p0 c0 r0 {1,S}
3 *2 O     u0         p2 c0 r0 {1,D}
4 *1 [C,O] u[1,2,3,4] r0 {5,[S,D,T,B]}
5    N     ux         {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N",
    group = 
"""
1 *3 C     u1         p0 c0 {2,S} {3,D}
2 *4 H     u0         p0 c0 {1,S}
3 *2 O     u0         p2 c0 {1,D}
4 *1 [C,O] u[1,2,3,4] {5,[S,D,T,B]}
5    O     ux         {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_4CO->C",
    group = 
"""
1 *3 C u1         p0 c0 {2,S} {3,D}
2 *4 H u0         p0 c0 {1,S}
3 *2 O u0         p2 c0 {1,D}
4 *1 C u[1,2,3,4] {5,[S,D,T,B]}
5    O u0         {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_4CO->C_Sp-5O-4C",
    group = 
"""
1 *3 C u1         p0 c0 r0 {2,S} {3,D}
2 *4 H u0         p0 c0 r0 {1,S}
3 *2 O u0         p2 c0 r0 {1,D}
4 *1 C u[1,2,3,4] r0 {5,S}
5    O u0         {4,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_4CO->C_N-Sp-5O-4C",
    group = 
"""
1 *3 C u1         p0 c0 r0 {2,S} {3,D}
2 *4 H u0         p0 c0 r0 {1,S}
3 *2 O u0         p2 c0 r0 {1,D}
4 *1 C u[1,2,3,4] r0 {5,D}
5    O u0         {4,D}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_N-4CO->C",
    group = 
"""
1 *3 C u1 p0 c0 {2,S} {3,D}
2 *4 H u0 p0 c0 {1,S}
3 *2 O u0 p2 c0 {1,D}
4 *1 O u1 {5,[S,D,T,B]}
5    O ux r0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_4CO->C",
    group = 
"""
1 *3 C u1         p0 c0 {2,S} {3,D}
2 *4 H u0         p0 c0 {1,S}
3 *2 O u0         p2 c0 {1,D}
4 *1 C u[1,2,3,4]
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_N-4CO->C",
    group = 
"""
1 *3 C u1         p0 c0 {2,S} {3,D}
2 *4 H u0         p0 c0 {1,S}
3 *2 O u0         p2 c0 {1,D}
4 *1 O u[1,2,3,4]
""",
    kinetics = None,
)

tree(
"""
L1: Root
    L2: Root_4R->N
    L2: Root_N-4R->N
        L3: Root_N-4R->N_4BrCClFHIOPSSi->H
        L3: Root_N-4R->N_N-4BrCClFHIOPSSi->H
            L4: Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R
                L5: Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C
                    L6: Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Ext-4CO-R
                    L6: Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO
                        L7: Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->C
                            L8: Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->C_Ext-5C-R
                        L7: Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_N-4CO->C
                    L6: Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_N-Sp-5C-4CO
                L5: Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C
                    L6: Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->N
                    L6: Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N
                        L7: Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_4CO->C
                            L8: Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_4CO->C_Sp-5O-4C
                            L8: Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_4CO->C_N-Sp-5O-4C
                        L7: Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_N-4CO->C
            L4: Root_N-4R->N_N-4BrCClFHIOPSSi->H_4CO->C
            L4: Root_N-4R->N_N-4BrCClFHIOPSSi->H_N-4CO->C
"""
)

forbidden(
    label = "O2d",
    group = 
"""
1 *2 O u0 {2,D}
2 *3 O u0 {1,D}
""",
    shortDesc = """""",
    longDesc = 
"""

""",
)

forbidden(
    label = "OS_XH_birad_singlet",
    group = 
"""
1 *3 [O,S] u0 p3 {2,[S,D,T]}
2 *2 R!H   ux {1,[S,D,T]} {3,S}
3 *4 H     u0 {2,S}
""",
    shortDesc = """""",
    longDesc = 
"""

""",
)

forbidden(
    label = "O_Orad",
    group = 
"""
1 *2 O u0 {2,S} {3,S}
2 *3 O u1 {1,S}
3 *4 H u0 {1,S}
""",
    shortDesc = """""",
    longDesc = 
"""

""",
)

forbidden(
    label = "XH_N_birad_singlet",
    group = 
"""
1 *3 N   u0 p2 {2,[S,D]}
2 *2 R!H ux {1,[S,D]} {3,S}
3 *4 H   u0 {2,S}
""",
    shortDesc = """""",
    longDesc = 
"""

""",
)

forbidden(
    label = "XH_birad_singlet",
    group = 
"""
1 *3 [C,Si] u0 p1 {2,[S,D,T]}
2 *2 R!H    ux {1,[S,D,T]} {3,S}
3 *4 H      u0 {2,S}
""",
    shortDesc = """""",
    longDesc = 
"""

""",
)

forbidden(
    label = "XH_quadrad_singlet",
    group = 
"""
1 *3 [C,Si] u0 p2 {2,[S,D,T]}
2 *2 R!H    ux {1,[S,D,T]} {3,S}
3 *4 H      u0 {2,S}
""",
    shortDesc = """""",
    longDesc = 
"""

""",
)

