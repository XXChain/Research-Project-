# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 15:09:37 2022

@author: User
"""

from Numerical_test import Error_mit,Backends,Observables,Plots,Quantum,Results,Funcs,FileManage,Numerical
T=2
Simulate =Quantum(name="quantums",M=40,Time=T)
Simulate.State_Vector()
Simulate.Quan_H()
Num=Numerical(name="ED",M=40,Time=T)
Num.ED()
Plots.colour_plot(Simulate,"StateVector",Simulate.Exp_Z)


        