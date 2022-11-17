#! /usr/bin/python
""" This file is the base of the page use for all the other pages
"""

from dash import Dash, dcc, Output, Input, html, State
import dash
import dash_bootstrap_components as dbc

app = Dash(
	__name__,
	use_pages=True,
	external_stylesheets=[dbc.themes.DARKLY]
)
application = app.server

# creation the starting image and project
img = html.A(
	dbc.Row([
		dbc.Col(html.Img(src="assets/favicon.ico", height="40px")),
		dbc.Col(dbc.NavbarBrand("CLG - Data Scientist", className="ms-2")),
		], align="center", className="g-0 ms-auto flex-nowrap mt-3 mt-md-0"),
	href="/",
	style={"textDecoration": "none"},
)

projects = dbc.DropdownMenu(
	children=[
		dbc.DropdownMenuItem("My Projects", header=True),
		dbc.DropdownMenuItem("CO2 Emissions", href="/CO2"),
		#dbc.DropdownMenuItem("Page 3", href="#"),
	],
	nav=True,
	in_navbar=True,
	label="Projects",
)
contacts = dbc.DropdownMenu(
	children=[
		dbc.DropdownMenuItem("My Pages", header=True),
		dbc.DropdownMenuItem("LinkedIn", href="https://www.linkedin.com/in/corentin-le-gall-91239a173/"),
		dbc.DropdownMenuItem("GitHub", href="https://github.com/Kernic"),
		dbc.DropdownMenuItem("Email me!", href="mailto:corentin.le.gall@proton.me")
	],
	in_navbar=True,
	label="Contact Me",
	color="success", className="m-1",
)

dropMenu = dbc.Row(
	[
		dbc.Col(projects),
		dbc.Col(contacts),
	],
	className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
	align="center",
)

#, className="g-0 ms-auto flex-nowrap mt-3 mt-md-0"
# creating navBar :
nvbar = dbc.Navbar(
	dbc.Container(
		[
			img,
			dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
			dbc.Collapse(
				dropMenu,
				id="navbar-collapse",
				is_open=False,
				navbar=True,
			),
		]
	),
	color="primary",
	dark=True,
	expand="lg",
	fixed='top'
)

get_pdf = html.A(
	"Get My CV in PDF !",
	id="CV",
	href="assets/Corentin-Le_Gall2022.pdf",
	download="Corentin-Le_Gall2022.pdf",
)

madeDash = dcc.Markdown("Made With Dash !")

footer = dbc.Container([
	dbc.Row(
		[
			dbc.Col(get_pdf),
			dbc.Col(madeDash)
		]
	)
])

# add callback for toggling the collapse on small screens
@app.callback(
	Output("navbar-collapse", "is_open"),
	[Input("navbar-toggler", "n_clicks")],
	[State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
	if n:
		return not is_open
	return is_open

app.layout = dbc.Container([
	nvbar,
	dash.page_container,
	dbc.Container(footer),
])
