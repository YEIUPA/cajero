# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 18:18:19 2025

@author: LENOVO
"""

import numpy as np

lista_nombres = ["Sofía", "Mateo", "Isabella", "Lucas", "Valentina", "Alejandro", "Emma", 
                 "Santiago", "Martina", "Sebastián", "Camila", "Nicolás", "Valeria", "Gabriel", 
                 "Antonella", "Daniel", "Lucía", "Andrés", "Renata", "Adrián", "Sara", "Diego", 
                 "Julieta", "Joaquín", "Paula", "Leonardo", "Victoria", "Benjamín", "María", "Samuel", 
                 "Amelia", "David", "Elena", "Maximiliano", "Montserrat", "Ángel", "Regina", "Tomás", 
                 "Jimena", "Cristóbal", "Fernanda", "Bruno", "Ana", "Ricardo", "Ximena", "Gael", "Andrea", 
                 "Matías", "Carolina", "Thiago", "Daniela", "Emilio", "Alicia", "Jerónimo", "Natalia", 
                 "Dylan", "Claudia", "Iker", "Patricia", "Iván", "Alejandra", "Alan", "Laura", "Franco", 
                 "Gabriela", "Jesús", "Mariana", "Rodrigo", "Lorena", "Martín", "Melissa", "Juan", "Paola", 
                 "Carlos", "Diana", "Pedro", "Carmen", "Miguel", "Rosa", "Jorge", "Gloria", "Luis", "Silvia", 
                 "Antonio", "Isabel", "José", "Esther", "Manuel", "Beatriz", "Francisco", "Raquel", "Javier", 
                 "Susana", "Raúl", "Pilar", "Alberto", "Eva", "Enrique", "Dolores", "Sergio", "Mercedes", 
                 "Óscar", "Cristina", "Julio", "Rosario"]

diccionario_nombres = {}
dict_users ={i:np.random.randint(10000, 500000) for i in lista_nombres}

str_nombre = ''


for enu, i_name in enumerate(lista_nombres):
    str_nombre = str_nombre + f"\n {enu}" + i_name
    diccionario_nombres[i_name]=[np.random.randint(10000, 500000), f"{i_name}_1"]
    
print(diccionario_nombres)

while True:
    seleccion = int(input(f" Usted quien es?: {str_nombre} \n105: SALIR\n"))
    seleccion_cliente = lista_nombres[seleccion]
    
    valor = diccionario_nombres[seleccion_cliente]
    iden = valor[1]
   
    contrasena= input("digite su contraseña")
    if iden != contrasena:
        print("error")
    
    if seleccion in range(len(lista_nombres)):
        while True:
            operaciones = int(input("Que quiere hacer? Ver\n1: Retirar\n2: Consignar\n3: SALIR\n"))
            
            saldo_cuenta_usuario = dict_users[seleccion_cliente]
            
            #Ver
            if operaciones == 0:
                print(saldo_cuenta_usuario)
            #Retirar
            elif operaciones == 1:
                valor_retiro = int(input("Cuanto quiere retirar?: "))
                if valor_retiro <= saldo_cuenta_usuario:
                    print("Retiro Exitoso")
                    dict_users[seleccion_cliente] = saldo_cuenta_usuario - valor_retiro
                    print("Su saldo es: ", dict_users[seleccion_cliente])
        
            #consignar
            elif operaciones == 2:
                valor_consignar = int(input("¿Cuanto quiere consignar?: "))
                dict_users[seleccion_cliente] = saldo_cuenta_usuario + valor_consignar
                
            else:
                break
            
    elif seleccion == 105:
            break 
    else:
            print("Error: no seleccionó una opción valida")