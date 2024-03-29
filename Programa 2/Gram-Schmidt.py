#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
from scipy import *
from sympy import *

def esBaseR2(v):
    x = Symbol('x')
    y = Symbol('y')
    
    e1v1 = v[0][0]
    e2v1 = v[0][1]    
    e1v2 = v[1][0]
    e2v2 = v[1][1]
    
    print(v)
    sistema = np.array([[e1v1, e1v2], [e2v1, e2v2]])
    print(sistema)
    vector2 = np.array([[0], [0]])
    sol = np.linalg.solve(sistema, vector2)
    print(sol)

def esBaseR3(v):
    x = Symbol('x')
    y = Symbol('y')
    z = Symbol('z')
    
    e1v1 = v[0][0]
    e2v1 = v[0][1]
    e3v1 = v[0][2]
    e1v2 = v[1][0]
    e2v2 = v[1][1]
    e3v2 = v[1][2]
    e1v3 = v[2][0]
    e2v3 = v[2][1]
    e3v3 = v[2][2]
    
    res = solve([e1v1*x + e1v2*y + e1v3*z, e2v1*x + e2v2*y + e2v3*z, e3v1*x + e3v2*y + e3v3*z], [x, y, z])
    print(res)
    print(res[x])
    
    
  #  print(v)
  #  sistema = np.array([[e1v1, e1v2, e1v3], [e2v1, e2v2, e2v3],[e3v1, e3v2, e3v3]])
  #  print("determinante: " ,np.linalg.det(sistema))
  #  print(sistema)
    
   # vector2 = np.array([[0], [0], [0]])
   # sol = np.linalg.solve(sistema, vector2)
   # print(sol)
    
    
    

#-------------------------------------------------------------------------------
def proj(normVector, constVector):
    Vn = array(normVector)
    Vc = array(constVector)
    return ((sum(Vc*Vn)/sum(Vn**2))*Vn)

#-------------------------------------------------------------------------------
def gsn(vL):
    Out = []
    for i in range(len(vL)):
        nowVec = array(vL[i])

        for v in Out :
            nowVec -= proj(v, nowVec)
        nowVec /= sqrt(sum(nowVec*nowVec))

        Out.append(nowVec)
    return Out
#-------------------------------------------------------------------------------

## http://www.scs.ryerson.ca/~danziger/mth141/Handouts/gram.pdf
#test_0 = array([[0., 1.], [1., 1.]])
## http://www.personal.psu.edu/tam44/Math2025/Lecture7.pdf
#test_1 = array([[1., 1.], [2., -1.]])
#
#test0 = array([[1., 1., 0.], [1., 3., 1.], [2.,-1., 1.]])
## http://www.personal.psu.edu/tam44/Math2025/Lecture7.pdf
#test1 = array([[0., 1., 2.], [1., 1., 2.], [1., 0., 1.]])
## http://www.math.ucla.edu/~yanovsky/Teaching/Math151B/handouts/GramSchmidt.pdf
#test2 = array([[1., 1., 0.], [1., 0., 1.], [0., 1., 1.]])
## http://www.scs.ryerson.ca/~danziger/mth141/Handouts/gram.pdf
#test3 = array([[1., 2., 1.],[1., 1., 3.],[2., 1., 1.]])
## https://www.math.hmc.edu/calculus/tutorials/gramschmidt/gramschmidt.pdf
#test4 = array([[1., -1., 1.],[1., 0., 1.],[1., 1., 2.]])
## http://perso.ens-lyon.fr/marco.mazzucchelli/teaching/2011/math220/notes/sec6_4.pdf
#test5 = array([[1., 1., 0.], [2., 2., 3.]])
#
#test6 = array([[1., -1., 1.],[-2., 3., -1.],[1., 2., -4.]])
#print()
#
#print ("----------------------------------------------------------------------")
#print (gsn(test_0))
#print ("----------------------------------------------------------------------")
#print (gsn(test_1))
#print ("----------------------------------------------------------------------")
#print (gsn(test0))
#print ("----------------------------------------------------------------------")
#print (gsn(test1))
#print ("----------------------------------------------------------------------")
#print (gsn(test2))
#print ("----------------------------------------------------------------------")
#print (gsn(test3))
#print ("----------------------------------------------------------------------")
#print (gsn(test4))
#print ("----------------------------------------------------------------------")
#print (gsn(test5))
#print ("----------------------------------------------------------------------")
#print ("----------------------------------------------------------------------")
#print (gsn(test6))
#b = array([[5], [6]])
#A = array([[1, 2], [3, 4]])
#print(linalg.inv(A).dot(b))


#test_0 = np.array([[3, 1], [-2, 4]])
#esBaseR2(test_0)


test_1 = np.array([[1, 1, 0], [0,2,3], [1, 2,3]])
test_2 = np.array([[1,1,3], [3,5,5], [2,1,8]])
test_3 = np.array([[2,3,1], [1,0,1], [0,3,-1]])
test_4 = np.array([[1,-2,3], [2,-2,0], [0,1,7]])


test_5 = np.array([[2,0,0], [0,1,0], [0,0,1]])
test_6 = np.array([[1,1,1], [1,1,0], [1,0,0]])
test_7 = np.array([[504,0,0], [0,7,0], [0,0,1.5]])

test_8 = np.array([[-1,0,2], [0,-4,2], [2,0,-4]])

esBaseR3(test_1)
esBaseR3(test_2)
esBaseR3(test_3)
esBaseR3(test_4)

esBaseR3(test_5)
esBaseR3(test_6)
esBaseR3(test_7)

esBaseR3(test_8)
#
##Se define los valores de la matriz A
#A = array([[1,2,3],[1,2,3],[1,2,3]])
#
##Se definen los valores de la matriz B
#B = array([[0],[0],[0]])
#
##Se calcula el valor de X con X=inv(A)*B
#X = linalg.inv(A).dot(B)
##Se muestra el resultado
#print("El resultado de X es:",X)