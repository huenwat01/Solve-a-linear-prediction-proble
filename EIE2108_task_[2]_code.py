# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 20:43:44 2022

@author: wingh
"""
import numpy as np
import matplotlib.pyplot as plt

def caldJdA1(data2,a12,a42):      #calculate new A1
    temp=0;
    for i in range(4,500):
        temp+=2*(data2[i]-a12*data2[i-1]-a42*data2[i-4])*(-data2[i-1])
    return temp

def caldJdA4(data2,a12,a42):      #calculate new A4
    temp=0
    for i in range(4,500):
        temp+=2*(data2[i]-a12*data2[i-1]-a42*data2[i-4])*(-data2[i-4])
    return temp
    
def calJ(data2,a12,a42):          #calculate new J
    temp=0;
    for i in range(4,500):
        temp+=(data2[i]-a12*data2[i-1]-a42*data2[i-4])**2
    return temp
    
data = []
with open('eie2108-22-lab-datafile-02.txt') as file:
    for i in range(0,500) :                          #read all data into list
        line = file.readline()
        data.append(float(line))
    
jresult = []   

a1 = 0.5;                        #Set A1
a4 = 0.55;                       #Set A4
beta = 0.0001                   #Set beta
maxIter = 55;                    #Set max iter
ite = []                         # list to store number of iter
a1list = []
a4list = []
for i in range (0,maxIter):
    tempa1 = a1                                        #temporary store A1
    tempa4 = a4                                        #temporary store A4
    jresult.append(calJ(data,a1,a4))                   #calculate new J
    a1 = a1 - beta*caldJdA1(data, tempa1, tempa4)      #calculate new A1
    a4 = a4- beta * caldJdA4(data, tempa1, tempa4)     #calculate new A4
    a1list.append(a1)
    a4list.append(a4)
    ite.append(i)
    #print(jresult[i])                                 #check the result of J


fig, j = plt.subplots()                                         #polt  J graph
j.plot(ite[:],jresult[:],color = "red",label = "cost J")
j.set_xlabel("iter")
j.set_ylabel("cost J")
j.set_ylim(round(min(jresult)-100), round(max(jresult))+100)
j.set_xlim(0,55)
j.grid(visible = True,which = 'major',axis = 'x')
j.legend(["cost J"], loc = 'upper right' )
fig



fig2, j2 = plt.subplots()                                       #polt A1 graph
j2.plot(ite[:],a1list[:],color = "blue",label = "A1")
j2.set_xlabel("iter")
j2.set_ylabel("A1")
j2.set_ylim(round(min(a1list)), round(max(a1list))+0.5)
j2.set_xlim(0,55)
j2.grid(visible = True,which = 'major',axis = 'x')
j2.legend(["A1"], loc = 'upper right' )
fig2

fig3, j3 = plt.subplots()                                       #polt A4 graph
j3.plot(ite[:],a4list[:],color = "green",label = "A4")
j3.set_xlabel("iter")
j3.set_ylabel("A4")
j3.set_ylim(round(min(a4list)-0.4), round(max(a4list))+0.5)
j3.set_xlim(0,55)
j3.grid(visible = True,which = 'major',axis = 'x')
j3.legend(["A4"], loc = 'upper right' )
fig3

















