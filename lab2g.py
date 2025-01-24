#!/usr/bin/env python3

import sys

# Author: Sambhav Sachdeva
# Author ID: ssachdeva25
# Date Created: 2025/01/23



if len(sys.argv) == 2:
    timer = int(sys.argv[1])  
else:
    timer = 3  


while timer > 0:
    print(timer)
    timer -= 1


print("blast off!")


