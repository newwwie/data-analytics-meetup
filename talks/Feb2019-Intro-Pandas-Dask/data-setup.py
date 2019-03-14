import os
import pandas as pd
import urllib.request as req


WORKDIR = os.path.dirname(__file__)
DATADIR = os.path.abspath(os.path.join(WORKDIR, 'data'))

if not os.path.exists(DATADIR):
	os.makedirs(DATADIR)

def electr_consump():
	'''
	Data Set Information:

	This archive contains 2075259 measurements gathered in a house located in Sceaux (7km of Paris, France) between December 2006 and November 2010 (47 months). 
	Notes: 
	1.(global_active_power*1000/60 - sub_metering_1 - sub_metering_2 - sub_metering_3) represents the active energy consumed every minute (in watt hour) in the household by electrical equipment not measured in sub-meterings 1, 2 and 3. 
	2.The dataset contains some missing values in the measurements (nearly 1,25% of the rows). All calendar timestamps are present in the dataset but for some timestamps, the measurement values are missing: a missing value is represented by the absence of value between two consecutive semi-colon attribute separators. For instance, the dataset shows missing values on April 28, 2007.


	Attribute Information:

	1.date: Date in format dd/mm/yyyy 
	2.time: time in format hh:mm:ss 
	3.global_active_power: household global minute-averaged active power (in kilowatt) 
	4.global_reactive_power: household global minute-averaged reactive power (in kilowatt) 
	5.voltage: minute-averaged voltage (in volt) 
	6.global_intensity: household global minute-averaged current intensity (in ampere) 
	7.sub_metering_1: energy sub-metering No. 1 (in watt-hour of active energy). It corresponds to the kitchen, containing mainly a dishwasher, an oven and a microwave (hot plates are not electric but gas powered). 
	8.sub_metering_2: energy sub-metering No. 2 (in watt-hour of active energy). It corresponds to the laundry room, containing a washing-machine, a tumble-drier, a refrigerator and a light. 
	9.sub_metering_3: energy sub-metering No. 3 (in watt-hour of active energy). It corresponds to an electric water-heater and an air-conditioner.
	'''
	print(electr_consump.__doc__, flush=True)
	url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00235/household_power_consumption.zip'
	fname = os.path.join(DATADIR, 'household_power_consumption.txt')
	# check if file is downloaded first
	if os.path.exists(fname):
		print('Electrical consumption data set already present', flush=True)
		return None

	# download the file
	req.urlretrieve(url, fname)
	print('Downloaded Electrical consumption data set', flush=True)

	return None


if __name__ == '__main__':
	electr_consump()