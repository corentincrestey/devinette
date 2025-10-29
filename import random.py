import random

def devinette():
    a, n = random.randint(1, 100), int(input("starting guess : "))
    for i in range(5):
        if n == a:
         return "you win"
        if n > a:
            n = int(input("smaller :"))
        else:
           n = int(input("greater :"))
    return("you loose")

print(devinette())