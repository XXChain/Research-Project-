# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 11:58:27 2022

@author: User
"""

#from Numerical_test import Funcs,Observables,plots 
import numpy as np 
from Numerical_test import FileManage,Funcs,Error_mit,Backends,Results,Plots,Numerical,Observables 
import json 
import matplotlib.pyplot as plt
T=1 #should have really added an extra step 
test=FileManage.open_json("ibmq_bogotasym_JobDic.txt")
M=Results(test)
M.load_results()
test=FileManage.open_json("ibmq_bogotaH_JobDic.txt")
P=Results(test)
P.load_results()
Plots.BMS("Sym vs Regular",P,M,bit=4,S=None,ED=True,Trot=True)