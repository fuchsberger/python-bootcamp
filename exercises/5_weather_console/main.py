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
        pass

    elif choice == "3":
        pass

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
    pass


def load_locations():
    pass


def list_locations():
    pass

menu()
