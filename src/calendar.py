#!/usr/bin/env python3

from ics import Calendar, Event
from course import Course
from section import Section
import datetime

def generateCal(courseList):
    c = Calendar()

    for course in courseList:
        for section in course.sectionList:
        e = Event()
        e.name = 