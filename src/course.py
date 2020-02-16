#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

class Course:

    # Initializer
    # to create the object, use Course(courseId, sectionId, termId)
    def __init__(self, courseId: str, sectionId: str, termId: str):
        url = getUrl(courseId, sectionId, termId)

        self.courseId = courseId
        self.sectionId = sectionId
        self.termId = termId

        page = requests.get(url)

        if page.status_code != 200:
            raise ValueError("Unknown Error - Website Out of Reach")

        soup = BeautifulSoup(page.text, features = 'html.parser')

        sectionInfo = soup.find('div', {'class':'class-days-container'})
        if sectionInfo == None:
            raise ValueError("Error - Course/Section doesn't exist")

    def __str__(self):
        return "Course Id: {0}\nSection Id: {1}\nTerm Id: {2}\n".format(self.courseId, self.sectionId, self.termId)

    def __repr__(self):
        return str(self)

def main():
    # For test purpose only
    c = Course("CMSC132", "0101", "202001")
    c.courseId
    print(c)

def getUrl(courseId, sectionId, termId):
    return "https://app.testudo.umd.edu/soc/search?courseId={0}&sectionId={1}&termId={2}&_openSectionsOnly=on&creditCompare=&credits=&courseLevelFilter=ALL&instructor=&_facetoface=on&_blended=on&_online=on&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&teachingCenter=ALL&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on".format(courseId, sectionId, termId)

if __name__ == "__main__":
    main()