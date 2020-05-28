#!/usr/bin/env python3
import requests
from cookie import loadCookie

SCHEDULE_URL = "https://app.testudo.umd.edu/services/schedule/"

def scrape(termid:str):
  s = requests.Session()
  loadCookie(s)

  r = s.get(url = SCHEDULE_URL + termid)
  print(r.url, r.status_code)
  with open("a.html", "w") as f:
    f.write(r.text)
  return True

