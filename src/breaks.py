#!/usr/bin/env python3
import requests
import re
from datetime import datetime
from datetime import timedelta
from bs4 import BeautifulSoup

fall = []
spring = []

def breaks(year):
    url = ""
    if year == 2019:
        url = "https://www.provost.umd.edu/calendar/19.html"
    elif year == 2020:
        url = "https://svp.umd.edu/node/1920"
    elif year == 2021:
        url = "https://svp.umd.edu/node/3010"
    page = requests.get(url)

    # check connectivity
    if page.status_code != 200:
        raise ValueError("Unknown Error - Website Out of Reach")

    # parse the website with BeautifulSoup
    soup = BeautifulSoup(page.text, features = 'html.parser')
    tableResults = soup.findAll('td', {'class': 'views-field views-field-field-description'})

    firstDaySeen = False
    lastDaySeen = False

    fallFirst = []
    fallSecond = []
    fallThird = []
    springFirst = []
    springSecond = []

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

        if "First Day" in element.get_text().strip() and not firstDaySeen:
            firstDaySeen = True
            fallFirst.append(datetime.strptime((" ".join(result) + " " + str(year)), '%B %d %Y'))
        elif element.get_text().strip() == "Labor Day":
            fallFirst.append(datetime.strptime((" ".join(result) + " " + str(year)), '%B %d %Y') - timedelta(days = 1))
            fallSecond.append(fallFirst[1] + timedelta(days = 2))
        elif element.get_text().strip() == "Thanksgiving Recess":
            fallSecond.append(datetime.strptime((result[0] + " " + result[1] + " " + str(year)), '%B %d %Y') - timedelta(days = 1))
            fallThird.append(datetime.strptime((result[2] + " " + result[3] + " " + str(year)), '%B %d %Y') + timedelta(days = 1))
        elif element.get_text().strip() == "Last Day of Classes" and not lastDaySeen:
            lastDaySeen = True
            fallThird.append(datetime.strptime((" ".join(result) + " " + str(year)), '%B %d %Y'))
        elif "First Day" in element.get_text().strip() and firstDaySeen:
            springFirst.append(datetime.strptime((" ".join(result) + " " + str(year + 1)), '%B %d %Y'))
        elif element.get_text().strip() == "Spring Break":
            springFirst.append(datetime.strptime((result[0] + " " + result[1] + " " + str(year + 1)), '%B %d %Y') - timedelta(days = 1))
            springSecond.append(datetime.strptime((result[2] + " " + result[3] + " " + str(year + 1)), '%B %d %Y') + timedelta(days = 1))
        elif element.get_text().strip() == "Last Day of Classes" and lastDaySeen:
            springSecond.append(datetime.strptime((" ".join(result) + " " + str(year + 1)), '%B %d %Y'))

    fall.append(fallFirst)
    fall.append(fallSecond)
    fall.append(fallThird)
    spring.append(springFirst)
    spring.append(springSecond)

def main(year:int):
    breaks(year)

if __name__ == "__main__":
    main(2019)