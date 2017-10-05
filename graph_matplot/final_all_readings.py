# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 23:45:45 2017

@author: ram
"""

import serial
from time import sleep
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

# plot class
class value:
  def __init__(self, strPort):
      self.ser = serial.Serial(strPort, 9600)

  def update(self,i):
      try:
          print('--------------------------------------------------')
          print(i)
          line = self.ser.readline()
          print(line)         
          data = []
          for val in line.split(','):
              """ reason for this check is sometimes serail value returns one or two empty value, to solve that error
                  we use this check if it is empty string, then return none """
              if val == "" :
                  return None
              else:
                  data.append(float(val))             

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
  z = [0,0,0,0,0,0,0]
  #strPort = '/dev/tty.usbserial-A7006Yqh'
  strPort = '/dev/ttyACM0'

  print('reading from serial port %s...' % strPort)

  # plot parameters
  

  print('plotting data...')
 
  # set up animation
  fig = plt.figure()
  objects = ('Psropane','Methane','Benzine','CO','NOx','NH3','CO2')
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