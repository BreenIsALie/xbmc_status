__author__ = 'BreenIsALie'
# Script for reading status of local linux hosts

## NOTES ##
# The "Ask to exit" functionality has been disabled, easier to just re-run the command. Might re-enable. Kept for now
# Current functionality:    Gets Hostname
#                           Gets HDD Usage
#                           Gets IP addresses


import subprocess   # Needed to run linux commands using subprocess.call
import socket       # Used to get the hostname
from sys import argv    # Used to take arguments from the command line when starting the script (currently just name)
import time             # Used for the time.sleep() function


script_name = argv  # saves the script name as a variable, used in the message at the end. Not *strictly* neccessary

def get_hostname(): # Gets the hostname and returns it to the main program
    host = socket.gethostname()
    return host

def get_main_disk_usage():  # Runs the linux command df -h to get an overview over hdd usage
        p1 = subprocess.Popen(["df", "-h"], stdout=subprocess.PIPE)  # runs the df -h command
        p2 = subprocess.Popen(('grep', 'sd..'), stdin=p1.stdout)  # runs grep on the df output to trim out non HDDs
        return p2  # returns the trimmed down output, now containing only the HDDs

def get_ip_addresses():
    p3 = subprocess.Popen((["ifconfig"]), stdout=subprocess.PIPE)
    p4 = subprocess.Popen((["grep", "inet addr"]), stdin=p3.stdout)
    print "\nIP ADDRESSES:\n"


def user_interaction(name):  # Used as"what now" question at the end. Allows refresh (press enter) or exit (type exit)
    print "\n\nThis is the %s script. Type exit to end the script, or press enter to run it again" % name
    user_input = raw_input("> ")
    return user_input

if __name__ == '__main__':  # Main function goes here
    # exit_condition = 0  # Initializes the exit condition as 0, if it turns into "exit" the loop finishes
    # while exit_condition != "exit":  # run while exit condition isn't "exit"
        hostname = get_hostname()

        print "\n"  # For readability, gets some space between text above and script text
        print "HOSTNAME: %s" "\n" % hostname    # Prints the hostname
        print "DISK USAGE: "
        get_main_disk_usage()                   # Prints the output of df-h. Maybe trim a bit in later versions
        get_ip_addresses()

        time.sleep(0.1)  # Holds script for 0.1 second, otherwise disk usage print interrupts the user prompt
        # exit_condition = user_interaction(script_name)  # Checks if user wants to exit, or run the script again
