#!/usr/bin/env python
# coding: utf-8

# In[45]:


# Imports

import math
import numpy

# Function for log

def log(x):
    return 196 * (math.log(30.02 - (.001 * x)))

# Function for lin
def lin(x):
    return 30.02 - (.001 * x)

# x,y,z time, logs, lin

x = []
y = []
z = []

# n is for number of steps in range(E.g. .01 will increment the range by .01, instead of the standard 10)
n = .01

# Range of times in certain increments
for t in numpy.arange(0,30000+n,n):
    x.append(t)

# For every number in x list, plug it into and append it to the appropriate function and list
for x in x:
    y.append(log(x))
    z.append(lin(x))

# Means of finding equal y and z values
# m is for how accurate you want the solution to be.
# The smaller the difference between the values of the log and lin, the closer they are
# The closer they are, the more accurate the solution for time is
m = .001

indice = 0

while indice <= len(y):
    if (y[indice] - z[indice]) < m:
        print("The time is",indice*n,"seconds")

        break

    else:
        indice += 1



