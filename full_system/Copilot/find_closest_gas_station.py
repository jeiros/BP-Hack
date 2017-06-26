import xml.etree.ElementTree as ET
import numpy as np
import requests
import json
import googlemaps
from datetime import datetime
import pandas as pd
import certifi

gmaps = googlemaps.Client(key='AIzaSyCqRbZGdjXPN_YUAQbXHPB5760dKXcTq20')


def location():
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    lat = j['latitude']
    lon = j['longitude']
    return np.array([lat, lon])


def closest_node(point, coordinates):
    coordinates = np.asarray(coordinates)
    dist_2 = np.sum((coordinates.T - point)**2, axis=1)
    return np.argmin(dist_2)


def get_closest_gas_station():
    return ("47 Shepherd's Bush Green, Shepherd's Bush, London W12 8PS, UK", 'BP Bush Centre Connect')
    try:
        df = pd.read_csv("./data_frame_gas_stations.csv")

    except:
        dict_data = {"name": [], "latitude": [], "longitude": [], "openingHoursMonday": [],
                     "openingHoursTuesday": [], "openingHoursWednesday": [], "openingHoursThursday": [],
                     "openingHoursFriday": [], "openingHoursSaturday": [], "openingHoursSunday": [], "keywords": [], }
        tree = ET.parse('./bpxml.xml')
        root = tree.getroot()
        for i, elem in enumerate(root):
            for children in elem.getchildren():
                for j in dict_data.keys():
                    if j in repr(children):
                        dict_data[j].append(children.text.rstrip())
        df = pd.DataFrame.from_dict(dict_data)
        df.to_csv("./data_frame_gas_stations.csv", index=False,  encoding='utf-8')

    # position = location()
    position = np.array([51.5132691, -0.2250459])
    coords = np.array([df.latitude.astype(float), df.longitude.astype(float)])
    where = closest_node(position, coords)
    print(coords)
    # import IPython; IPython.embed()
    # destination = gmaps.reverse_geocode((coords[0][where], coords[1][where]))

    origin = gmaps.reverse_geocode((position[0], position[1]),)
    now = datetime.now()
    directions_result = gmaps.directions(origin[0]["formatted_address"], destination[
                                         0]["formatted_address"], mode="driving", departure_time=now)

    # retorna la destinacio i el nom
    # Format the destination and address
    destination = ' '.join(destination[0]["formatted_address"].split())
    address_name = ' '.join(df.iloc[where]["name"].split())
    # return destination, address_name

if __name__ == '__main__':
    get_closest_gas_station()
