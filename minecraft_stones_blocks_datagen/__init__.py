import database.BlockHelpers as BlockHelpers
import Writter
import Globals
from database.BlockModel import BlockModel
from database.gen.Block import Block
from database.gen.Wall import Wall
from database.gen.Stairs import Stairs
from database.gen.Slab import Slab
import Generation

print()
print("***/ Init /***")

#Generation.ExtraSet("minecraft:dripstone_block", [])
#Generation.ExtraSet("minecraft:calcite", [])
#Generation.ExtraSet("minecraft:basalt", [], BlockModel.CUBE_COLUMN)
#Generation.ExtraSet("minecraft:smooth_basalt", [], BlockModel.CUBE)
#Generation.ExtraSet("minecraft:polished_basalt", ["minecraft:basalt"], BlockModel.CUBE_COLUMN)
#Stairs("dpsvarmod:smooth_stone_stairs", ["minecraft:smooth_stone"], BlockModel.CUBE, "minecraft:smooth_stone")
#Wall("dpsvarmod:smooth_stone_wall", ["minecraft:smooth_stone"], BlockModel.CUBE, "minecraft:smooth_stone")
#Wall("dpsvarmod:quartz_block_wall", ["minecraft:quartz_block"], BlockModel.CUBE_BOTTOM_TOP, "minecraft:quartz_block")
#Wall("dpsvarmod:smooth_quartz_wall", ["minecraft:smooth_quartz"], BlockModel.CUBE_BOTTOM_TOP, "minecraft:smooth_quartz")
#Generation.ExtraSet("minecraft:quartz_bricks", ["minecraft:quartz_block"])
#Wall("dpsvarmod:polished_granite_wall", ["minecraft:polished_granite", "minecraft:granite"], BlockModel.CUBE, "minecraft:polished_granite")
#Wall("dpsvarmod:polished_diorite_wall", ["minecraft:polished_diorite", "minecraft:diorite"], BlockModel.CUBE, "minecraft:polished_diorite")
#Wall("dpsvarmod:polished_andesite_wall", ["minecraft:polished_andesite", "minecraft:andesite"], BlockModel.CUBE, "minecraft:polished_andesite")

Globals.writeLang()
Globals.writeWallsTag()
Globals.writePickaxeTag()
Globals.writeCodeLike()
Globals.writeCreativeCodeLike()

print("***/ All Done!!! /***")
print()