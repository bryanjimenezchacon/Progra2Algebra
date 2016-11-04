# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 22:31:05 2016

@author: bryan
"""

import numpy as np

matrix = np.array(
    [
        [0, 1 ,0 ,0],
        [0, 0, 1, 0],
        [0, 1, 1, 0],
        [1, 0, 0, 1]
    ])

print (np.linalg.det(matrix))

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[0]):
        if i != j:
            inner_product = np.inner(
                matrix[:,i],
                matrix[:,j]
            )
            norm_i = np.linalg.norm(matrix[:,i])
            norm_j = np.linalg.norm(matrix[:,j])

            print('I: ', matrix[:,i])
            print ('J: ', matrix[:,j])
            print ('Prod: ', inner_product)
            print ('Norm i: ', norm_i)
            print ('Norm j: ', norm_j)
            if np.abs(inner_product - norm_j * norm_i) < 1E-5:
                print ('Dependent')
            else:
                print ('Independent')