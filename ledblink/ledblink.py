#!/usr/bin/env python
import sys
from threading import Thread
from rflib import rf2serial, request_reply
import rflib
from time import sleep
import time


def send_rf_msg(msg):
  print "Transmitting " + msg
  request=request_reply(msg) 
  if (request.rt):
      for x in range(request.num_replies):
          print "RECEIVED OK - " + str(request.id[x]) + str(request.message[x])
  else:
      print msg+ "-ERROR"
          
def main():
  try:
      rflib.init()
      #start serial processing thread
      a=Thread(target=rf2serial, args=())
      a.start()
      while (True):
        send_rf_msg("a03GPIOA1") 
        send_rf_msg("a03GPIOB1") 
        send_rf_msg("a03GPIOC1") 
        send_rf_msg("a03RELAYAON") 
        send_rf_msg("a03RELAYBON") 
        send_rf_msg("a03GPIOA0") 
        send_rf_msg("a03GPIOB0") 
        send_rf_msg("a03GPIOC0") 
        send_rf_msg("a03RELAYAOFF") 
        send_rf_msg("a03RELAYBOFF") 
    
  except KeyboardInterrupt:
      rflib.event.set()  #exit on ctrl-c
      
if __name__ == "__main__":
    try:
      main()
    except:
      rflib.event.set()
      print "Error"
