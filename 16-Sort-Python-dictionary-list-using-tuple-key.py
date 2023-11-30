"""
Sorting a list of dictionaries in Python can seem intimidating at first. This is especially true if you want to sort using multiple keys. Luckily, the sorted() function can be used to sort a list of dictionaries using a tuple key. Simply return a tuple with the order of keys you want to sort by and the sorted() function will do the rest.
"""
friends =  [
  {"name": "John", "surname": "Doe", "age": 26},
  {"name": "Jane", "surname": "Doe", "age": 28},
  {"name": "Adam", "surname": "Smith", "age": 30},
  {"name": "Michael", "surname": "Jones", "age": 28}
]

print(
  sorted(
    friends,
    key=lambda friend:
    (friend["age"], friend["surname"], friend["name"])
  )
)
# PRINTS:
# [
#   {'name': 'John', 'surname': 'Doe', 'age': 26},
#   {'name': 'Jane', 'surname': 'Doe', 'age': 28},
#   {'name': 'Michael', 'surname': 'Jones', 'age': 28},
#   {'name': 'Adam', 'surname': 'Smith', 'age': 30}
# ]