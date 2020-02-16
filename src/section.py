#!/usr/bin/env python3
from room import Building

class Section:

    # Initializer
    # to create the object, use Section(day, start, end, room, isLecture)
    def __init__(self, day: str, start, end, building: Building, room: str, isLecture: bool):
        self.day = day
        self.start = start
        self.end = end
        self.room = building + room
        self.isLecture = isLecture
        print("hi")

    def __str__(self):
        return "Section Days: {0}\nClass Start Time: {1}\nClass End Time: {2}\nRoom: {3}\nLecture: {4}".format(self.day, self.start, self.end, self.room, self.isLecture)

    def __repr__(self):
        return str(self)