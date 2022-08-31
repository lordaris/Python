import operator as op

msg_ = [
    "Enter an equation ",
    "Do you even know what numbers are? Stay focused!",
    "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    "Yeah... division by zero. Smart move...",
    "Do you want to store the result? (y / n):",
    "Do you want to continue calculations? (y / n):",
    " ... lazy",
    " ... very lazy",
    " ... very, very lazy",
    "You are",
    "Are you sure? It is only one digit! (y / n)",
    "Don't be silly! It's just one number! Add to the memory? (y / n)",
    "Last chance! Do you really want to embarrass yourself? (y / n)",
]
memory = 0
ops = {
    "+": op.add,
    "-": op.sub,
    "*": op.mul,
    "/": op.truediv,
}
store = ""


def is_one_digit(v):
    if float(v).is_integer():
        if -10 < float(v) < 10:
            return True
    else:
        return False


def check_(v1, v2, v3):
    msg = ""
    is_one_digit1 = is_one_digit(v1)
    is_one_digit2 = is_one_digit(v2)
    if is_one_digit1 and is_one_digit2:
        msg = msg + msg_[6]
    if (v1 == "1" or v2 == "1") and (v3 == "*"):
        msg = msg + msg_[7]
    if (v1 == "0" or v2 == "0") and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_[8]
    if msg != "":
        msg = msg_[9] + msg
    print(msg)


def loop_(n):
    global store
    mensaje = ""
    msg_index = 10
    if is_one_digit(n):
        while store == "y" and msg_index < 13:
            mensaje = input(msg_[msg_index])
            store = mensaje
            msg_index += 1
        if mensaje == "n":
            store = "n"
    else:
        store = "y"


while True:
    calc = input(msg_[0])
    x, oper, y = calc.split(" ")
    operators = "+-*/"
    c = oper in operators
    if c:
        try:
            if x == "M":
                x = memory
            if y == "m":
                y = memory
            elif y == "M":
                y = memory
            else:
                pass
            check_(str(x), str(y), oper)
            x = float(x)
            y = float(y)
            answer = (ops[oper](x, y))
            print(answer)

            store = input(msg_[4])
            if store == "y":
                loop_(answer)
            if store == "y":
                memory = answer
                continue_ = input(msg_[5])
                if continue_ == "y":
                    continue
                else:
                    break
            else:
                #               memory = 0
                continue_ = input(msg_[5])
                if continue_ == "y":
                    continue
                else:
                    break

        except ValueError:
            print(msg_[1])
        except ZeroDivisionError:
            print(msg_[3])
    else:
        print(msg_[2])
