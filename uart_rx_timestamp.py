#!/usr/bin/python
# -*- coding:utf-8 -*-
import serial
import binascii
from time import sleep
from time import localtime, strftime
from sys import platform as _platform


if _platform == "linux" or _platform == "linux2":
    # linux
    ser = serial.Serial(
            port='/dev/ttyUSB0',
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=10
        )
elif _platform == "darwin":
    # MAC OS X
    ser = serial.Serial(
            port='/dev/tty.SLAB_USBtoUART',
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=10
        )
elif _platform == "win32":
    # Windows
    ser = serial.Serial(
            port='/dev/ttyUSB0',
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=10
        )
elif _platform == "win64":
    # Windows 64-bit
    ser = serial.Serial(
            port='/dev/ttyUSB0',
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=10
        )


print('serial test start ...')
rx_cnt = 0
try:
    while True:
        if ser.in_waiting > 0:
            current_time = strftime("%y%m%d-%H:%M:%S  ", localtime())
            print(current_time + binascii.b2a_hex(ser.read(ser.in_waiting)) + '\n')
            sleep(1)
except KeyboardInterrupt:
    if ser != None:
        ser.close()
