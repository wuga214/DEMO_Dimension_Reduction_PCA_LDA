'''
Created on 11-30-2015

@author: Wuga
'''
import numpy as np
import fileoperator
import cluster
import evaluation
import visualization

def PCA(data,num):
    X=data.features
    m,n=X.shape
    mean_X = np.mean(X,axis=0)
    for i in range(m):
        X[i]=X[i]-mean_X
    covar = np.cov(X.T)/(m-1)
    eigvalues,eigvectors = np.linalg.eig(covar)
    idx = np.argsort(eigvalues)[::-1]
    V=eigvectors[:,idx]
    eigvalues=eigvalues[idx]
    W= V[:,:num]
    InfoSaved=np.sum(eigvalues[:num])/np.sum(eigvalues)
    Xtrans=X.dot(W)
    return Xtrans.real,InfoSaved
