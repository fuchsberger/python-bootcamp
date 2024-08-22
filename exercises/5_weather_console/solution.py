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
