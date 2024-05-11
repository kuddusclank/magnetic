from datetime import datetime
SurveyName="New Untitled Survey"
Longitude=""
Lattitude=""
Intervals=0
Elevation=""
global profile
profile = 1
value=""
global Station
Station= 0
dataset={"Datapoint":[],"Reading 1":[],"Reading 2":[],"Reading 3":[],"Reading 4":[],
 "Reading_Average":[],"Time":[],"Longitude":[],"Lattitude":[],"Elevation":[]}

def add_data(z1,z2,z3,Longitude,Lattitude,Elevation):
	now =datetime.now()
	current_time=now.strftime("%H:%M:%S")
	Z=(z1+z2+z3)/3
	global Station
	dataset["Datapoint"]+=[Station]
	Station = Station + Intervals
	global profile
	profile = profile + 1
	dataset["Reading 1"]+=[z1]
	dataset["Reading 2"]+=[z2]
	dataset["Reading 3"]+=[z3]
	dataset["Reading 4"]+=[Z]
	dataset["Reading_Average"]+=[current_time]
	dataset["Time"]+=[Longitude]
	dataset["Longitude"]+=[Lattitude]
	dataset["Lattitude"]+=[Elevation]
	dataset["Elevation"]+=[" "]
def basemap(status,z1,z2,z3,z4,Longitude,Lattitude,Elevation):
	now =datetime.now()
	current_time=now.strftime("%H:%M:%S")
	Z=(z1+z2+z3+z4)/4
	dataset["Datapoint"]+=[status]
	dataset["Reading 1"]+=[z1]
	dataset["Reading 2"]+=[z2]
	dataset["Reading 3"]+=[z3]
	dataset["Reading 4"]+=[z4]
	dataset["Reading_Average"]+=[Z]
	dataset["Time"]+=[current_time]
	dataset["Longitude"]+=[Longitude]
	dataset["Lattitude"]+=[Lattitude]
	dataset["Elevation"]+=[Elevation]

def StartDP():
	dataset["Datapoint"]+=["Datapoint"]
	dataset["Reading 1"]+=["Reading 1"]
	dataset["Reading 2"]+=["Reading 2"]
	dataset["Reading 3"]+=["Reading 3"]
	dataset["Reading 4"]+=["Reading_Average"]
	dataset["Reading_Average"]+=["Time"]
	dataset["Time"]+=["Longitude"]
	dataset["Longitude"]+=["Lattitude"]
	dataset["Lattitude"]+=["Elevation"]
	dataset["Elevation"]+=[""]
def CloseDp():
	dataset["Datapoint"]+=["Datapoint"]
	dataset["Reading 1"]+=["Reading 1"]
	dataset["Reading 2"]+=["Reading 2"]
	dataset["Reading 3"]+=["Reading 3"]
	dataset["Reading 4"]+=["Reading 4"]
	dataset["Reading_Average"]+=["Reading_Average"]
	dataset["Time"]+=["Time"]
	dataset["Longitude"]+=["Longitude"]
	dataset["Lattitude"]+=["Lattitude"]
	dataset["Elevation"]+=["Elevation"]

def config():
	dataset={"Datapoint":[],"Reading 1":[],"Reading 2":[],"Reading 3":[],"Reading 4":[], "Reading_Average":[],"Time":[],"Longitude":[],"Lattitude":[],"Elevation":[]}



