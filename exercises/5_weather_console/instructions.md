## Weather Forecast App

In this exercise we will learn how to create a console based data app that allows us to create and remove locations for which we can look up a weather forcast.

A menu guides the user through the process and locations are saved as they are added so when we rerun the program we don't have to start from scratch.

We are going to use the national weather service api to achieve this:
[https://www.weather.gov/documentation/services-web-api](https://www.weather.gov/documentation/services-web-api)

The website provides examples for how to access weather data so its always a good idea to practice an example before actually starting to code.

In order to get a forecast we need to know the x/y grid coordinates of the location. Unfortunately this is not the same as the latitude / longitude.

```
https://api.weather.gov/gridpoints/{office}/{grid X},{grid Y}/forecast
```

Fortunately we can retrieve the grid coordinate if we do have the latitude / longitude:
```
https://api.weather.gov/points/{latitude},{longitude}
```

Lets try that with the coordinates of Lewisburg, PA.

A quick google search (type: `lewisburg pa lat long`) reveals that Lewisburg is located at `40.9645° N`, `76.8844° W`.

We can therefore use this link to access the grid coordinates of Lewisburg:
[https://api.weather.gov/points/40.9645,-76.8844](https://api.weather.gov/points/40.9645,-76.8844)

Search the JSON file for `gridX` and `gridY`. This will be needed in the next API call:

[https://api.weather.gov/gridpoints/CTP/100,68/forecast/hourly](https://api.weather.gov/gridpoints/CTP/100,68/forecast/hourly)

Here we can find a wide range of data we could use for our daily forecast.
To keep things simple we are going to just use the next hour's verbal forecast (short version).

In this excerce we will work though the entire code from scratch (start with nothing) but in case you get lost along the way, here is the full code:

**Please do not copy it in it's entirety and instead follow along with the lecture, step by step.**

```python
import json
import urllib.request

locations = []


def menu():
    global locations

    load_locations()

    print("(1) Add Location")
    print("(2) Remove Location")
    print("(3) Get Forcast")

    choice = input("Choose a menu option (1-3): ")
    print()

    if choice == "1":
        print("Adding Location...")
        name = input("Provide the name of the location: ")
        lat = input("Provide the latitude of the location: ")
        long = input("Provide the longitude of the location: ")

        # do an api lookup to get the grid cell
        data = response(f"https://api.weather.gov/points/{lat},{long}")

        x = data["properties"]["gridX"]
        y = data["properties"]["gridY"]
        print(x, y)

        locations.append({"name": name, "gridX": x, "gridY": y})
        save_locations()

    elif choice == "2":
        list_locations()

        id = input("Which location would you like to remove (id):")

        locations.pop(int(id))
        save_locations()

    elif choice == "3":
        list_locations()

        id = input("Which location would you like to lookup (id):")

        location = locations[int(id)]
        x = location["gridX"]
        y = location["gridY"]

        data = response(
            f"https://api.weather.gov/gridpoints/CTP/{x},{y}/forecast/hourly")

        print("Forcast for the next hour in " + location["name"] + ":")
        print(data["properties"]["periods"][0]["shortForecast"])
        print()

    else:
        print("Unknown choice. Try again.")
        print()

    menu()


def response(url):
    """
    Loads and interprets json content from a given url.
    """
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read())


def save_locations():
    f = open("locations.json", "w")
    f.write(json.dumps(locations, indent=2))
    f.close()


def load_locations():
    global locations
    f = open("locations.json")
    locations = json.loads(f.read())
    f.close()


def list_locations():
    print("We found the following locations:")
    for i in range(len(locations)):
        print(i, locations[i]["name"])
    print()


menu()

```
