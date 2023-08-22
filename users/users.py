f=open("C:\\Users\\Admin\\PycharmProjects\\pythonProject1\\users\\data.txt","r")
users=[]
for line in f:
    text=line.rstrip("\n")
    name,followers,followings=text.split(",")
    print(name,followers,followings)
