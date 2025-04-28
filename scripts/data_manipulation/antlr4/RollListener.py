# Generated from grammars/Roll.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RollParser import RollParser
else:
    from RollParser import RollParser

# This class defines a complete listener for a parse tree produced by RollParser.
class RollListener(ParseTreeListener):

    # Enter a parse tree produced by RollParser#roll.
    def enterRoll(self, ctx:RollParser.RollContext):
        pass

    # Exit a parse tree produced by RollParser#roll.
    def exitRoll(self, ctx:RollParser.RollContext):
        pass


    # Enter a parse tree produced by RollParser#count.
    def enterCount(self, ctx:RollParser.CountContext):
        pass

    # Exit a parse tree produced by RollParser#count.
    def exitCount(self, ctx:RollParser.CountContext):
        pass


    # Enter a parse tree produced by RollParser#sides.
    def enterSides(self, ctx:RollParser.SidesContext):
        pass

    # Exit a parse tree produced by RollParser#sides.
    def exitSides(self, ctx:RollParser.SidesContext):
        pass


    # Enter a parse tree produced by RollParser#modifier.
    def enterModifier(self, ctx:RollParser.ModifierContext):
        pass

    # Exit a parse tree produced by RollParser#modifier.
    def exitModifier(self, ctx:RollParser.ModifierContext):
        pass



del RollParser