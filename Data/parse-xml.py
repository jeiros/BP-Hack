import xml.etree.ElementTree as ET
import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.basemap import Basemap


# def draw_world():
#     return Basemap()


# def draw_UK():
#     return Basemap(projection='mill',
#                    resolution='f',
#                    lon_0=-5.23636, lat_0=53.866772,
#                    llcrnrlon=-10.65073, llcrnrlat=49.16209,
#                    urcrnrlon=1.76334, urcrnrlat=60.860699)

if __name__ == '__main__':

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

    np.savetxt('./gas_stations_coords.csv', coords, delimiter=',', fmt='%.4f')

    # lat = coords[:, 0]
    # lon = coords[:, 1]

    # # World plot
    # f, ax = plt.subplots(figsize=(14, 10))
    # m = draw_world()
    # m.fillcontinents(color='white', lake_color='#eeeeee')
    # m.drawstates(color='lightgray')
    # m.drawcoastlines(color='lightgray')
    # m.drawcountries(color='lightgray')
    # m.drawmapboundary(fill_color='#eeeeee')
    # style = dict(s=5, marker='o', alpha=0.5, zorder=2)
    # m.scatter(lon, lat, latlon=True,
    #           color='#00592D', **style)
    # f.savefig('world.png')

    # # UK plot
    # f, ax = plt.subplots(figsize=(10, 14))
    # m = draw_UK()
    # m.scatter(lon, lat, latlon=True, s=1, marker=',', color="steelblue", alpha=1)
    # m.fillcontinents(color='white', lake_color='#eeeeee', alpha=.2)
    # m.drawstates(color='lightgray')
    # m.drawcoastlines(color='lightgray')
    # m.drawcountries(color='lightgray')
    # m.drawmapboundary(fill_color='#eeeeee')
    # f.savefig('uk.png')
