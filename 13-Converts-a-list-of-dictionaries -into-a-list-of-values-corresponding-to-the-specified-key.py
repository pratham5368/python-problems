"""
Use a list comprehension and dict.get() to get the value of key for each dictionary in lst.
"""
def pluck(lst, key):
  return [x.get(key) for x in lst]

people = [
  { 'name': 'lisa', 'age': 8 },
  { 'name': 'homer', 'age': 36 },
  { 'name': 'marge', 'age': 34 },
  { 'name': 'bart', 'age': 10 }
]
pluck(people, 'age') # [8, 36, 34, 10]