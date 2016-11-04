# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 22:33:49 2016

@author: bryan
"""

from numpy import dot, zeros
from numpy.linalg import matrix_rank, norm

def find_li_vectors(dim, R):

    r = matrix_rank(R) 
    index = zeros( r ) #this will save the positions of the li columns in the matrix
    counter = 0
    index[0] = 0 #without loss of generality we pick the first column as linearly independent
    j = 0 #therefore the second index is simply 0

    for i in range(R.shape[0]): #loop over the columns
        if i != j: #if the two columns are not the same
            inner_product = dot( R[:,i], R[:,j] ) #compute the scalar product
            norm_i = norm(R[:,i]) #compute norms
            norm_j = norm(R[:,j])

            #inner product and the product of the norms are equal only if the two vectors are parallel
            #therefore we are looking for the ones which exhibit a difference which is bigger than a threshold
            if absolute(inner_product - norm_j * norm_i) > 1e-4:
                counter += 1 #counter is incremented
                index[counter] = i #index is saved
                j = i #j is refreshed
            #do not forget to refresh j: otherwise you would compute only the vectors li with the first column!!

    R_independent = zeros((r, dim))

    i = 0
    #now save everything in a new matrix
    while( i < r ):
        R_independent[i,:] = R[index[i],:] 
        i += 1

    return R_independent
    