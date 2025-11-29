"""script pour exécuter toutes les cellules du notebook kmeans_analysis.ipynb"""
import json
import sys
import os
import io

# config de l'encodage UTF-8 
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# config du chemin
notebook_path = os.path.join('notebooks', 'kmeans_analysis.ipynb')

# lire le notebook
print("Lecture du notebook...")
with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

print(f"OK - Notebook charge: {len(notebook['cells'])} cellules trouvees\n")

# créer un namespace global pour l'exécution
namespace = {}

# exécuter toutes les cellules de code
executed_count = 0
error_count = 0

for i, cell in enumerate(notebook['cells']):
    if cell['cell_type'] == 'code':
        code = ''.join(cell['source'])
        
        # corriger les chemins relatifs pour qu'ils fonctionnent
        code = code.replace('../data/', 'data/')
        
        # ignorer les cellules vides
        if code.strip():
            print(f"Execution de la cellule {i+1}...")
            try:
                exec(code, namespace)
                executed_count += 1
                print(f"OK - Cellule {i+1} executee avec succes\n")
            except Exception as e:
                error_count += 1
                print(f"ERREUR dans la cellule {i+1}: {type(e).__name__}: {e}\n")
                # continuer l'exécution même en cas d'erreur
                continue

print(f"Resume de l'execution:")
print(f"  Cellules executees: {executed_count}")
print(f"  Erreurs: {error_count}")


