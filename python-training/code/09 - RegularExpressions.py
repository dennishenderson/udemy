import re

"""
pattern = r"eggs"

if re.match(pattern, "baconeggseggsbacon"):
    print('Match found')
else:
    print('No match found')
"""

"""
# Search & Find All
pattern = r"eggs"

if re.match(pattern, "baconeggseggsbacon"):
    print('Match found')
else:
    print('No match found')

if re.search(pattern, "baconeggseggsbacon"):
    print('Match found')
else:
    print('No match found')

print(re.findall(pattern, "baconeggseggsbacon"))
"""

"""
# Find and Replace
string = "My name is John, Hi I'm John"
pattern = r"John"
newstring = re.sub(pattern, "Rob", string)
print(newstring)
"""

"""
# The dot metacharacter
pattern = r"gr.y"

if re.match(pattern, "gray"):
    print("Match Found")
"""

"""
# Caret & Dollar Metacharacter
pattern = r"^gr.y$"

if re.match(pattern, "grey"):
    print("Match Found")
"""

"""
# Character class
#AA1
pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "AH6"):
    print("Match Found")
"""

"""
# Star Metacharacter
pattern = r"eggs(bacon)*"

if re.match(pattern, "eggsbaconbacon"):
    print('Match found')
"""



# Group
pattern = r"bread(eggs)*bread"

if re.match(pattern, "breadeggseggsbread"):
    print('Match found')