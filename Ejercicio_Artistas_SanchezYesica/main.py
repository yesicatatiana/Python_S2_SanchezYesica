#Gestion de datos musicales:
#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
'''
    {
        "Artist name": "Aretha Franklin",
        "Country": "United States",
        "Active years": "1956\\u20132018",
        "Release year of first charted record": 1961,
        "Genre": "Soul \\/ jazz \\/ blues \\/ R&B",
        "Total certified units": "27 millionUS: 23.5 millionUK: 3.040 millionFRA: 275,000CAN: 150,000ITA: 110,000",
        "Claimed sales": "75 million"
    }
'''

from data import *
from funciones.funcionesGGDD import *
from funciones.funcionesMod import *

booleanito = True
listaArtistas = abrirArtistasJSON()
while(booleanito):
    
    print("="*linea)
    print("bienvenido al programa".upper().center(linea))
    print("="*linea)
    modulos = int(input("Elige una opción\n 1. Gestión de artistas\n 2. Generación de informes\n 3. Modulo reportes\n 4. Salir\n"))

    if(modulos == 1):
        print("-"*linea)
        print("Modulo artistas".upper().center(linea))
        print("-"*linea)
        elegirArt = int(input("Elige una opción\n 1. Registrar Artista\n 2. Mostrar Artistas\n 3. Actualizar Artistas\n 4. Eliminar Artistas\n"))
        if(elegirArt == 1):
            print("-"*linea)
            print("Registro de artista".upper().center(linea))
            print("-"*linea)
            nomArt = input("Digite el nombre del artista: ")
            paisArt = input("Digite el país del artista: ")
            actAniosArt = input("Años activo: ")
            anioPrimerDiscoArt = int(input("Año de lanzamiento del primer disco: "))
            GenArt = input("Genero musical: ")
            totalUnidades = input("Total de unidades certificadas: ")
            ventasReclamadas= input("Ventas reclamadas: ")
            dicArtistas = { "Artist name": nomArt,
                        "Country": paisArt,
                        "Active years": actAniosArt,
                        "Release year of first charted record": anioPrimerDiscoArt,
                        "Genre": GenArt,
                        "Total certified units": totalUnidades,
                        "Claimed sales": ventasReclamadas
                        }
            listaArtistas.append(dicArtistas)
            guardarArtistasJSON(listaArtistas)

        elif(elegirArt == 2):
            print("-"*linea)
            print("mostrar artistas".upper().center(linea))
            print("-"*linea)
            mostrarArtistas(listaArtistas)
        elif(elegirArt == 3):
            print("-"*linea)
            print("mostrar artistas".upper().center(linea))
            print("-"*linea)
            mostrarArtistas(listaArtistas)

    elif(modulos == 4):
        print("Adiós")
        booleanito = False


