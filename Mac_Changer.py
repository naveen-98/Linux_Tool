#!/usr/bin/env python

import subprocess

from tqdm import tqdm

import time



def run_command(command):

    """Run a shell command and return True if it succeeds, False otherwise."""

    result = subprocess.call(command, shell=True)

    return result == 0



# Attempt to bring down the network interface

if not run_command("sudo ifconfig eth0 down"):

    print("Error: Failed to bring down the network interface.")

    exit(1)



# Attempt to change the MAC address

if not run_command("ifconfig eth0 hw ether 00:11:22:33:44:55"):

    print("Error: Failed to change the MAC address.")

    exit(1)



# Attempt to bring up the network interface

if not run_command("ifconfig eth0 up"):

    print("Error: Failed to bring up the network interface.")

    exit(1)



# If all commands succeed, activate the progress bar

total_iterations = 100



# Create a tqdm instance with the total number of iterations

progress_bar = tqdm(total=total_iterations, desc="Processing")



# Simulate some work

for _ in range(total_iterations):

    # Simulate work by sleeping for a short duration

    time.sleep(0.1)



    # Update the progress bar

    progress_bar.update(1)



# Close the progress bar

progress_bar.close()



print("Processing complete")


# Code By - Naveen_Wijesinghe

