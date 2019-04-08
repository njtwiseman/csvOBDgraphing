import os
folder = '/home/frankstire/OBDGraph'

import plotly.offline as py
import plotly.graph_objs as go

import numpy as np
import pandas as pd

counter = 0
for filename in os.listdir(folder):
	if os.path.isdir(filename):
		vehiclePath = os.path.join(folder, filename + '/CSVLogs')
		for filename in os.listdir(vehiclePath):
			if not filename.find(".csv") > 0: continue

			with open(os.path.join(vehiclePath, filename)) as csv_file:
				data = []
				df = pd.read_csv(csv_file, skiprows=[0])
				#df.head()
				print(df.columns)
					# print datum
				for column in df.columns:
					print(column)
					if column == df.columns[0]: continue
					data.append(go.Scatter(
						name = column,
						x = df[df.columns[0]],
						y = df[column]
					))
				fig = dict(data=data)#, layout=layout) 
				py.plot(fig, filename=vehiclePath+filename.replace('.csv', '.html'))
