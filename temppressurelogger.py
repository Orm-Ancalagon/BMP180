import Adafruit_BMP.BMP085 as BMP085 # Using the Adafruit BMP sensor library
import time	
import numpy as np

sensor = BMP085.BMP085() # Defines sensor from which to read

t = time.asctime(time.localtime(time.time())) # Stores local time in t
temperature = sensor.read_temperature()
pressure = sensor.read_pressure()

data = np.array([[temperature], [pressure], [t]])  
np.dtype([("temperature", float), ("pressure", float), ("t", "S20")])
#print(array.shape)

np.savetxt("output.csv", data.reshape((1,3)), fmt = "%.2f %.2f %s", delimiter=",")

