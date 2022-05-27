# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 14:23:09 2022

@author: User
"""

import numpy as np
from Numerical_test import FileManage,Funcs,Error_mit,Backends,Results,Plots,Numerical,Observables 
import matplotlib.pyplot as plt 

def min_index(array, val):
     idx = (np.abs(array - val)).argmin()
     return idx

T=2.4
m=1000
x_ED= np.arange(0,T+T/m,(T+T/m)/(m+1))
Num=Numerical(name="ED 48 ",Time=T,M=m)
Num.ED()
Trot=Numerical(name="Trotter",M=8,Time=T)
Trot.Trot()
names=["ibmq_santiago","ibmq_manila","ibmq_bogota"]
dum=FileManage.open_json("ibmq_bogota_JobDic.txt")
Bogota= Results(dum)
Bogota.load_results()
dum=FileManage.open_json("ibmq_manila_Day2_JobDic.txt")
Manila= Results(dum)
Manila.load_results()
dum=FileManage.open_json("ibmq_santiago_JobDic.txt")
Santiago= Results(dum)
Santiago.load_results()
k=Manila.M +1
x=np.arange(0,T+T/(k-1),(T+T/(k-1))/(k))
ind=[]
for i in range(k):
    ind.append(min_index(x_ED, x[i]))
data=np.zeros((4,5))
Exp=Num.Exp_ED
for j in range(5):
    M=Manila.Exp_FullMit[:,j]
    S=Manila.Exp_NormMit[:,j]
    B=Manila.Exp_MeasMit[:,j]
    T=Manila.Exp_NoMit[:,j]
    Test=Exp[ind,j]
    data[0,j]=Funcs.RSS(Exp[ind,j],T)
    data[1,j]=Funcs.RSS(Exp[ind,j],B)
    data[2,j]=Funcs.RSS(Exp[ind,j],M)
    data[3,j]=Funcs.RSS(Exp[ind,j],S)
x_bar= np.arange(0,5,1)
width = 0.5
fig, ax = plt.subplots()
rec3= ax.bar(x_bar+width/4,data[3,:],label="FullMit",width=0.2)  
rec2= ax.bar(x_bar+width/2,data[2,:],label="NormMit",width=0.2)  
rec1= ax.bar(x_bar-width/2,data[1,:],label="MeasMit",width=0.2)  
rec0= ax.bar(x_bar-width/4,data[0,:],label="NoMit",width=0.2)
ax.set_ylabel('RSS Value')
ax.set_xlabel('Sites')
ax.set_title('RSS Values of each site')
ax.set_xticks(x_bar)
ax.grid(axis='y')
fig.tight_layout()
ax.legend()
plt.savefig("RSSMeas.png")



