f1=open("C:\\Users\\Admin\\PycharmProjects\\pythonProject1\\fileinputoutput\\attendence.txt")
f2=open("C:\\Users\\Admin\\PycharmProjects\\pythonProject1\\fileinputoutput\\present.txt")
total=set()
present=set()
for line in f1:
    total.add(line.rstrip("\n"))
print(total)

for line in f2:
    present.add(line.rstrip("\n"))
print(present)
absent=total-present
print(absent)