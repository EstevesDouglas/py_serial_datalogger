#!/usr/bin/python

from datetime import datetime
import serial

serial_ob = serial.Serial(port='COM5', baudrate=115200)
serial_ob.write(b'AT+START\n\r')

filename = datetime.now().strftime("datalog_%Y%m%d_%H%M%S.log")

try:
    while True:
        serial_log = open(filename + '.csv','a')
        serial_log.write(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f,"))
                +str(serial_ob.readline()))
        serial_log.close()
except KeyboardInterrupt:
    pass
