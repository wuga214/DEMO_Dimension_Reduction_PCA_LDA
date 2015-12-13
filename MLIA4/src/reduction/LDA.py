'''
Created on 11-30-2015

@author: Wuga
'''

import numpy as np
import fileoperator
import cluster
import evaluation
import visualization
from visualization.plot2D import plot2D

def LDA(data,num):
    X=data.features
    m,n=X.shape
    Y=data.label
    labels=np.unique(Y)
    mu=np.mean(X, axis=0)
    SB=0
    SW=0
    for i in labels:
        labeli=np.where(Y==i)[0]
        mui=np.mean(X[labeli],axis=0)
        SW+=getSi(mui, X[labeli])
        abst=mu-mui
        SB+=np.dot(abst[:,None],abst[None,:])
    #print SB.shape
    #print SW.shape
    eigvalues,eigvectors = np.linalg.eig(np.dot(np.linalg.pinv(SW),SB/Y.size))
    idx = np.argsort(eigvalues)[::-1]
    V=eigvectors[:,idx]
    eigvalues=eigvalues[idx]
    W= V[:,:num]
    Xtrans=X.dot(W)
    return Xtrans.real
        
def getSi(mu,data):
    Si=0
    for i in data:
        abst=i-mu
        Si+=np.dot(abst[:,None],abst[None,:])
    return Si





        

        
