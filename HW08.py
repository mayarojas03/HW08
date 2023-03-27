
#///////////////////////////////////////////////////////#

def inSeason(favDrinks, currentMonth):
    
    inSeasonDict = {
        "January": [],
        "February": ["mango"],
        "March": ["matcha", "oolong tea"],
        "April": [],
        "May": ["pina colada smoothie"],
        "June": ["green juice", "lychee passionfruit smoothie"],
        "July": ["blueberry smoothie", "acai", "coconut smoothie"],
        "August": ["mango smoothie"],
        "September": [],
        "October": ["flat white", "pumpkin pie smoothie"],
        "November": ["americano"],
        "December": ["jasmine latte", "london fog"] }
    
    inSeasonFruits = inSeasonDict.get(currentMonth, [])

    uncaffeinatedDrinks = [drink for drink in favDrinks if "caffeinated" not in drink]
    
    inSeasonDrinks = sorted([drink for drink in uncaffeinatedDrinks if any(fruit in drink for fruit in inSeasonFruits)])
  
    return inSeasonDrinks if inSeasonDrinks else "Nothing is in season :("

#///////////////////////////////////////////////////////#

def bestDrink(temp, drinks, caffeinated):
    perfect_drink = None
    bevDict = {}
    for drink in drinks:
        if abs(temp - drink_temps[drink]) <= 5 and caffeinated == drink_caf[drink]:
            perfect_drink = drink
        bevDict[drink] = (drink_temps[drink], drink_caf[drink])
    if perfect_drink:
        print(f"A {perfect_drink} is the perfect drink for today!")
    else:
        print("Guess I'll just have water.")
    return bevDict

#///////////////////////////////////////////////////////#

import requests

def possibleCities(favCountries):
    endpoint = "https://restcountries.com/v2/name/"
    destinationDict = {}

    for country in favCountries:
        url = endpoint + country
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()[0]
            if "languages" in data and any(lang["name"] == "English" for lang in data["languages"]):
                destinationDict[country] = data["capital"]

    return destinationDict

#///////////////////////////////////////////////////////#

def populationDensities(country):
    url = f"https://restcountries.com/v2/name/{country}?fullText=true"

    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json()[0]
    area = data["area"]
    population = data["population"]
    name = data["name"]
    density = population / area

    borders = data["borders"]
    border_densities = []
    for border in borders:
        border_url = f"https://restcountries.com/v2/alpha/{border}"
        border_response = requests.get(border_url)
        if border_response.status_code == 200:
            border_data = border_response.json()
            border_name = border_data["name"]
            border_area = border_data["area"]
            border_population = border_data["population"]
            border_density = border_population / border_area
            border_densities.append((border_name, border_density))

    border_densities.append((name, density))

    border_densities.sort
  #///////////////////////////////////////////////////////#

import csv
import requests

def countriesInfo(countriesList):
    header = ['Country', 'Capital', 'Population', 'Area']
    data = [header]
    
    for country in countriesList:
        response = requests.get(f'https://restcountries.com/v2/name/{country}')
        if response.status_code != 200:
            continue
        
        country_info = response.json()[0]
        name = country_info['name']
        capital = country_info['capital']
        population = country_info['population']
        area = country_info['area']
        
        data.append([name, capital, population, area])
    
    with open('countries.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
      
#///////////////////////////////////////////////////////#

def countriesInfo(countriesList):
    header = ['Country', 'Capital', 'Population', 'Area']
    data = [header]
    
    for country in countriesList:
        response = requests.get(f'https://restcountries.com/v2/name/{country}')
        if response.status_code != 200:
            continue
        
        country_info = response.json()[0]
        name = country_info['name']
        capital = country_info['capital']
        population = country_info['population']
        area = country_info['area']
        
        data.append([name, capital, population, area])
    
    with open('countries.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
