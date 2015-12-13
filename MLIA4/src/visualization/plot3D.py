'''
Created on 12-4-2015

@author: Wuga
'''

import matplotlib.pyplot as plt
def plot3D(X,Y1,Y2,Name):
    plt.figure(figsize=(14,6))

    ax = plt.subplot(121,projection='3d')
    for label,marker,color in zip(
        range(0,2),('s', 'o'),('red', 'green')):

        ax.scatter(X[:,0][Y1 == label],
                X[:,1][Y1 == label],
                X[:,2][Y1 == label],
                marker=marker,
                color=color,
                alpha=0.5,
                label='Cluster:{0}'.format(label)
                )

    ax.set_xlabel(Name+'1')
    ax.set_ylabel(Name+'2')
    ax.set_zlabel(Name+'3')
    leg = ax.legend(loc='upper right', fancybox=True)
    leg.get_frame().set_alpha(0.5)
    plt.title('3D plot of dimension reduced data')

    # hide axis ticks
    plt.tick_params(axis="both", which="both", bottom="off", top="off",
            labelbottom="on", left="off", right="off", labelleft="on")

    # remove axis spines
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)

    plt.grid()
    
    ax = plt.subplot(122,projection='3d')
    for label,marker,color in zip(
        [7,9],('s', 'o'),('steelblue', 'orangered')):

        ax.scatter(X[:,0][Y2 == label],
                X[:,1][Y2 == label],
                X[:,2][Y2 == label],
                marker=marker,
                color=color,
                alpha=0.5,
                label='Class:{0}'.format(label)
                )

    ax.set_xlabel(Name+'1')
    ax.set_ylabel(Name+'2')
    ax.set_zlabel(Name+'3')
    leg = ax.legend(loc='upper right', fancybox=True)
    leg.get_frame().set_alpha(0.5)
    plt.title('3D plot of dimension reduced data')

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
    plt.savefig('../../data/plot3d_'+Name+'.png')
