import os
import pandas as pd
import urllib.request as req
from glob import glob
import tarfile


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

def au_elec_dev():
	urls ={ 
		'AirConditioners':'https://data.gov.au/data/dataset/559708e5-480e-4f94-8429-c49571e82761/resource/0973a476-eb0c-45e6-9a18-054f74307843/download/tmpxdamix_ac_2019_03_17.csv',
		'Clothes-dryers':'https://data.gov.au/data/dataset/559708e5-480e-4f94-8429-c49571e82761/resource/f734c56b-a255-4c4e-a3c1-e835c38b8774/download/tmpcf_j7j_cd_2019_03_17.csv',
		'Dishwashers':'https://data.gov.au/data/dataset/559708e5-480e-4f94-8429-c49571e82761/resource/cbe7057d-e132-4297-b8be-eecf8322d4e6/download/tmp9jiwbq_dw_2019_03_17.csv',
		'Clothes-Washers':'https://data.gov.au/data/dataset/559708e5-480e-4f94-8429-c49571e82761/resource/eb3b9d8e-f39d-47b7-9db0-309856176951/download/tmpxjwy19_cw_2019_03_17.csv',
		'Fridges-and-Freezers':'https://data.gov.au/data/dataset/559708e5-480e-4f94-8429-c49571e82761/resource/0eabca18-49bb-4a9e-8019-28d5d56501c4/download/tmp0sld1e_rf_2019_03_17.csv',
		'Televisions':'https://data.gov.au/data/dataset/559708e5-480e-4f94-8429-c49571e82761/resource/93a615e5-935e-4713-a4b0-379e3f6dedc9/download/tmplhf9bo_tv_2019_03_17.csv',
		'Computer-monitors':'https://data.gov.au/data/dataset/559708e5-480e-4f94-8429-c49571e82761/resource/f1ea4c89-282c-4d64-b870-10a5ab039030/download/tmp2gwicy_mo_2019_03_17.csv',
	}

	names = []
	for csv in urls.keys():
		fname = os.path.join(DATADIR, 'Australian-Electrical-Appliances', csv + '.csv')
		names.append(fname)
		if os.path.exists(fname):
			print(f'{os.path.basename(fname)} present')
		else:
			print(f'retrieving {csv}')
			req.urlretrieve(urls[csv], fname)

	return names

def flights():
    flights_raw = os.path.join(DATADIR, 'nycflights.tar.gz')
    flightdir = os.path.join(DATADIR, 'nycflights')

    if not os.path.exists(flights_raw):
        print("- Downloading NYC Flights dataset... ", end='', flush=True)
        url = "https://storage.googleapis.com/dask-tutorial-data/nycflights.tar.gz"
        req.urlretrieve(url, flights_raw)
        print("done", flush=True)

    if not os.path.exists(flightdir):
        print("- Extracting flight data... ", end='', flush=True)
        tar_path = os.path.join(DATADIR, 'nycflights.tar.gz')
        with tarfile.open(tar_path, mode='r:gz') as flights:
            flights.extractall('data/')
        print("done", flush=True)

    print("** Finished! **")
    return glob(os.path.join(flightdir, '*.csv'))

def nasa_file():
    url = ''
    return None

if __name__ == '__main__':
	electr_consump()