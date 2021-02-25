# emulating an offer of a travel agency - calculating a trip cost based on a destination and duration given by a user

# asking a user to input their chosen destination and duration of a trip
city = input("Choose your trip destination out of Boston, Cologne, Paris or Split: ")
days = int(input("How many days would you like to spend there?: "))

# claculating hotel cost for each city, NOTE: nights = days -1
def hotel_cost(nights):
  if city == "Split":
    return 20 * nights
  elif city == "Paris":
    return 100 * nights
  elif city == "Cologne":
    return 75 * nights
  elif city == "Boston":
    return 150 * nights

# defining a flight ticket cost to each city
def flight_cost(city):
  if city == "Split":
    return 183
  elif city == "Paris":
    return 220
  elif city == "Cologne":
    return 222
  elif city == "Boston":
    return 475
    
# calculating rental car cost including a 50 euro discount for over 7 days and 20 euro discount for over 3 days
def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost
def trip_cost(city, days):
  return rental_car_cost(days) + flight_cost(city) + hotel_cost(days - 1)

print ("The total cost of your trip (flight + renting a car + accomodation) is going to be: ", str(trip_cost(city, days)), " euros")
