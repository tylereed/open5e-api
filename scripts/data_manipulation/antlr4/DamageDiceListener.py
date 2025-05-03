from antlr4 import *
from .RollListener import RollListener

class DamageDiceListener(RollListener):
    def __init__(self):
        self.result = {
            'count': 1,
            'sides': 0,
            'modifier': 0
        }

    def enterCount(self, ctx):
        self.result['count'] = int(ctx.NUMBER().getText())

    def enterSides(self, ctx):
        self.result['sides'] = int(ctx.NUMBER().getText())

    def enterModifier(self, ctx):
        self.result['modifier'] = int(ctx.getText())
