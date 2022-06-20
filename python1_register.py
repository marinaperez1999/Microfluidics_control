#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
.. module:: python1_register.py
    :synopsis: Module for creating a register of the characteristics of 
    the system for each day.

.. moduleauthor:: Marina Perez (mperez234@ehu.eus)
"""

import paho.mqtt.subscribe as subscribe
import time
from datetime import datetime

myHostname='192.168.0.18'   #IP address of the broker

date=datetime.today().strftime('%d-%m-%Y')
day=int(datetime.today().strftime('%d'))
previous_day = day

filename="/home/marinap/Documents/TFG_IE/mqtt/Microfluidics_" + date + ".txt"
file=open(filename,'w')

while True:
    day = int (datetime.today().strftime('%d'))
    #check if the day has changed to open a new file
    if (day != previous_day):
        file.close()
        date=datetime.today().strftime('%d-%m-%Y')
        filename="/home/marinap/Documents/TFG_IE/mqtt/Microfluidics_" + date + ".csv"
        file=open(filename,'w')
        previous_day = day
        file.writelines("hora, minuto, segundo, millis(), temperatura, " +
                        "frecuencia, voltaje, caudal \n")
        
    #subscribe to topics and recibe the messages
    msg0 = subscribe.simple('características/tiempo', hostname = myHostname, 
                            port = 1883).payload.decode('utf-8')
    msg1 = subscribe.simple('características/temperatura', hostname = myHostname, 
                            port = 1883).payload.decode('utf-8')
    msg2 = subscribe.simple('características/frecuencia', hostname = myHostname, 
                            port = 1883).payload.decode('utf-8')
    msg3 = subscribe.simple('características/voltaje', hostname = myHostname, 
                            port = 1883).payload.decode('utf-8')
    msg4 = subscribe.simple('características/caudal', hostname = myHostname, 
                            port = 1883).payload.decode('utf-8')   
    
    #get the exact time of the moment
    hour = datetime.now().strftime('%H')
    minute = datetime.now().strftime('%M')
    seg = datetime.now().strftime('%S')
    
    #write in the file the time and the received messages
    file.writelines(hour)
    file.writelines(', ')
    file.writelines(minute)
    file.writelines(', ')
    file.writelines(seg)
    file.writelines(', ')    
    file.writelines(msg0)
    file.writelines(', ')
    file.writelines(msg1)
    file.writelines(', ')
    file.writelines(msg2)
    file.writelines(', ')
    file.writelines(msg3)
    file.writelines(', ')
    file.writelines(msg4)
    file.writelines('\n') 
    
    #wait for one second
    time.sleep(1)
    
