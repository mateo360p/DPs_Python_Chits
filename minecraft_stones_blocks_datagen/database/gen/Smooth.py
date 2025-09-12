import database.BlockHelpers as BlockHelpers
import Writter
from database import Data
from database.BlockModel import BlockModel
from database.gen.Block import Block
import Globals
from typing import override

class Smooth(Block):
    def __init__(self, fullBlockID : str, ingredients : list[str], modelType : BlockModel = BlockModel.CUBE, baseBlock : str = None):
        super().__init__(fullBlockID, ingredients, modelType, baseBlock)

    @override
    def finishPrint(self, fullBlockID : str, daType : str = "Smooth Block"):
        super().finishPrint(fullBlockID, daType)

    @override
    def genRecipe(self, fullBlockID : str, ingredient : str, count : int = 1, pattern : list[str] = ["###", "###"]):
        return {
            "type": "minecraft:smelting",
            "category": "blocks",
            "cookingtime": 200,
            "experience": 0.1,
            "ingredient": ingredient,
            "result": {
                "id": fullBlockID
            }
        }

    @override
    def genCode(self, fullBlockID : str) -> str:
        return f'   public static final DeferredBlock<Block> {BlockHelpers.getBlockBaseID(fullBlockID).upper()} = registerBlockItem("{BlockHelpers.getBlockBaseID(fullBlockID)}",\n         (properties) -> new Block(properties));'

    @override
    def writeStonecuttingRecipe(self, fullBlockID : str, ingredient : str, count : int = 1, isDecoration : bool = False):
        pass