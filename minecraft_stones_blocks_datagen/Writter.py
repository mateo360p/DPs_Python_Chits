import os
import json
import database.Data as Data

def writeJSON(content, toFile : str, typeInfo : str = ""):
    folder = os.path.dirname(os.path.join(Data.getExportFolder(), f"{toFile}.json"))
    os.makedirs(folder, exist_ok=True) # Makes sure the path exists

    with open(Data.JSONexportPath(toFile), "w", encoding="utf-8") as export:
        json.dump(content, export, indent=4)

    print(f"Written {typeInfo}: {Data.JSONexportPath(toFile)}")

def writeTXT(content : str, toFile : str, typeInfo : str = "", daType : str = "txt"):
    folder = os.path.dirname(os.path.join(Data.getExportFolder(), f"{toFile}.{daType}"))
    os.makedirs(folder, exist_ok=True) # Makes sure the path exists

    with open(Data.typedExportPath(toFile, daType), "w", encoding="utf-8") as export:
        export.write(content)

    print(f"Written {typeInfo}: {Data.typedExportPath(toFile, daType)}")
