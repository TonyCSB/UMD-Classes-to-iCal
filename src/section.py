#!/usr/bin/env python3
from room import Building
from enum import Enum
import datetime, re

class Day(Enum):
    Sunday = "SU"
    Monday = "MO"
    Tuesday = "TU"
    Wednesday = "WE"
    Thursday = "TH"
    Friday = "FR"
    Saturday = "SA"

class Section:

    # Initializer
    # to create the object, use Section(day, start, end, room, isLecture)
    def __init__(self, day: str, start: str, end: str, building: str, room: str, isLecture: bool):

        # initialize the values
        if day != None:
            self.day = processDay(day)
            self.start = processTime(start)
            self.end = processTime(end)
            self.room = Building(building, room)
            self.online = False
        else:
            self.day, self.start, self.end, self.room = None, None, None, None
            self.online = True
        self.isLecture = isLecture

    def __str__(self):
        return "Section Days: {0}\nClass Start Time: {1}\nClass End Time: {2}\nRoom: \n\n{3}\n\n\nLecture: {4}".format(self.day, self.start, self.end, self.room, self.isLecture)

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

def processTime(time):
    regex = r"^(\d?\d):(\d{2})(am|pm)$"
    match = re.search(regex, time)
    
    hour = int(match.group(1))
    minute = int(match.group(2))

    if match.group(3) == "pm" and hour != 12:
        hour = hour + 12

    if hour == 12 and match.group(3) == "am":
        hour = 0

    return datetime.time(hour, minute)