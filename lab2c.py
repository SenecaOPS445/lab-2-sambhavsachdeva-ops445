#!/usr/bin/env python3

import sys


if len(sys.argv) < 3:
    print("Error: Not enough arguments provided.")
    sys.exit(1)


name = sys.argv[1]  
age = int(sys.argv[2])  

print(f"Hi {name}, you are {age} years old.")
