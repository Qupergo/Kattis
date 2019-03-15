import folium
from geopy.geocoders import ArcGIS
import pandas as pd

arc = ArcGIS()
classmates = pd.DataFrame()
names = []
adress = []
postnumber = []
adresses = []
with open(r'klasskamrater.txt', 'r') as k:
    iteration = 0
    for i in k.readlines():
        iteration += 1

        if iteration == 1:
            names.append(i)
        if iteration == 4:
            adress.append(i)
        if iteration == 5:
            postnumber.append(i)
            iteration = 0

classmates['Names'] = [i for i in names]
classmates['Home Location'] = [arc.geocode(f"{adress[i]}, {postnumber[i]}") for i in range(len(adress))]

alve = {'name':'Alve Pilo', 'home_location':arc.geocode('Lars Påhls väg 24, Sweden, 26352')}
magnus_kerstin = {'name':'Magnus och Kerstin', 'home_location':arc.geocode('Ässjö 449, Hassela, Sweden, 82998')}

p = pd.DataFrame()
p['Names'] = [i for i in classmates['Names']]
p['Home Location'] = [i[0] for i in classmates['Home Location']]
p['Latitude'] = [i.latitude for i in classmates['Home Location']]
p['Longitude'] = [i.longitude for i in classmates['Home Location']]

peopleMap = folium.Map(location=[59.354752, 17.942070])
peopleMarkers = folium.FeatureGroup(name='People Markers')
for i in range(len(classmates['Names'])):
    peopleMarkers.add_child(folium.Marker(location=[p['Latitude'][i], p['Longitude'][i]], popup=f"{p['Names'][i]} {p['Home Location'][i]}", icon=folium.Icon(color='blue')))

peopleMap.add_child(peopleMarkers)
peopleMap.save('TE18C Locations.html')
