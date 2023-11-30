"""
Finds all keys in the provided dictionary that have the given value.

Use dictionary.items(), a generator and list() to return all keys that have a value equal to val.
"""
def find_keys(dict, val):
  return list(key for key, value in dict.items() if value == val)

ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 10,
}
find_keys(ages, 10) # [ 'Peter', 'Anna' ]