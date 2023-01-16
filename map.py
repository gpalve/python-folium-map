import folium
import webbrowser
import pandas as pd

class Map:
    def __init__(self, center, zoom_start):
        self.center = center
        self.zoom_start = zoom_start
    
    def showMap(self):
        #Create the map
        df1 = pd.read_csv(f'route1.csv')
        df2 = pd.read_csv(f'route2.csv')
        df5 = pd.read_csv(f'route5.csv')
        latitude = df1['latitude']
        longitude = df1['longitude']
        latitude2 = df2['latitude']
        longitude2 = df2['longitude']
        latitude5 = df5['Latitude']
        longitude5 = df5['Longitude']

        
        my_map = folium.Map()
        
        folium.PolyLine(list(zip(latitude, longitude)), color='green', weight=2.5, opacity=1).add_to(my_map)
        folium.PolyLine(list(zip(latitude2, longitude2)), color='red', weight=2.5, opacity=1).add_to(my_map)
        folium.PolyLine(list(zip(latitude5, longitude5)), color='violet', weight=2.5, opacity=1).add_to(my_map)

        #Display the map
        my_map.save("map.html")
        webbrowser.open("map.html")


#Define coordinates of where we want to center our map
coords = [51.5074, 0.1278]
map = Map(center = coords, zoom_start = 13)
map.showMap()