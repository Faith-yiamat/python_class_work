def hello():
    print("Hello AkiraChix")

def hello1(name):
    print(f"Hello {name}")

def year_of_birth(name,age):
    print(f"Hello {name},you are born in {2024-age}")
    
  
def my_country(country = "Kenya"):
    print(f"Hello Akirachix is from {country}")

#  position arguments *
def greet ( *names):
    for name in names:

         print(f"Hello {name}") 

#   key word arguments **
def create_sentence(**words):
    print(words)
    sentence= ""
    for word in words.values():
        sentence += word
        sentence += " "
    return sentence  
# a function that accepts both keyword and positional arguments  
def students():
    students = [{"age": 19, "name": "Eunice"},{"age": 22,"name": "Agnes"},{"age": 21, "name": "Amanda"},{"age": 20,"name": "Asha"}]
    print(students.k)

        
    




