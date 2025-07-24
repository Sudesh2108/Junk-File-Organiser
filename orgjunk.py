import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

# File types and categories
DIRECTORIES = {
    "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg", ".heif", ".psd"],
    "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
    "Documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn",
                  ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Archives": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip"],
    "Audio": [".aac", ".aa", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
    "Plain Text": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "PYTHON": [".py","ipynb"],
    "Java" : [".java"],
    "C" : ['.c'],
    "Javascript" : [".js"],
    "HTML" : [".html"],
    "CSS" : [".css"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"]
}

FILE_FORMATS = {
    ext: folder
    for folder, extensions in DIRECTORIES.items()
    for ext in extensions
}


def organize_directory(path: Path):
    count = 0
    for entry in os.scandir(path):
        if entry.is_dir():
            continue
        file_path = Path(entry)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            dest_folder = path / FILE_FORMATS[file_format]
            dest_folder.mkdir(exist_ok=True)
            file_path.rename(dest_folder / file_path.name)
            count += 1
    return count


def select_and_organize():
    folder = filedialog.askdirectory(title="Select Folder to Organize")
    if folder:
        moved = organize_directory(Path(folder))
        messagebox.showinfo("Done", f"Organized {moved} files in:\n{folder}")
    else:
        messagebox.showwarning("Cancelled", "No folder selected!")



app = tk.Tk()
app.title("File Organizer App")
app.geometry("400x200")
app.resizable(True, True)

title = tk.Label(app, text="File Organizer", font=("Helvetica", 16, "bold"))
title.pack(pady=20)

organize_btn = tk.Button(app, text="Select Folder & Organize", command=select_and_organize, font=("Arial", 12), width=25, height=2, bg="#4CAF50", fg="white")
organize_btn.pack(pady=10)

footer = tk.Label(app, text="Made with Python ❤️", font=("Arial", 10), fg="gray")
footer.pack(side="bottom", pady=10)

app.mainloop()
