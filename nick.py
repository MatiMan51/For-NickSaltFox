# да да, типа канкулятор

print("Канкулятор для Ника")
print("ver. 0.69")

what = input("Ник, выбери уже что нить (+, -, *, /): ")

a = float( input("Введи первое число, бистра: ") )
b = float( input("Введи второе число, позязя: ") )

if what == "+":
    c = a + b
    print("Ответ: " + str(c) )
elif what == "-":
    c = a - b    
    print("Ответ: " + str(c) )
elif what == "*":
    c = a * b    
    print("Ответ: " + str(c) )
elif what == "/":
    c = a / b   
    print("Ответ: " + str(c) ) 
else:
    print("А-та-та! Что это ты делаешь? Так писать нельзя!")    