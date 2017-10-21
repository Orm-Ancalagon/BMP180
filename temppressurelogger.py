import Adafruit_BMP.BMP085 as BMP085 # Using the Adafruit BMP sensor library
import time	
import numpy as np

# Defines sensor from which to read
sensor = BMP085.BMP085()

# Stores the time, temperature, and pressure in their respective variables 
t = time.asctime(time.localtime(time.time())) 
temperature = sensor.read_temperature()
pressure = sensor.read_pressure()	

""" Two arrays are constructed in order to deal with the different data types.
sensorData stores temperature and pressure as float. timeData saves localtime as 
a string. Both arrays are then reshaped so that they have the same number of rows 
in order to be concatenated later."""

sensorData = np.array([[temperature], [pressure]]) 
sensorData = sensorData.reshape(1,2)
timeData = np.array([[t]], dtype = "S")
timeData = timeData.reshape(1,1)

""" Two arrarys are joined hozintally into a single array """
fullArray = np.hstack((sensorData, timeData))

""" Output.csv is opened in append mode so that it is now overwritten and the 
file pointer is placed at the end of the file."""

with open("output.csv", "a") as output:
	np.savetxt(output, fullArray, fmt = "%s",  delimiter=",")
