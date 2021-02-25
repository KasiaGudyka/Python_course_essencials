# prints a length of the string, converts to all lower case and all upper case.
# scanning a string from a user
my_string = input("Write a string you'd like to convert: ")

# converting and printing, NOTE: length needed a convertion from int to string
print ("your string length: " + str(len(my_string)))
print ("Your string in all lower case: " + my_string.lower())
print ("Your string in all upper case: " + my_string.upper())
