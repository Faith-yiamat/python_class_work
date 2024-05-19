def print_numbers(n):
    numbers = range(n)
    for number in numbers:
        print(number)
def print_even_numbers(n):
    numbers = range(n)
    for number in numbers:
        if number % 2 == 0:
            print(f"{number} is even")
        else: 
             print(f"{number} is odd") 
def check_divisibility(n):
    numbers = range(n) 
    for number in numbers:
        if number % 3 == 0:
            print(f"{number} is divible by 3")
        elif number % 5 == 0:
            print(f"{number} is divible by 5")
        elif number % 7 == 0:
            print(f"{number} is divible by 7")
        else:
            print(f"{number} is not divisible by 3,5, or 7")        
# while loop continues iterating as long as the set condition is true
def count_down(n):
    x = 4
    while n > x:
        print(n)
        if n == 5:
            break
        n-=1  
 # break is used to break the loop even if the set condition is true
 # continue statement is used to skip the reminder of the current iteration and jumps to the next iteration of the while loop.
def divisible_by_seven(n):
    x = 1
    while x <= n:
        x+=1
        if x % 7 != 0:
            continue

        print(f"{x} is divisible by 7")
# Using while continue and if statement write a function that prints all the odd numbers between 0 and 100

def odd_numbers(n):
    x = 0
    while x < n:
        x+=1
        if x % 2 == 0:
            continue
        print(f"{x} is an odd number")

# create a function named fizzbuzz
# - for numbers divisible by 3 it prints fizz
# - for numbers divisible by 5 it prints buzz
# - for all the other numbers it prints fizzbuzz use if,elif and else
def divisible(n):
    numbers = range(n)
    for number in numbers:
        if number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")  
        else:
            print("fizzbuzz")      

    

          

                      
            
