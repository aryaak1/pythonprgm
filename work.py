text="ABABC"
#FIND RECURSIVE CHARACTER

#create empty dictionary
#ch=A
#
wc={}
count = 0
for ch in text:
    if ch in wc:
       wc[ch]+= 1
    else:
      wc[ch] = 1
print(wc)

#A:2 B:2 c:1




