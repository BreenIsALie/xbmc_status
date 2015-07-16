__author__ = 'BreenIsALie'
# Script for reading status of local linux hosts

## NOTES ##
# Current functionality:    Gets Hostname
#                           Gets HDD Usage

import commands
import subprocess
import socket
from sys import argv


script_name = argv

def get_hostname():
    hostname = socket.gethostname()
    return hostname

def get_main_disk_usage():
        subprocess.call(["df", "-h"])

def user_interaction(name):
    print "This is the %s script. Type exit to end the script, or press enter to run it again" % name
    user_input = raw_input("> ")
    return user_input

if __name__ == '__main__':
    exit_condition = 0
    while exit_condition != "exit":
        hostname = get_hostname()

        print "HOSTNAME: %s" "\n" % hostname
        print "DISK USAGE: \n"
        get_main_disk_usage()
        exit_condition = user_interaction(script_name)