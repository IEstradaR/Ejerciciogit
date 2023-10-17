#Crea un diccionario para 3 monedas, dolar, euro y bitcoin
#2. Averigua a como está cada moneda. Ej: Dolar:790
#3. Agrega otra moneda diferente al diccionario
#4. Actualiza el valor del dolar a 800
#5. Recupera el valor del Euro e imprimelo
#6. Imprime Claves, Valores e items del diccionario.

monedas = {"Dolar":788.28, "euro":852, "bitcoin":21650}
#Agregando moneda
monedas["UTF"]=28687
#Actualizando valor 
monedas["Dolar"]=800
#Recuperando o buscando
print(monedas.get("euro"))

#Imprimiendo claves
print("Claves:", monedas.keys())
print("Valores:", monedas.values())
print("Items:", monedas.items())
