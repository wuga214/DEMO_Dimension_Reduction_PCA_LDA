'''
Created on 11-29-2015

@author: Wuga
'''

import numpy as np

class datastruct:
    def __init__(self, datapath,labelpath):
        self.features=np.loadtxt(datapath,delimiter=',',unpack=False)
        self.label=np.loadtxt(labelpath,delimiter=',',unpack=False)
    
    def getSize(self):
        m,_=self.features.shape
        return m
    
    def getDimension(self):
        _,n=self.features.shape
        return n