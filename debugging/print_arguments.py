#!/usr/bin/python3
import sys

# Check if any arguments were passed
if len(sys.argv) > 1:
    print("Arguments passed:")
    for arg in sys.argv[1:]:  # Skip the script name
        print(arg)
else:
    print("No arguments provided.")
