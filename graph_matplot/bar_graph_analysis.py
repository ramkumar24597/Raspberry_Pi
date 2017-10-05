# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 23:00:59 2017

@author: ram
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

fig = plt.figure()

objects = ('HC','CO','NOx')
x = np.arange(len(objects))
y = [5,7,3]

data = np.column_stack([np.linspace(0, yi, 50) for yi in y])
print(data)

rects = plt.bar(x, data[0], color='c')
plt.xticks(x, objects)
plt.ylim(0, 50)

def animate(i):
    print(i)
    print(data[i])
    print(rects)
    for rect, yi in zip(rects, data[49]):
        print(yi)
        print(rect.set_height(yi))

    return rects
    

anim = animation.FuncAnimation(fig, animate, interval=40)
plt.show()