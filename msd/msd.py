##!/usr/bin/env python


import pandas as pd
import numpy as np

'calculates MSD from x, y, z coordinates'
'the input file format should be: "time"  "ids"  "x"  "y"  "z"  ' 



# Correction of Periodic Boundary Conditions
def AdjustPeriodicity(x,L):
    for i in range(len(x)-1):
        if x[i+1] - x[i] > L/2:
            x[i+1] -= (x[i+1] - x[i]+L/2)//L*L
        if x[i+1] - x[i] < -L/2:
            x[i+1] += (x[i] - x[i+1]+L/2)//L*L
    return x


def msd_np(x):
    'x is numpy array of position of particle)'
 #   x=AdjustPeriodicity(x, L)
    n = len(x)
    msd = []
    for s in range(1,n):
        dx = x[s:] - x[:-s]
        msd.append(np.average(dx**2))
    return msd


df = pd.read_csv('pos.dat', sep='\s+', header=None)
ntype = max(df[1])
nlines = len(df)
nstep = nlines/ntype

a=1000
gphi=0.001
L = a*(4.0/3.0*3.14159260*ntype/gphi)**(1.0/3.0)*1/1000

msd_sum = np.zeros((int(nstep)-1))

list_r = []
list_msd = []
msdout = open("msd.out" , 'w')  # to store msd averaged over all particle ids
for i in range(0,ntype):
    id = i+1

    s=i
    x = []
    y = []
    z = []
    for j in range(0, int(nstep)):  ## nstep
        'This block separates the x,y,z coordinates of ith particle'

        x.append(df[2][j+s])   ## x coordinate of ith particle 
        y.append(df[3][j+s])
        z.append(df[4][j+s])
        s=s+ntype-1

        if s > nlines:
            break

    x_adjusted =  AdjustPeriodicity(x,L)
    y_adjusted =  AdjustPeriodicity(y,L)
    z_adjusted =  AdjustPeriodicity(z,L)

    r = np.sqrt( [ x_adjusted[im]**2 + y_adjusted[im]**2 + z_adjusted[im]**2  for im in range(len(x_adjusted))])
 #   print(r)
    list_r.append(r)
    msd = msd_np(np.array(r))   ##  msd of ith particle
    list_msd.append(msd)


for ntype_msd in list_msd:
    msd_sum = [(msd_sum[i]+ ntype_msd[i]) for i in range(len(ntype_msd))]
    
for lll in range(len(msd_sum)):
    msdout.write('%s    %s    \n' % (lll,  msd_sum[lll]/ntype) )
msdout.close()


