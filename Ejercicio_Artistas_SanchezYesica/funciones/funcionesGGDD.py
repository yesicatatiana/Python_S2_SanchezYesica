import json 

def abrirArtistasJSON():
    dicArtistas = []
    with open("data/datos.json","r") as openFile:
        dicArtistas=json.load(openFile)
    return dicArtistas

def guardarArtistasJSON(dic):
    with open("data/datos.json","w") as outFile:
        json.dump(dic,outFile)

