#!/usr/bin/env python3

class Building:

    def __init__(self, building: str, room: str):
        self.building = building
        self.room = room
        print("hi")

    def __str__(self):
        return "Building Code: {0}\nRoom Number: {1}".format(self.building, self.room)
    
    def __repr__(self):
        return str(self)