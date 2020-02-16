#!/usr/bin/env python3

from ics import Calendar, Event
import datetime

def generateCal(courseList):
    c = Calendar()

    for course in courseList:
        e = Event()
        