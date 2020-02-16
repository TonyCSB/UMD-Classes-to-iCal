#!/usr/bin/env python3
import requests

class Building:

    def __init__(self, building: str, room: str):
        self.building = building
        self.room = room
        print("hi")
        self.buildingName = ""
        self.address = ""
        self.city = ""
        self.state = ""
        self.zip = 0
        
        idJson = requests.get("https://maps.umd.edu/arcgis/rest/services/Layers/CampusMapDefault/MapServer/0/query?f=json&where=UPPER(NAME)%20like%20%27%25" + building + "%25%27%20OR%20BUILDINGID%20like%20%27%25" + building + "%25%27%20OR%20UPPER(BLDG_CODE)%20like%20%27%25ESJ%25%27&outFields=BUILDINGID").json()
        if page.status_code != 200:
            raise ValueError("Unknown Error - Website Out of Reach")
        print(idJson)
        

    def __str__(self):
        return "Building Code: {0}\nRoom Number: {1}".format(self.building, self.room)
    
    def __repr__(self):
        return str(self)