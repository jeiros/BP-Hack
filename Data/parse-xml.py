import xml.etree.ElementTree as ET
import numpy as np
import requests
import json
import googlemaps
from datetime import datetime
gmaps = googlemaps.Client(key='AIzaSyCqRbZGdjXPN_YUAQbXHPB5760dKXcTq20')
import pandas as pd


def location():
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    lat = j['latitude']
    lon = j['longitude']
    return np.array([lat,lon])


def closest_node(point, coordinates):
    coordinates = np.asarray(coordinates)
    dist_2 = np.sum((coordinates.T - point)**2, axis=1)
    return np.argmin(dist_2)



if __name__ == '__main__':
    dict_data = {"name" : [],"latitude" : [], "longitude" : [],"openingHoursMonday" : [],
                 "openingHoursTuesday": [], "openingHoursWednesday" : [], "openingHoursThursday":[],
                 "openingHoursFriday":[], "openingHoursSaturday":[], "openingHoursSunday":[],"keywords" : [],}
    tree = ET.parse('./bpxml.xml')
    root = tree.getroot()
    #position==location()
    position=np.array([51.5132691, -0.2250459])
    for i, elem in enumerate(root):
        for children in elem.getchildren():
            for j in dict_data.keys():
                if j in repr(children):
                    dict_data[j].append(children.text.rstrip())
    df=pd.DataFrame.from_dict(dict_data)
    print(type(dict_data["latitude"]))
    coords=np.array([df.latitude.astype(float),df.longitude.astype(float)])
    where=closest_node(position,coords)
    destination = gmaps.reverse_geocode((coords[0][where],coords[1][where]))
    origin = gmaps.reverse_geocode((position[0], position[1]))
    now = datetime.now()
    directions_result = gmaps.directions(origin[0]["formatted_address"], destination[0]["formatted_address"], mode="driving", departure_time=now)
    #print(directions_result[0])
    print(origin[0]["formatted_address"])
    print(destination[0]["formatted_address"])
    print(df.iloc[where]["name"],df.iloc[where]["keywords"])
        #print(now)
