# BPopeMI @ Github
# Downloads Folder Optimization
import os
import shutil
from pathlib import Path

class FolderOrganizer:
    def __init__(self, src_folder, dest_folders):
        self.src_folder = Path(os.path.expanduser(src_folder))
        self.dest_folders = {category: Path(os.path.expanduser(folder)) for category, folder in dest_folders.items()}

    def move_files(self):
        for file in self.src_folder.iterdir():
            if file.is_file():
                moved = False
                for category, extensions in FILE_TYPES.items():
                    if any(file.name.lower().endswith(ext) for ext in extensions):
                        self._move_file(file, self.dest_folders[category])
                        moved = True
                        break
                if not moved:
                    self._move_file(file, self.dest_folders['misc'])
                    print(f"Moved to Misc: {file.name}")

    def _move_file(self, file_path, dest_folder):
        dest_folder.mkdir(parents=True, exist_ok=True)
        shutil.move(str(file_path), str(dest_folder / file_path.name))
        print(f'Moved: {file_path.name} to {dest_folder}')
                
# File type categories and their destination folders
FILE_TYPES = {
    'photos': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'documents_compressed': ['.zip', '.rar', '.gz', '.tar', '.7z'],
    'documents_text': ['.txt', '.pdf', '.doc', '.docx', '.xls', '.xlsx'],
    'music': ['.mp3', '.wav', '.aac', '.flac', '.ogg']
}
# Paths
paths = {
    'photos': '~/Pictures',
    'documents_compressed': '~/Documents/Compressed',
    'documents_text': '~/Documents/Text',
    'music': '~/Music',
    'misc': '~/Documents/Misc'
}
# Downloads folder - Clean up starting destination
downloads_folder = '~/Downloads'

organizer = FolderOrganizer(downloads_folder, paths)
organizer.move_files()
print('Download folder cleanup complete!')