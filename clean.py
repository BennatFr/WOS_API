import os
import glob

# Parcours tous les répertoires 'migrations'
for dirpath, dirnames, filenames in os.walk("."):
    if "migrations" in dirnames:
        migration_dir = os.path.join(dirpath, "migrations")
        # Supprimer tous les fichiers .py sauf __init__.py
        for migration_file in glob.glob(os.path.join(migration_dir, "*.py")):
            if not migration_file.endswith("__init__.py"):
                os.remove(migration_file)
        # Supprimer les fichiers .pyc si nécessaire
        for migration_file in glob.glob(os.path.join(migration_dir, "*.pyc")):
            os.remove(migration_file)

print("Migrations cleaned.")