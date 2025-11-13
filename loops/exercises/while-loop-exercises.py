# Define three variables for the LaunchCode shuttle - one for the starting fuel level, another for the number of astronauts aboard, and the third for the altitude the shuttle reaches.

fuel_level = 0
total_crew = 0
shuttle_altitude = 0

# Exercise #1: Construct while loops to do the following:
  # a. Query the user for the starting fuel level. Validate that the user enters a positive, integer value greater than 5000 but less than 30000. 

fuel_level = 0
while fuel_level <= 5000 or fuel_level >= 30000:
    fuel_level = int(input("Please enter starting fuel level: "))
    if fuel_level <= 5000 or fuel_level >= 30000:
        print("Invalid fuel level")
print(f"Fuel level {fuel_level} confirmed.")



# b. Use a second loop to query the user for the number of astronauts (up to a maximum of 7). Validate the entry.
total_crew = 0
while total_crew <= 0 or total_crew > 7:
    total_crew = int(input("Please confirm number of crew: "))
    if total_crew <= 0:
        print("Shuttle must be manned.")
    if total_crew > 7:
        print("Shuttle crew cannot exceed capacity.")
print(f"Crew members confirmed: {total_crew}.")
  
# c. Use a final loop to monitor the fuel status and the altitude of the shuttle. Each iteration, decrease the fuel level by 100 units for each astronaut aboard. Also, increase the altitude by 50 kilometers.
while fuel_level > 0:
    fuel_level -= (total_crew * 100)
    shuttle_altitude += 50
    print(f"Fuel remaining: {fuel_level}.  Altitude {shuttle_altitude} kilometers.")



# Exercise #2: Print the result with the phrase, The shuttle gained an altitude of ___ km and has ___ kg of fuel left. Fill in the blanks with the altitude and fuel level values.

# If the altitude is 2000 km or higher, add “Orbit achieved!” Otherwise add, “Failed to reach orbit.”
