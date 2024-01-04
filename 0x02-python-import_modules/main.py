#!/usr/bin/python3

# Import and execute each task script

# Task 0
from add_0 import add
a = 1
b = 2
print("{} + {} = {}".format(a, b, add(a, b)))

# Task 1
from calculator_1 import add, sub, mul, div
a = 10
b = 5
print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))

# Task 2
import sys
n = len(sys.argv) - 1
print("{} argument{}{}.".format(n, '' if n == 1 else 's', ':' if n > 0 else '.'))
for i in range(1, n + 1):
    print("{}: {}".format(i, sys.argv[i]))

# Task 3
result = sum(int(arg) for arg in sys.argv[1:])
print(result)

# Task 4
import hidden_4
names = [name for name in dir(hidden_4) if not name.startswith("__")]
for name in sorted(names):
    print(name)

# Task 5
from variable_load_5 import a
print(a)

