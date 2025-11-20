proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.
if ',' in proto_list1:
    print('proto_list1 - commas')
elif ';' in proto_list1:
    print ('proto_list1 - semicolons')
elif ' ' in proto_list1:
    print ('proto_list1 - spaces')
else:
    print ('proto_list1 - unknown')

if ',' in proto_list2:
    print('proto_list2 - commas')
elif ';' in proto_list2:
    print ('proto_list2 - semicolons')
elif ' ' in proto_list2:
    print ('proto_list2 - spaces')
else:
    print ('proto_list2 - unknown')

if ',' in proto_list3:
    print('proto_list3 - commas')
elif ';' in proto_list3:
    print ('proto_list3 - semicolons')
elif ' ' in proto_list3:
    print ('proto_list3 - spaces')
else:
    print ('proto_list3 - unknown')

if ',' in proto_list4:
    print('proto_list4 - commas')
elif ';' in proto_list4:
    print ('proto_list4 - semicolons')
elif ' ' in proto_list4:
    print ('proto_list4 - spaces')
else:
    print ('proto_list4 - unknown')
# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.
if "," in proto_list1:
    split_string1 = proto_list1.split(',')
    split_string1.reverse()
    mod_string1 = ','.join(split_string1)
print(mod_string1)
#12,9,6,3

# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.
if ';' in proto_list2:
    split_string2 = sorted(proto_list2.split(';'))
    mod_string2 = ','.join(split_string2)
print(mod_string2)
#A,C,E,M
    
# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.
if " " in proto_list3:
    split_string3 = sorted(proto_list3.split(" "), reverse=True)
    mod_string3 = " ".join(split_string3)
print(mod_string3)
#string space delimited
# I got "reverse=True" to work here, but not B

# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.
if ", " in proto_list4:
    split_string4 = proto_list4.split(", ")
    split_string4.reverse()
    mod_string4 = ",".join(split_string4)
print(mod_string4)
#caution,typing,require,might,Comma-spaces