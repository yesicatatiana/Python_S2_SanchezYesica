linea = 45

def mostrarArtistas(lista):
    for artista in lista:
        print("-"*linea)
        print(f'ID Artista: {artista["id"]}')
        print(f'Nombre Artista: {artista["Artist name"]}')
        print(f'País de Origen: {artista["Country"]}')
        print(f'Años de actividad: {artista["Active years"]}')
        print(f'Año de lanzamiento del primer disco: {artista["Release year of first charted record"]}')
        print(f'Genero Musical: {artista["Genre"]}')
        print(f'Unidades certificadas totales: {artista["Total certified units"]}')
        print(f'Ventas Reclamadas: {artista["Claimed sales"]}')
        print("-"*linea)
