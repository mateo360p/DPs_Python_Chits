import database.BlockHelpers as BlockHelpers
import Writter
import Globals
from database.BlockType import BlockType
from database.gen.Block import Block
from database.gen.Smooth import Smooth
from database.gen.Wall import Wall
from database.gen.Stairs import Stairs
from database.gen.Slab import Slab
import database.Data as Data
from database.BlockModel import BlockModel

def validateSubBlock(fullBlockID : str) -> str: # removes "s" from tiles and bricks
    if fullBlockID.endswith("s"): return fullBlockID[:-1]
    return fullBlockID

def setModdedID(fullBlockID) -> str:
    return Data.getModdedID() + ":" + BlockHelpers.getBlockBaseID(fullBlockID)


def ExtraSet(baseID : str, ingredients : list[str], modelType : BlockModel = BlockModel.CUBE):
    Stairs(setModdedID(validateSubBlock(baseID) + "_stairs"), [baseID] + ingredients, modelType, baseID)
    Slab(setModdedID(validateSubBlock(baseID) + "_slab"), [baseID] + ingredients, modelType, baseID)
    Wall(setModdedID(validateSubBlock(baseID)) + "_wall", [baseID] + ingredients, modelType, baseID)

def BlockSet(baseID : str, ingredients : list[str], modelType : BlockModel = BlockModel.CUBE):
    Block(setModdedID(baseID), ingredients, modelType)
    ExtraSet(baseID, ingredients, modelType)

def SmoothSet(baseID : str, ingredients : list[str]):
    Smooth(setModdedID(baseID), ingredients, BlockModel.CUBE)
    ExtraSet(baseID, ingredients, BlockModel.CUBE)
