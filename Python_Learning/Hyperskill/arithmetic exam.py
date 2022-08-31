import random
from random import choice
# Genera dos números del 2 al 9 y los imprime en forma de operación, con un operador aleatorio
# Se ingresa la respuesta. Si la respuesta es correcta imprime "Right" y "Wrong" si es incorrecta.
welcome = """Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares 11-29"""
print(welcome)

mark = 0
n = 5
operands = "23456789"
operators = "+-*"

def menu():
    while True:
        try:
            a = int(input())
            if a == 1 or a == 2:
                return a
            else:
                raise ValueError
        except ValueError:
            print("Incorrect format")

option = menu()

if option == 1:
    level = "simple operations with numbers 2-9"
elif option ==2:
    level = "integral squares 11-29"


def get_int_from_user():
    while True:
        try:
            return int(input())
        except ValueError:
            print("Incorrect format.")


def simple():
    for _ in range(n):
        global mark
        expr = choice(operands) + " " + choice(operators) + " " + choice(operands)
        print(expr)
        if get_int_from_user() == eval(expr):
            print("Right!")
            mark += 1
        else:
            print("Wrong!")


def integral():
    for _ in range(n):
        global mark 
        base = random.randint(11, 29)
        print(base)
        r = get_int_from_user()
        if r == base ** 2:
            print("Right!")
            mark +=1
        else:
            print("Wrong!")


question = "Would you like to save your result to the file? Enter yes or no "
if option == 1:
    simple()
    answer = input(f"Your mark is {mark}/{n}. {question}") 
elif option == 2:
    integral()
    answer = input(f"Your mark is {mark}/{n}. {question}")

# Evaluador de respuestas: 
accepted_yes = " yes , YES , y , Yes "
accepted_no = "no, NO, n, No"
if answer in accepted_yes:
    name = input("What is your name? ")
    with open("results.txt", "w") as name_file:
        name_file.write(f"{name}: {mark}/{n} in level {option} ({level})")
    print('The results are saved in "results.txt"')
elif answer in accepted_no:
    pass
