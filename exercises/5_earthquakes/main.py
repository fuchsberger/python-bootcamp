from helpers import response, preprocess, plot

url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson'

data = response(url)
data = preprocess(data)
plot(data)
