#! /usr/bin/python

import DashBase

from dash import Dash, dcc, Output, Input, html, State
import dash
import dash_bootstrap_components as dbc
from pages.GetText import ReadText

textReader = ReadText("main")

dash.register_page(
	__name__,
	path="/",
	title="CLG - Main page",
)

def layout():
	textReader.update()
	card_profile = dbc.Card(
			[
				dbc.CardHeader(dcc.Markdown(dangerously_allow_html=True, children='#### <p style="text-align: center;" children="Corentin Le Gall"/>')),
				dbc.Row(
					[
						dbc.Col(
							dbc.CardImg(
								src="assets/Me.png",
								className="img-fluid rounded-start",
								style={"maxWidth": "250px", "margin-left":"2%"}
							),
							className="col-md-4",
						),
						dbc.Col(
							dbc.CardBody(
								[
									dcc.Markdown(
										textReader.read(0),
										className="card-text",
									),
									html.Small(
										"Last updated 4/11/2022",
										className="card-text text-muted",
									),
								]
							), className="col-md-8",
						),
					],
					className="g-0 d-flex align-items-center",
				)
			],
			className="mb-3",
			style={"maxWidth": "100%", "margin-top":"95px"},
			color="primary", outline=True
	)

	card_projects = dbc.Card(
			[
				dbc.CardHeader(html.H4("Professional Projects")),
				dbc.CardBody(
					dcc.Markdown(textReader.read(2), className="card-text", dangerously_allow_html=True)
				)
			], 
			style={"maxWidth": "100%"}, 
			color="primary", outline=True
		)

	card_comp = dbc.Card([
		dbc.CardHeader(html.H4("Competences")),
		dbc.CardBody(
				[
					dcc.Markdown(textReader.read(1), className="card-text", dangerously_allow_html=True),
				]
		)], 
		className="l-100",
		style={"maxWidth": "100%", "margin-top":"95px", "height":"auto"}, 
		color="primary", outline=True
	)

	cards = dbc.Container(dbc.Row(
		[
			dbc.Col([card_profile, card_projects]),
			dbc.Col(card_comp)
		]
	))

	card_formations = dbc.Card(
		[
			dbc.CardHeader(html.H4("Vocational training")),
			dbc.CardBody(dcc.Markdown(textReader.read(3), className="card-text", dangerously_allow_html=True))
		],
		style={"maxWidth": "100%", "Length":"100%", "margin-top":"1%",},
		color="primary", outline=True
	)

	card_diplo = dbc.Card(
		[
			dbc.CardHeader(html.H4("Diplomas")),
			dbc.CardBody(dcc.Markdown(textReader.read(4), className="card-text"))
		],
		style={"maxWidth": "100%", "Length":"100%", "margin-top":"1%"}, 
		color="primary", outline=True
	)

	adding = dbc.Container(dbc.CardGroup(
		[
			card_formations,
			card_diplo,
		],
	))
	return dbc.Container([
		cards,
		adding,
	])