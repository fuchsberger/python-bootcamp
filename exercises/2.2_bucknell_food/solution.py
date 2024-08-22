time = float(input("What time is it? (0 - 24): "))

# Create an empty list to add to if a location is open
locations = []

# Check if the time entered is valid
if time > 24 or time < 0:
  print("INVALID")

# If the time is valid, check each dining hall time range
else:
  if time >= 7.5 and time < 23:
    # If its in the time range, append the dining hall name to our earlier list
    locations.append("Bison Cafe")
  # Bostwick requires nested and and or statements because of the separate time ranges
  if (time >=7 and time <10) or (time >=11 and time < 15) or (time >=17 and time <22):
    locations.append("Bostwick")
  if time >= 10 and time < 21:
    locations.append("Commons")
  if time >= 11 and time < 14:
    locations.append("Terrace")

# Loop through the list of open locations and print each one
for dining_hall in locations:
  print (dining_hall)
