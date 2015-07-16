__author__ = 'BreenIsALie'
# Script for reading status of local linux hosts

## NOTES ##
# Current functionality:    Gets Hostname
#                           Gets HDD Usage


import subprocess   # Needed to run linux commands using subprocess.call
import socket       # Used to get the hostname
from sys import argv   # Used to take arguments from the command line when starting the script (currently just the name)


script_name = argv  # saves the script name as a variable, used in the message at the end. Not *strictly* neccessary

def get_hostname(): # Gets the hostname and returns it to the main program
    hostname = socket.gethostname()
    return hostname

def get_main_disk_usage():  # Runs the linux command df -h to get an overview over hdd usage
        subprocess.call(["df", "-h"])

def user_interaction(name):  # Used as"what now" question at the end. Allows refresh (press enter) or exit (type exit)
    print "This is the %s script. Type exit to end the script, or press enter to run it again" % name
    user_input = raw_input("> ")
    return user_input

if __name__ == '__main__':  # Main function goes here
    exit_condition = 0  # Initializes the exit condition as 0, if it turns into "exit" the loop finishes
    while exit_condition != "exit":  # run while exit condition isn't "exit"
        hostname = get_hostname()

        print "\n\n\n"  # For readability, gets some space between text above and script text
        print "HOSTNAME: %s" "\n" % hostname    # Prints the hostname
        print "DISK USAGE: \n"
        get_main_disk_usage()                   # Prints the output of df-h. Maybe trim a bit in later versions

        exit_condition = user_interaction(script_name)  # Checks if user wants to exit, or run the script again
