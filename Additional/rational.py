x = 0
y = 0

def init(a,b):
    global x
    global y
    x = a
    y = b

def summa():
    return x + y

def sub():
    return x - y

def mult():
    return x * y

def diff():
    if y != 0:
        return x / y
    else:
        return print("Делить на 0 нельзя")