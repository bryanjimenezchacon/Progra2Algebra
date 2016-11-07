#!/usr/bin/python3
# -*- coding: utf-8 -*-


import numpy as np
from scipy import *
from sympy import *
import sys
from PyQt4 import QtCore, QtGui, uic
from itertools import *
import copy

#import InterfazMenu
# Cargar nuestro archivo .ui
form_class = uic.loadUiType("InterfazMenu.ui")[0]

class Principal(QtGui.QMainWindow, form_class):
 def __init__(self, parent=None):
  QtGui.QMainWindow.__init__(self, parent)
  self.setupUi(self)
  
  #Para Programa 1
  
  #Para Programa 2
  self.pushButtonCalcularR2P2.clicked.connect(self.calcOrtonormalR2)
  self.pushButtonCalcularR3P2.clicked.connect(self.calcOrtonormalR3)

 def calcOrtonormalR2(self):#Para el programa 2
 #Obtiene los vectores
  vector1R2 = self.tableWidgetBaseR2P2.item(0,0).text()
  vector2R2 = self.tableWidgetBaseR2P2.item(0,1).text()
  
  v1 = vector1R2.split(",")
  v2 = vector2R2.split(",")
  vectores = np.array([v1, v2])
  
  if (esBaseR2(vectores)):
      print("soy base")
  else:
      print("Nope, no base here")

 def calcOrtonormalR3(self):#Para el programa 2
 #Obtiene los vectores
  vector1R3 = self.tableWidgetBaseR3P2.item(0,0).text()
  vector2R3 = self.tableWidgetBaseR3P2.item(0,1).text()
  vector3R3 = self.tableWidgetBaseR3P2.item(0,2).text()
  
  v1 = vector1R3.split(",")
  v2 = vector2R3.split(",")
  v3 = vector3R3.split(",")
  vectores = np.array([v1, v2, v3])
  
  if (esBaseR3(vectores)):
      print("soy base")
  else:
      print("Nope, no base here")


##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def esBaseR2(v):
    print(v)
    x = Symbol('x')
    y = Symbol('y')
    
    e1v1 = v[0][0]
    e2v1 = v[0][1]
    e1v2 = v[1][0]
    e2v2 = v[1][1]
    
    sistema = solve([float(e1v1)*x +float(e1v2)*y,float(e2v1)*x + float(e2v2)*y], [x, y])
    print(sistema)
    
    if len(sistema) < 2:
        return False
    else:
        valorX = sistema[x]
        valorY = sistema[y]
    
        if (int(valorX) == int(valorY) == 0):
            return True
        else:
            return False


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
    
    sistema = solve([float(e1v1)*x + float(e1v2)*y + float(e1v3)*z, float(e2v1)*x + float(e2v2)*y + float(e2v3)*z, float(e3v1)*x + float(e3v2)*y + float(e3v3)*z], [x, y, z])   
    print(sistema)
    
    if len(sistema) < 3:
        return False
    else:
        valorX = sistema[x]
        valorY = sistema[y]
        valorZ = sistema[z]
    
        if (int(valorX) == int(valorY) == int(valorZ) == 0):
            return True
        else:
            return False
 ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""   
    

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


#test_1 = np.array([[1, 1, 0], [0,2,3], [1, 2,3]])
#test_2 = np.array([[1,1,3], [3,5,5], [2,1,8]])
#test_3 = np.array([[2,3,1], [1,0,1], [0,3,-1]])
#test_4 = np.array([[1,-2,3], [2,-2,0], [0,1,7]])
#
#
#test_5 = np.array([[2,0,0], [0,1,0], [0,0,1]])
#test_6 = np.array([[1,1,1], [1,1,0], [1,0,0]])
#test_7 = np.array([[504,0,0], [0,7,0], [0,0,1.5]])
#
#test_8 = np.array([[-1,0,2], [0,-4,2], [2,0,-4]])
#
#esBaseR3(test_1)
#esBaseR3(test_2)
#esBaseR3(test_3)
#esBaseR3(test_4)
#
#esBaseR3(test_5)
#esBaseR3(test_6)
#esBaseR3(test_7)
#
#esBaseR3(test_8)
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


## MAIN ##
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MyWindow = Principal(None)
    MyWindow.show()
    app.exec_()