
def getBlockAssetFolder() -> str:
    return "vanilla_extras"

def getAssetFolder(daID : str) -> str:
    if daID.startswith("minecraft"): return "/"
    return f"/{getBlockAssetFolder()}/"

def getModdedID() -> str:
    return "dpsvarmod"

def getExportFolder() -> str:
    return "_export"

def getModBlocksJava() -> str:
    return "DPsBlocks"

def JSONexportPath(middlePath : str) -> str:
    return f"{getExportFolder()}/{middlePath}.json"

def typedExportPath(middlePath : str, daType : str) -> str:
    return f"{getExportFolder()}/{middlePath}.{daType}"