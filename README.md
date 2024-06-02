# FolderOptimize
Python script - By default it searches through the downloads folder for a set dictionary of file types. It then moves those found items to set locations within the system. Any file not defined within FILE_TYPES is moved to a Misc folder.

This script does not touch folders within the downloads folder.

You could add your own file type and location pretty easy.

Current File types:
```
    'photos': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'documents_compressed': ['.zip', '.rar', '.gz', '.tar', '.7z'],
    'documents_text': ['.txt', '.pdf', '.doc', '.docx', '.xls', '.xlsx'],
    'music': ['.mp3', '.wav', '.aac', '.flac', '.ogg']
```

Current Locations:
```
    'photos': '~/Pictures',
    'documents_compressed': '~/Documents/Compressed',
    'documents_text': '~/Documents/Text',
    'music': '~/Music'
```
