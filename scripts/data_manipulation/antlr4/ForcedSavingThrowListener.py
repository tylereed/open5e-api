from antlr4 import *

from .common import buildCommonResult, getDamageTypesAsList
from .SavingThrowListener import SavingThrowListener

class ForcedSavingThrowListener(SavingThrowListener):
    def __init__(self):
        super().__init__()
        self.result = buildCommonResult()
    
    def enterPreText(self, ctx):
        pass

    def enterSavingThrow(self, ctx):
        saveDC = ctx.NUMBER(0)
        if saveDC:
            self.result['saveDC'] = int(saveDC.getText())

        saveType = ctx.ABILITY()
        if saveType is not None:
            self.result['saveType'] = saveType.getText()

        damageAverage = ctx.NUMBER(1)
        if damageAverage is not None:
            self.result['damageAverage'] = int(damageAverage.getText())

        damageDice = ctx.DICE()
        if damageDice is not None:
            self.result['damageDice'] = damageDice.getText()

        # damageType = ctx.DAMAGE_TYPE()
        # if damageType is not None:
        #     self.result['damageType'] = [damageType.getText()]


    def enterDamageType(self, ctx):
        if ctx is not None:
            self.result['damageType'] = getDamageTypesAsList(ctx)

    def enterPostText(self, ctx):
        pass