#!/usr/bin/env python3

import sys

def whois(hello = "World"):
    if len(sys.argv) > 1:
        hello = str(sys.argv[1])
    return hello

print ("Hello " + whois() + "!")
