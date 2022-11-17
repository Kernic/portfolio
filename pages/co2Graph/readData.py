#! /usr/bin/python
import pandas as pds

def get_data():
	df = pds.read_csv("./data/owid-co2-data.csv")
	G20 = [
		"Argentina",
		"Australia",
		"Brazil",
		"Canada",
		"China",
		"France",
		"Germany",
		"India",
		"Indonesia",
		"Italy",
		"Japan",
		"Mexico",
		"South Korea",
		"Russia",
		"Saudi Arabia",
		"South Africa",
		"Turkey",
		"United Kingdom",
		"United States",
		"European Union (27)",
	]

	countries = []
	df_na = df.fillna(0)
	for idx in range(len(df_na)):
		if df_na.iloc[idx]["iso_code"] != 0 and df_na.iloc[idx]["country"] not in countries:
			countries.append(df_na.iloc[idx]["country"])

	EU = [
		"France",
		"Germany",
		"Italy",
		"Austria",
		"Belgium",
		"Bulgaria",
		"Coratia",
		"Cyprus",
		"Czech Republic",
		"Exstonia",
		"Finland",
		"Greece",
		"Hungary",
		"Ireland",
		"Latvia",
		"Lithuania",
		"Luxembourg",
		"Malta",
		"Netherlands",
		"Poland",
		"Portugal",
		"Romania",
		"Slovakia",
		"Slovenia",
		"Spain",
		"Sweden",
	]

	Africa = [
		"Algeria",
		"Angola",
		"Benin",
		"Botswana",
		"Burkina Faso",
		"Burundi",
		"Cameroon",
		"Cameroun",
		"Cape Verde",
		"Central African Republic",
		"Chad",
		"Tchad",
		"Comoros",
		"Republic of the Congo",
		"Democratic Republic of the Congo",
		"Côte d'Ivoire",
		"Ivory Coast",
		"Djibouti",
		"Equatorial Guinea",
		"Egypt",
		"Eritrea",
		"Ethiopia",
		"Gabon",
		"The Gambia",
		"Ghana",
		"Guinea",
		"Guinea-Bissau",
		"Kenya"
		"Lesotho",
		"Liberia",
		"Libya",
		"Madagascar",
		"Malawi",
		"Mali",
		"Mauritania",
		"Mauritius",
		"Morocco",
		"Mozambique",
		"Namibia",
		"Niger",
		"Nigeria",
		"Rwanda",
		"São Tomé and Príncipe",
		"Senegal",
		"Seychelles",
		"Sierra Leone",
		"Somalia",
		"South Africa",
		"South Sudan",
		"Sudan",
		"Swaziland",
		"Tanzania",
		"Togo",
		"Tunisia",
		"Uganda",
		"Western Sahara",
		"Zambia",
		"Zimbabwe",
	]

	Asia = [
		"Afghanistan",
		"Armenia",
		"Azerbaijan",
		"Bahrain",
		"Bangladesh",
		"Bhutan",
		"Brunei",
		"Cambodia",
		"China",
		"East Timor",
		"Georgia",
		"India",
		"Indonesia",
		"Iran",
		"Iraq",
		"Israel",
		"Japan", 
		"Jordan",
		"Kazakhstan",
		"Kuwait",
		"Kyrgyzstan",
		"Laos",
		"Lebanon",
		"Malaysia",
		"The Maldives",
		"Mongolia",
		"Myanmar",
		"Nepal",
		"North Korea",
		"Oman",
		"Pakistan",
		"Palestine",
		"The Philippines",
		"Qatar",
		"Russia",
		"Saudi Arabia",
		"Singapore",
		"South Korea",
		"Sri Lanka",
		"Syria",
		"Taiwan",
		"Tajikistan",
		"Thailand",
		"Turkey",
		"Turkmenistan",
		"United Arab Emirates",
		"Uzbekistan",
		"Vietnam",
		"Yemen",
	]

	Europe = [
		"Albania",
		"Andorra",
		"Austria",
		"Belarus",
		"Belgium",
		"Bosnia and Herzegovina",
		"Bulgaria",
		"Croatia",
		"Cyprus",
		"Czech Republic",
		"Denmark",
		"Estonia",
		"Finland",
		"France",
		"Georgia",
		"Germany",
		"Greece",
		"Hungary",
		"Iceland",
		"Ireland",
		"Italy",
		"Kosovo",
		"Latvia",
		"Liechtenstein",
		"Lithuania",
		"Luxembourg",
		"North Macedonia",
		"Malta",
		"Moldova",
		"Monaco",
		"Montenegro",
		"Netherlands",
		"Norway",
		"Poland",
		"Portugal",
		"Romania",
		"San Marino",
		"Serbia",
		"Slovakia",
		"Slovenia",
		"Spain",
		"Sweden",
		"Switzerland",
		"Turkey",
		"Ukraine",
		"United Kingdom",
		"Vatican City",
	]
	
	NAmerica = [
		"Canada",
		"Mexico",
		"United States",
		"Navassa Island",
		"Dominican Republic",
		"Cuba",
		"Haiti",
		"Belize",
		"Costa Rica",
		"El Salvador",
		"Guatemala",
		"Honduras",
		"Nicaragua",
		"Panama",
		"Jamaica",
		"Bahamas",
		"Barbados",
		"Dominica",
	]

	SAmerica = [
		"Brazil",
		"Argentina",
		"Bolivia",
		"Chile",
		"Colombia",
		"Ecuador",
		"Guyana",
		"Paraguay",
		"Peru",
		"Suriname",
		"Trinidad and Tobago",
		"Uruguay",
		"Venezuela"
	]

	Oceania = [
		"Australia",
		"Fiji",
		"New Zealand",
		"Federated States of Micronesia",
		"Kiribati",
		"Marshall Islands",
		"Nauru",
		"Palau",
		"Papua New Guinea",
		"Samoa",
		"Solomon Islands",
		"Tonga",
		"Tuvalu",
		"Vanuatu",
	]

	return df, countries, G20, EU, Africa, Asia, Europe, NAmerica, SAmerica, Oceania