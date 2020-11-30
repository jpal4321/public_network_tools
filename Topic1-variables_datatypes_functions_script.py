# Lesson 1 - Variables, Data Types, and Functions

# Author: Jake Palczewski, CCIE #63320
# Last Updated: November 29, 2020

my_var1 = "This is my string!"
# in the example above, the variable name (my_var1) is on the left of the =, 
# and the string encapsulated in the variable is on the right of the =

print(my_var1)
# above, we use the print() function to output the value of my_var1 to the terminal

my_list1 = ["Hello", 4, 2.5]
# above, we define list named my_list, and within it, we add a string, an integer, and a floating-point number

print(type(my_list1))
# above, we use the print() function and the type() function to display my_list1's data type. 

my_dict1 = {"this is my key":"and this is my value"}
# above, we define a dictionary and assign a key-value pair

print(my_dict1["this is my key"])
# above, we use the print() function and square brackets to display the value associated with the key "this is my key"

print(my_dict1.values())
# lastly, we use the print() function and the values() method to display the values within the my_dict1 dictionary