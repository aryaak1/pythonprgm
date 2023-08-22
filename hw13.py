text="ABBAACCCDA"
#PRINT MOST RECURSIVE CHARACTER


text="goodmorning hello goodevening hello"
#print longest word in given text

#----------------------------------------------
text="ABBAACCCDA"
wc={}
for ch in text:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
print(wc)
#wc={'A': 4, 'B': 2, 'C': 1, 'D': 1}
#max,min,sum,sort
#print(max(wc))
#---max recursive character-------
print(max(wc,key=lambda key:wc.get(key)))
#-----min recursive character-------
print(min(wc,key=lambda key:wc.get(key)))

# def get_value(key):
#     return wc.get(key)

# --------------example---------------------
# person={"name":"mumthas","salary":"25000"}
#  person["salary"]=50000
# print(person["salary"])
# def get_value_bykey(key):
#     return person.get(key)
# print(get_value_bykey("name"))
# -----------------------------------


