'''
Created on 11-30-2015

@author: Wuga
'''
import numpy as np
def Purity(truelabels, predlabels,k):
    summantion=0
    for i in range(k):
        index=np.where(predlabels==i)[0]
        labelinclust=truelabels[index]
        unique, counts = np.unique(labelinclust, return_counts=True)
        #print unique[np.argmax(counts)]
        if np.all(counts==0): return 0
        summantion += np.amax(counts)
    return (1.0/truelabels.size)*summantion