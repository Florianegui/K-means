"""script pour exécuter le notebook kmeans_analysis.ipynb"""
import sys
import os

# ajt le répertoire notebooks au path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'notebooks'))
sys.path.insert(0, os.path.dirname(__file__))

# exécute le notebook avec nbconvert
import subprocess

notebook_path = os.path.join('notebooks', 'kmeans_analysis.ipynb')
output_path = os.path.join('notebooks', 'kmeans_analysis_executed.ipynb')

try:
    # essayer avec python -m jupyter
    result = subprocess.run(
        [sys.executable, '-m', 'jupyter', 'nbconvert', 
         '--to', 'notebook', '--execute', 
         '--inplace', notebook_path],
        capture_output=True,
        text=True,
        cwd=os.path.dirname(__file__)
    )
    
    if result.returncode == 0:
        print("✓ Notebook exécuté avec succès!")
        print(f"✓ Résultats sauvegardés dans: {notebook_path}")
    else:
        print("Erreur lors de l'exécution:")
        print(result.stderr)
        print("\nTentative d'exécution directe du code...")
        # exécuter directement le code
        exec(open(notebook_path).read())
        
except Exception as e:
    print(f"Erreur: {e}")
    print("\nTentative d'exécution directe du code Python...")
    # alternative: exécuter directement le code
    import json
    
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # exécuter toutes les cellules de code.
    for i, cell in enumerate(notebook['cells']):
        if cell['cell_type'] == 'code':
            code = ''.join(cell['source'])
            try:
                exec(code)
                print(f"✓ Cellule {i+1} exécutée")
            except Exception as e:
                print(f"⚠ Erreur dans la cellule {i+1}: {e}")

