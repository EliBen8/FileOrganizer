from pathlib import Path
import shutil

from categories import CATEGORIES

def organize_folders(folder_path):
    """ 
    Organizes files in the given folder by file extension. 
    Returns: 
        list[str]: Log messages describing moved files. 
    """
    dir_path = Path(folder_path)

    if not dir_path.is_dir():
        raise ValueError(f"{folder_path} is not a valid directory.")
    
    results = []

    for file in dir_path.iterdir():
        if file.is_file():
            for dir_name, extensions in CATEGORIES.items():
                if file.suffix.lower() in extensions:
                    destination_dir = dir_path / dir_name
                    destination_dir.mkdir(exist_ok=True)
                    destination_path = destination_dir / file.name
                    shutil.move(str(file), str(destination_path))
                    results.append(f"Moved {file.name} → {dir_name}/")
                    break
                else:
                    results.append(f"Skipped {file.name} — no matching category")
    return results

def undo_organize(last_organized_path):
    """
    Reverses the organization of files in the given folder.
    Moves files from category subdirectories back to the root folder
    and removes the empty subdirectories.
    Returns:
        list[str]: Log messages describing moved files and removed directories.
    """
    dir_path = Path(last_organized_path)
    if not dir_path.is_dir():
        raise ValueError(f"{last_organized_path} is not a valid directory.")
    
    results = []

    for dir_name in CATEGORIES.keys():
        destination_dir = dir_path / dir_name
        if destination_dir.is_dir():
            for file in destination_dir.iterdir():
                shutil.move(str(file), str(dir_path))
                results.append(f"Moved {file.name} → {dir_path}")
            destination_dir.rmdir() # delete the directory once files are moved out
            results.append(f"Removed directory: {dir_name}")

    return results





# Old Command Line Version
# import sys
# from pathlib import Path
# # to move files to directories
# import shutil
# import tkinter as tk

# # create a dictionary of directories and their respective paths
# list_of_directories = {
#     "Media" : [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff"],
#     "Videos" : [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv"],
#     "Audio" : [".mp3", ".wav", ".flac", ".acc", ".ogg", ".m4a"],
#     "Documents" : [".pdf", ".docx", ".doc", ".txt", ".rtf", ".odt", ".pages"],
#     "Spreadsheets" : [".xlsx", ".xls", ".csv", ".ods"],
#     "Presentations" : [".pptx", ".ppt", ".key"],
#     "Code" : [".py", ".js", ".ts", ".html", ".css", ".java", ".cpp", ".c", ".go", ".rs", ".sh"],
#     "Compressed" : [".zip", ".tar", ".gz", ".rar", ".7z"],
#     "Executables" : [".exe", ".msi", ".dmg", ".pkg", ".deb", ".appimage"],
# }

# # command line validation
# if len(sys.argv) < 2:
#     print("Usage: python3 app.py <target_folder>")
#     sys.exit(1)

# # python3 app.py target_folder
# target_folder = sys.argv[1]

# # directory path for selected folder
# dir_path = Path(target_folder)

# for file in dir_path.iterdir():
#     if file.is_file():
#         for dir_name, extensions in list_of_directories.items():
#             if file.suffix.lower() in extensions:
#                 destination_dir = dir_path / dir_name
#                 destination_dir.mkdir(exist_ok=True)

#                 destination_path = destination_dir / file.name
#                 shutil.move(file, destination_path)
#                 break