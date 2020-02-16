#!/usr/bin/env python3
from room import Building
from enum import Enum

class Day(Enum):
    Sunday = 0
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6

class Section:

    # Initializer
    # to create the object, use Section(day, start, end, room, isLecture)
    def __init__(self, day: str, start: str, end: str, building: str, room: str, isLecture: bool):
        self.day = processDay(day)
        self.start = start
        self.end = end
        self.room = building + room
        self.isLecture = isLecture
        print("hi")

    def __str__(self):
        return "Section Days: {0}\nClass Start Time: {1}\nClass End Time: {2}\nRoom: {3}\nLecture: {4}".format(self.day, self.start, self.end, self.room, self.isLecture)

    def __repr__(self):
        return str(self)

def processDay(day:str):
    dayList = []
    if "M" in day:
        dayList.append(Day.Monday)
    if "Tu" in day:
        dayList.append(Day.Tuesday)
    if "W" in day:
        dayList.append(Day.Wednesday)
    if "Th" in day:
        dayList.append(Day.Thursday)
    if "F" in day:
        dayList.append(Day.Friday)

    return dayList
    