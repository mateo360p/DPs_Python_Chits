import database.Data as Data

def isVanilla(fullBlockID : str) -> bool:
    return fullBlockID.startswith("minecraft")

def getModID(fullBlockID : str) -> str:
    dummy = fullBlockID.split(sep=":", maxsplit=1)[0]
    
    if dummy == fullBlockID: dummy = Data.getModdedID() # Assumes is a modded block
    return dummy

def getBlockBaseID(fullBlockID : str) -> str:
    if fullBlockID.__contains__(":"):
        return fullBlockID.split(sep=":", maxsplit=1)[1]
    else:
        return fullBlockID

# Pretty unnecesary, but idc
def getSplitIDs(fullBlockID : str) -> tuple[str, str]:
    return getModID(fullBlockID), getBlockBaseID(fullBlockID)

def getBlockStatePath(modid : str) -> str:
    return f"assets/{modid}/blockstates"

def getModelPath(modid : str) -> str:
    return f"assets/{modid}/models/block/{Data.getBlockAssetFolder()}"

def getItemPath(modid : str) -> str:
    return f"assets/{modid}/items"

def getRecipePath(modid : str) -> str:
    return f"data/{modid}/recipe"

def getLootTablePath(modid : str) -> str:
    return f"data/{modid}/loot_table/blocks"

def getRecipeAdvPath(modid : str, isDecoration : bool = False) -> str:
    return f"data/{modid}/advancement/recipes/{"decorations" if isDecoration else "building_blocks"}"