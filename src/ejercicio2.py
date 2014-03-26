#!/usr/bin/python
import error
l=[]
t=5
t_upla_intervalos=(100,1000,10000,100000,1000000)
t_upla_umbrales=(0.1,0.01,0.0001,0.00001,0,000001)
for i in t_upla_intervalos:
  for j in t_upla_umbrales:
    error(i,t,j,)