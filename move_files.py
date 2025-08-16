
import os
import shutil

# Define source and destination folders
folder1 = "/workspaces/Eurotechniker/Folder1"
folder = "/workspaces/Eurotechniker/Folder"

# Get a list of files in folder1
files_in_folder1 = os.listdir(folder1)

# Get a list of all files in folder and its subdirectories
files_in_folder = []
for dirpath, dirnames, filenames in os.walk(folder):
    for filename in filenames:
        files_in_folder.append(filename)

# Find files that are in folder1 but not in folder
missing_files = set(files_in_folder1) - set(files_in_folder)

# Define a mapping of keywords in filenames to destination subfolders
keyword_to_folder = {
    "riken": "Abrasivos",
    "corte": "Abrasivos",
    "TACOS": "Abrasivos",
    "ASP": "Aspiradores",
    "MACACÃO": "EquipamentosProtecao",
    "filtro": "FiltrosReguladores",
    "MASCARAMENTO": "FolhetosGerais",
    "lixadeira": "Lixadeiras",
    "LE-150": "Lixadeiras",
    "N-125G": "Lixadeiras",
    "AP-EM-20N": "OutrosEquipamentos",
    "CP-10": "OutrosEquipamentos",
    "DP-800": "OutrosEquipamentos",
    "LS-20G": "OutrosEquipamentos",
    "kha-200P": "OutrosEquipamentos",
    "H-90G": "Pistolas",
    "HK-827G": "Pistolas",
    "S-990G-AV": "Pistolas",
    "S-990S-AV": "Pistolas",
    "f-100": "Pistolas",
}

# Move the missing files to the appropriate subfolder
for file in missing_files:
    moved = False
    for keyword, dest_folder in keyword_to_folder.items():
        if keyword in file:
            source_path = os.path.join(folder1, file)
            dest_path = os.path.join(folder, dest_folder, file)
            shutil.move(source_path, dest_path)
            print(f"Moved {file} to {dest_folder}")
            moved = True
            break
    if not moved:
        print(f"Could not find a destination for {file}")

# List files in both folders
print("\nFiles in Folder:")
for dirpath, dirnames, filenames in os.walk(folder):
    for filename in filenames:
        print(os.path.join(dirpath, filename))

print("\nFiles in Folder1:")
print(os.listdir(folder1))

# Delete Folder1
shutil.rmtree(folder1)
print("\nDeleted Folder1")
