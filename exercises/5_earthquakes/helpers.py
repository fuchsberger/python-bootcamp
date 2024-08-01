import urllib.request
import json

import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

def response(url):
    """
    Loads and interprets json content from a given url.
    """
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read())


def preprocess(raw):
    """
    Converts a raw python dictionary with earthquake data into a list of dictionaries.

    [
        {
            "mag": 2.9,
            "latitude": -30.23,
            "longitude": 34.34
        }
    ]
    """


    data = []

    for eq in raw["features"]:

        mag = eq["properties"]["mag"]
        lat = eq["geometry"]["coordinates"][1]
        long = eq["geometry"]["coordinates"][0]

        if mag < 0:
            continue

        data.append({
            "mag": mag,
            "lat": lat,
            "long": long
        })

    # safe it to processed.json
    f = open("processed.json", "w")
    f.write(json.dumps(data))
    f.close()



    return data






#     # f = open("raw.json", "w")
#     # f.write(json.dumps(raw, indent=2))
#     # f.close()

#     # print(raw["features"])

#     data = [{
#         "mag": e["properties"]["mag"],
#         "lat": e["geometry"]["coordinates"][1],
#         "long": e["geometry"]["coordinates"][0],
#     } for e in raw["features"] if e["properties"]["mag"] > 1]

#     data = sorted(data, key=lambda i: i['mag'], reverse=True)

#     # print(data)

#     # f = open("data.json", "w")
#     # f.write(json.dumps(data, indent=2))
#     # f.close()

#     return data


def plot(data):
    """
    Plots the graph.any
    """

    df = pd.DataFrame(data)

    # initialize an axis
    fig, ax = plt.subplots(figsize=(4,4))

    countries = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

    countries[countries["name"] == "United States of America"].plot(color="lightgrey", ax=ax)

    # plot points
    df.plot(x="long", y="lat", kind="scatter", c="mag", colormap="YlOrRd", title=f"Today's earthquakes over US Mainland", ax=ax)

#     # add grid
    # ax.grid(b=True, alpha=0.5)

    # restrict the map to the following coordinates
    plt.xlim([-170, -70])
    plt.ylim([20, 75])


    plt.show()
