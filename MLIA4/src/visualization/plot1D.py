'''
Created on 12-4-2015

@author: Wuga
'''
import matplotlib.pyplot as plt
def plot1D(X,Y1,Y2,Name):
    plt.figure(figsize=(14,6))

    ax = plt.subplot(121)
    for label,color,name in zip(
        range(0,2),('red', 'green'),('Cluster1','Cluster2')):
        plt.hist(x=X[:,0][Y1 == label],bins=20,color=color,label=name)
    plt.legend(loc='upper right', fancybox=True)
    plt.xlabel(Name+'1')
    plt.title('1D plot of dimension reduced data')

    # hide axis ticks
    plt.tick_params(axis="both", which="both", bottom="off", top="off",
            labelbottom="on", left="off", right="off", labelleft="on")

    # remove axis spines
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)

    plt.grid()
    
    ax = plt.subplot(122)
    for label,color,name in zip(
        [7,9],('steelblue', 'orangered'),('Class7','Class9')):
        plt.hist(x=X[:,0][Y2 == label],bins=20,color=color,label=name)
    plt.legend(loc='upper right', fancybox=True)
    plt.xlabel(Name+'1')
    plt.title('1D plot of dimension reduced data')

    # hide axis ticks
    plt.tick_params(axis="both", which="both", bottom="off", top="off",
            labelbottom="on", left="off", right="off", labelleft="on")

    # remove axis spines
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)

    plt.grid()
    plt.tight_layout
    plt.savefig('../../data/plot1d_'+Name+'.png')