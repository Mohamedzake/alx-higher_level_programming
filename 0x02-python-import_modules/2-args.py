#!/usr/bin/python3
from sys import argv

argc = len(argv)

print(f"{argc - 1} argument{'s' if argc != 2 else ''}:", end='')
print("." if argc == 1 else "")

for i, arg in enumerate(argv[1:], 1):
    print(f"{i}: {arg}")
