# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 22:35:13 2017

@author: ram
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

fig = plt.figure()

x = [1,2,3,4,5]
y = [5,7,2,5,3]

data = np.column_stack([np.linspace(0, yi, 50) for yi in y])


rects = plt.bar(x, data[0], color='c')

plt.ylim(0, max(y))
def animate(i):
    print(i)
    print(data[i])
    for rect, yi in zip(rects, data[i]):
        print(rect.set_height(yi))

    return rects
    

anim = animation.FuncAnimation(fig, animate, interval=40)
plt.show()