my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.

pigstring = my_string[7:10] + my_string[0:7]
# odeLaunchC

# Use a template literal to print the original and modified string in a descriptive phrase.

print(f"{my_string} in pseudo-pig latin is {pigstring}")

# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
user_num = input("Select a number of letters to relocate: ")
user_num = int(user_num)
user_pigstring = (my_string[user_num:10] + my_string[0:user_num])
print(f"{my_string} in pseudo-pig latin is {user_pigstring}")

# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
my_string = "LaunchCode"
user_num = input("Select a number of letters to relocate: ")
user_num = int(user_num)
if user_num >= 10:
    print('Entry must be less than 10.')
user_pigstring = (my_string[user_num:10] + my_string[0:user_num])
print(f"{my_string} in pseudo-pig latin is {user_pigstring}")