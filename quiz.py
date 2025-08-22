class Employee_mamagement:
    def __init__(self,name ,id,salary):
       self.name=name
       self.id=id
       self.salary=salary

    def display(self):
        print(f'''
              id is: {self.id}
              name is:{self.name}
             salary is: {self.salary}
              ''')
    def applay(self,persentage):
        # self.per=persentage
         self.salary += self.salary*(persentage/100)
         return self.salary
    



m=Employee_mamagement("mina",1,1000)
m.display()
m.applay(20)
m.display()