import re
mob=input("enter your mobile number with country code:")
x=re.search("^[+]91",mob)
if(x):
    print("number is Indian")
else:
    print("number is not indian")
