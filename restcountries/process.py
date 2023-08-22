from json import load
with open("C:\\Users\\Admin\\PycharmProjects\\pythonProject1\\restcountries\\rest.json",encoding="UTF-8") as f:
    data=load(f)


    # print(len(data))


#print all country names
# for d in data:
#     print(d.get("name"))

# all_country_names=[c.get("name") for c in data ]
# print(all_country_names)

#print all regions

# region={d.get("region")for d in data}
# print(region)

#print asian country names

# asian_country_names=[d.get("name")for d in data if "Asia" in d.get("region")]
# print(asian_country_names)

#print  afghanisthan population

# for d in data:
#     if d.get("name")=="Afghanistan":
#       print(d.get("population"))


#indian borders

# for d in data:
#     if d.get("name")=="indian_borders":
#         print(d.get("indian_borders"))
#         print(d)

# country_borders=[c.get("borders")for c in data if c.get("name")=="India"][0]
# print(country_borders)
# country_border_name=[c.get("name")for c in data if c.get("alpha3Code") in country_borders]
# print(country_border_name)

#indian currency code
# for d in data:



#print

