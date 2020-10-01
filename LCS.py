# -*- coding: utf-8 -*-
"""


@author: Nirav
"""

import numpy as np

s1 = input('enter first string')
s2 = input('enter second string')
l1 = len(s1)
l2 = len(s2)

c = np.zeros((l1+1,l2+1),int)

for i in range(1,l1+1):
    for j in range(1,l2+1):
        if(s1[i-1] == s2[j-1]):
            c[i][j] = c[i-1][j-1] + 1
        else:
            c[i][j] = max(c[i-1][j] , c[i][j-1])
            

print(c)  

s = c[l1][l2]
lcs = ""
i=l1
j=l2
while (s>0):
    if(s1[i-1] == s2[j-1]):
        lcs = s1[i-1] + lcs
        s-=1
        i-=1
        j-=1
    elif (c[i][j] == c[i-1][j]):
        i-=1
    else:
        j-=1
            

print(lcs)
