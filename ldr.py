import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import time as T
import numpy as NP

# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

currentTime = T.asctime(T.localtime(T.time()))
light = mcp.read_adc(7)

timeData = NP.array([[currentTime]], dtype = "S")
sensorData = NP.array([[light]], dtype = "int16")

fullArray = NP.hstack((sensorData, timeData))

with open("light.csv", "a") as light:
	NP.savetxt(light, fullArray, fmt = "%s", delimiter = ",")
