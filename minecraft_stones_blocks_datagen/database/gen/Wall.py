import database.BlockHelpers as BlockHelpers
import Writter
from database import Data
from database.BlockModel import BlockModel
from database.gen.Block import Block
import Globals
from typing import override

class Wall(Block):
    def __init__(self, fullBlockID : str, ingredients : list[str], modelType : BlockModel = BlockModel.CUBE, baseBlock : str = None):
        super().__init__(fullBlockID, ingredients, modelType, baseBlock)
        Globals.addWall(fullBlockID)

    @override
    def finishPrint(self, fullBlockID : str, daType : str = "Wall"):
        super().finishPrint(fullBlockID, daType)

    @override
    def genBlockState(self, fullBlockID : str):
        modID, blockID = BlockHelpers.getSplitIDs(fullBlockID)
        return {
            "multipart": [
                {
                    "apply": {
                        "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_post"
                    },
                    "when": {
                        "up": "true"
                    }
                },
                {
                    "apply": {
                        "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_side",
                        "uvlock": True
                    },
                    "when": {
                        "north": "low"
                    }
                },
                {
                    "apply": {
                        "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_side",
                        "uvlock": True,
                        "y": 90
                    },
                    "when": {
                        "east": "low"
                    }
                },
                {
                    "apply": {
                        "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_side",
                        "uvlock": True,
                        "y": 180
                    },
                    "when": {
                        "south": "low"
                    }
                },
                {
                    "apply": {
                        "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_side",
                        "uvlock": True,
                        "y": 270
                    },
                    "when": {
                        "west": "low"
                    }
                },
                {
                    "apply": {
                        "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_side_tall",
                        "uvlock": True
                    },
                    "when": {
                        "north": "tall"
                    }
                },
                {
                    "apply": {
                        "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_side_tall",
                        "uvlock": True,
                        "y": 90
                    },
                    "when": {
                        "east": "tall"
                    }
                },
                {
                    "apply": {
                        "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_side_tall",
                        "uvlock": True,
                        "y": 180
                    },
                    "when": {
                        "south": "tall"
                    }
                },
                {
                    "apply": {
                        "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_side_tall",
                        "uvlock": True,
                        "y": 270
                    },
                    "when": {
                        "west": "tall"
                    }
                }
            ]
        }

    @override
    def genItemModel(self, modID : str, blockModel : str):
        return super().genItemModel(modID, blockModel + "_inventory")

    @override
    def genRecipe(self, fullBlockID : str, ingredient : str, count : int = 6, pattern : list[str] = ["###", "###"]):
        return super().genRecipe(fullBlockID, ingredient, count, pattern)

    @override
    def genCode(self, fullBlockID : str) -> str:
            return f'   public static final DeferredBlock<Block> {BlockHelpers.getBlockBaseID(fullBlockID).upper()} = registerBlockItem("{BlockHelpers.getBlockBaseID(fullBlockID)}",\n         (properties) -> new WallBlock(properties));'

    @override
    def writeStonecuttingRecipe(self, fullBlockID : str, ingredient : str, count : int = 1, isDecoration : bool = True):
        return super().writeStonecuttingRecipe(fullBlockID, ingredient, count, isDecoration)

    @override
    def writeRecipe(self, fullBlockID : str, ingredient : str, count : int = 6, isDecoration : bool = True):
        return super().writeRecipe(fullBlockID, ingredient, count, isDecoration)

    @override
    def writeBlockModel(self, fullBlockID : str):
        modID, blockID = BlockHelpers.getSplitIDs(fullBlockID)
        isSide = (self.modelType != BlockModel.CUBE)
        Writter.writeJSON(Wall.genDummyModel(self.modelBlock, isSide), f"{BlockHelpers.getModelPath(modID)}/{blockID}_post", "(Block Model)")
        Writter.writeJSON(Wall.genDummyModel(self.modelBlock, isSide, "template_wall_side"), f"{BlockHelpers.getModelPath(modID)}/{blockID}_side", "(Block Model)")
        Writter.writeJSON(Wall.genDummyModel(self.modelBlock, isSide, "template_wall_side_tall"), f"{BlockHelpers.getModelPath(modID)}/{blockID}_side_tall", "(Block Model)")
        Writter.writeJSON(Wall.genDummyModel(self.modelBlock, isSide, "wall_inventory"), f"{BlockHelpers.getModelPath(modID)}/{blockID}_inventory", "(Block Model)")

    @staticmethod
    def genDummyModel(fullBlockID : str, isSide : bool, parent : str = "template_wall_post"):
        modID, blockID = BlockHelpers.getSplitIDs(fullBlockID)
        return {
            "parent": f"minecraft:block/{parent}",
            "textures": {
                "wall": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}{"_side" if isSide else ""}"
            }
        }