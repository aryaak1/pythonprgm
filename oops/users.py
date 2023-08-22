class Users:
    data = [
        {"id": 1, "username": "jhon", "email": "jhon@gmail.com", "password": "password@123"},
        {"id": 2, "username": "hari", "email": "hari@gmail.com", "password": "password@123"},
        {"id": 3, "username": "ravi", "email": "ravi@gmail.com", "password": "password@123"},
        {"id": 4, "username": "vijay", "email": "vijay@gmail.com", "password": "password@123"},
        {"id": 5, "username": "vinu", "email": "vinu@gmail.com", "password": "password@123"},
        {"id": 6, "username": "tom", "email": "tom@gmail.com", "password": "password@123"},
    ]

    #def getall_users(self):
    def get(self):
        return(self.data)

    #get one user
    #def getuser_detail(self, id):
    def retrieve(self,id):
        return[u for u in self.data if u.get("id")==id]

    #create a user
    def post(self,obj1):
        self.data.append(obj1)

    #delete a user
    def destroy(self,id):
        obj=[u for u in self.data if u.get("id")==id][0]
        self.data.remove(obj)

    #update a user
    def put(self,id,value):
        obj








obj=Users()
# print(obj.get())

# print(obj.retrieve(2))

# student_data={"id":7,"username":"ram","email":"ram@gmail.com","password":"password@123"}
# obj.post(student_data)
#
# obj.destroy(5)
# print(obj.retrieve(5))
payload={"id": 5,"username":"vinus","email":"vinus@gmail.com","password":"password@123"},
obj.put(5,payload)

print(obj.retrieve(5))

#----------------------------------------------
# list -> get()
# detail -> retrieve(id)
# create -> post()
# update -> put(id)
# delete -> destroy(id)
#--------------------------------------