# Lesson 2 - Loops and Conditional Statements

# Author: Jake Palczewski, CCIE #63320
# Last Updated: November 29, 2020

my_list1 = ["CCNA", "CCNP", "CCIE"]
for cert in my_list1:
    print(cert)
# above, we define a list, and for each element in the list print the element to the terminal 


if "CCIE" in my_list1:
    print("I have a CCIE!")
# here, we re-use the list in an if conditional statement. 
# if CCIE is in the list (which is is), the string is printed to the terminal


if "Network+" in my_list1:
    print("I have a Network+")
elif "A+" in my_list1:
    print("I have an A+")
else:
    print("I don't have any Comptia certs")
# above, we re-use the list in an if/elif/else condition. 
# since Network+ and A+ are NOT in the list, the else statement will be matched


my_dict1 = {"CCNA": "Security", "CCNP": "Data Center", "CCIE": "Routing and Switching"}
for key, value in my_dict1.items():
    if key == "CCIE":
        print(f"I have a {key} in {value}")
# above, we do something tricky!
# we define a dictionary with three key-value pairs
# we then define a for loop that runs once for each key-value pair in the dictionary
# using the items() method, we can manipulate both the key AND the value!
# within the for loop is an if condition, that is met when the key is "CCIE"
# the print() function takes the key and value ingested in the loop, and adds both to the printed string


my_range = range(10)
for number in my_range:
    if number == 5:
        continue 
    print(number)
# as seen in the PDF lesson, this for loop and if statement prints numbers 0-9
# but, the continue statement tells the for loop to continue to the next number when the ingested number is equal to 5
# the for loop  and if statement say, "Oh, I'm iterating on the number 5. Let me stop that and CONTINUE with the next number"