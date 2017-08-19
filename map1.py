import folium
import pandas

map = folium.Map(location=[47.586160, -122.308046], zoom_start=10)

fg = folium.FeatureGroup(name="My Map")

data = pandas.read_csv("data.csv")

location = list(data["Names"])
lat = list(data["Lat"])
lon = list(data["Lon"])

for lt, ln, lc in zip(lat, lon, location):
    fg.add_child(folium.Marker(location=[lt, ln], popup="%s" % lc, icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")
