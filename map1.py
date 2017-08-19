import folium
import pandas

map = folium.Map(location=[47.586160, -122.308046], zoom_start=9)

fg = folium.FeatureGroup(name="My Map")

data = pandas.read_csv("data.csv")

location = list(data["Names"])
lat = list(data["Lat"])
lon = list(data["Lon"])

for place in range(0, len(location)):
    fg.add_child(folium.Marker(location=[lat[place], lon[place]], popup="%s" % location[place], icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")
