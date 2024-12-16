import os
import shutil
from filecmp import cmp

def backup_folder(src, dest):
    """
    Back up all contents (including subfolders) from the 'src' folder to the 'dest' path.
    If the file already exists in the target path and the content is the same, skip the backup.
    """
    for root, dirs, files in os.walk(src):
        # Calculate the target directory corresponding to the current directory
        relative_path = os.path.relpath(root, src)
        dest_path = os.path.join(dest, relative_path)
        
        # Create the target directory (if it does not exist)
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
        
        # Traverse files and create backups
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_path, file)
            
            # If the target file does not exist or the content is different, copy it.
            if not os.path.exists(dest_file) or not cmp(src_file, dest_file, shallow=False):
                shutil.copy2(src_file, dest_file)  # Preserve file metadata (such as modification time, etc.)

if __name__ == "__main__":
    # Source folder path
    source_folder = "G:/photo/Pictures"
    # Target file path
    destination_folder = "G:/photo/GTneo5/Pictures"
    
    backup_folder(source_folder, destination_folder)
    print("Backup successful！")
