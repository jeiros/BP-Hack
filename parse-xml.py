import xml.etree.ElementTree as ET
import numpy as np

tree = ET.parse('./bpxml.xml')
root = tree.getroot()

coords = np.empty((len(root), 2))


for i, elem in enumerate(root):
  for children in elem.getchildren():
    if 'latitude' in repr(children):
      lat = children
    elif 'longitude' in repr(children):
      lon = children
  coords[i] = (float(lat.text), float(lon.text))
  
np.savetxt('./gas_stations_coords.csv', coords, delimiter=' ', fmt='%.4f')


