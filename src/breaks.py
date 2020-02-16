#!/usr/bin/env python3
import requests
import re
from datetime import datetime
from bs4 import BeautifulSoup

fallYear = 2019
springYear = 2020

url = "https://www.provost.umd.edu/calendar/19.html"
page = requests.get(url)

# check connectivity
if page.status_code != 200:
    raise ValueError("Unknown Error - Website Out of Reach")

# parse the website with BeautifulSoup
soup = BeautifulSoup(page.text, features = 'html.parser')
tableResults = soup.findAll('td', {'class': 'views-field views-field-field-description'})

lastDaySeen = False
fall = []
laborDay = None
thanksgiving = []
spring = []
springBreak = []

for element in tableResults:
    result = element.find_next('td').get_text().strip()
    result = result.replace(")", ") ")
    result = result.strip().split()
    result[:] = [word for word in result if not ")" in word]

    result[1] = re.sub('[A-Za-z]', '', result[1])
    if len(result[1]) == 1:
        result[1] = "0" + result[1]
    if 3 < len(result):
        result[3] = re.sub('[A-Za-z]', '', result[3])
        if len(result[3]) == 1:
            result[3] = "0" + result[3]

    if element.get_text().strip() == "First Day of Class":
        fall.append(datetime.strptime((" ".join(result) + " " + str(fallYear)), '%B %d %Y'))
    elif element.get_text().strip() == "Labor Day":
        laborDay = datetime.strptime((" ".join(result) + " " + str(fallYear)), '%B %d %Y')
    elif element.get_text().strip() == "Thanksgiving Recess":
        thanksgiving.append(datetime.strptime((result[0] + " " + result[1] + " " + str(fallYear)), '%B %d %Y'))
        thanksgiving.append(datetime.strptime((result[2] + " " + result[3] + " " + str(fallYear)), '%B %d %Y'))
    elif element.get_text().strip() == "Last Day of Classes" and not lastDaySeen:
        lastDaySeen = True
        fall.append(datetime.strptime((" ".join(result) + " " + str(fallYear)), '%B %d %Y'))
    elif element.get_text().strip() == "First Day of Classes":
        spring.append(datetime.strptime((" ".join(result) + " " + str(springYear)), '%B %d %Y'))
    elif element.get_text().strip() == "Spring Break":
        springBreak.append(datetime.strptime((result[0] + " " + result[1] + " " + str(springYear)), '%B %d %Y'))
        springBreak.append(datetime.strptime((result[2] + " " + result[3] + " " + str(springYear)), '%B %d %Y'))
    elif element.get_text().strip() == "Last Day of Classes" and lastDaySeen:
        spring.append(datetime.strptime((" ".join(result) + " " + str(springYear)), '%B %d %Y'))