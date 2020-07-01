#!/usr/bin/env python
import serial
from time import sleep

port = '/dev/ttyAMA0'
baud = 9600
ser = serial.Serial(port=port, baudrate=baud)

while (True):
    ser.write("a03GPIOA1") 
    sleep(0.5)
    ser.write("a03GPIOB1") 
    sleep(0.5)
    ser.write("a03GPIOC1") 
    sleep(0.5)
    ser.write("a03RELAYAON") 
    sleep(0.5)
    ser.write("a03RELAYBON") 
    sleep(0.5)
    ser.write("a03GPIOA0") 
    sleep(0.5)
    ser.write("a03GPIOB0") 
    sleep(0.5)
    ser.write("a03GPIOC0") 
    sleep(0.5)
    ser.write("a03RELAYAOFF") 
    sleep(0.5)
    ser.write("a03RELAYBOFF") 
    sleep(0.5)

