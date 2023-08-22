from re import *
text="luminar technolab luminar techno hub"
matcher=finditer("luminar",text)
count=0
for m in matcher:
    count+=1
    print(count)
