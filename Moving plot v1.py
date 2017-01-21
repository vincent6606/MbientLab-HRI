# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 22:40:16 2016

@author: zhiting6606
"""

import pyqtgraph as pg
import numpy as np
import pandas as pd
plt = pg.plot(title="Acceleration vs Time")
pg.setConfigOption('background', 'w')

curve = plt.plot()
#line = plt.addLine(x=0)

graph_data = pd.read_csv('vab.csv',header = None)
graph_data = graph_data.as_matrix()
size = 150
data1 = graph_data[1:size,1]
time = graph_data[1:size,0]
plt.setRange(yRange=[0, 5.5])
curve = plt.plot(pen=(255,0,0),penSize=10)

i = 0
ptr1 = 0


def update():
    global data1, curve, ptr1,i,time
    data1[:-1] = data1[1:]  # shift data in the array one sample left
                            # (see also: np.roll)
    data1[-1] = graph_data[size+i,1]
    
    time[:-1] = time[1:]
    time[-1] = graph_data[size+i,0]
    
    
    
    i +=1
    ptr1 += 1
    curve.setData(x = time,y=data1)
    #curve.setPos(ptr1, 0) #This sets the viewing window, remove this if the window is determined by timestamps
    print time[1:size+i]
    

timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(20)
