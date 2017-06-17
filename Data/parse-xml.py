import xml.etree.ElementTree as ET
import numpy as np
import requests
import json
import googlemaps
from datetime import datetime
gmaps = googlemaps.Client(key='AIzaSyCqRbZGdjXPN_YUAQbXHPB5760dKXcTq20')
import pandas as pd
import xmltodict


def location():
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    lat = j['latitude']
    lon = j['longitude']
    return np.array([lat,lon])


def closest_node(point, coordinates):
    coordinates = np.asarray(coordinates)
    dist_2 = np.sum((coordinates - point)**2, axis=1)
    return np.argmin(dist_2)



if __name__ == '__main__':
    dict_data = {"LA" : [], "LO" : [],"openingHoursMonday" : [],
                 "openingHoursTuesday": [], "openingHoursWednesday" : [], "openingHoursThursday":[],
                 "openingHoursFriday":[], "openingHoursSaturday":[], "openingHoursSunday":[]}
    tree = ET.parse('./bpxml.xml')
    root = tree.getroot()
    print
    dict(xmltodict.parse('./bpxml.xml')['poiid'])
    #position==location()
    position=np.array([51.5132691, -0.2250459])
    coords = np.empty((len(root), 2))
    if False:
        for i, elem in enumerate(root):
            for children in elem.getchildren():
                if 'latitude' in repr(children):
                    lat = children
                elif 'longitude' in repr(children):
                    lon = children
                elif 'openingHoursMonday' in repr(children):
                    mon=children
            coords[i] = (float(lat.text), float(lon.text))
            #dict_data.append([float(lat.text),float(lat.text),mon,tu,wed,thu,fri,sat,sun])
    if False:
        where=closest_node(position,coords)
        destination = gmaps.reverse_geocode((coords[where][0],coords[where][1]))
        origin = gmaps.reverse_geocode((position[0], position[1]))
        now = datetime.now()
        directions_result = gmaps.directions(origin[0]["formatted_address"], destination[0]["formatted_address"], mode="driving", departure_time=now)
        print(directions_result[0])
        print(origin[0]["formatted_address"])
        print(destination[0]["formatted_address"])
        #print(now)
        print(data.head())
