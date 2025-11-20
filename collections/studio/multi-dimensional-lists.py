food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
food_cabinet = sorted(food.split(","))
equipment_cabinet = sorted(equipment.split(","))
pets_cabinet = sorted(pets.split(","))
sleep_aids_cabinet = sorted(sleep_aids.split(","))

print(food_cabinet)
print(equipment_cabinet)
print(pets_cabinet)
print(sleep_aids_cabinet)


# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.

cargo_hold_list = [food_cabinet, equipment_cabinet, pets_cabinet, sleep_aids_cabinet]
print(cargo_hold_list)

# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.
while True:
    user_cabinet_selection = input("Please select cabinet(0-3): ")
    if user_cabinet_selection.isdigit():
        user_cabinet_selection = int(user_cabinet_selection)
        if 0 <= user_cabinet_selection <= 3:
            break
    print("Cabinet must be selected by valid cabinet number.")

# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.

print(cargo_hold_list[(user_cabinet_selection)])
#input validation is contained in the previous section

# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”
user_item_selection = input("Please select an item: ")
if user_item_selection in cargo_hold_list[(user_cabinet_selection)]:
    print(f"Cabinet DOES contain {user_item_selection}.")
else:
    print(f"Cabinet DOES NOT contain {user_item_selection}.")