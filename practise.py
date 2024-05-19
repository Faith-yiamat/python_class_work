# How to use the break and a while loop

w = [1,2,3,4,5,6]
for i in w:
    if(i == 4):
        break
    print(i)

x = ["Faith","Daisy","Yvonne","Lilian","Maureen"]  
for i in x:
    if(i == "Daisy"):
        continue  
    print(i)



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello My name is" " " + self.name)

p1 = Person("John", 36)
print(p1.myfunc())

