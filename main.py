# Un petit programme qui une fois utiliser sur un fichier 
# te donne le nombre de ligne de code de tout les fichiers avec les extension choisie,
#et peut ensuite te donner des stats 



def CountLine(_path):
    _nbLine = 0
    _Path = str(_path)
    f = open(_Path, 'r')
    contenu = f.read()

    with open(_Path, 'r') as f:
        lignes = f.readlines()  # Retourne une liste

    for ligne in lignes:
        _nbLine += 1
    f.close()
    return _nbLine



test = 0
test += CountLine('test.txt')
print(test)