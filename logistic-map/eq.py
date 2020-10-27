#!/usr/bin/env python3

# See https://www.youtube.com/watch?v=ovJcsL7vyrk for reference

import matplotlib.pyplot as plt
import numpy as np

def seqlast(r, i):
  x = np.empty(100+1)
  x[0] = i
  for n in range(100): x[n+1] = r*x[n]*(1-x[n])
  return x[n]
  
if __name__=="__main__":
  x = np.arange(0,5,0.0001)
  for init in np.arange(0.0, 10.0, 0.01):
    y = np.empty(len(x))
    for (i,r) in enumerate(x): y[i] = seqlast(r, init)
    plt.plot(x, y)
    plt.savefig('weird.{}.png'.format(init))
    plt.clf()
