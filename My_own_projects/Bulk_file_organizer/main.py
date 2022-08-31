import os
import glob
import shutil
import datetime

extensions = {
    "jpg": "Images",
    "jpeg": "Images",
    "png": "Images",
    "ico": "Images",
    "gif": "Images",
    "svg": "Images",
    "sql": "SQL",
    "exe": "Programs",
    "msi": "Programs",
    "pdf": "PDF",
    "xlsx": "Excel",
    "csv": "Excel",
    "rar": "Compressed",
    "zip": "Compressed",
    "gz": "Compressed",
    "tar": "Compressed",
    "docx": "Word Documents",
    "torrent": "Torrents",
    "txt": "Text",
    "ipynb": "Python",
    "py": "Python",
    "pptx": "powerpoint",
    "ppt": "powerpoint",
    "mp3": "Audio",
    "wav": "Audio",
    "mp4": "Video",
    "m3u8": "Video",
    "webm": "Video",
    "mkv": "Video",
    "ts": "Video",
    "json": "json",
    "css": "web",
    "js": "web",
    "html": "web",
    "apk": "apk",
    "sqlite3": "sqlite3",
}

usr = os.path.expanduser("~")
path = rf"{usr}/Descargas"
# setting verbose to 1 (or True) will show all file moves
# setting verbose to 0 (or False) will show basic necessary info
verbose = 0
for extension, folder_name in extensions.items():
    # get all the files matching the extension
    files = glob.glob(os.path.join(path, f"*.{extension}"))
    if len(files) > 0:
        print(f"[*] Found {len(files)} files with {extension} extension")
    if not os.path.isdir(os.path.join(path, folder_name)) and files:
        # create the folder if it does not exist before
        print(f"[+] Making {folder_name} folder")
        os.mkdir(os.path.join(path, folder_name))
    for file in files:
        # for each file in that extension, move it to the corresponding folder
        basename = os.path.basename(file)
        dst = os.path.join(path, folder_name, basename)
        if verbose:
            print(f"[*] Moving {file} to {dst}")
        shutil.move(file, dst)
