'''
Created on 11-29-2015

@author: Wuga
'''
import numpy as np

def euclidean(x1,x2):
    x=x1-x2;
    sim=np.sqrt(np.sum(np.power(x,2)))
    return sim

# x1=np.array([-1,2,3,4])
# x2=np.array([2,3,4,5])
# sim=euclidean(x1, x2)
# print sim