data={"django":"framework",
      "react":"library",
      "fastapi":"framework",
      "vue":"framework",
      "ajax":"library"}


# values=data.values()
# print(values)
# wc={}
# for w in values:
#       if w in wc:
#             wc[w]+=1
#       else:
#             wc[w]=1
# print(wc)


wc={}
for k,v in data.items():
       if v in wc:
             wc[v].append(k)

       else:
            wc[v]=[k]
print(wc)


