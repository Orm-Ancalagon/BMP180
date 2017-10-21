import Adafruit_BMP.BMP085 as BMP085 # Using the Adafruit BMP sensor library
import time	
import numpy as np

sensor = BMP085.BMP085() # Defines sensor from which to read

t = time.asctime(time.localtime(time.time())) # Stores local time in t
temperature = sensor.read_temperature()
pressure = sensor.read_pressure()

sensorData = np.array([[temperature], [pressure]]) 
sensorData = sensorData.reshape(1,2)
timeData = np.array([[t]], dtype = "S")
timeData = timeData.reshape(1,1)

fullArray = np.hstack((sensorData, timeData))
#print fullArray

with open("output.csv", "a") as output:
	np.savetxt(output, fullArray, fmt = "%s",  delimiter=",")
