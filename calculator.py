def add(x,y):
    result = x+y
    return result
def subtract(x,y):
    result = x-y
    return result
def divide(x,y):
    result = x/y
    return result
def multiply(x,y):
    result = x*y
    return result
def remainder(x,y):
    result = x%y
    return result
def power_of(x,y):
    result = x ** y
    return result
def addAll (* numbers):
    total = 0
    for number in numbers:
        total += number
    return total
def multiply_many( * numbers):
    total = 1
    for number in numbers:
        total *= number 
    return total 

   # both kwargs and args
def sum_and_greeting(*args, **kwargs):
    total = 0
    for x in args:
        total+= x
    f = kwargs["firstname"]
    l = kwargs["lastname"]
    greeting = f"Hello {f} {l}  the sum of your numbers is {total}"
    return greeting

def modulus(numbers):
    sum = 0
    for i in numbers:
        sum +=i
        modulus = sum % 3
    print(modulus)
def mod(num):
    sum = 0
    for i in num:
      total = sum + i
      module = total % 3
    print(module) 



    