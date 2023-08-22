w1=input("enter word1:")
w2=input("enter word2:")
# s_w1=sorted(w1)
# s_w2=sorted(w2)
# for i in w1:
#
wc={}
is_kangaroo=True
for c in w1:
    if c in wc:
        wc[c]+=1
    else:
        wc[c]=1
for ch in w2:
    if ch in wc and wc[ch]>0:
        wc[ch]-=1
    else:
        is_kangaroo=False
        break
print(is_kangaroo)