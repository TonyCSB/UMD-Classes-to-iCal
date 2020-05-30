#!/usr/bin/env python3
from user import User
from course import Course
import requests, json

SCHEDULE_URL = "https://app.testudo.umd.edu/services/schedule/"

def scrape(user:User, termid:str):
    s = requests.Session()
    s.cookies.update(user.cookie)

    r = s.get(url = SCHEDULE_URL + termid)
    if r.status_code == 503:
        print("ERROR: " + r.text)
        return None

    data = r.json()

    courseList = []

    for c in data["courseMap"]:
        s = data["courseMap"][c]["sectionId"]
        t = data["courseMap"][c]["termId"]
        c = data["courseMap"][c]["courseCode"]
        courseList.append(Course(c["code"], s, t))

    return courseList

if __name__ == "__main__":
    scrape(None, "202008")