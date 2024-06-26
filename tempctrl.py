#!/usr/bin/python3
#This script is designesd to provide fan curve control on amd64 chromebooks running Linux
#Please read the comments to understand how to use this program
#This script must be run as root

from time import sleep
from os import system

#This defines the path to your cpu temperature sensor
#Replace 5 with X where
#$ cat /sys/class/thermal/thermal_zoneX/type
#returns TCPU

sensorPath="/sys/class/thermal/thermal_zone5/temp"

#You must have ectool installed on your system
#You can download the binary at https://tree123.org/files/utils/ectool
#Here you must specify its location, I recommend copying it to /usr/local/bin
#However if it is somewhere else (such as /bin/ectool), you must change this to match
ectoolPath="/usr/local/bin/ectool"

#This defines the fan curve for temperatures of
#40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90 degrees celcius
#The values in the list are fan speed percentage
fanCurve = [0, 0, 0, 10, 15, 20, 30, 40, 50, 100, 100]

#In case you want to adjust the temperatures that correspond to the various fan settings
#Must be the same length as fanCurve
tempList = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

#Number of seconds the program takes to get cpu temp and change fan speed
#Lowering it will cause sudden spikes in the fan as a result of the cpu boosting
refreshFreq = 1

def getCpuTemp():
	temp = open(sensorPath, 'r').read().strip()
	temp = int(int(temp)/1000) #The raw output of the sensor has a bunch of extra zeroes at the end
			      #I think its the same on every system, but if not adjust accordingly
	return temp

def closestIndex(list, value):
	return min(range(len(list)), key=lambda i: abs(list[i]-value))

print("Initializing...")
lastTemp = 60

while True:
	sleep(refreshFreq)
	temp = getCpuTemp()
	print("The cpu temperature is " + str(temp) + " degrees Celcius\n")

	if abs(lastTemp - temp) > 1:
		print("Temperature inconsistent, not adjusting fan speed to prevent overcompensation\n")
	else:
		FCIndex = closestIndex(tempList, temp)
		print("This is closest to fan curve index " + str(FCIndex))
		fanPercent = (fanCurve[FCIndex])
		print("Setting fan speed to " + str(fanPercent) + "%\n")
		system(ectoolPath + " fanduty " + str(fanPercent))
	lastTemp = temp
