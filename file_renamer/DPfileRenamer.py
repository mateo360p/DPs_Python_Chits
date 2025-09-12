import os
import tkinter as tk
from tkinter import filedialog, messagebox

def rename():
    folder = daFolderPath.get()

    if not os.path.isdir(folder):
        messagebox.showerror("Error!", "Invalid folder")
        return

    oldSuff = oldEntry.get()
    newSuff = newEntry.get()

    if not oldSuff or not newSuff:
        messagebox.showerror("Error!", "You must write both suffixes!")
        return

    renamedCount = 0

    for file in os.listdir(folder):
        if not file.endswith(oldSuff): continue

        oldFile = os.path.join(folder, file)
        newFile = os.path.join(folder, file[:-len(oldSuff)] + newSuff)

        os.rename(oldFile, newFile)
        renamedCount += 1

    messagebox.showinfo("All Done!", f"Renamed {renamedCount} file(s)")

def selectFolder():
    folder = filedialog.askdirectory()
    if folder: daFolderPath.set(folder)

# -------------- GUI stuff
root = tk.Tk()
root.title("File Renamer")

daFolderPath = tk.StringVar()

tk.Label(root, text="Folder:").grid(row=0, column=0, sticky="w")
tk.Entry(root, textvariable=daFolderPath, width=50).grid(row=0, column=1)
tk.Button(root, text="Select Folder", command=selectFolder).grid(row=0, column=2)

tk.Label(root, text="Old suffix (including file extension):").grid(row=1, column=0, columnspan=2, sticky="w")
oldEntry = tk.Entry(root, width=60)
oldEntry.grid(row=2, column=0, columnspan=2)

tk.Label(root, text="New suffix (including file extension):").grid(row=3, column=0, columnspan=2, sticky="w")
newEntry = tk.Entry(root, width=60)
newEntry.grid(row=4, column=0, columnspan=2)

tk.Button(root, text="Rename files", command=rename).grid(row=5, column=0, columnspan=3, pady=10)

root.mainloop()