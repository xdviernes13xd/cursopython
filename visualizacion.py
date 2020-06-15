# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 21:10:55 2020

@author: trabajo
"""


import numpy as np
a=[456,864,456,5324,32665]
b=[635,584,284,433646,43663]
c=[254,575,595,34363,365316]
d=[53342,563454,24535,524,1344513]
e=[5235,56456,24624,45745,56256]
r=np.array([a,b,c,d])
seasons=[2000,2001,2002,2003,2004]
jugadores=["Jorge","Ramón","Paco","Suaña","López"]
jugdic={"Jorge":0,"Ramón":1,"Paco":2,"Suaña":3,"López":4}
import matplotlib.pyplot as plt
'''plt.plot(r[0],color="blue",ls="--",marker="s",ms="5",label=jugadores[0])
plt.plot(r[1],color="green",ls="--",marker="o",ms="5",label=jugadores[1])
plt.plot(r[2],color="brown",ls="--",marker="s",ms="5",label=jugadores[2])
plt.plot(r[-1],color="red",ls="--",marker="s",ms="5",label=jugadores[-1])
plt.legend(loc='upper left',bbox_to_anchor=(2,3))
plt.xticks(list(range(0,10)),seasons,rotation='horizontal')
plt.show()'''

import warnings
warnings.filterwarnings('ignore')
def myplot(data,playerlist):
    col={"Jorge":"black","Ramón":"green","Paco":"purple","Suaña":"pink","López":"red"}
    mrk={"Jorge":"s","Ramón":"o","Paco":"^","Suaña":"D","López":"s"}
    for name in playerlist:
        plt.plot(data[jugdic[name]],color=col[name],ls="--",marker=mrk[name],ms="5",label=jugadores[jugdic[name]])
    plt.legend()
    plt.xticks(list(range(0,10)),seasons,rotation='horizontal')
    plt.show()
myplot(r,["Jorge","Ramón","López"])