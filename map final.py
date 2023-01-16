
import folium
import webbrowser
import pandas as pd
import random


class Map:
    def __init__(self, location, zoom_start):
        self.location = location
        self.zoom_start = zoom_start

    def showMap(self):
        # Create the map
        my_map = folium.Map(location=[21, 78], zoom_start=6)

        colors = ['red', 'green', 'darkorchid4', 'darkorange4', 'darkorange1', 'darkgreen', 'cyan4', 'crimson', 'coral',
                  'burntumber', 'blue4', 'black', 'bisque4', 'lightpink3', 'mediumorchid4']        # for j in range(15):
        #     rand_colors = "#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])
        #     colors.append(rand_colors)
        print(colors)
        for i in range(1, 16):
            lat = pd.read_excel(f'route{i}.xlsx')['Latitude']
            longi = pd.read_excel(f'route{i}.xlsx')['longitude']
            stn = pd.read_excel(f'route{i}.xlsx')['Station']
            code = pd.read_excel(f'route{i}.xlsx')['Code']
            dist = pd.read_excel(f'route{i}.xlsx')['Distance']

            folium.PolyLine(list(zip(
                lat, longi)), color=colors[i-1], width=750, height=500, weight=5, opacity=2).add_to(my_map)
            for j in range(0, len(lat)-1, 10):
                # start_stn = stn[0]
                # end_stn  = stn[-1]
                folium.Marker([lat[j], longi[j]], popup="<b>Station: </b>" + "\n" + stn[j]+ "\n"   +
                              "<b>Code: </b>"+ "\n"  + str(code[j]) + "\n" + "<b>Distance: </b>"+ "\n"  + str(dist[j])).add_to(my_map)
                # folium.Marker(icon=folium.Icon(icon='star'))
            my_map.save("map.html")
        webbrowser.open("map.html")


# Define coordinates of where we want to center our map

map = Map((52, 0), zoom_start=8)


map.showMap()

# %%
