#! /usr/bin/python

from dash import Dash, dcc, Output, Input, html, State
import dash
import dash_bootstrap_components as dbc
from pages.GetText import ReadText
import pandas as pds
import pages.co2Graph.pies as pies
import pages.co2Graph.lines as lines
import plotly.express as px
import pages.co2Graph.readData as readData

df, countries, G20, EU, Africa, Asia, Europe, NAmerica, SAmerica, Oceania = readData.get_data()

text = ReadText("CO2")

dash.register_page(
	__name__,
	path="/CO2",
	title="CLG - CO2 Emissions",
)

def layout():


	intro = dbc.Card([
				dbc.CardHeader(dcc.Markdown(dangerously_allow_html=True, children='#### <p style="text-align: center;" children="Inroduction"/>')),
				dbc.CardBody(dcc.Markdown(text.read(0), dangerously_allow_html=True, className="card-text")),
			],
			style={"maxWidth": "100%"}, 
			color="primary", outline=True
	)

	obj = dbc.Card([
		dbc.CardHeader(dcc.Markdown(dangerously_allow_html=True, children='#### <p style="text-align: center;" children="Objectives"/>')),
		dbc.CardBody(dcc.Markdown(text.read(1), dangerously_allow_html=True, className="card-text")),
	],style={"maxWidth": "100%"}, color="primary", outline=True)


	fig = px.bar(
		y=df.corr().loc["cumulative_co2", :], 
		x=df.corr().loc["cumulative_co2", :].index, 
		template="plotly_dark",
		labels=dict(y="cumulative_co2", x=""),
		title="Bar plot showing the correlation between cumulative co2 and other parameters",
	)
	fig.update_layout({
		"plot_bgcolor": "rgba(0, 0, 0, 0)",
		"paper_bgcolor": "rgba(0, 0, 0, 0)",
	})

	fig2 = px.bar(
		y=df.corr().loc["gdp_growth", :], 
		x=df.corr().loc["gdp_growth", :].index, 
		template="plotly_dark",
		labels=dict(y="gdp", x=""),
		title="Bar plot showing the correlation between gdp_growth and other parameters",
	)
	fig2.update_layout({
		"plot_bgcolor": "rgba(0, 0, 0, 0)",
		"paper_bgcolor": "rgba(0, 0, 0, 0)",
	})

	project = dbc.Container(
			[
				dbc.Row(
					dbc.Card(
						dbc.CardBody(
							dcc.Markdown(text.read(2))
						), style={"margin-top":"10px"}, color="secondary"
					)
				),
				dbc.Row(
					[
						dbc.Col(dcc.Graph(figure=pies.data_by_continent(value="cumulative_co2", title="Pie Chart of cumulative co2 emmissions by continient"))),
						#dbc.Col(dcc.Graph(figure=pies.data_by_continent(value="gdp", title="Pie Chart of cumulative co2 emmissions by continient"))),
					]
				),
				dbc.Row(
					[
						dbc.Col(dcc.Graph(figure=pies.data_G20(value="cumulative_co2", title="Pie Chart of cumulative co2 emmissions of G20 members"))),
						dbc.Col(dcc.Graph(figure=pies.data_G20(value="gdp", title="Pie Chart showing the gpd of G20 members"))),
					]
				),
				dbc.Row(
					dbc.Card(
						dbc.CardBody(
							dcc.Markdown(text.read(3))
						), style={"margin-top":"10px"}, color="secondary"
					)
				),
				dbc.Row(
					dbc.Col(dcc.Graph(figure=lines.corr_by_year("gdp_growth", "cumulative_co2", "Line chart showing the correlation between gdp growth and cumulative co2 between 1821 and 2018")))
				),
				dbc.Row(
					dbc.Col(dcc.Graph(figure=fig)),
				),
				dbc.Row(
					dbc.Col(dcc.Graph(figure=pies.corr_prct(df.corr(), "cumulative_co2", "Pie chart showing the bigests correlation values between cumulative_co2 and other parameters")))
				),
				dbc.Row(
					dbc.Card(
						dbc.CardBody(
							dcc.Markdown(text.read(4))
						), style={"margin-top":"10px"}, color="secondary"
					)
				),
				dbc.Row(
					dbc.Col(dcc.Graph(figure=fig2)),
				),
				dbc.Row(
					dbc.Col(dcc.Graph(figure=pies.corr_prct(df.corr(), "gdp_growth", "Pie chart showing the bigests correlation values between gdp growth and other parameters")))
				),
				dbc.Row(
					dbc.Card(
						dbc.CardBody(
							dcc.Markdown(text.read(5))
						), style={"margin-top":"10px"}, color="secondary"
					)
				),
			]
		)

	main_card = dbc.Card([
		dbc.CardHeader(dcc.Markdown(dangerously_allow_html=True, children='#### <p style="text-align: center;" children="Project"/>')),
		dbc.CardBody([
			project,
		])
	], style={"margin-top":"10px"}, color="primary", outline=True)

	header = dbc.CardGroup(
		[
			intro,
			obj,
		], 
		style={"margin-top":"95px"}
	)

	layout = dbc.Container([
		header,
		main_card,
	])

	return dbc.Container(layout)