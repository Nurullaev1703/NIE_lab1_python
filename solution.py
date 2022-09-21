def my_program():
    try:
        a = float(input("Введите число а: "))
        b = float(input("Введите число b: "))
        x = float(input("Введите число c: "))
        y = 0
    except ArithmeticError:
        print("Неправильно введенные данные!")
    try:
        if x < 7:
            y = (2*a*b*x)/(a+pow(b,2))
        else:
            y = x*(pow(a,2)+ 4*b)
        print("y = " , y)
    except ArithmeticError:
        print("Нет ответа!")