import os
folder = '/home/frankstire/OBDGraph'

import plotly.offline as py
import plotly.graph_objs as go

import numpy as np
import pandas as pd

for filename in os.listdir(folder):
	if os.path.isdir(filename):
		csvPath = os.path.join(folder, filename)
		vehiclePath = csvPath + '/CSVLogs/'
		for filename in os.listdir(vehiclePath):
			if not filename.find(".csv") > 0: continue
			if filename.find(".done") > 0: continue 
			with open(os.path.join(vehiclePath, filename)) as csv_file:

				keys = {
					'rpm' : ' Engine RPM (RPM)',
					'load' : ' Calculated load value (%)',
					'stft' : ' Short term fuel % trim - Bank 1 (%)',
	   				'ltft' : ' Long term fuel % trim - Bank 1 (%)',
					'time' : 'Time (sec)',
				}
				data = []
				df = pd.read_csv(csv_file, skiprows=[0])
				loadSorted = df.sort_values(by=keys['load'])
				rpmSorted = df.sort_values(by=keys['rpm'])
				
				data.append({
					'name' : "STFT",
					'x' : loadSorted[keys['load']],
					'y' : loadSorted[keys['stft']],
					'type' : 'box'
				})

				data.append({
					'name' : "LTFT",
					'x' : loadSorted[keys['load']],
					'y' : loadSorted[keys['ltft']],
					'type' : 'box'					
				})

				data.append({
					'name' : 'Added Trim',
					'x' : loadSorted[keys['load']],
					'y' : loadSorted[keys['ltft']] + df[keys['stft']],
					'type' : 'box'					
				})

				fig = dict(data=data)
				py.plot(fig, filename=os.path.join(csvPath, filename).replace('.csv', '_load.html'))
				
				
				data = []
				

				data.append({ 
					'name': "STFT",
					'x' : rpmSorted[keys['rpm']],
					'y' : rpmSorted[keys['stft']],
					'type': 'box'
				})

				data.append({
					'name' : "LTFT",
					'x' : rpmSorted[keys['rpm']],
					'y' : rpmSorted[keys['ltft']],
					'type': 'box'					
				})

				data.append({
					'name' : 'Added Trim',
					'x' : rpmSorted[keys['rpm']],
					'y' : rpmSorted[keys['ltft']] + df[keys['stft']],
					'type': 'box'					
				})

				fig = dict(data=data)
				py.plot(fig, filename=os.path.join(csvPath, filename).replace('.csv', '_rpm.html'))
				
				os.rename(vehiclePath+filename, vehiclePath+filename+'.done')

