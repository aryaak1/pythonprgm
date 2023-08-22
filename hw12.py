words=["hello","hai","hello","hai","good","morning","evening"]
#word count

wc={}
for w in words:
    if w in wc:
        wc[w]+=1
    else:
        wc[w]=1
print(wc)


age=input("enter AGE")
if age>0 and age<=10:
    print("child")
elif age>10 and


