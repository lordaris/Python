"""A program based on the Collatz Conjecture. Proposed in the book "Automate the Boring Stuff with Python" by Al Sweigart """

def collatz(number):
    while number > 1:
        if number % 2 == 0:
            number = (number // 2)
            print(number)
        elif number % 2 == 1:
            number = (3 * number + 1)
            print(number)

while ValueError:
    try:
        number = int(input("Introduzca un número "))
        break
    except ValueError:
        print("Debe ser un número entero")

collatz(number)
