# Lesson 4 - Netmiko
 
# Author: Jake Palczewski, CCIE #63320
# Last Updated: December 6, 2020
 
# below, we us from/import statements to import modules into our script
from netmiko import ConnectHandler
from getpass import *
 
# here, we ask for a username and password, so Python can SSH into our Nexus switch
username = input("What is your username?: ")
password = getpass("What is your password?: ")
 
# here, we use the ConnectHandler function from the Netmiko module to define SSH parameters
device_handler = ConnectHandler(
    device_type = 'cisco_nxos',
    username = username,
    password = password,
    ip = 'NXswitch01',
    )
 
# the output variable uses the send_command method to send a command to the Nexus switch. 
# the output variable also stores the result of the command!
output = device_handler.send_command("show run | include hostname")
 
# here, we print the result of the command to the terminal
print(output)