# Script for reading status of local linux hosts

## NOTES ##



import socket  # Used to read system info from host
import os
import subprocess

# CONFIG SECTION START

hdd1 = "/"  # Path to check disk usage for, one for each disk. Add relevant paths here
hdd2 = "/HDD2/"  # Path to check disk usage for, one for each disk. Add relevant paths here
#  hdd* = "[path]"

# CONFIG SECTION END

def user_prompt():  # Asks the user if to shutdown or refresh. Also used to keep info on screen
    print("Press enter to refresh the program, or type exit to end the program")
    user_input = raw_input(">> ")
    return user_input

def disk_free(path):
    free_space = subprocess.Popen("df -k / | grep 'sd..'", stdout=subprocess.PIPE .communicate()[0])

exit_sequence = 0  # Defines the exit sequence to 0 so the loop can run
while exit_sequence != "exit":  # Run the loop until the user says to exit using user_prompt():


    hostname = socket.gethostname()  # Gets the hostname of the system
    ip_address = socket.gethostbyname(socket.gethostname())  # Gets the IP of the host
    disk1_space = disk_free(hdd1)  # Uses the hdd1 variable (path to disk 1) to get the amount of used storage
    disk2_space = disk_free(hdd2)  # Uses the hdd2 variable (path to disk 1) to get the amount of used storage



    # For debug use
    print ("%s") % hostname
    print ("%s") % ip_address
    print ("%s") % disk1_space
    print ("%s") % disk2_space
    exit_sequence = user_prompt()

exit()




