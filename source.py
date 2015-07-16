# Script for reading status of local linux hosts

## NOTES ##



import socket  # Used to read system info from host
import os
import subprocess
import commands

# CONFIG SECTION START

hdd1 = "/"  # Path to check disk usage for, one for each disk. Add relevant paths here
hdd2 = "/HDD2/"  # Path to check disk usage for, one for each disk. Add relevant paths here
#  hdd* = "[path]"

# CONFIG SECTION END

def user_prompt():  # Asks the user if to shutdown or refresh. Also used to keep info on screen
    print("Press enter to refresh the program, or type exit to end the program")
    user_input = raw_input(">> ")
    return user_input

def disk_free():
    # free_space = commands.getstatusoutput("df -k | grep 'sd..'")
    process = subprocess.Popen(["df -k | grep 'sd.."], shell=False, stdout=subprocess.PIPE)
    data = process.communicate()
    free_space = int(data[0].spilit()[5][1:3])
    return free_space

def get_ip():
    ip = commands.getstatusoutput("ifconfig | grep 'inet addr:'")
    return ip

exit_sequence = 0  # Defines the exit sequence to 0 so the loop can run
while exit_sequence != "exit":  # Run the loop until the user says to exit using user_prompt():

    hostname = socket.gethostname()  # Gets the hostname of the system
    ip_address = get_ip()  # Gets the IP of the host
    disk_space = disk_free()  # Uses the hdd1 variable (path to disk 1) to get the amount of used storage

    # For debug use
    print ("%s") % hostname
    print ("%s") % ip_address
    print ("%s") % disk_space
    exit_sequence = user_prompt()

exit()




