#Importar librerias
import random, os, time

contador_player = 0
contador_cpu = 0

#Este bucle para cuando alguien gane, es decir, cuando alguien acumule 3 contadores
while contador_player < 3 and contador_cpu < 3:
    #El PC elige una opción
    lista_opc = ["piedra", "papel", "tijeras"]
    elegir_opc = random.choice(lista_opc)
    
    opc = str(input("Piedra(R), papel(P) o tijeras(S)... > "))
    opc = opc.lower()
    
    #Hace todas las comparaciones cuanto tu eliges piedra
    if opc == "r" and elegir_opc == "tijeras":
        contador_player += 1
    
    elif opc == "r" and elegir_opc == "papel":
        contador_cpu += 1
    
    elif opc == "r" and elegir_opc == "piedra":
        pass
    

    #Hace todas las comparaciones cuanto tu eliges papel
    elif opc == "p" and elegir_opc == "piedra":
        contador_player += 1
    
    elif opc == "p" and elegir_opc == "tijeras":
        contador_cpu += 1
    
    elif opc == "p" and elegir_opc == "papel":
        pass
    

    #Hace todas las comparaciones cuanto tu eliges tijeras
    elif opc == "s" and elegir_opc == "papel":
        contador_player += 1
    
    elif opc == "s" and elegir_opc == "piedra":
        contador_cpu += 1
    
    elif opc == "s" and elegir_opc == "tijeras":
        pass

    opc = opc.capitalize()
    elegir_opc = elegir_opc.capitalize()

    #Muestra resultados
    print(""" 
    +----------------------------+
    |          ELECCIÓN          |
    +----------------------------+
    Tu --> """, opc , """                   
    CPU --> """, elegir_opc,"""
    
    +----------------------------+
    |         PUNTUACIÓN         |
    +----------------------------+
    Tu --> """, contador_player, """
    CPU --> """, contador_cpu,"""
    """)
    
    time.sleep(3.5)
    
    os.system("cls")

    #Muestra este texto cuando alguien gana
    if contador_cpu == 3:
        for letra in range(5):
            print("cpu win".upper())
            time.sleep(0.5)
            os.system("cls")
            print("cpu win".lower())
            time.sleep(0.5)
            os.system("cls")


    if contador_player == 3:
        for letra in range(5):
            print("you win".upper())
            time.sleep(0.5)
            os.system("cls")
            print("you win".lower())
            time.sleep(0.5)
            os.system("cls")
