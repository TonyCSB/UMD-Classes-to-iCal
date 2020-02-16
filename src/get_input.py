#!/usr/bin/env python3

import re
from course import Course

def getInput():
    termId = input("Enter the term ID: ")
    courseInput = input("Enter a course (Press <ENTER> to break): ")
    
    courseList = []

    while courseInput != "":
        courseList.append(createCourse(courseInput, termId))
        courseInput = input("Enter a course (Press <ENTER> to break): ")

    return courseList

def createCourse(courseInput, termId):
    regex = r'^([a-zA-Z]{4})\W*(\d{3}[a-zA-Z]?)\W*(\d{4})?$'
    match = re.search(regex, courseInput)
    courseId = (match.group(1) + match.group(2)).upper()
    section = ""
    if match.group(3) is None:
        section = input("Enter the section number: ")
    else:
        section = match.group(3)
    course = Course(courseId, section, termId)
    
    print()
    print(course)
    return course

if __name__ == "__main__":
    getInput()
