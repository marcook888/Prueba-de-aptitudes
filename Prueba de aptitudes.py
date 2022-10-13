
# Datos a evaluar 
arreglo_de_piso = [5, 29, 13, 10]
piso_de_ejecucion = 4 
piso_ingresado = {5:2, 29: 10, 13: 1, 10:1}

#extraigo los values del diccionario
pisos_ingresados = piso_ingresado.values()

#print(pisos_ingresados)


#Junto las tablas para tener todos los pisos del arreglo y ingresados juntos 
arreglo_de_piso.extend(pisos_ingresados)

#print (arreglo_de_piso)

#recorre primero los pisos del arreglo 
for x in arreglo_de_piso:
    #imprime los pisos 
    for i in range (piso_de_ejecucion,arreglo_de_piso[0]):
        print("elevador en piso",i)

    #identifica si sube o baja
    if arreglo_de_piso[0] > piso_de_ejecucion :
        direccion="subiendo"
    else:
        direccion="descendiendo"
    
    #cambia el piso actual
    piso_de_ejecucion = arreglo_de_piso[0]  
    
    #elimina el primer elemneto del arreglo
    arreglo_de_piso.pop(0)

    #imprime lo esperado
    print("elevador en piso", piso_de_ejecucion)

    print("elevador", direccion)

    print("elevador se detiene  -->",arreglo_de_piso )


 
#recorre los pisos ingresados 
for x in arreglo_de_piso:
    #imprime los pisos 
    for i in range (piso_de_ejecucion,arreglo_de_piso[0]):
        print("elevador en piso",i)

    #identifica si sube o baja
    if arreglo_de_piso[0] > piso_de_ejecucion :
        direccion="subiendo"
    else:
        direccion="descendiendo"
    
    #cambia el piso actual
    piso_de_ejecucion = arreglo_de_piso[0]  
    
    #elimina el primer elemneto del arreglo
    arreglo_de_piso.pop(0)

    #imprime lo esperado
    print("elevador en piso", piso_de_ejecucion)

    print("elevador", direccion)

    print("elevador se detiene  -->",arreglo_de_piso )





   