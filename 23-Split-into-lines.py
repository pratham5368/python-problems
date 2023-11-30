"""
Splits a multiline string into a list of lines.

Use str.split() and '\n' to match line breaks and create a list.
str.splitlines() provides similar functionality to this snippet.
"""
def split_lines(s):
  return s.split('\n')

split_lines('This\nis a\nmultiline\nstring.\n')
# ['This', 'is a', 'multiline', 'string.' , '']