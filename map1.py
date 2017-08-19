import folium
import pandas

map = folium.Map(location=[47.586160, -122.308046], zoom_start=7)

fg = folium.FeatureGroup(name="My Map")

data = pandas.read_csv("data.csv")

location = list(data["Names"])
lat = list(data["Lat"])
lon = list(data["Lon"])

for lt, ln, lc in zip(lat, lon, location):
    fg.add_child(folium.Marker(location=[lt, ln], popup="%s" % lc, icon=folium.Icon(color='green')))

fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig'), 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 1000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)

map.save("Map1.html")
