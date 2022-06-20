#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
.. module:: python3_modifications.py
    :synopsis: Module for publishing in the broker the modification 
    on the system the user wishes to make.

.. moduleauthor:: Marina Perez (mperez234@ehu.eus)
"""

import paho.mqtt.publish as publish

#the user enters the value
input_function = input ("For priming tap 1, " + 
                        "for increasing 50 ul/min the flowrate tap 2, "+
                        "for decreasing 50 ul/min the flowrate tap 3, " + 
                        "for stopping or reanudating the system tap 4 ")

myHostname='192.168.0.18'   #IP address of the broker

#This function publishes the input instruction of modification  in its corresponding topic.
def setFunction(input_function):
    if input_function=='1':
        publish.single('modificaciones/priming', input_function, 
                   hostname = myHostname, port = 1883)
    elif input_function=='2':
        publish.single('modificaciones/caudal_aumentar_o_disminuir', input_function, 
                   hostname = myHostname, port = 1883)
    elif input_function=='3':
        publish.single('modificaciones/caudal_aumentar_o_disminuir', input_function, 
                   hostname = myHostname, port = 1883)
    elif input_function=='4':
        publish.single('modificaciones/pausar_o_reanudar', input_function, 
                   hostname = myHostname, port = 1883)
    else:
        input_function = input ("Please enter 1, 2 or 3 ")
        setFunction(input_function)
       
setFunction(input_function)