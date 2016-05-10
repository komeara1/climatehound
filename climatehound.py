#!/bin/python

'''
ClimateHound script to read output from P9.40 from TMP36 sensor and convert it to Fahrenheit
Author: Kyle O'Meara 
Date: 10 May 2016


Citation: Simon Monk - https://learn.adafruit.com/downloads/pdf/measuring-temperature-with-a-beaglebone-black.pdf

'''

import Adafruit_BBIO.ADC as ADC
import time

def main():

	output = file('ClimateHound_Temp_Readings.txt','a')

	sensor_pin = 'P9_40'

	ADC.setup()

	reading = ADC.rea(sensor_pin)
	
	#millivolts reading
	mv =reading * 1800
	
	#Celsius reading
	celsius = (mv - 500)/10

	#Fahrenheit reading
	fahrenheit = (celsius * 9/5) + 32

	now = time.strftime("%Y-%m-%d %H:%M")

	output.write('{0} - The temperature is {1} degrees.').format(now, fahrenheit)

	time.sleep(3600)

if __name__ == '__main__':
    main()
