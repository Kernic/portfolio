import plotly.express as px
import pages.co2Graph.readData as readData

df, countries, G20, EU, Africa, Asia, Europe, NAmerica, SAmerica, Oceania = readData.get_data()

def corr_by_year(first:str, second:str, title:str) -> px.line:
	filtered = df[df["country"].isin(countries)][["year", first, second]]

	corr = []
	years = []
	for year in sorted(filtered["year"].unique()):
		corr.append(filtered[filtered["year"]==year].corr().iloc[1, 2])
		years.append(year)
	corr = dict(
		correlation=corr,
		year=years,
	)
	fig = px.line(corr, x="year", y="correlation", template="plotly_dark", title=title)
	fig.update_layout({
		"plot_bgcolor": "rgba(0, 0, 0, 0)",
		"paper_bgcolor": "rgba(0, 0, 0, 0)",
	})

	return fig