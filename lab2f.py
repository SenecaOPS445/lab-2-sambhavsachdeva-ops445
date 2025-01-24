#!/usr/bin/env python3

import sys

# Author: Sambhav Sachdeva
# Author ID: ssachdeva25
# Date Created: 2025/01/23


if len(sys.argv) != 2:
    print("Usage: ./lab2f.py <count>")
    sys.exit(1)


timer = int(sys.argv[1])  


while timer > 0:
    print(timer)
    timer -= 1


print("blast off!")
