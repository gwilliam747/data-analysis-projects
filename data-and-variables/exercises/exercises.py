# 1. Declare and assign the variables here:
shuttle_name = 'Determination'
shuttle_speed_mph = 17500
km_to_mars = 225000000
km_to_moon = 384400
mpk = .621

# 2. Use print() to print the 'type' each variable. Print one item per line.

print(type(shuttle_name))
print(type(shuttle_speed_mph))
print(type(km_to_mars))
print(type(km_to_moon))
print(type(mpk))

# Code your solution to exercises 3 and 4 here:

miles_to_mars = km_to_mars * mpk
hrs_to_mars = miles_to_mars / shuttle_speed_mph
days_to_mars = hrs_to_mars / 24

print((shuttle_name),  'will take',  (days_to_mars), 'days to reach Mars.')

# Code your solution to exercise 5 here
miles_to_moon = km_to_moon * mpk
hrs_to_moon = miles_to_moon / shuttle_speed_mph
days_to_moon = hrs_to_moon / 24

print((shuttle_name), ' will take ', (days_to_moon), 'days to reach the moon')