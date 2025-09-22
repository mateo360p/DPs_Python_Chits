import json
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, simpledialog
import re
from typing import Any

version = "2.4.1"

# xd
def doSet(d: dict[str, Any], field: str, value: Any):
    if value is not None: d[field] = value

class CharacterConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("DP's Character converter v" + version)

        self.exportFolder = tk.StringVar()
        self.daFiles = []
        self.conversionType = tk.StringVar(value="psych_to_vslice")

        self.createStuff()

    def createStuff(self):
        daMain = ttk.Frame(self.root, padding="10")
        daMain.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        daMain.columnconfigure(1, weight=1)

        ttk.Label(daMain, text="JSON file(s):").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.filesEntry = ttk.Entry(daMain, width=50)
        self.filesEntry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        ttk.Button(daMain, text="Browse...", command=self.browseFiles).grid(row=0, column=2, pady=5)

        ttk.Label(daMain, text="Export folder:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.exportEntry = ttk.Entry(daMain, textvariable=self.exportFolder, width=50)
        self.exportEntry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        ttk.Button(daMain, text="Browse...", command=self.browseExportFolder).grid(row=1, column=2, pady=5)

        ttk.Label(daMain, text="Convert:").grid(row=2, column=0, sticky=tk.W, pady=5)
        selectors = ttk.Frame(daMain)
        selectors.grid(row=2, column=1, columnspan=2, sticky=tk.W, pady=5)
        
        ttk.Radiobutton(selectors, text="Psych to V-Slice", variable=self.conversionType, value="psych_to_vslice").pack(side=tk.LEFT)
        ttk.Radiobutton(selectors, text="V-Slice to Psych", variable=self.conversionType, value="vslice_to_psych").pack(side=tk.LEFT)

        ttk.Button(daMain, text="Convert", command=self.doConvert).grid(row=3, column=1, pady=20)
        
        ttk.Label(daMain, text="Log:").grid(row=4, column=0, sticky=tk.W, pady=5)

        logFrame = ttk.Frame(daMain)
        logFrame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        logFrame.columnconfigure(0, weight=1)
        logFrame.rowconfigure(0, weight=1)

        scrollbar = ttk.Scrollbar(logFrame)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

        self.daLog = tk.Listbox(logFrame, height=10, width=70, yscrollcommand=scrollbar.set, selectmode=tk.SINGLE, state='disabled')
        self.daLog.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        scrollbar.config(command=self.daLog.yview)

        daMain.rowconfigure(6, weight=1)

# --------------------------- Getting paths -------------------------------
    def browseFiles(self):
        files = filedialog.askopenfilenames(
            title="Select JSON file(s)",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )

        if not files: return

        self.daFiles = files
        self.filesEntry.delete(0, tk.END)
        self.filesEntry.insert(0, ", ".join(files))

    def browseExportFolder(self):
        folder = filedialog.askdirectory(title="Select Export Folder")
        if folder: self.exportFolder.set(folder)

# --------------------------- Processing stuff -------------------------------
    def doConvert(self):
        if not self.daFiles:
            messagebox.showerror("Dumbass", "Select at least one JSON file")
            return
            
        if not self.exportFolder.get():
            messagebox.showerror("Dumbass", "Select an export folder")
            return

        self.daLog.config(state='normal')
        self.daLog.delete(0, tk.END)
        self.daLog.config(state='disabled')
        
        self.logMSG("Starting, please wait...")

        try:
            for file_path in self.daFiles: 
                self.processFile(file_path)

            messagebox.showinfo("Done!", f"The files were succesfully converted.\nExport Folder: {self.exportFolder.get()}")
            self.logMSG("All Done!")

        except Exception as e:
            messagebox.showerror("Error", f"Error while converting: {str(e)}")
            self.logMSG(f"Error: {str(e)}")

    def processFile(self, filePath):
        fileName = os.path.basename(filePath)
        try:
            with open(filePath, 'r', encoding='utf-8') as f:
                data = json.load(f)

            ogName = os.path.splitext(fileName)[0]
            exportName = self.cleanName(ogName) + "_converted.json"
            exportPath = os.path.join(self.exportFolder.get(), exportName)

            self.logMSG(f"Processing: {ogName} -> {exportName}")

            if self.conversionType.get() == "psych_to_vslice":
                data["charName"] = simpledialog.askstring(
                    "Character Naming", 
                    f"Enter a caracter name for the file:\n{fileName}",
                    parent=self.root
                )
                data["renderType"] = messagebox.askyesno(
                    "Character Render", 
                    f"Is the following character an animate atlas?:\n{fileName}",
                    parent=self.root
                )
                converted = self.psychToVslice(data)
            else:
                converted = self.vsliceToPsych(data)

            with open(exportPath, 'w', encoding='utf-8') as f:
                json.dump(converted, f, indent=2, ensure_ascii=False)

            self.logMSG(f"Saved: {exportName}")

        except Exception as e:
            self.logMSG(f"Error while processing {fileName}: {str(e)}")
            raise

    def cleanName(self, name):
        name = name.lower()
        name = re.sub(r'\s+', '_', name)
        name = re.sub(r'[^\w._-]', '', name)
        return name

    def logMSG(self, message):
        self.daLog.config(state='normal')
        self.daLog.insert(tk.END, message)
        self.daLog.see(tk.END)

        self.daLog.config(state='disabled')

# --------------------------- JSON writting -------------------------------
    def psychToVslice(self, data:dict[str, Any]):
        vsliceDefs = {
            "version": "1.0.0",
            "danceEvery": 1,
            "startingAnimation": "idle",
            "name": "Converted Dummy",
            "renderType": "multisparrow",
            "assetPath": "characters/BOYFRIEND",
            "offsets": [
                0,
                0
            ],
            "cameraOffsets": [
                0,
                0
            ],
            "scale": 1,
            "singTime": 8,
            "isPixel": False,
            "flipX": True,
            "healthIcon": {
                "id": "bf",
                "isPixel": False,
                "flipX": False,
                "scale": 1,
                "offsets": [
                    0,
                    0
                ]
            },
            "animations": []
        }

        result = vsliceDefs.copy()
        
        doSet(result, "name", data.get("charName")) ###
        doSet(result, "renderType", "animateatlas" if data.get("renderType") else None) ###
        doSet(result, "assetPath", data.get("image"))
        doSet(result, "offsets", data.get("position"))
        doSet(result, "cameraOffsets", data.get("camera_position"))
        doSet(result, "scale", data.get("scale"))
        doSet(result, "singTime", data.get("sing_duration"))
        doSet(result, "isPixel", data.get("no_antialiasing"))
        doSet(result, "flipX", data.get("flip_x"))
        doSet(result, "healthIcon", 
            {
                "id": data.get("healthicon"),
                "isPixel": ("" if not str(data.get("healthicon")) else str(data.get("healthicon"))).endswith("-pixel"),
                "flipX": False,
                "scale": 1,
                "offsets": [
                    0,
                    0
                ]
            })

        anims = []
        if data.get("animations"):
            for i in data.get("animations"):
                dummy : dict[str, Any] = {}
                doSet(dummy, "name", i.get("anim"))
                doSet(dummy, "prefix", i.get("name"))
                doSet(dummy, "offsets", i.get("offsets"))
                doSet(dummy, "frameRate", i.get("fps"))
                doSet(dummy, "looped", i.get("loop"))
                dummy["flipX"] = False
                dummy["flipY"] = False
                anims.append(dummy)
            doSet(result, "animations", anims)

        return result

    def vsliceToPsych(self, data):
        psychDefs = {
            "vocals_file": "",
            "healthbar_colors": [161, 161, 161],
            "image": "characters/BOYFRIEND",
            "position": [
                0,
                0
            ],
            "camera_position": [
                0,
                0
            ],
            "scale": 1,
            "sing_duration": 8,
            "no_antialiasing": False,
            "flip_x": False,
            "healthicon": "face",
            "animations": []
        }

        result = psychDefs.copy()
        doSet(result, "image", data.get("assetPath"))
        doSet(result, "position", data.get("offsets"))
        doSet(result, "camera_position", data.get("cameraOffsets"))
        doSet(result, "scale", data.get("scale"))
        doSet(result, "sing_duration", data.get("singTime"))
        doSet(result, "no_antialiasing", data.get("isPixel"))
        doSet(result, "flip_x", data.get("flipX"))
        doSet(result, "healthicon", data.get("healthIcon").get("id"))

        anims = []
        if data.get("animations"):
            for i in data.get("animations"):
                dummy : dict[str, Any] = {}
                doSet(dummy, "anim", i.get("name"))
                doSet(dummy, "name", i.get("prefix"))
                doSet(dummy, "offsets", i.get("offsets"))
                doSet(dummy, "fps", i.get("frameRate"))
                doSet(dummy, "loop", i.get("looped"))
                anims.append(dummy)
            doSet(result, "animations", anims)

        return result

if __name__ == "__main__":
    root = tk.Tk()
    app = CharacterConverter(root)
    root.mainloop()

# Okay, this works!, credits to me, Dipazio347, i guess-?