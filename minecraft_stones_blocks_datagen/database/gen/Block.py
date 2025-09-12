import database.BlockHelpers as BlockHelpers
import Globals
from database.BlockModel import BlockModel
import database.Data as Data
import Writter

from typing import override

class Block:
    def genBlockState(self, fullBlockID : str):
        modID, blockID = BlockHelpers.getSplitIDs(fullBlockID)
        return {
            "variants": {
                "": {
                    "model": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}"
                }
            }
        }

    def genBlockModel(self, fullBlockID : str):
        modID, blockID = BlockHelpers.getSplitIDs(self.modelBlock)

        match self.modelType:
            case BlockModel.CUBE_COLUMN:
                return {
                    "parent": "minecraft:block/cube_column",
                    "textures": {
                        "end": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_top",
                        "side": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_side"
                    }
                }
            case BlockModel.CUBE_BOTTOM_TOP:
                return {
                    "parent": "minecraft:block/cube_bottom_top",
                    "textures": {
                        "bottom": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_bottom",
                        "side": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_side",
                        "top": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}_top"
                    }
                }
            case _:
                return {
                    "parent": "minecraft:block/cube_all",
                    "textures": {
                        "all": f"{modID}:block{Data.getAssetFolder(fullBlockID)}{blockID}"
                    }
                }

    def genItemModel(self, modID : str, blockModel : str):
        return {
            "model": {
                "type": "minecraft:model",
                "model": f"{modID}:block{Data.getAssetFolder(modID)}{blockModel}"
            }
        }

    def genLootTable(self, fullBlockID : str):
        modID, blockID = BlockHelpers.getSplitIDs(fullBlockID)
        return {
            "type": "minecraft:block",
            "pools": [
                {
                    "bonus_rolls": 0.0,
                    "conditions": [
                        {
                            "condition": "minecraft:survives_explosion"
                        }
                    ],
                    "entries": [
                        {
                            "type": "minecraft:item",
                            "name": fullBlockID
                        }
                    ],
                    "rolls": 1.0
                }
            ],
            "random_sequence": f"{modID}:blocks/{blockID}"
        }

    def genRecipe(self, fullBlockID : str, ingredient : str, count : int = 4, pattern : list[str] = ["##", "##"]):
        return {
            "type": "minecraft:crafting_shaped",
            "category": "building",
            "key": {
                "#": ingredient
            },
            "pattern": pattern,
            "result": {
                "count": count,
                "id": fullBlockID
            }
        }

    def genRecipeAdvancement(self, recipeName : str, ingredient : str):
        return {
            "parent": "minecraft:recipes/root",
            "criteria": {
                "has_" + BlockHelpers.getBlockBaseID(ingredient): {
                    "conditions": {
                        "items": [
                            {
                                "items": ingredient
                            }
                        ]
                    },
                    "trigger": "minecraft:inventory_changed"
                },
                "has_the_recipe": {
                    "conditions": {
                        "recipe": recipeName
                    },
                    "trigger": "minecraft:recipe_unlocked"
                }
            },
            "requirements": [
                [
                    "has_the_recipe",
                    "has_" + BlockHelpers.getBlockBaseID(ingredient)
                ]
            ],
            "rewards": {
                "recipes": [
                    recipeName
                ]
            }
        }

    def genStonecuttingRecipe(self, product : str, ingredient : str, count : int = 1):
        return {
            "type": "minecraft:stonecutting",
            "ingredient": ingredient,
            "result": {
                "count": count,
                "id": product
            }
        }

    def genCode(self, fullBlockID : str) -> str:
        return f'   public static final DeferredBlock<Block> {BlockHelpers.getBlockBaseID(fullBlockID).upper()} = registerBlockItem("{BlockHelpers.getBlockBaseID(fullBlockID)}",\n         (properties) -> new Block(properties));'

    def writeBlockState(self, fullBlockID : str):
        modID, blockID = BlockHelpers.getSplitIDs(fullBlockID)
        Writter.writeJSON(self.genBlockState(fullBlockID), f"{BlockHelpers.getBlockStatePath(modID)}/{blockID}", "(Block State)")

    def writeBlockModel(self, fullBlockID : str):
        modID, blockID = BlockHelpers.getSplitIDs(fullBlockID)
        Writter.writeJSON(self.genBlockModel(fullBlockID), f"{BlockHelpers.getModelPath(modID)}/{blockID}", "(Block Model)")

    def writeItemModel(self, fullBlockID : str):
        modID, blockID = BlockHelpers.getSplitIDs(fullBlockID)
        Writter.writeJSON(self.genItemModel(modID, blockID), f"{BlockHelpers.getItemPath(modID)}/{blockID}", "(Item Model)")

    def writeLootTable(self, fullBlockID : str):
        modID, blockID = BlockHelpers.getSplitIDs(fullBlockID)
        Writter.writeJSON(self.genLootTable(fullBlockID), f"{BlockHelpers.getLootTablePath(modID)}/{blockID}", "(Loot Table)")

    def writeRecipe(self, fullBlockID : str, ingredient : str, count : int = 4, isDecoration : bool = False):
        modID, blockID = BlockHelpers.getSplitIDs(fullBlockID)
        # Recipe
        Writter.writeJSON(self.genRecipe(fullBlockID, ingredient, count), f"{BlockHelpers.getRecipePath(modID)}/{blockID}", "(Recipe)")
        # Adv
        Writter.writeJSON(self.genRecipeAdvancement(fullBlockID, ingredient), f"{BlockHelpers.getRecipeAdvPath(modID, isDecoration)}/{blockID}", "(Recipe)")

    def writeStonecuttingRecipe(self, fullBlockID : str, ingredient : str, count : int = 1, isDecoration : bool = False):
        modID, blockID = BlockHelpers.getSplitIDs(fullBlockID)
        # Recipe
        Writter.writeJSON(self.genStonecuttingRecipe(fullBlockID, ingredient, count), f"{BlockHelpers.getRecipePath(modID)}/{blockID}_from_{BlockHelpers.getBlockBaseID(ingredient)}_stonecutting", "(Recipe)")
        # Adv
        Writter.writeJSON(self.genRecipeAdvancement(f"{fullBlockID}_from_{BlockHelpers.getBlockBaseID(ingredient)}_stonecutting", ingredient), f"{BlockHelpers.getRecipeAdvPath(modID, isDecoration)}/{blockID}_from_{BlockHelpers.getBlockBaseID(ingredient)}_stonecutting", "(Recipe)")

    def finishPrint(self, fullBlockID : str, daType : str = "Block"):
        print(f"***** Completed ({daType}) : " + fullBlockID)

    def genCreativeCode(self, fullBlockID : str) -> str:
        return f"output.accept({Data.getModBlocksJava()}.{BlockHelpers.getBlockBaseID(fullBlockID).upper()});"

    # A block generated with this will ALWAYS have the modded ID i think-
    def __init__(self, fullBlockID : str, ingredients : list[str], modelType : BlockModel = BlockModel.CUBE, baseBlock : str = None):
        self.modelType : BlockModel = modelType

        if baseBlock == None: baseBlock = fullBlockID
        self.modelBlock : str = baseBlock

        self.writeBlockState(fullBlockID)
        self.writeBlockModel(fullBlockID)
        self.writeItemModel(fullBlockID)
        self.writeLootTable(fullBlockID)
        self.writeRecipe(fullBlockID, ingredients[0])
        for daIngredient in ingredients: self.writeStonecuttingRecipe(fullBlockID, daIngredient)
        
        Globals.addBlock(fullBlockID)
        Globals.addCode(self.genCode(fullBlockID))
        Globals.addCreativeCode(self.genCreativeCode(fullBlockID))
        
        self.finishPrint(fullBlockID)