student={"id":1,"admission no":3887,"batch":"python","year":2023,"fees":25000}
print(student)

if("batch" in student):
    print(student["batch"])
else:
    print("no such key value")

#print all key value pair----

for key in student:
    print(key,":",student[key])

#add new key value pair---

student["name"]="arya"
print(student)

#add 500 rs discount on fees

student["fees"]-=500
print(student)


