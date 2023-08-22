class student:
    rolno:int
    name:str
    course:str

    def add_student(selfself,rol,name,course):
        self.rolno=rol
        self.name=name
        self.course=course

    def get_student(selfself):
        print(self.rolno,self.name,self.course)

obj1=student()
obj2=student()
obj1.add_student(123,"hari","django")
obj1.get_student()
obj2.add_student()