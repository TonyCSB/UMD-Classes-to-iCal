#!/usr/bin/env python3
import requests

class Building:

    def __init__(self, building: str, room: str):
        self.building = building
        self.room = room
        self.buildingName = ""
        self.address = ""
        self.city = ""
        self.state = ""
        self.zip = 0
        
        idDict = requests.get("https://maps.umd.edu/arcgis/rest/services/Layers/CampusMapDefault/MapServer/0/query?f=json&where=UPPER(NAME)%20like%20%27%25" + building + "%25%27%20OR%20BUILDINGID%20like%20%27%25" + building + "%25%27%20OR%20UPPER(BLDG_CODE)%20like%20%27%25ESJ%25%27&outFields=BUILDINGID").json()
        buildingId = idDict["features"][0]["attributes"]["BUILDINGID"]
        addressDict = requests.get("https://maps.umd.edu/arcgis/rest/services/Layers/CampusMapDefault/MapServer/9/query?f=json&where=BLDGNUM%20%3D%20%27" + buildingId + "%27&returnGeometry=false&outFields=BLDGNUM%2CNAME%2CSTREET%2CCITY%2CSTATE%2CZIP").json()
        self.buildingName = addressDict["features"][0]["attributes"]["NAME"]
        self.buildingName = self.buildingName.title()
        self.address = addressDict["features"][0]["attributes"]["STREET"]
        self.address = self.address.rstrip('.')
        self.city = addressDict["features"][0]["attributes"]["CITY"]
        self.state = addressDict["features"][0]["attributes"]["STATE"]
        self.zip = addressDict["features"][0]["attributes"]["ZIP"]

    def getAddress(self):
        return ", ".join([self.buildingName, self.city, self.state + " " + str(self.zip), "USA"])

    def __str__(self):
        return "Building Code: {0}\nRoom Number: {1}\nBuilding Name: {2}\nAddress: {3}\nCity: {4}\nState: {5}\nZip: {6}".format(self.building, self.room, self.buildingName, self.address, self.city, self.state, self.zip)
    
    def __repr__(self):
        return str(self)