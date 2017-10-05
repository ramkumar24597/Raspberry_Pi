# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 22:27:41 2017

@author: ram
"""

import numpy as np
import matplotlib.pyplot as plt
 
objects = ('co','nox')
y_arrange = np.arange(len(objects))
performance = [20,8]
 
plt.ylim(0,50)
plt.bar(y_arrange, performance, align='center', alpha=0.6)
plt.xticks(y_arrange, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')
 
plt.show()

