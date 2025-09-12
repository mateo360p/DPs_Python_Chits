import database.BlockHelpers as BlockHelpers
import Writter
from database import Data
from database.BlockModel import BlockModel
from database.gen.Block import Block
import Globals
from typing import override

class Slab(Block):
    def __init__(self, fullBlockID : str, ingredients : list[str], modelType : BlockModel = BlockModel.CUBE, baseBlock : str = None):
        self.blockFinal = ingredients[0]
        super().__init__(fullBlockID, ingredients, modelType, baseBlock)

    @override
    def finishPrint(self, fullBlockID : str, daType : str = "Slab"):
        super().finishPrint(fullBlockID, daType)

    @override
    def genBlockState(self, fullBlockID : str):
        modID, blockID = BlockHelpers.getSplitIDs(fullBlockID)
        return {
            "variants": {
                "type=bottom": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}"
                },
                "type=double": {
                    "model": f"{BlockHelpers.getModID(self.modelBlock)}:block{Data.getAssetFolder(self.modelBlock)}{BlockHelpers.getBlockBaseID(self.modelBlock)}"
                },
                "type=top": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_top"
                }
            }
        }

    @override
    def genLootTable(self, fullBlockID : str):
        modID, blockID = BlockHelpers.getSplitIDs(fullBlockID)
        return {
            "type": "minecraft:block",
            "pools": [
                {
                    "bonus_rolls": 0.0,
                    "entries": [
                        {
                            "type": "minecraft:item",
                            "functions": [
                                {
                                    "add": False,
                                    "conditions": [
                                        {
                                            "block": fullBlockID,
                                            "condition": "minecraft:block_state_property",
                                            "properties": {
                                                "type": "double"
                                            }
                                        }
                                    ],
                                    "count": 2.0,
                                    "function": "minecraft:set_count"
                                },
                                {
                                    "function": "minecraft:explosion_decay"
                                }
                            ],
                            "name": fullBlockID
                        }
                    ],
                    "rolls": 1.0
                }
            ],
            "random_sequence": f"{modID}:blocks/{blockID}"
        }

    @override
    def genRecipe(self, fullBlockID : str, ingredient : str, count : int = 6, pattern : list[str] = ["###"]):
        return super().genRecipe(fullBlockID, ingredient, count, pattern)

    @override
    def genStonecuttingRecipe(self, product : str, ingredient : str, count : int = 2):
        return super().genStonecuttingRecipe(product, ingredient, count)

    @override
    def genCode(self, fullBlockID : str) -> str:
            return f'   public static final DeferredBlock<Block> {BlockHelpers.getBlockBaseID(fullBlockID).upper()} = registerBlockItem("{BlockHelpers.getBlockBaseID(fullBlockID)}",\n         (properties) -> new SlabBlock(properties));'

    @override
    def writeStonecuttingRecipe(self, fullBlockID : str, ingredient : str, count : int = 2, isDecoration : bool = False):
        return super().writeStonecuttingRecipe(fullBlockID, ingredient, count, isDecoration)

    @override
    def writeRecipe(self, fullBlockID : str, ingredient : str, count : int = 6, isDecoration : bool = False):
        return super().writeRecipe(fullBlockID, ingredient, count, isDecoration)

    @override
    def writeBlockModel(self, fullBlockID : str):
        modID, blockID = BlockHelpers.getSplitIDs(fullBlockID)
        Writter.writeJSON(Slab.genDummyModel(self.modelBlock, self.modelType, False), f"{BlockHelpers.getModelPath(modID)}/{blockID}", "(Block Model)")
        Writter.writeJSON(Slab.genDummyModel(self.modelBlock, self.modelType, True), f"{BlockHelpers.getModelPath(modID)}/{blockID}_top", "(Block Model)")

    @staticmethod
    def genDummyModel(fullBlockID : str, modelType : BlockModel, isTop : bool):
        modID, blockID = BlockHelpers.getSplitIDs(fullBlockID)
        
        return {
            "parent": f"minecraft:block/slab{"_top" if isTop else ""}",
            "textures": {
                "bottom": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}{"_bottom" if modelType == BlockModel.CUBE_BOTTOM_TOP else "_top" if modelType == BlockModel.CUBE_COLUMN else ""}",
                "side": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}{"_side" if modelType != BlockModel.CUBE else ""}",
                "top": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}{"_top" if modelType != BlockModel.CUBE else ""}"
            }
        }