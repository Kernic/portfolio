#! /usr/bin/python
import plotly.express as px
import pandas as pds
import pages.co2Graph.readData as readData

df, countries, G20, EU, Africa, Asia, Europe, NAmerica, SAmerica, Oceania = readData.get_data()

def data_by_continent(value:str, title:str) -> px.pie:
	fig = px.pie(
		df[df["country"].isin(["Africa", "Europe", "Asia", "North America", "South America", "Oceania"]) & (df["year"]==2018)],
		color_discrete_map={
			"Africa":"#636363",
			"Europe":"#9ecae1",
			"Asia":"#fec44f",
			"Oceania":"#a1d99b",
			"North America":"#de2d26",
			"South America":"#fc9272",
		},
		color="country",
		values=value,
		names="country",
		title=title,
		template="plotly_dark"
	)
	fig.update_layout({
		"plot_bgcolor": "rgba(0, 0, 0, 0)",
		"paper_bgcolor": "rgba(0, 0, 0, 0)",
	})

	return fig

def data_G20(value:str, title:str) -> px.pie:
	fig = px.pie(
		df[df["country"].isin(G20[:-1]) & (df["year"]==2018)],
		values=value,
		color_discrete_map={
			"Argentina":"#6CACE4",
			"Australia":"#012169",
			"Brazil":"#009639",
			"Canada":"#EF3340",
			"China":"#C8102E",
			"France":"#0055a4",
			"Germany":"#000000",
			"India":"#FF8F1C",
			"Indonesia":"#EF3340",
			"Italy":"#007A33",
			"Japan":"#FFFFFF",
			"Mexico":"#006341",
			"South Korea":"#C8102E",
			"Russia":"#0072CE",
			"Saudi Arabia":"#009639",
			"South Africa":"#E03C31",
			"Turkey":"#C8102E",
			"United Kingdom":"#012169",
			"United States":"#041E42",
		},
		color="country",
		names="country",
		title=title,
		template="plotly_dark"
	)
	fig.update_layout({
		"plot_bgcolor": "rgba(0, 0, 0, 0)",
		"paper_bgcolor": "rgba(0, 0, 0, 0)",
	})

	return fig

def corr_prct(corr_matrix: pds.DataFrame, value:str, title:str = "Title of the pie chart"):
	df = corr_matrix.loc[value, :]
	fig = px.pie(
		df,
		values=value,
		color=df.index,
		title=title,
		template="plotly_dark",
	)
	fig.update_traces(textposition='inside', textinfo='value')
	fig.update_layout({
		"plot_bgcolor": "rgba(0, 0, 0, 0)",
		"paper_bgcolor": "rgba(0, 0, 0, 0)",
	})
	return fig