#11-1
def city_country(city, country,population=0):
	formatted_city_country = city.title() + ', ' + country.title()
	if population:
		formatted_city_country += " - population " + str(population)
	return formatted_city_country
