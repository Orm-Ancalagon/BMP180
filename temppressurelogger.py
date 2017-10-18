import Adafruit_BMP.BMP085 as BMP085
import time
import numpy
import itertools

sensor = BMP085.BMP085()
t = time.asctime(time.localtime(time.time())) 

temperature = sensor.read_temperature()
float(temperature)

pressure = sensor.read_pressure()
float(pressure)

array = numpy.array((temperature, pressure, t), 
		dtype = [("temperature", float), ("pressure", float), ("t", "S16")]) 

numpy.savetxt("output.csv", array, fmt = ["%.2f",]*2 + ["%s"],  delimiter=",")

#print('Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
#print('Pressure = {0:0.2f} Pa'.format(sensor.read_pressure()))
#print('Altitude = {0:0.2f} m'.format(sensor.read_altitude()))
#print('Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure())) 
