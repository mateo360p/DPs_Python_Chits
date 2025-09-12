import Writter
import database.BlockHelpers as BlockHelpers
import database.Data as Data

walls = []
miningBlocks = []
code = ""
creativeCode = ""

def addWall(fullBlockID : str):
    walls.append(fullBlockID)

def addBlock(fullBlockID : str):
    miningBlocks.append(fullBlockID)

def addCode(daCode : str):
    global code
    code += daCode + "\n"

def addCreativeCode(daCode : str):
    global creativeCode
    creativeCode += daCode + "\n"

def prepareForLang(fullBlockID : str) -> str:
    dummy : list[str] = BlockHelpers.getBlockBaseID(fullBlockID).split("_")

    for i in range(len(dummy)):
        dummy[i] = dummy[i].capitalize()

    return " ".join(dummy)

# IMMMMMMMMMMMMM HALFFFFFFFFFFFFFFFFF CRAAAAAAAAAAZYYYYYYYYYYY
# ALLL FOR THE LOOOOVVEEEEEE OFFF UUUUUU <3 (kill me please)
def writeLang():
    Writter.writeJSON({f"block.{Data.getModdedID()}.{BlockHelpers.getBlockBaseID(variable)}": prepareForLang(variable) for variable in miningBlocks}, "en-us", "(Lang)")

def writeWallsTag():
    Writter.writeJSON({"values": [variable for variable in walls]}, "wallsTag", "(Tag)")

def writePickaxeTag():
    Writter.writeJSON({"values": [variable for variable in miningBlocks]}, "pickTag", "(Tag)")

def writeCodeLike():
    Writter.writeTXT(code, "code", "(Code-like)")

def writeCreativeCodeLike():
    Writter.writeTXT(creativeCode, "creativeCode", "(Code-like)")
