import random
#random para generar elementos aleatorios

def jugar(humano, pc):

    if(humano=="piedra" and pc=="papel") or (humano=="papel" and pc=="tijera"):
        print("Gana el PC")
    elif humano==pc:
        print("empate")
    else:
        print("Ganaste a la Pc")

if __name__ == "__main__":

    print("Opciones: piedra, papel, tijera")

    opciones = ["piedra", "papel", "tijera"]

    humano = input("Ingrese su jugada \n") #Tiro del humano

    while humano not in opciones:
        print("Opcion es invalida, intente nuevamente")
        humano = input("Ingrese su jugada \n")
    
    computador = random.choice(opciones)#Tiro del computador
    print("El PC escogio ", computador)
    
    jugar(humano, computador)