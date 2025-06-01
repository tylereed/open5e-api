from antlr4 import *

from .common import buildCommonResult, getDamageTypesAsList
from .SavingThrowListener import SavingThrowListener

class ForcedSavingThrowListener(SavingThrowListener):
    def __init__(self):
        super().__init__()
        self.result = buildCommonResult()
        
    def enterForcedSavingThrow2014(self, ctx):
        self.result['2014'] = True

    def enterForcedSavingThrow2024(self, ctx):
        self.result['2024'] = True
        
        saveType = ctx.ABILITY()
        if saveType is not None:
            self.result['saveType'] = saveType.getText()

        saveDC = ctx.NUMBER()
        if saveDC:
            self.result['saveDC'] = int(saveDC.getText())

    def enterDamage2024(self, ctx):
        damageAverage = ctx.NUMBER()
        if damageAverage is not None:
            damageAverageText: str = damageAverage.getText()
            if not damageAverageText.startswith("<"):
                self.result['damageAverage'] = int(damageAverage.getText())

        damageDice = ctx.DICE()
        if damageDice is not None:
            self.result['damageDice'] = damageDice.getText()

        damageType = ctx.damageType()
        if damageType is not None:
            self.result['damageType'] = getDamageTypesAsList(damageType)

    def enterPlusDamage2024(self, ctx):
        damageAverage = ctx.NUMBER()
        if damageAverage is not None:
            damageAverageText: str = damageAverage.getText()
            if not damageAverageText.startswith("<"):
                self.result['plusDamageAverage'] = int(damageAverage.getText())

        damageDice = ctx.DICE()
        if damageDice is not None:
            self.result['plusDamageDice'] = damageDice.getText()

        damageType = ctx.damageType()
        if damageType is not None:
            self.result['plusDamageType'] = getDamageTypesAsList(damageType)

    def enterDamageThenSave(self, ctx):
        damageAverage = ctx.NUMBER(0)
        if damageAverage is not None:
            damageAverageText: str = damageAverage.getText()
            if not damageAverageText.startswith("<"):
                self.result['damageAverage'] = int(damageAverage.getText())

        damageDice = ctx.DICE()
        if damageDice is not None:
            self.result['damageDice'] = damageDice.getText()
        
        damageType = ctx.damageType()
        if damageType is not None:
            self.result['damageType'] = getDamageTypesAsList(damageType)

        saveDC = ctx.NUMBER(1)
        if saveDC:
            self.result['saveDC'] = int(saveDC.getText())

        saveType = ctx.ABILITY()
        if saveType is not None:
            self.result['saveType'] = saveType.getText()
        

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

        damageDice = ctx.DICE(0)
        if damageDice is not None:
            self.result['damageDice'] = damageDice.getText()
        
        damageType = ctx.damageType(0)
        if damageType is not None:
            self.result['damageType'] = getDamageTypesAsList(damageType)
        
        plusDamageAverage = ctx.NUMBER(2)
        if plusDamageAverage is not None:
            self.result['plusDamageAverage'] = int(plusDamageAverage.getText())
        
        plusDamageDice = ctx.DICE(1)
        if plusDamageDice is not None:
            self.result['plusDamageDice'] = plusDamageDice.getText()
        
        plusDamageType = ctx.damageType(1)
        if plusDamageType is not None:
            self.result['plusDamageType'] = getDamageTypesAsList(plusDamageType)
        # damageType = ctx.DAMAGE_TYPE()
        # if damageType is not None:
        #     self.result['damageType'] = [damageType.getText()]


    # def enterDamageType(self, ctx):
    #     if ctx is not None:
    #         self.result['damageType'] = getDamageTypesAsList(ctx)

    def enterPostText(self, ctx):
        pass