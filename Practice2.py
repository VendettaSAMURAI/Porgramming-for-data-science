#!/usr/bin/env python3
import sys

def main(s):
    print("Hello"+s+"!")

def hello():
    name = sys.argv[1]
    main(name)

if __name__ == "__main__":
    hello()

