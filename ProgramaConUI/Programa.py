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
##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""  
  #Para Programa 1
  self.pushButtonCalcularTrans.clicked.connect(self.calcTransicion)
  
##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""  
  #Para Programa 2
  self.pushButtonCalcularR2P2.clicked.connect(self.calcOrtonormalR2)
  self.pushButtonCalcularR3P2.clicked.connect(self.calcOrtonormalR3)
  
 def calcTransicion(self):#Paraq programa 1
    try:
        vectorA1R3 = self.tableWidgetBasesP1.item(0,0).text()
        vectorA2R3 = self.tableWidgetBasesP1.item(0,1).text()
        vectorA3R3 = self.tableWidgetBasesP1.item(0,2).text()
       
        vectorB1R3 = self.tableWidgetBasesP1.item(1,0).text()
        vectorB2R3 = self.tableWidgetBasesP1.item(1,1).text()
        vectorB3R3 = self.tableWidgetBasesP1.item(1,2).text()
        
        E1U = self.tableWidgetVectorP1.item(0,0).text()
        E2U = self.tableWidgetVectorP1.item(0,1).text()
        E3U = self.tableWidgetVectorP1.item(0,2).text()
        
        vA1 = vectorA1R3.split(",")
        vA2 = vectorA2R3.split(",")
        vA3 = vectorA3R3.split(",")
        
        vB1 = vectorB1R3.split(",")
        vB2 = vectorB2R3.split(",")
        vB3 = vectorB3R3.split(",")
        
        vU1 = E1U.split(",")
        vU2 = E2U.split(",")
        vU3 = E3U.split(",")    
    
        baseATemp = np.array([vA1, vA2, vA3])
        baseBTemp = np.array([vB1, vB2, vB3])
        vectorU = np.array([vU1, vU2, vU3])
        
        baseA = baseATemp.astype(np.float)
        baseB = baseBTemp.astype(np.float)
        U = vectorU.astype(np.float)
    except:
        self.labelTransisiones.setText("Todos los valores deben ser numéricos :(") 
        self.labelTransisiones2.setText("")  
        
    try:
        if (esBaseR3(baseA) and esBaseR3(baseB)):
            print("soy base")
            mTransicionA = transicion(baseA, baseB)
            mTransicionB = transicion(baseB, baseA)
            print("Matrices de transicion")
            print(mTransicionA)
            print(mTransicionB)
            print("Bases como matrices")
            print(baseA)
            print(baseB)
            self.labelTransisiones.setText(respuestaTransP1(mTransicionA))
            self.labelTransisiones2.setText(respuestaTransP1(mTransicionB))
            print("Combinacion lineal")
            ##Combinacion lineal
            self.labelCombinaciones2.setText(respuestaComb(mTransicionA.dot(U), baseB))
            self.labelCombinaciones.setText(respuestaComb(mTransicionB.dot(mTransicionA.dot(U)), baseA))
            combinacionLineal(mTransicionA, mTransicionB, U)

            
        else:
            self.labelTransisiones.setText("No son Base, hay dependencia :(")
            self.labelTransisiones.setText("")
            print("Nope, no base here")
    except:
        self.labelTransisiones.setText("Los valores deben ser numéricos :/") 
        self.labelTransisiones2.setText("") 
     
 def calcOrtonormalR2(self):#Para el programa 2
 #Obtiene los vectores
  try:
      vector1R2 = self.tableWidgetBaseR2P2.item(0,0).text()
      vector2R2 = self.tableWidgetBaseR2P2.item(0,1).text()
      
      v1 = vector1R2.split(",")
      v2 = vector2R2.split(",")
      vectores = np.array([v1, v2])
  except:
    self.labelR2Ortonormal.setText("Todos los valores deben ser numéricos :(")  
  #try:
  if (esBaseR2(vectores)):
      print("soy base")
      vectoresFloatR2 = vectores.astype(np.float)
      print(gs(vectoresFloatR2))
      self.labelR2Ortonormal.setText(respuestaP2(gs(vectoresFloatR2)))
  else:
      self.labelR2Ortonormal.setText("No es Base, hay dependencia :(")
      print("Nope, no base here")
  #except:
   #   self.labelR2Ortonormal.setText("Los valores deben ser numéricos :/")  

 def calcOrtonormalR3(self):#Para el programa 2
 #Obtiene los vectores
  try:
      vector1R3 = self.tableWidgetBaseR3P2.item(0,0).text()
      vector2R3 = self.tableWidgetBaseR3P2.item(0,1).text()
      vector3R3 = self.tableWidgetBaseR3P2.item(0,2).text()
      
      v1 = vector1R3.split(",")
      v2 = vector2R3.split(",")
      v3 = vector3R3.split(",")
      vectores = np.array([v1, v2, v3])
  except:
    self.labelR3Ortonormal.setText("Todos los valores deben ser numéricos :(") 
  try:
      if (esBaseR3(vectores)):
          print("soy base")
          vectoresFloatR3 = vectores.astype(np.float)
          print(gs(vectoresFloatR3))
          self.labelR3Ortonormal.setText(respuestaP2(gs(vectoresFloatR3)))
      else:
          self.labelR3Ortonormal.setText("No es Base, hay dependencia :(")
          print("Nope, no base here")
  except:
      self.labelR3Ortonormal.setText("Los valores deben ser numéricos :/")

##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
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
 ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""   

##"""""""""""""""""""""""Para Programa 1"""""""""""""""""""""""""""""""""""""""
#-------------------------------------------------------------------------------
def transicion(A, B):

    BT = B.T
    BInversa = np.linalg.inv(BT)   
    AT = A.T 
    resultado = BInversa.dot(AT)
    return resultado
#-------------------------------------------------------------------------------    
def respuestaTransP1(A):
    respuesta = ""
    for i in range(len(A)):
        respuesta += str(A[i])
        respuesta += "\n"

    return respuesta
#-------------------------------------------------------------------------------    
def respuestaComb(A, base):
    respuesta = ""
    for i in range(len(A)):
        respuesta += str(A[i][0])
        respuesta += "("
        for j in range(len(base[i])):
            
            respuesta += str(base[i][j])
            if (j != (len(base[i])-1)):  
                respuesta += ","
                
        respuesta += ")"
        respuesta += "   "
        
    return respuesta
#-------------------------------------------------------------------------------       
def combinacionLineal(MTA, MTB, U):
    print(MTA.dot(U))
    print(MTB.dot(MTA.dot(U)))
    
    
##"""""""""""""""""""""""FIN Programa 1"""""""""""""""""""""""""""""""""""""""
#-------------------------------------------------------------------------------

##"""""""""""""""""""""""Para Programa 2"""""""""""""""""""""""""""""""""""""""
#-------------------------------------------------------------------------------
def aux(V1, V2):
    Vn = array(V1)
    Vc = array(V2)
    return ((sum(Vc*Vn)/sum(Vn**2))*Vn)

#-------------------------------------------------------------------------------
def gs(vectores):
    resGS = []
    print(vectores)
    for i in range(len(vectores)):
        vectActual = array(vectores[i])
        for v in resGS :
            vectActual -= aux(v, vectActual)
        vectActual /= sqrt(sum(vectActual*vectActual))

        resGS.append(vectActual)
    return resGS
#-------------------------------------------------------------------------------
def respuestaP2(sol):
    respuesta = "{ "
    for i in range(len(sol)):
        respuesta += "("
        for j in range(len(sol[i])):
            respuesta += str(sol[i][j])
            if (j != (len(sol[i])-1)):
                respuesta += ",  "
            print(sol[i][j])
        if(i != (len(sol)-1)):
            respuesta += "), "
        else:
            respuesta += ") "
    respuesta += " }"
    
    return respuesta
    
    
##"""""""""""""""""""""""FIN Programa 2"""""""""""""""""""""""""""""""""""""""
#-------------------------------------------------------------------------------
## MAIN ##
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MyWindow = Principal(None)
    MyWindow.show()
    app.exec_()
