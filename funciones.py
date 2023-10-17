
def sumar(num1, num2):
    return num1+num2

def restar(num1, num2):
    return num1-num2

def dividir(num1, num2):
    return num1/num2

def multiplicar(num1, num2):
    return num1*num2

numero1=float(input("Ingrese un numero \n"))
numero2=float(input("Ingrese otro numero \n"))
operacion=input("Que operacion desea realizar +, -, *, /")

if operacion=="+":
    print(sumar(numero1, numero2))
elif operacion=="-":
    print(restar(numero1, numero2))
elif operacion=="*":
    print(multiplicar(numero1, numero2))
elif operacion=="/":
    print(dividir(numero1, numero2))
else:
    print("Operacion Invalida")



