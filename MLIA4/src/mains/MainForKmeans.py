'''
Created on 11-30-2015

@author: Wuga
'''

import numpy as np
import fileoperator
import similarity
import sys
import evaluation
import cluster

dataset=fileoperator.GiveMeData()
avepurity=[]
SSE=[]
for i in range(10):
    centroids=cluster.Kmeans(dataset.features, 2)
    labels=cluster.getLabels(dataset.features, centroids)  
    avepurity.append(evaluation.Purity(dataset.label,labels,2))
    SSE.append(sum((dataset.label-labels)**2))
index=np.asarray(SSE).argsort()
print 'Best Sum Square Error:{0}'.format(SSE[index[0]])
print 'Best Purity of Kmean with 10 iterations: {0}'.format(avepurity[index[0]])
