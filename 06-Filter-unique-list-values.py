"""
Creates a list with the unique values filtered out.

Use collections.Counter to get the count of each value in the list.
Use a list comprehension to create a list containing only the non-unique values.
"""
from collections import Counter

def filter_unique(lst):
  return [item for item, count in Counter(lst).items() if count > 1]

filter_unique([1, 2, 2, 3, 4, 4, 5]) # [2, 4]
