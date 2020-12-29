import logging

import adafruit_mcp9600
import board
import busio

class MCP9600(object):
    '''Driver for [Thermocouple EMF to Temperature Converter](https://ww1.microchip.com/downloads/en/DeviceDoc/MCP960X-L0X-RL0X-Data-Sheet-20005426F.pdf)
     Requires:
     - adafruit's MCP9600 device library (adafruit_mcp9600)

    '''
    def __init__(self, scl_pin, sda_pin, frequency=100000):
        i2c = busio.I2C(scl_pin, sda_pin, frequency)
        self.mcp9600 = adafruit_mcp9600.MCP9600(i2c)
        self.log = logging.getLogger(__name__)

    def get(self):
        '''Reads SPI bus and returns current value of thermocouple.'''
        temp = self.mcp9600.temperature
        self.log.debug("temp %s" % temp)
  
        return temp

class MCP9600Error(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
