f= open("C:\\Users\\Admin\\PycharmProjects\\pythonProject1\\leapyear\\data.txt","w")

years=[20000,2024,1991,1995,1200,1400,1234]
for y in years:
    if(y %100==0 and y %400==0):
        f.write(y)
    elif(y %100 !=0 and y %4==0):
        f.write(y)