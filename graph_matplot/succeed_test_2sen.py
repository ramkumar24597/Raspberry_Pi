# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 23:17:36 2017

@author: ram
"""

import serial
import numpy as np

import matplotlib.pyplot as plt 
import matplotlib.animation as animation

# plot class
class AnalogPlot:
  def __init__(self, strPort):
      self.ser = serial.Serial(strPort, 9600)

  def update(self,h):
      try:    
          print h
          line = self.ser.readline()
          print(line)
          data = [float(val) for val in line.split()]
          print(data)
          print(rects)
          print(data)
          for rect, yi in zip(rects, data):
            print(yi)
            print(rect.set_height(yi))
          
      except KeyboardInterrupt:
          print('exiting')
          

      return rects

  # clean up
  def close(self):
      # close serial
      self.ser.flush()
      self.ser.close()    

# main() function
def main():
  global rects
  z = [0,0]
  #strPort = '/dev/tty.usbserial-A7006Yqh'
  strPort = '/dev/ttyACM0'

  print('reading from serial port %s...' % strPort)

  # plot parameters
  analogPlot = AnalogPlot(strPort)

  print('plotting data...')
 
  # set up animation
  fig = plt.figure()
  objects = ('CO','NOx')
  x = np.arange(len(objects))
  rects = plt.bar(x, z, color='c')
  plt.xticks(x, objects)
  plt.ylim(0,1023)
  anim = animation.FuncAnimation(fig, analogPlot.update, interval=40)
  plt.show()
  
  # clean up
  analogPlot.close()

  print('exiting.')
  

# call main
if __name__ == '__main__':
    main()