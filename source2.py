__author__ = 'BreenIsALie'
# Script for reading status of local linux hosts

## NOTES ##
# The "Ask to exit" functionality has been disabled, easier to just re-run the command. Might re-enable. Kept for now
# Functionality:    Hostname
#                   HDD Usage
#                   IP addresses
#                   System version
#                   Current system time
#                   Memory statistics


import subprocess   # Needed to run linux commands using subprocess.call
import socket       # Used to get the hostname
from sys import argv    # Used to take arguments from the command line when starting the script (currently just name)
import time             # Used for the time.sleep() function
import platform

script_name = argv  # saves the script name as a variable, used in the message at the end. Not *strictly* neccessary

def get_hostname():  # Gets the hostname and returns it to the main program
    host = socket.gethostname()
    return host

def get_main_disk_usage():  # Runs the linux command df -h to get an overview over hdd usage
        p1 = subprocess.Popen(["df", "-h"], stdout=subprocess.PIPE)  # runs the df -h command
        p2 = subprocess.Popen(('grep', 'sd..'), stdin=p1.stdout)  # runs grep on the df output to trim out non HDDs
        return p2  # returns the trimmed down output, now containing only the HDDs

def get_ip_addresses():
    p3 = subprocess.Popen((["ifconfig"]), stdout=subprocess.PIPE)
    p4 = subprocess.Popen((["grep", "inet addr"]), stdin=p3.stdout)
    print "\nIP ADDRESSES:"


def user_interaction(name):  # Used as"what now" question at the end. Allows refresh (press enter) or exit (type exit)
    print "\n\nThis is the %s script. Type exit to end the script, or press enter to run it again" % name
    user_input = raw_input("> ")
    return user_input

def get_mem_usage():
    vmstat = subprocess.Popen((["vmstat", "-s", "-S", "M"]),stdout=subprocess.PIPE)
    head = subprocess.Popen((["head"]), stdin=vmstat.stdout)

if __name__ == '__main__':  # Main function goes here
        hostname = get_hostname()

        print "\n\n-----------------------------------------------------------------------------\n\n"  # For readability
        print "HOSTNAME: %s" "\n" % hostname    # Prints the hostname

        sys_info = platform.platform()
        print "SYSTEM: %s" % sys_info

        sys_time = time.asctime()
        print "\nSYSTEM TIME: %s" % sys_time

        get_mem_usage()
        print"\nMEMORY USAGE: \n"
        time.sleep(0.1)

        print "\nDISK USAGE: "
        get_main_disk_usage()                   # Prints the output of df-h. Maybe trim a bit in later versions

        get_ip_addresses()

        time.sleep(0.1)  # Holds script for 0.1 second, stopping the script from outpacing linux commands
        print "\n\n-----------------------------------------------------------------------------\n\n"  # For readability

