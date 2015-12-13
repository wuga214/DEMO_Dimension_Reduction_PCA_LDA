'''
Created on 11-30-2015

@author: Wuga
'''

import fileoperator
import cluster
import evaluation
import reduction

dataset=fileoperator.GiveMeData()
m,_=dataset.features.shape
newdata=reduction.LDA(dataset,1)
#print newdata.shape
newdata=newdata.reshape(m,1)
centroids=cluster.Kmeans(newdata, 2)
labels=cluster.getLabels(newdata, centroids)
purity=evaluation.Purity(dataset.label,labels,2)
print 'Purity of Kmean: {0}'.format(purity)
#visualization.plot2D(newdata,labels)
