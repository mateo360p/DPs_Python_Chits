import database.BlockHelpers as BlockHelpers
import Writter
from database import Data
from database.BlockModel import BlockModel
from database.gen.Block import Block
import Globals
from typing import override

class Stairs(Block):
    def __init__(self, fullBlockID : str, ingredients : list[str], modelType : BlockModel = BlockModel.CUBE, baseBlock : str = None):
        self.blockFinal = ingredients[0]
        super().__init__(fullBlockID, ingredients, modelType, baseBlock)

    @override
    def finishPrint(self, fullBlockID : str, daType : str = "Stairs"):
        super().finishPrint(fullBlockID, daType)

    @override
    def genBlockState(self, fullBlockID : str):
        modID, blockID = BlockHelpers.getSplitIDs(fullBlockID)
        return {
            "variants": {
                "facing=east,half=bottom,shape=inner_left": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_inner",
                    "uvlock": True,
                    "y": 270
                },
                "facing=east,half=bottom,shape=inner_right": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_inner"
                },
                "facing=east,half=bottom,shape=outer_left": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_outer",
                    "uvlock": True,
                    "y": 270
                },
                "facing=east,half=bottom,shape=outer_right": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_outer"
                },
                "facing=east,half=bottom,shape=straight": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}"
                },
                "facing=east,half=top,shape=inner_left": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_inner",
                    "uvlock": True,
                    "x": 180
                },
                "facing=east,half=top,shape=inner_right": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_inner",
                    "uvlock": True,
                    "x": 180,
                    "y": 90
                },
                "facing=east,half=top,shape=outer_left": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_outer",
                    "uvlock": True,
                    "x": 180
                },
                "facing=east,half=top,shape=outer_right": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_outer",
                    "uvlock": True,
                    "x": 180,
                    "y": 90
                },
                "facing=east,half=top,shape=straight": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}",
                    "uvlock": True,
                    "x": 180
                },
                "facing=north,half=bottom,shape=inner_left": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_inner",
                    "uvlock": True,
                    "y": 180
                },
                "facing=north,half=bottom,shape=inner_right": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_inner",
                    "uvlock": True,
                    "y": 270
                },
                "facing=north,half=bottom,shape=outer_left": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_outer",
                    "uvlock": True,
                    "y": 180
                },
                "facing=north,half=bottom,shape=outer_right": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_outer",
                    "uvlock": True,
                    "y": 270
                },
                "facing=north,half=bottom,shape=straight": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}",
                    "uvlock": True,
                    "y": 270
                },
                "facing=north,half=top,shape=inner_left": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_inner",
                    "uvlock": True,
                    "x": 180,
                    "y": 270
                },
                    "facing=north,half=top,shape=inner_right": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_inner",
                    "uvlock": True,
                    "x": 180
                },
                "facing=north,half=top,shape=outer_left": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_outer",
                    "uvlock": True,
                    "x": 180,
                    "y": 270
                },
                    "facing=north,half=top,shape=outer_right": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_outer",
                    "uvlock": True,
                    "x": 180
                },
                "facing=north,half=top,shape=straight": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}",
                    "uvlock": True,
                    "x": 180,
                    "y": 270
                },
                "facing=south,half=bottom,shape=inner_left": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_inner"
                },
                "facing=south,half=bottom,shape=inner_right": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_inner",
                    "uvlock": True,
                    "y": 90
                },
                "facing=south,half=bottom,shape=outer_left": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_outer"
                },
                    "facing=south,half=bottom,shape=outer_right": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_outer",
                    "uvlock": True,
                    "y": 90
                },
                "facing=south,half=bottom,shape=straight": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}",
                    "uvlock": True,
                    "y": 90
                },
                "facing=south,half=top,shape=inner_left": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_inner",
                    "uvlock": True,
                    "x": 180,
                    "y": 90
                },
                "facing=south,half=top,shape=inner_right": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_inner",
                    "uvlock": True,
                    "x": 180,
                    "y": 180
                },
                "facing=south,half=top,shape=outer_left": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_outer",
                    "uvlock": True,
                    "x": 180,
                    "y": 90
                },
                "facing=south,half=top,shape=outer_right": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_outer",
                    "uvlock": True,
                    "x": 180,
                    "y": 180
                },
                "facing=south,half=top,shape=straight": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}",
                    "uvlock": True,
                    "x": 180,
                    "y": 90
                },
                "facing=west,half=bottom,shape=inner_left": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_inner",
                    "uvlock": True,
                    "y": 90
                },
                "facing=west,half=bottom,shape=inner_right": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_inner",
                    "uvlock": True,
                    "y": 180
                },
                "facing=west,half=bottom,shape=outer_left": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_outer",
                    "uvlock": True,
                    "y": 90
                },
                "facing=west,half=bottom,shape=outer_right": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_outer",
                    "uvlock": True,
                    "y": 180
                },
                "facing=west,half=bottom,shape=straight": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}",
                    "uvlock": True,
                    "y": 180
                },
                "facing=west,half=top,shape=inner_left": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_inner",
                    "uvlock": True,
                    "x": 180,
                    "y": 180
                },
                "facing=west,half=top,shape=inner_right": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_inner",
                    "uvlock": True,
                    "x": 180,
                    "y": 270
                },
                "facing=west,half=top,shape=outer_left": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_outer",
                    "uvlock": True,
                    "x": 180,
                    "y": 180
                },
                "facing=west,half=top,shape=outer_right": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_outer",
                    "uvlock": True,
                    "x": 180,
                    "y": 270
                },
                "facing=west,half=top,shape=straight": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}",
                    "uvlock": True,
                    "x": 180,
                    "y": 180
                }
            }
        }

    @override
    def genCode(self, fullBlockID : str) -> str:
        isVanilla = BlockHelpers.isVanilla(self.blockFinal)
        daStr = "Blocks" if isVanilla else Data.getModBlocksJava()
        return f'   public static final DeferredBlock<Block> {BlockHelpers.getBlockBaseID(fullBlockID).upper()} = registerBlockItem("{BlockHelpers.getBlockBaseID(fullBlockID)}",\n         (properties) -> new StairBlock({daStr}.{BlockHelpers.getBlockBaseID(self.blockFinal).upper()}.defaultBlockState(),\n                    properties));'

    @override
    def genRecipe(self, fullBlockID : str, ingredient : str, count : int = 4, pattern : list[str] = ["#  ","## ","###"]):
        return super().genRecipe(fullBlockID, ingredient, count, pattern)

    @override
    def writeRecipe(self, fullBlockID : str, ingredient : str, count : int = 4, isDecoration : bool = False):
        return super().writeRecipe(fullBlockID, ingredient, count, isDecoration)

    @override
    def writeBlockModel(self, fullBlockID : str):
        modID, blockID = BlockHelpers.getSplitIDs(fullBlockID)
        Writter.writeJSON(Stairs.genDummyModel(self.modelBlock, self.modelType), f"{BlockHelpers.getModelPath(modID)}/{blockID}", "(Block Model)")
        Writter.writeJSON(Stairs.genDummyModel(self.modelBlock, self.modelType, "inner_stairs"), f"{BlockHelpers.getModelPath(modID)}/{blockID}_inner", "(Block Model)")
        Writter.writeJSON(Stairs.genDummyModel(self.modelBlock, self.modelType, "outer_stairs"), f"{BlockHelpers.getModelPath(modID)}/{blockID}_outer", "(Block Model)")

    @staticmethod
    def genDummyModel(fullBlockID : str, modelType : BlockModel, parent : str = "stairs"):
        modID, blockID = BlockHelpers.getSplitIDs(fullBlockID)
        return {
            "parent": f"minecraft:block/{parent}",
            "textures": {
                "bottom": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}{"_bottom" if modelType == BlockModel.CUBE_BOTTOM_TOP else "_top" if modelType == BlockModel.CUBE_COLUMN else ""}",
                "side": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}{"_side" if modelType != BlockModel.CUBE else ""}",
                "top": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}{"_top" if modelType != BlockModel.CUBE else ""}"
            }
        }
