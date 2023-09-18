def get_content(num):
    content = (num**2)*3.14
    print("Obsah kruhu je "+str(content))

def get_num():
    global number
    x = int((input("Zadej polomer: ")))
    number = x

try:
    get_num()
    if number > 0:
        get_content(number)
    else:
        raise ArithmeticError
except ArithmeticError:
    print('You have just made an Arithmetic error')

