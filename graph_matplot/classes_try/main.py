# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 21:57:50 2017

@author: ram
"""

from serialvalue import value
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

def main():
  global rects
  z = [0,0,0]
  #strPort = '/dev/tty.usbserial-A7006Yqh'
  strPort = '/dev/ttyACM1'

  print('reading from serial port %s...' % strPort)

  # plot parameters
  

  print('plotting data...')
 
  # set up animation
  fig = plt.figure()
  objects = ('Hydrocarbons','Carbon Monoxide','Nitrous Oxide')
  x = np.arange(len(objects))
  rects = plt.bar(x, z,align='center', color='c')
  call = value(strPort)
  plt.xticks(x, objects)
  plt.ylim(0,500)
  anim = animation.FuncAnimation(fig, call.update, interval=50)
  plt.show()
  
  # clean up
  call.close()

  print('exiting.')
  

# call main
if __name__ == '__main__':
    main()