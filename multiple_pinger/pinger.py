import os
'''
This program is designed to be executed in Command Prompt in Admin mode.
It is capable of pinging a large list of addresses and returning whether there was a response or not.
Enjoy! 
Christopher Loutsch
'''
def logo():
    print("'||    ||'          '||    .    ||     '||''|.   ||                   ")
    print(" |||  |||  ... ...   ||  .||.  ...      ||   || ...  .. ...     ... . ")
    print(" |'|..'||   ||  ||   ||   ||    ||      ||...|'  ||   ||  ||   || ||  ")
    print(" | '|' ||   ||  ||   ||   ||    ||      ||       ||   ||  ||    |''   ")
    print(".|. | .||.  '|..'|. .||.  '|.' .||.    .||.     .||. .||. ||.  '||||. ")
    print("                                                              .|....' ")
    print("----------------------------------------------------------------------")

os.system("cls")
os.system("title "+"Multiple Pinger")
logo()
# defined variables
hostname_list = []
host_loop_control = 0

# num_of_loops will be set as the limit for extentions to hostname_list
num_of_loops = int(input("How many hosts to ping: "))

while host_loop_control < num_of_loops:

    hostname = str(input("Enter Host: "))
    hostname_list.append(hostname)
    host_loop_control += 1

print("--------------------------------------------------")
host_loop_control = 0
# This loop pings all of the addresses and returns results in console
while host_loop_control < num_of_loops:
    
    hostname = hostname_list.pop()

    response = os.system("ping -n 1 " + hostname)

## response from pings
    if response == 0:
        print ('\033[92m' + hostname + " is up!" + '\033[0m')
    else:
        print ('\033[93m' + hostname + " is down!" + '\033[0m')
    
    host_loop_control += 1

os.system("pause")