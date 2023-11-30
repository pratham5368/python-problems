

#Use map() combined with int on the string representation of n and return a list from the result.
def digitize(n):
  return list(map(int, str(n)))

digitize(123) # [1, 2, 3]
