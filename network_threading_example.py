from getpass import getpass
from netmiko import ConnectHandler
import threading
import queue
import time
 
username = input("Username: ")
password = getpass("Password: ")
 
start = time.time()
 
def Handler(my_queue):
    try:
        get_device = my_queue.get()
        device = get_device
 
        device_handler = ConnectHandler(
        device_type = 'cisco_nxos',
        username = username,
        password = password,
        ip = device,
        global_delay_factor = 1
        )
 
        output = device_handler.send_command("show int status")
 
        print(f"######################### {device} starting #########################")
        print(output)  
        print(f"######################### {device} complete #########################") 
        print("")    
        success_list.append(device)
 
    except Exception as error:
        print(error)
        fail_list.append(device)
    device_handler.disconnect
    my_queue.task_done()
    
success_list = []
fail_list = []
my_queue = queue.Queue()

 
devices = [
    "router1",
    "router2"
    ]

for device in devices:
    thread = threading.Thread(target=Handler, args=[my_queue])
    thread.daemon = True
    thread.start()

for device in devices:
    my_queue.put(device)

my_queue.join()

print('Successfully logged into the following devices:')
for x in success_list:
    print(x)
 
print('Unsuccessfully logged into the following devices:')
if len(fail_list) == 0:
    print("All devices were logged into successfully")

else:
    for x in fail_list:
        print(x)

print('The script took', round(time.time()-start), 'seconds.')