# import re
# text="abababab"
# text1="aaaabbbbcccc"
# t=re.search("[a]{4}",text)
# t1=re.search("[a]{4}",text1)
# print(t)
# print(t1)


#abcd56789
# import re
# te="abcd1234"
# check=re.search("[a-z]{4}",te)
# print(check)


import re
stri="3457abDARG5643"
s=re.search("[a-z]{2}[A=Z]{4}",stri)
print(s)
