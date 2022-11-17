#! /usr/bin/python
""" This file is dedicated to get all the data from :
Our World in Data : https://ourworldindata.org/co2-emissions
"""

import pandas as pds
from pandas.io.json import json_normalize
from tqdm import tqdm
import json
import requests
import os
import numpy as np
from pages.co2Graph.readData import get_data

def get_data_url(format="csv"):
	""" This function is for downloading the dataset on multiple format
	Variable:
		format (str): format of the file that is downloaded (csv, xlsx, json) 

	"""
	if format.lower() == "csv":
		url = "https://nyc3.digitaloceanspaces.com/owid-public/data/co2/owid-co2-data.csv"
	elif format.lower() == "xlsx":
		url ="https://nyc3.digitaloceanspaces.com/owid-public/data/co2/owid-co2-data.xlsx"
	elif format.lower() == "json":
		url = "https://nyc3.digitaloceanspaces.com/owid-public/data/co2/owid-co2-data.json"
	else:
		print(f"Please select a good format (csv, xlsx, json)\nEntered : {format.lower()}")
		exit(0)

	# remove the files that already there
	for file in os.listdir("./data"):
		if file.startswith("owid-co2-data"):
			os.remove("./data/" + file)

	# String so we can iterate over the response
	chunkSize = 1024
	r = requests.get(url, stream=True)
	with open(f"./data/owid-co2-data.{format}", "wb") as f:
		pbar = tqdm(unit="B", total=int(r.headers["Content-Length"]))
		for chunk in r.iter_content(chunk_size=chunkSize):
			if chunk:
				pbar.update(len(chunk))
				f.write(chunk)

def transformToCsv():
	""" This function is to convert the downloaded file to a csv
	for better use by pandas

	"""
	for file in os.listdir("./data"):
		if file.startswith("owid-co2-data"):
			format = file.split(".")[-1]
			break
	if format == "xlsx":
		df = pds.DataFrame(
				pds.read_excel("./data/owid-co2-data.xlsx")
		)
		df.to_csv(
			"./data/owid-co2-data.csv", 
			index=False, 
			sep=",", 
			encoding="utf-8"
		)
		# remove the files that already there
		for file in os.listdir("./data"):
			if file.startswith("owid-co2-data") and file.split(".")[-1] == "xlsx":
				os.remove("./data/" + file)

	elif format == "json":
		with open("./data/owid-co2-data.json") as file:
			data = json.load(file)

		df = json_normalize(data)
		df.to_csv(
			"./data/owid-co2-data.csv", 
			index=False, 
			sep=",", 
			encoding="utf-8"
		)
		# remove the files that already there
		for file in os.listdir("./data"):
			if file.startswith("owid-co2-data") and file.split(".")[-1] == "json":
				os.remove("./data/" + file)

def add_gdp_growth() -> None:
	df, countries = get_data()[0:2]
	df["gdp_growth"] = [np.nan for i in range(len(df))]
	
	for i in tqdm(range(len(countries))):
		# getting country
		country = countries[i]
		
		# isolating country and it's data, filling with 1 for gdp growth
		data = df[df["country"]==country].fillna(1)
		
		# looping on each year
		for idx in range(1, len(data["year"])-2):
			# getting year
			year = data["year"].iloc[idx]
			
			# gdp_growth formula
			gdp_growth = (data[data["year"]==year]["gdp"].iloc[0] - data[data["year"]==year-1]["gdp"].iloc[0])/data[data["year"]==year-1]["gdp"].iloc[0]
			
			# replacing invalid values by NaN
			gdp_growth = np.nan if (gdp_growth >= 1.0 or gdp_growth == -1.0 or gdp_growth==0) else gdp_growth
			
			index = data[data["year"]==year].index
			df.loc[index, "gdp_growth"] = gdp_growth
	df.to_csv(
		"./data/owid-co2-data.csv", 
		index=False, 
		sep=",", 
		encoding="utf-8"
	)


if __name__ == "__main__":
	get_data_url("csv")
	add_gdp_growth()
	#transformToCsv()


