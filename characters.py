import re
from re import *
text="aabdXYZ$#098"
mathcter=re.finditer("[^a-zA-Z0-9]",text)
print(mathcter)
for m in mathcter:
    print(m.group())

