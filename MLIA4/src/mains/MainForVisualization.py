'''
Created on 11-30-2015

@author: Wuga
'''
import fileoperator
import cluster
import evaluation
import visualization
import reduction
from mpl_toolkits.mplot3d import axes3d

#
#One dimensional visualization
#
dataset=fileoperator.GiveMeData()
m,_=dataset.features.shape
newdata=reduction.LDA(dataset,1)
newdata=newdata.reshape(m,1)
centroids=cluster.Kmeans(newdata, 2)
labels=cluster.getLabels(newdata, centroids)
purity=evaluation.Purity(dataset.label,labels,2)
print 'Purity of Kmean: {0}'.format(purity)
visualization.plot1D(newdata,labels,dataset.label,'LDA')
  
dataset=fileoperator.GiveMeData()
m,_=dataset.features.shape
newdata,_=reduction.PCA(dataset,1)
newdata=newdata.reshape(m,1)
labels=cluster.getLabels(newdata, centroids) 
purity=evaluation.Purity(dataset.label,labels,2)
print 'Purity of Kmean: {0}'.format(purity)
visualization.plot1D(newdata,labels,dataset.label,'PCA')
 
#
#Two dimensional visualization
#
 
dataset=fileoperator.GiveMeData()
m,_=dataset.features.shape
newdata=reduction.LDA(dataset,2)
newdata=newdata.reshape(m,2)
centroids=cluster.Kmeans(newdata, 2)
labels=cluster.getLabels(newdata, centroids)
purity=evaluation.Purity(dataset.label,labels,2)
print 'Purity of Kmean: {0}'.format(purity)
visualization.plot2D(newdata,labels,dataset.label,'LDA')
 
dataset=fileoperator.GiveMeData()
m,_=dataset.features.shape
newdata,_=reduction.PCA(dataset,2)
newdata=newdata.reshape(m,2)
centroids=cluster.Kmeans(newdata, 2)
labels=cluster.getLabels(newdata, centroids)
purity=evaluation.Purity(dataset.label,labels,2)
print 'Purity of Kmean: {0}'.format(purity)
visualization.plot2D(newdata,labels,dataset.label,'PCA')

#
#Three dimensional visualization
#
 
dataset=fileoperator.GiveMeData()
m,_=dataset.features.shape
newdata=reduction.LDA(dataset,3)
newdata=newdata.reshape(m,3)
centroids=cluster.Kmeans(newdata, 2)
labels=cluster.getLabels(newdata, centroids)
purity=evaluation.Purity(dataset.label,labels,2)
print 'Purity of Kmean: {0}'.format(purity)
visualization.plot3D(newdata,labels,dataset.label,'LDA')
 
dataset=fileoperator.GiveMeData()
m,_=dataset.features.shape
newdata,_=reduction.PCA(dataset,3)
newdata=newdata.reshape(m,3)
centroids=cluster.Kmeans(newdata, 2)
labels=cluster.getLabels(newdata, centroids)
purity=evaluation.Purity(dataset.label,labels,2)
print 'Purity of Kmean: {0}'.format(purity)
visualization.plot3D(newdata,labels,dataset.label,'PCA')