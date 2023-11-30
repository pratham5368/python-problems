"""
Use a list comprehension and zip() to add elements to groups, based on filter.
If filter has a truthy value for any element, add it to the first group, otherwise add it to the second group.
"""
def bifurcate(lst, filter):
  return [
    [x for x, flag in zip(lst, filter) if flag],
    [x for x, flag in zip(lst, filter) if not flag]
  ]

bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True])
# [ ['beep', 'boop', 'bar'], ['foo'] ]