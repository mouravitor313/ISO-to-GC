# built-in libs to read files and folders
import os
import shutil

FILES_PATH = './files/'

def read_files_and_create_folders(files_path: str) -> str:
    for file in os.listdir(files_path):
        
        if file.lower().endswith(".iso"):
            
            file_path = os.path.join(files_path, file)
            file_name_without_extension = os.path.splitext(file)[0]
            
            destination_folder = os.path.join(files_path, file_name_without_extension)
            os.makedirs(destination_folder, exist_ok=True)

            new_file_path = os.path.join(destination_folder, file)
            shutil.move(file_path, new_file_path)

            new_file_name = "game.iso" # used by gamecube loaders

            path_iso = os.path.join(destination_folder, new_file_name)
            os.rename(new_file_path, path_iso)
        
            print(f"File {file} already.\n\n")

    return "Finish!"

read_files_and_create_folders(FILES_PATH)
