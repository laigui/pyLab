#!/usr/bin/python
# -*- coding:utf-8 -*-
import serial
import binascii
from time import sleep
from time import localtime, strftime

ser = serial.Serial(
    port='/dev/tty.SLAB_USBtoUART',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

print('serial test start ...')
rx_cnt = 0
try:
    while True:
        if ser.in_waiting > 0:
            current_time = strftime("test-%y%m%d-%H:%M:%S  ", localtime())
            print current_time + binascii.b2a_hex(ser.read(ser.in_waiting)) + '\n'
            sleep(1)
except KeyboardInterrupt:
    if ser != None:
        ser.close()
