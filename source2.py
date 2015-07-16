__author__ = 'BreenIsALie'
# Script for reading status of local linux hosts

## NOTES ##

import commands
import subprocess
import socket
from sys import argv
from subprocess import check_output

script_name = argv

def user_prompt():  # Asks the user if to shutdown or refresh. Also used to keep info on screen
    print("Press enter to refresh the program, or type exit to end the program")
    user_input = raw_input(">> ")
    return user_input

def get_ip():
    ip_addr = check_output(["ifconfig", "grep 'inet addr:'"])
    return ip_addr

def get_hostname():
    hostname = socket.gethostname()
    return hostname

def get_main_disk_usage():
    disk_use = subprocess.Popen(["ifconfig | grep 'inet addr:'"], shell=False, stdout=subprocess.PIPE)
    return disk_use

def user_interaction(name):
    print "This is the %s script. Type exit to end the script, or press enter to run it again" % name
    user_input = raw_input("> ")
    return user_input

if __name__ == '__main__':
    exit_condition = 0
    while exit_condition != "exit":
        exit_condition = user_interaction(script_name)

        hostname = get_hostname()
        ip = get_ip()

        print "HOSTNAME: %s" % hostname
        print "IP: '{0}'" .format(ip)