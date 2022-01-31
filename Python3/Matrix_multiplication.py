# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 17:22:28 2022

@author: Efe Kurdoğlu
"""


import sympy as sym

theta1, theta2, y1, y2, d1, d2, d3, d4, d5, f1 = sym.symbols('theta1, theta2, y1, y2, d1, d2, d3, d4, d5, f1')


"""
M = M1*M2*M3*M4*M5*M6

Y2 = M*Y1
y2 = theta1*(d1 + d2*(-d1/f1 + 1) + d3*(-d1/f1 + 1) + d4*(-d1/f1 + 1) + d5*(-d1/f1 + 1)) + y1*(-d2/f1 - d3/f1 - d4/f1 - d5/f1 + 1)]
theta2 =  theta1*(-d1/f1 + 1) - y1/f1

"""

M1 = sym.Matrix([[1, d1], [0, 1]])
M2 = sym.Matrix([[1, 0], [-1/f1, 1]])
M3 = sym.Matrix([[1, d2], [0, 1]])
M4 = sym.Matrix([[1, d3], [0, 1]])
M5 = sym.Matrix([[1, d4], [0, 1]])
M6 = sym.Matrix([[1, d5], [0, 1]])

y = sym.Matrix([y2, theta2])
x = sym.Matrix([y1, theta1])

M11 = M2*M1
M22 = M3*M11
M33 = M4*M22
M44 = M5*M33
M = M6*M44

a = M.subs(d1, 1)
n = a.subs(d2, 1)
n = a.subs(d3, 1)
n = a.subs(d4, 1)
n = a.subs(d5, 1)
n = a.subs(f1, 1)
y2 = M*x

m = sym.simplify(n)





