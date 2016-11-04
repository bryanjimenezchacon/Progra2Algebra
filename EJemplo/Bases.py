# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 22:27:17 2016

@author: bryan
"""

import numpy as np

matrix = np.array(
    [
        [1,2,45],
        [1,0,0],
        [1,-1,1]
    ])
    

lambdas, V =  np.linalg.eig(matrix.T)
# The linearly dependent row vectors 
print (matrix[lambdas == 0,:])