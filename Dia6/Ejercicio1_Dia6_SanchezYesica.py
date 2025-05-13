# #######################
# ##### clase dia 6 #####
# #######################

# Diccionario {}


contador=True
p=1 

lisPersonas=[]
while(contador):
    print("##############################")
    print("#### Librería de personas ####")
    print("##############################")

    #CRUD (CREATE , READ , UPDATE & DELETE)

    print("1. Crear Persona")
    print("2. Mostrar todas las personas")
    print("3. Mostrar a una persona individual")
    print("4. Actualizar a una persona en específico")
    print("5. Eliminar a una persona en específico")
    print("6. Cerrar programa")
    opcionUsuario=int(input("Escoja una opción (Numérica):"))

    if(opcionUsuario==1):
        print("#######################")
        print("#### crear persona ####")
        print("#######################")

        nombre=(input("ingresa el nombre de la persona "+str(p)+":"))
        apelllido=(input("ingresa el apellido de la persona "+str(p)+":"))
        edad=int(input("ingresa la edad de la persona "+str(p)+":"))
        telefonoTrabajo=int(input("ingresa el numero de telefono del trabajo de la persona "+str(p)+":"))
        telefonoPersonal=int(input("ingresa el numero de telefono perosnal de la persona "+str(p)+":"))

        personas={"id":p,"nombre":nombre,"apellido":apelllido,"edad":edad,"telefonoTrabajo":telefonoTrabajo,"telefonoPersonal":telefonoPersonal}

        lisPersonas.append(personas)
        print(lisPersonas)
        p=p+1

    elif(opcionUsuario==2):
        if lisPersonas==[]:
            print("__________________")
            print("####################################")
            print("#### no hay personas ingresadas ####")
            print("####################################")
        else:
            for i in range(len(lisPersonas)):
                print("#################")
            print("#### Persona #",i+1," ####")
            print("##########################")
            print("ID:", lisPersonas[i]["id"])
            print("Nombre:",lisPersonas[i]["nombre"])
            print("Apellido:",lisPersonas[i]["apellido"])
            print("Edad",lisPersonas[i]["edad"])
            print("numero personal",lisPersonas[i]["numero personal"])
            print("numero trabajo",lisPersonas[i]["numero trabajo"] )

