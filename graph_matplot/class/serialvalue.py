# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 21:41:48 2017

@author: ram
"""

import serial

class value:
  def __init__(self, strPort):
      self.ser = serial.Serial(strPort, 9600)

  def update(self,i):
      try:    
          print(i)
          line = self.ser.readline()
          print(line)
          data = [float(val) for val in line.split(',')]
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