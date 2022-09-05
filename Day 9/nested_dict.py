travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

def add_new_country(name_of_country, no_of_visits, cities_list):
    # new_country = {
    #     "country": name_of_country,
    #     "visits": no_of_visits,
    #     "cities": cities_list
    # }

    #Another method
    new_country = {}
    new_country["country"] = name_of_country
    new_country["visits"] = no_of_visits
    new_country["cities"] = cities_list
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)