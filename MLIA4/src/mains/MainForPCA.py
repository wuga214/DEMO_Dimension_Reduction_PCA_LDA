'''
Created on 11-30-2015

@author: Wuga
'''

import fileoperator
import cluster
import evaluation
import reduction


dataset=fileoperator.GiveMeData()
m,n=dataset.features.shape
infosaved=0
iteration=1
purity=0
while infosaved<0.9:
    newdata,infosaved=reduction.PCA(dataset,iteration)
    newdata=newdata.reshape(m,iteration)
    centroids=cluster.Kmeans(newdata, 2)
    labels=cluster.getLabels(newdata, centroids)
    purity=evaluation.Purity(dataset.label,labels,2)
    iteration+=1
print 'Number of Columns:{0}'.format(iteration-1)
print 'Purity of Kmean: {0}'.format(purity)
print 'Information reserved:{0}'.format(infosaved)