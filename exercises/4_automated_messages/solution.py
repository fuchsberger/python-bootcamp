# Define a dictionary with the members
Larry = {"name":"Larry",
  "year_joined":1987,
  "state":"GA",
  "subscriptions":["Daily weather emails", "Umbrella of the month club", "Snow birds magazine", "The Raining Cats and Dogs Podcast"]
}
Sami = {"name":"Sami",
  "year_joined":2007,
  "state":"PA",
  "subscriptions":["Daily weather emails"]
}
George = {"name":"George",
  "year_joined":2020,
  "state":"NY",
  "subscriptions":[]
}
Donna = {"name":"Donna",
  "year_joined":2023,
  "state":"GA",
  "subscriptions":["Daily weather emails", "Umbrella of the month club"]
}

# Put each dictionary into a list
members = [Larry, Sami, George, Donna]

def create_message(member_info):
  # Define each of the variables by referencing the dictionary
  name = member_info["name"]
  member_years = 2023 - int(member_info["year_joined"])

  # Check if the member has any subscriptions
  if len(member_info["subscriptions"]) == 0:
    # If no subscriptions:
    print(f"Hello {name},\nThank you for being a valued member for the last {str(member_years)} years. Would you like to sign up for a subscription?")
  else:
    # If they have at least one subscription, define the first and last subscription in the list to use later
    first_subscription = str(member_info["subscriptions"][0])
    last_subscription = str(member_info["subscriptions"][-1])
    # Check how long they have been a member and print the corresponding message
    if member_years <= 1:
      # If they are a new member
      print(f"Hello {name},\nWelcome to our weather subscription service! We have an exclusive discount on our {first_subscription}.")
    elif member_years > 1 and len(member_info["subscriptions"]) == 1:
      print(f"Hello {name},\nThank you for being a valued member for the last {str(member_years)} years. We have an exclusive discount on our {first_subscription}.")
    elif member_years > 1 and len(member_info["subscriptions"]) > 1:
      print(f"Hello {name},\nThank you for being a valued member for the last {str(member_years)} years. We have an exclusive discount on {first_subscription} and {last_subscription}.")



for person in members:
  create_message(person)
