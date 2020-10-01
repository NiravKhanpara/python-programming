# -*- coding: utf-8 -*-
"""


@author: Nirav
"""
import numpy as np
print("============='nCr'=============")

n = int(input('Enter value of n'))
r = int(input('Enter value of r'))

c = np.zeros((n+1,r+1),int)

for i in range(n+1):
    for j in range(min(i,r)+1):
        if(j==0 or j==i):
            c[i][j]=1
        else:
            c[i][j] = c[i-1][j-1] + c[i-1][j]

print('Answer is : ',c[n][r])            
