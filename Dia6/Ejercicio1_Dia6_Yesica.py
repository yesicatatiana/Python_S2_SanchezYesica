# #######################
# ##### clase dia 6 #####
# #######################

# diccionarios

#producto = {
#    "nombre" : " ",
#   "precio" : 0.0
#}
#inventario = []

#inventario.append({"nombre":"clavo","precio": .30} )
#inventario.append({"nombre":"tornillo","precio":.15})

#print(inventario)

#for p in inventario:
#    print("_____________________")
#    print('\t nombre',p['nombre'])
#    print('\t precio',p['precio'])


'''
miPrimerDiccionario={
    "nombre":"Pedro",
    "apellido":"Gómez",
    "edad":25
}

print(miPrimerDiccionario)
print(type(miPrimerDiccionario))

##Para recorrer un DICcionario debes llamar a la llave

print(miPrimerDiccionario["nombre"])
print(type(miPrimerDiccionario["nombre"]))

# Se puede recorrer con puntos en algunos casos

'''
#print(miPrimerDiccionario.nombre)
'''

##Para reemplazar un valor del diccionario

miPrimerDiccionario["nombre"]="Pedro"
nombre = miPrimerDiccionario["nombre"]
apellido= miPrimerDiccionario["apellido"]
print(miPrimerDiccionario["nombre"]+" "+miPrimerDiccionario["apellido"])

miPrimerDiccionario["ciudadNacimiento"]="Monteria"

print(miPrimerDiccionario)
miPrimerDiccionario["ciudadNacimiento"]="Bucaramanga"

print(miPrimerDiccionario)


#Un objeto tiene varios atributos, 
# que pertenecen al mismo objeto. 

listaPersonas=[]
listaPersonas.append(miPrimerDiccionario)
print("")
print("")
print(listaPersonas)
listaPersonas.append({
    "nombre":"Corpus",
    "apellido":"Bejarano",
    "edad":27
})

print("")
print("")
print(listaPersonas)
print("")
print("")
print(listaPersonas[1])
print(type(listaPersonas[1]))
print(listaPersonas[0]["edad"])



#Recorrer listas con diccionarios

for i in range(len(listaPersonas)):
    print("#################")
    print("####Persona #",i+1," ####")
    print("#################")
    print("Nombre:",listaPersonas[i]["nombre"])
    print("Apllido:",listaPersonas[i]["apellido"])
    print("Edad:",listaPersonas[i]["edad"])

    ##Diccionario con listas


diccionarioRobusto={
    "id":1,
    "nombre":"Pedro",
    "apellido":"Gómez",
    "edad":25,
    "telefonos":[{"codigo":57,"numero":3023019865,"tipo":"trabajo"}
                 ,{"codigo":1,"numero":3983054625,"tipo":"personal"}]
}

listaRobusta=[]
listaRobusta.append(diccionarioRobusto)
listaRobusta.append(diccionarioRobusto2)
print("")
print("")
print(listaRobusta)
print("")
print("")
#print(listaRobusta[0]["telefonos"][1]['numero'])

for i in range(len(listaRobusta[0]["telefonos"])):
    if(listaRobusta[0]["telefonos"][i]['tipo']=="trabajo"):
        print(listaRobusta[0]["telefonos"][i]['numero'])
print("")
print("")
numeroPrimeraPersona=listaRobusta[0]["telefonos"][1]['numero']
tipoNumeroPP=listaRobusta[0]["telefonos"][1]['tipo']
print(str(numeroPrimeraPersona)+ tipoNumeroPP)

booleanito = True


while(booleanito):
    print("#################")
    print("#### Librería de personas ####")
    print("#################")

    #CRUD (CREATE , READ , UPDATE & DELETE)

    print("1. Crear Persona")
    print("2. Mostrar todas las personas")
    print("3. Mostrar a una persona individual")
    print("4. Actualizar a una persona en específico")
    print("5. Eliminar a una persona en específico")
    print("6. Cerrar programa")
    opcionUsuario=int(input("Escoja una opción (Numérica):"))
    if(opcionUsuario==1):
        print("#################")
        print("#### Crear Persona ####")
        print("#################")
        diccionarioVacio={}

    elif(opcionUsuario==2):
        for i in range(len(listaRobusta)):
            print("#################")
            print("#### Persona #",i+1," ####")
            print("#################")
            print("ID:", listaRobusta[i]["id"])
            print("Nombre:",listaRobusta[i]["nombre"])
            print("Apellido:",listaRobusta[i]["apellido"])
            print("Edad",listaRobusta[i]["edad"])

            for q in range(len(listaRobusta[i]["telefonos"])):
                print("---------------------------")
                print("Telefono#",q+1,":")
                print("#### - Código:",listaRobusta[i]["telefonos"][q]["codigo"])
                print("#### - Numero:",listaRobusta[i]["telefonos"][q]["numero"])
                if(listaRobusta[i]["telefonos"][q]["tipo"] == "personal"):
                    print("#### - Tipo: Es su número Personal")
                else:
                    print("#### - Tipo: Es su número de Trabajo")
                print("---------------------------")

    elif(opcionUsuario==6):
        print("Chaousssss")
        booleanito=False
    else:
        print("No es una opción válida")


'''