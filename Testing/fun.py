

def get_formatted_name(first,last, middle = ''):
    #generate formatted name
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

def city_function(city_name, country_name):
    get_city_country_name = f"'{city_name}', '{country_name}'"
    return f"{get_city_country_name}"

