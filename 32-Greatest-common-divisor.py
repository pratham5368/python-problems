"""
Calculates the greatest common divisor of a list of numbers.

Use functools.reduce() and math.gcd() over the given list.
"""
from functools import reduce
from math import gcd as _gcd

def gcd(numbers):
  return reduce(_gcd, numbers)

gcd([8, 36, 28]) # 4