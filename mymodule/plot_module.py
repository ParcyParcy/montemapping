import re
import folium
import numpy as np
import pandas as pd
import lxml.html



def plot_mdl(path):
    with open(path) as key:
        fileobj = key.read()
    latlon = fileobj.split('\n')
    latlon = [x for x in latlon if x]

    time_l = []
    lat_l = []
    lon_l = []
    node_l = []
    for i in range(len(latlon)):
        time_1 = re.search(r'\d{2}\S\d{2}.\d{2}', latlon[i]).group()
        lat_1 = re.search(r'\d{2}.\d{6}', latlon[i]).group()
        lon_1 = re.search(r'\d{3}.\d{6}', latlon[i]).group()
        node_1 = re.search(r'\w{4}\S\d{4}', latlon[i]).group()
        time_l.append(time_1)
        lat_l.append(lat_1)
        lon_l.append(lon_1)
        node_l.append(node_1)
    time_s = pd.Series(time_l)
    lat_s = pd.Series(lat_l)
    lon_s = pd.Series(lon_l)
    node_s = pd.Series(node_l)
    df = pd.DataFrame({'time': time_s,
                       'lat': lat_s,
                       'lon': lon_s,
                       'node': node_s})
    df_1 = df[df.node == "NODE:0001"].drop('node', axis=1)
    df_2 = df[df.node == "NODE:0002"].drop('node', axis=1)

    df_1_lat = pd.Series(df_1['lat'].astype(np.float64))
    l_1_lat = df_1_lat.tolist()

    df_1_lon = pd.Series(df_1['lon'].astype(np.float64))
    l_1_lon = df_1_lon.tolist()

    df_1_time = pd.Series(df_1['time'])
    l_1_time = df_1_time.tolist()

    df_2_time = pd.Series(df_2['time'])
    l_2_time = df_2_time.tolist()

    df_2_lat = pd.Series(df_2['lat'].astype(np.float64))
    l_2_lat = df_2_lat.tolist()

    df_2_lon = pd.Series(df_2['lon'].astype(np.float64))
    l_2_lon = df_2_lon.tolist()

    last_1_lat = l_1_lat[-5:]
    last_1_lon = l_1_lon[-5:]
    last_1_time = l_1_time[-5:]
    last_2_lat = l_2_lat[-5:]
    last_2_lon = l_2_lon[-5:]
    last_2_time = l_2_time[-5:]

    map = folium.Map(location=[last_1_lat[-1], last_1_lon[-1]], zoom_start=16)  # max_zoom=18

    for a, b, c in zip(last_1_lat, last_1_lon, last_1_time):
        folium.Marker(location=[a, b], popup=c, icon=folium.Icon(color='red')).add_to(map)
    for a, b, c in zip(last_2_lat, last_2_lon, last_2_time):
        folium.Marker(location=[a, b], popup=c, icon=folium.Icon(color='blue'), ).add_to(map)
    map.save('templates/map.html')

    # html = open('templates/map.html').read()
    # dom = lxml.html.fromstring(html)
    # size = dom.xpath('//style')[0]
    # size.text = 'html, body {width: 70%;height: 70%;margin: 0;padding: 0;}'

