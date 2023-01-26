# TODO: shortcut for run line shift + enter

# upgrade python 🐍

# why?
# faster 🐆
# more optimaze 
# more secure 🔒
# better support for typing
# we could use black or other tool
# better syntax warnings and error messages 


# features:
# 3.6 -> 3.7

# Simple class creation using data classes
# Customized access to module attributes
# Improved support for type hinting
# Higher precision timing functions

# There is less overhead in calling many methods in the standard library.
# Method calls are up to 20% faster in general.
# The startup time of Python itself is reduced by 10-30%.
# Importing typing is 7 times faster.

# The Order of Dictionaries Is Guaranteed
# 3.7 -> 3.8
# Walrus 🦭
walrus = False
print(walrus)
print(walrus := True)


inputs = list()
while True:
    current = input("Write something: ")
    if current == "quit":
        break
    inputs.append(current)

inputs = list()
while (current := input("Write something: ")) != "quit":
    inputs.append(current)


# Simpler Debugging With f-Strings
import math
r = 3.8
f"Diameter {(diam := 2 * r)} gives circumference {math.pi * diam:.2f}"

python = 3.7
f"python={python}"
python = 3.8
f"{python=}"
name = "Eric"
f"{name = }"
f"{name.upper()[::-1] = }"

# Positional-only arguments & keyword-only arguments
def headline(text, /, border="♦", *, width=50):
    return f" {text} ".center(width, border)

# 3.8 -> 3.9

# The zoneinfo module for dealing with time zones
# Union operators that can update dictionaries
# More expressive decorator syntax


# Python version                       3.4     3.5     3.6     3.7     3.8    3.9
# --------------                       ---     ---     ---     ---     ---    ---

# Variable and attribute read access:
#     read_local                       7.1     7.1     5.4     5.1     3.9    3.9
#     read_nonlocal                    7.1     8.1     5.8     5.4     4.4    4.5
#     read_global                     15.5    19.0    14.3    13.6     7.6    7.8
#     read_builtin                    21.1    21.6    18.5    19.0     7.5    7.8
#     read_classvar_from_class        25.6    26.5    20.7    19.5    18.4   17.9
#     read_classvar_from_instance     22.8    23.5    18.8    17.1    16.4   16.9
#     read_instancevar                32.4    33.1    28.0    26.3    25.4   25.3
#     read_instancevar_slots          27.8    31.3    20.8    20.8    20.2   20.5
#     read_namedtuple                 73.8    57.5    45.0    46.8    18.4   18.7
#     read_boundmethod                37.6    37.9    29.6    26.9    27.7   41.1

# Variable and attribute write access:
#     write_local                      8.7     9.3     5.5     5.3     4.3    4.3
#     write_nonlocal                  10.5    11.1     5.6     5.5     4.7    4.8
#     write_global                    19.7    21.2    18.0    18.0    15.8   16.7
#     write_classvar                  92.9    96.0   104.6   102.1    39.2   39.8
#     write_instancevar               44.6    45.8    40.0    38.9    35.5   37.4
#     write_instancevar_slots         35.6    36.1    27.3    26.6    25.7   25.8

# Data structure read access:
#     read_list                       24.2    24.5    20.8    20.8    19.0   19.5
#     read_deque                      24.7    25.5    20.2    20.6    19.8   20.2
#     read_dict                       24.3    25.7    22.3    23.0    21.0   22.4
#     read_strdict                    22.6    24.3    19.5    21.2    18.9   21.5

# Data structure write access:
#     write_list                      27.1    28.5    22.5    21.6    20.0   20.0
#     write_deque                     28.7    30.1    22.7    21.8    23.5   21.7
#     write_dict                      31.4    33.3    29.3    29.2    24.7   25.4
#     write_strdict                   28.4    29.9    27.5    25.2    23.1   24.5

# Stack (or queue) operations:
#     list_append_pop                 93.4   112.7    75.4    74.2    50.8   50.6
#     deque_append_pop                43.5    57.0    49.4    49.2    42.5   44.2
#     deque_append_popleft            43.7    57.3    49.7    49.7    42.8   46.4

# Timing loop:
#     loop_overhead                    0.5     0.6     0.4     0.3     0.3    0.3

# 3.9 -> 3.10
# Structural Pattern Matching
# https://twitter.com/anthonypjshaw/status/1526034155448184832?s=20&t=UFxO6tj5S-c3YZxeupdC7w
def fizzbuzz(number):
    mod_3 = number % 3
    mod_5 = number % 5

    if mod_3 == 0 and mod_5 == 0:
        return "fizzbuzz"
    elif mod_3 == 0:
        return "fizz"
    elif mod_5 == 0:
        return "buzz"
    else:
        return str(number)

fizzbuzz(3)
fizzbuzz(14)
fizzbuzz(15)
fizzbuzz(92)
fizzbuzz(65)

def fizzbuzz(number):
    mod_3 = number % 3
    mod_5 = number % 5

    match (mod_3, mod_5):
        case (0, 0):
            return "fizzbuzz"
        case (0, _):
            return "fizz"
        case (_, 0):
            return "buzz"
        case _:
            return str(number)

fizzbuzz(3)
fizzbuzz(14)
fizzbuzz(15)
fizzbuzz(92)
fizzbuzz(65)

# Mapping patterns match mapping structures like dictionaries.
# Sequence patterns match sequence structures like tuples and lists.
# Capture patterns bind values to names.
# AS patterns bind the value of subpatterns to names.
# OR patterns match one of several different subpatterns.
# Wildcard patterns match anything.
# Class patterns match class structures.
# Value patterns match values stored in attributes.
# Literal patterns match literal values.

# links:
# https://realpython.com/python37-new-features/#data-classes
# https://realpython.com/python38-new-features/#the-walrus-in-the-room-assignment-expressions
# https://realpython.com/python39-new-features/#conclusion
# https://realpython.com/python310-new-features/

# https://realpython.com/python-wheels/#calling-all-developers-build-your-wheels

# https://docs.python.org/3.10/whatsnew/3.10.html

# 3.11
# Python 3.11 is between 10-60% faster than Python 3.10. On average, we measured a 1.25x speedup on the standard benchmark suite.

# https://stackoverflow.com/questions/73681086/streamlining-python-3-6-3-10-migration

# notes TODO:
# check end support date
# https://endoflife.date/python
# more tests
# check libs
# upgade 2 version than next 2
# to upgrade python, you will need to upgrade pyenv
# check deprecated warnings
