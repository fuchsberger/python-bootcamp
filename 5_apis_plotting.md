# Instructions

Your goal is to draw a USA map and place all earthquake data points on the correct locations on the map.

- Do not color landmass, leave it white.
- the stronger an earthquake is, the larger the circle should be
- paint earquakes as red dots, tsunamis as blue dots and everything else with black dots.

### Loading API data from a web url

The following API provides data of all seismic activities that were detected on US soil in the last 24 hours:
[https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson)

Similarily to loading local files via `open()` and `read()` we can use a python library to load data from a weblink:
```python
import urllib.request
import inheritance
import json

url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson'

def response(url):
    with urllib.request.urlopen(url) as response:
        return response.read()

res = response(url)
print(json.loads(res))
```

### Preprocess data

As you can see in the print output, there is a lot of data, most of it irrellevant for us. In order to process the data we are interested in only some pieces of the data and preprocessing is thus not a bad idea.

Screen the data to get a sense for what could be relevant to achieve our objective.

We need to end up with a list that contains the following objects:
```json
[
    {
        "mag": 1.000,
        "lat": 1.000,
        "lon": 1.000
    },
    ...
]
```
We also want this list to be sorted in descending order and filter away all earthquakes below a magnitue of 1 as they are not felt by humans, only seismological instruments.


Complete the function preprocess that takes the full data (a python dictionary) received from the url and returns the formated list.

> Tips: You may find [this article](https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/) for sorting a list of dictionaries helpful.
>
> Also list comprehension is useful here to filter and create the list with the required data.

Here is a possible solution:
```python
# use list comprehension to put together preprocessed data
data = [{
    "mag": e["properties"]["mag"],
    "long": e["geometry"]["coordinates"][0],
    "lat": e["geometry"]["coordinates"][1],
} for e in raw["features"] if e["properties"]["mag"] > 1]
```

We can sort a list of dictionaries by a dictionary key using a lambda (anonymous) function:
```python
# sort by magnitude
data = sorted(data, key=lambda i: i['mag'], reverse=True)
```
To change the order to `descending` we simply added the reverse optional argument and set it to `True`.

### Plot US map with earthquake data

#### Imports
First we need some imports at the top of our `support.py` file:
```python
import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"

import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
```
When running your program for the first time with those imports you will notice it takes a while to install those libraries as they do not come by default with Python.

To install pandas type this into the shell:
```bash
pip install pandas
pip install geopandas
```

- The first two lines prevent a cache warning and allow your plots to render faster.
- Pandas is a library for data processing data analytics / processing
- Geopandas contains lots of geodata such as graphs of countries, cities and more.
- Mathplot lib is a library to render all sorts of plots.

#### Preparing Panda Dataframe
Our preprocessed list of dictionaries is great but panda wants us to take it to another level and convert it into a panda dataframe. This allows internally some advanced data processing and generally enables effective handling of large data sets.

Since we already have a list of dictionaries all we have to do is convert it:
```python
df = pd.DataFrame(data)
df.head()
```
`head(x)` allows us to load the first `x` rows into an internal buffer but providing no `x` we can load all rows (earthquakes).

### Preparing Plot

Next we need to prepare the plot itself. With the following line we specify variables for the figure itself and it's axis,  as well as the final size (in inches) of the rendered graphic.

```python
# initialize an axis
fig, ax = plt.subplots(figsize=(8,6))
```

#### Plotting US map
We need to plot two things:
1. colored points resembling earthquakes at specific locations
2. a US map in the background.

`2.` is achieved by specififying which countries we would like to drop on the plot.
```python
# plot map on axis
countries = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

countries[countries["name"] == "United States of America"].plot(color="lightgrey", ax=ax)
```
Here we loaded all countries in lowres polygons and then specified t hat we only want to plot the United States in a `lightgray`.

#### Plotting earthquakes

Next we want to create the earthquake points (colored) and place them on a scatter plot.

By specifying `x` and `y` to be latitude and longditude we essentially ensure the previous map data lines up nicely with the earthquake data. We can do additional things such as specifying that `c` (magnitude) should be used to color the points and what colors the gradient is made up from. We can also give the chart a title:
```python
# plot points
df.plot(x="lat", y="long", kind="scatter", c="mag", colormap="YlOrRd", title=f"Today's earthquakes over US Mainland", ax=ax)
```


To finalize, we want to add a grid to the plot making it easier to determine locations on the plot and ensure we are showing only the US mainland by changing the bounds to the area the US occupies.

Finally we plot the graph.

```python
# add grid
ax.grid(b=True, alpha=0.5)

# restrict the map to the following coordinates
plt.xlim([-170, -70])
plt.ylim([20, 75])

plt.show()
```
#### Final Result
If everything was done correctly you should see this final plot:
![Plot](assets/plot.png)
