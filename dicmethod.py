# methods inside dict

#list (append,pop,insert,extend,clear)
#set (add,union,intersection,difference)
#tuple(count)
#all utility classes and function are defined in builtins.py

student={"roll":1234,"name":"hari","age":25,"course":"mca"}

#to print values-----------

# print(student.values())

#to print keys--------

# print(student.keys())

#to print keys and values-----(items)

# for k,v in student.items():
#     print(k,v)

#get(key)

# print(student["names"])
# print(student.get("name"))

# print("file transfer")
# print("database commit")

#pop (key)

student.pop("course")
print(student)