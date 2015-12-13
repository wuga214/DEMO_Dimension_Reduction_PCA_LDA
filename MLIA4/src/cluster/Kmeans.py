'''
Created on 11-29-2015

@author: Wuga
'''
import numpy as np
import similarity
import sys

def Kmeans(data, k):
    
    # Initialize 
    _,numOfFeatures = data.shape
    centroids = getInitCentroids(numOfFeatures,k)
    
    # Intermediate results
    iterations = 0
    oldCentroids = None
    
    while not stopCondition(oldCentroids, centroids, iterations):
        oldCentroids = centroids
        iterations += 1
        labels = getLabels(data, centroids)
        centroids = getCentroids(data, labels, k)
    return centroids       

             
    
def getInitCentroids(numOfFeatures, k):
    return np.random.randint(256, size=(k, numOfFeatures))-128

def getCentroids(data, labels, k):
    centroids=None
    _,numOfFeatures = data.shape
    for i in range(k):
        incluster=np.where(labels == i)[0]
        if incluster.size == 0:
            newCentroid=np.random.randint(256, size=(1, numOfFeatures))-128
        else:
            newCentroid=np.mean(data[incluster], axis=0)
        if np.any(np.equal(centroids, None)):
            centroids=newCentroid
        else:        
            centroids=np.vstack((centroids, newCentroid))

    return centroids

def stopCondition(oldCentroids, centroids, iterations):
    # Constant    
    MAX_ITERATIONS = 100 
    if iterations > MAX_ITERATIONS: return True
    #print iterations
    return  np.all(np.equal(oldCentroids, centroids))

def getLabels(data, centroids):
    m,_ = data.shape
    labels=np.arange(m)
    for idxdata, valdata in enumerate(data):
        centroid=0
        MIN_VALUE=sys.float_info.max
        for idxcent, valcent in enumerate(centroids):
            if similarity.euclidean(valcent,valdata)<MIN_VALUE:
                MIN_VALUE=similarity.euclidean(valcent,valdata)
                centroid=idxcent
        np.put(labels, idxdata, centroid)
    return labels
              

    
    
        