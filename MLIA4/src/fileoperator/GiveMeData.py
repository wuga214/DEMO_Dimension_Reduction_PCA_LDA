'''
Created on 11-29-2015

@author: Wuga
'''

import datastruct
import os

def GiveMeData():
    datapath='data\digits79.txt'
    labelpath='data\digitslabels.txt'
    script_dir = os.path.dirname(__file__)
    abs_data_path = os.path.join(script_dir, '..', '..',datapath)
    abs_label_path = os.path.join(script_dir,'..', '..', labelpath)
    data=datastruct.datastruct(abs_data_path,abs_label_path)
    #print 'Number of Data: {0}'.format(data.getSize())
    return data

#GiveMeData()