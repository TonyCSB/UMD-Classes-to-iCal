#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

url = "https://www.provost.umd.edu/calendar/19.html"
page = requests.get(url)

# check connectivity
if page.status_code != 200:
    raise ValueError("Unknown Error - Website Out of Reach")

# parse the website with BeautifulSoup
soup = BeautifulSoup(page.text, features = 'html.parser')
firstDay = soup.find('td', {'class': 'views-field views-field-field-description'})
print(firstDay)