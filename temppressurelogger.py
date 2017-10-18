import Adafruit_BMP.BMP085 as BMP085 # Using the Adafruit BMP sensor library
import time	
import numpy 

sensor = BMP085.BMP085() # Defines sensor from which to read
t = time.asctime(time.localtime(time.time())) # Stores local time in t

temperature = sensor.read_temperature()
float(temperature)

pressure = sensor.read_pressure()
float(pressure)

array = numpy.array(zip(temperature, pressure, t), 
		dtype = [("temperature", float), ("pressure", float), ("t", "S16")]) 

numpy.savetxt("output.csv", array, fmt = ["%.2f",]*2 + ["%s"],  delimiter=",")

