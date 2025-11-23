"""script pour exécuter le notebook et capturer les sorties (+graph) """
import json
import sys
import os
import io
import base64
import matplotlib
matplotlib.use('Agg')  # backend non-interactif pour cap les graphiques
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from IPython.display import display
import warnings
warnings.filterwarnings('ignore')

# config de l'encodage UTF-8 
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# config du chemin
notebook_path = os.path.join('notebooks', 'kmeans_analysis.ipynb')
output_path = os.path.join('notebooks', 'kmeans_analysis.ipynb')  # Sauvegarder dans le même fichier

def capture_all_plots():
    """capture tous les graph matplotlib ouvert"""
    images = []
    fignums = plt.get_fignums()
    
    for fig_num in fignums:
        fig = plt.figure(fig_num)
        buf = io.BytesIO()
        fig.savefig(buf, format='png', dpi=100, bbox_inches='tight')
        buf.seek(0)
        img_data = base64.b64encode(buf.read()).decode('utf-8')
        buf.close()
        images.append(img_data)
        plt.close(fig)
    
    return images

def execute_cell(code, namespace):
    """exécute une cellule"""
    outputs = []
    stdout_capture = io.StringIO()
    stderr_capture = io.StringIO()
    
    # remplacer plt.show() par une fonction qui capture le graph
    original_show = plt.show
    def show_capture():
        # capturer tous les graph avant de les fermer
        images = capture_all_plots()
        for img_data in images:
            outputs.append({
                'output_type': 'display_data',
                'data': {
                    'image/png': img_data
                },
                'metadata': {}
            })
    
    # remplacer plt.show dans le namespace
    namespace['plt'].show = show_capture
    # et aussi dans matplotlib.pyplot 
    import matplotlib.pyplot as plt_module
    plt_module.show = show_capture
    
    # rediriger stdout et stderr
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = stdout_capture
    sys.stderr = stderr_capture
    
    try:
        # exécuter le code
        exec(code, namespace)
        
        # si plt.show() n'a pas été appelé, capture les graph restants
        if plt.get_fignums():
            images = capture_all_plots()
            for img_data in images:
                outputs.append({
                    'output_type': 'display_data',
                    'data': {
                        'image/png': img_data
                    },
                    'metadata': {}
                })
        
        # capturer les sorties texte
        stdout_text = stdout_capture.getvalue()
        stderr_text = stderr_capture.getvalue()
        
        # ajt les sorties texte
        if stdout_text:
            outputs.append({
                'output_type': 'stream',
                'name': 'stdout',
                'text': stdout_text.splitlines(True)
            })
        
        if stderr_text:
            outputs.append({
                'output_type': 'stream',
                'name': 'stderr',
                'text': stderr_text.splitlines(True)
            })
            
    except Exception as e:
        # capturer les erreurs
        error_output = {
            'output_type': 'error',
            'ename': type(e).__name__,
            'evalue': str(e),
            'traceback': [f"{type(e).__name__}: {str(e)}"]
        }
        outputs.append(error_output)
        print(f"Erreur: {e}", file=old_stderr)
    finally:
        # restaurer stdout et stderr
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        namespace['plt'].show = original_show
        import matplotlib.pyplot as plt_module
        plt_module.show = original_show
        stdout_capture.close()
        stderr_capture.close()
    
    return outputs

# lire le notebook
print("Lecture du notebook...")
with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

print(f"✓ Notebook chargé: {len(notebook['cells'])} cellules trouvées\n")

# créer un namespace global pour l'exécution
namespace = {
    '__builtins__': __builtins__,
    'pd': pd,
    'np': np,
    'plt': plt,
    'sns': sns,
    'display': display,
    'warnings': warnings
}

# exécuter toutes les cellules de code
executed_count = 0
error_count = 0

for i, cell in enumerate(notebook['cells']):
    if cell['cell_type'] == 'code':
        code = ''.join(cell['source'])
        
        # corriger les chemins relatifs pour qu'ils fonctionnent depuis la racine
        code = code.replace('../data/', 'data/')
        
        # ignorer les cellules vides
        if code.strip():
            print(f"Exécution de la cellule {i+1}...")
            try:
                # exécuter et capturer les sorties
                outputs = execute_cell(code, namespace)
                
                # maj la cellule avec les sorties
                cell['outputs'] = outputs
                cell['execution_count'] = executed_count + 1
                
                executed_count += 1
                print(f"✓ Cellule {i+1} exécutée avec succès ({len(outputs)} sortie(s))\n")
            except Exception as e:
                error_count += 1
                print(f"⚠ Erreur dans la cellule {i+1}: {type(e).__name__}: {e}\n")
                # ajt l'erreur comme sortie
                cell['outputs'] = [{
                    'output_type': 'error',
                    'ename': type(e).__name__,
                    'evalue': str(e),
                    'traceback': [f"{type(e).__name__}: {str(e)}"]
                }]
                continue

# sav le notebook avec toutes les sorties
print("Sauvegarde du notebook avec toutes les sorties...")
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)

print("="*70)
print(f"Résumé de l'exécution:")
print(f"  Cellules exécutées: {executed_count}")
print(f"  Erreurs: {error_count}")
print(f"  Notebook sauvegardé: {output_path}")
print("="*70)
print("\n✓ Notebook exécuté avec tous les graphiques!")

