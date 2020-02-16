#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

class Course:

    # Initializer
    # to create the object, use Course(courseId, sectionId, termId)
    def __init__(self, courseId: str, sectionId: str, termId: str):
        url = getUrl(courseId, sectionId, termId)
        page = requests.get(url)

    def __str__(self):
        print()

    def __repr__(self):
        return str(self)

def main():
    # For test purpose only
    c = Course("CMSC132", "0101", "202001")
    print(c)

def getUrl(courseId, sectionId, termId):
    return "https://app.testudo.umd.edu/soc/search?courseId={0}&sectionId={1}&termId={2}&_openSectionsOnly=on&creditCompare=&credits=&courseLevelFilter=ALL&instructor=&_facetoface=on&_blended=on&_online=on&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&teachingCenter=ALL&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on".format(courseId, sectionId, termId)

if __name__ == "__main__":
    main()