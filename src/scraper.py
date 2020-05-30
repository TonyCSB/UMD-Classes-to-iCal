#!/usr/bin/env python3
from user import User
import requests

SCHEDULE_URL = "https://app.testudo.umd.edu/services/schedule/"

def scrape(user:User, termid:str):
    s = requests.Session()
    s.cookies.update(user.cookie)

    r = s.get(url = SCHEDULE_URL + termid)
    if r.status_code == 503:
        print("ERROR: " + r.text)
        return None

    data = r.json()
    print(data)
    return True
