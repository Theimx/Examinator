import os

#Le fichier avec le plus de ligne 
#Une option pour afficher tout les fichiers avec un certains nombre de lignes, +200, 100<fichier<1000,-100
#nombre de fichier par extension

def count_lines_in_file(_filePath):

    try:
        with open(_filePath, 'r', encoding='utf-8') as f:
            _lines = f.readlines()
        return len(_lines)
    except Exception as e:
        print("Erreur lors de la lecture du fichier ", _filePath, ":",e)
        return 0

def count_lines_in_directory(_directory, _extensions):

    _totalLines = 0
    _fileCount = 0

    for root, _, files in os.walk(_directory):
        for file in files:
            if any(file.endswith(ext) for ext in _extensions):
                file_path = os.path.join(root, file)
                lines = count_lines_in_file(file_path)
                _totalLines += lines
                _fileCount += 1
                print(file,":", lines," lignes")

    _sumLine = _totalLines 
    _sumFile = _fileCount
    _arevage = format(_sumLine / _sumFile,'.2f')

    print("\n--- Statistiques ---")
    print("Nombre total de fichiers : ", _fileCount)
    print("Nombre total de lignes : " , _totalLines)
    print("Nombre moyen de lignes par fichier : " , _arevage )

# Config :
if __name__ == "__main__":
    chemin = r"D:\NSI"
    extensionsCibles = [".py", ".txt"]  # Extensions recherchés/comptabilisé par le programme 
    count_lines_in_directory(chemin, extensionsCibles)
