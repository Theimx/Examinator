# Un petit programme qui une fois utiliser sur un fichier 
# te donne le nombre de ligne de code de tout les fichiers avec les extension choisie,
#et peut ensuite te donner des stats 

import os

def count_lines_in_file(file_path):

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return len(lines)
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {file_path}: {e}")
        return 0

def count_lines_in_directory(directory, extensions):

    total_lines = 0
    file_count = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                lines = count_lines_in_file(file_path)
                total_lines += lines
                file_count += 1
                print(f"{file}: {lines} lignes")
    
    print("\n--- Statistiques ---")
    print(f"Nombre total de fichiers : {file_count}")
    print(f"Nombre total de lignes : {total_lines}")

# Config :
if __name__ == "__main__":
    chemin = r"YOUR\PATH"
    extensions_cibles = [".py", ".txt"]  # Extensions recherchés
    count_lines_in_directory(chemin, extensions_cibles)
