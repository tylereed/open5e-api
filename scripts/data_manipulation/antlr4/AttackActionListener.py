from antlr4 import *

from .common import buildCommonResult, getDamageTypesAsList
from .AttackListener import AttackListener

class AttackActionListener(AttackListener):
    def __init__(self):
        super().__init__()
        self.result = buildCommonResult()

    def enterMeleeRanged(self, ctx):
        meleeRanged = ctx.getText()
        if meleeRanged == "Melee":
            self.result['isMelee'] = True
        elif meleeRanged == "Ranged":
            self.result['isRanged'] = True
        elif meleeRanged == "Melee or Ranged":
            self.result['isMelee'] = True
            self.result['isRanged'] = True
            
    def enterWeaponSpell(self, ctx):
        weaponSpell = ctx.getText()
        if weaponSpell == "Weapon":
            self.result['isWeapon'] = True
        elif weaponSpell == "Spell":
            self.result['isSpell'] = True
            
    def enterToHit(self, ctx):
        toHitBonus = ctx.NUMBER()
        if toHitBonus is not None:
            self.result['toHitBonus'] = int(toHitBonus.getText())

    def enterReach(self, ctx):
        reach = ctx.NUMBER()
        self.result['reach'] = int(reach.getText())

    def enterRange(self, ctx):
        range = ctx.NUMBER(0)
        if range is not None:
            self.result['range'] = int(range.getText())
        maxRange = ctx.NUMBER(1)
        if maxRange is not None:
            self.result['rangeMax'] = int(maxRange.getText())
            
    def enterTargets(self, ctx):
        targets = ctx.NUMBER_TEXT(0) if ctx.NUMBER_TEXT(1) is None else ctx.NUMBER_TEXT(1)
        if targets is not None:
            self.result['numberTargets'] = AttackActionListener.wordToNumber(targets.getText())
        else:
            targets = ctx.NUMBER(0) if ctx.NUMBER(1) is None else ctx.NUMBER(1)
            if targets is not None:
                self.result['numberTargets'] = int(targets.getText())
        targetType = ctx.TARGET_TYPE()
        if targetType is not None:
            self.result['targetType'] = targetType.getText()
    
    def enterHit(self, ctx):
        pass

    def enterDamage(self, ctx):
        damageAverage = ctx.NUMBER()
        if damageAverage is not None:
            self.result['damageAverage'] = int(damageAverage.getText())
        damageDice = ctx.DICE()
        if damageDice is not None:
            self.result['damageDice'] = damageDice.getText()
        damageType = ctx.damageType()
        if damageType is not None:
            self.result['damageType'] = getDamageTypesAsList(damageType)

    def enterPlusDamage(self, ctx):
        damageAverage = ctx.NUMBER()
        if damageAverage is not None:
            self.result['plusDamageAverage'] = int(damageAverage.getText())
        damageDice = ctx.DICE()
        if damageDice is not None:
            self.result['plusDamageDice'] = damageDice.getText()
        damageType = ctx.damageType()
        if damageType is not None:
            self.result['plusDamageType'] = getDamageTypesAsList(damageType)

    def enterVersatileDamage(self, ctx):
        damageAverage = ctx.NUMBER()
        if damageAverage is not None:
            self.result['twoHandedDamageAverage'] = int(damageAverage.getText())
        damageDice = ctx.DICE()
        if damageDice is not None:
            self.result['twoHandedDamageDice'] = damageDice.getText()
        damageType = ctx.damageType()
        if damageType is not None:
            self.result['twoHandedDamageType'] = getDamageTypesAsList(damageType)

    def enterSavingThrow(self, ctx):
        isDamage = False
        if self.result['damageAverage'] is None and self.result['damageDice'] is None and self.result['damageType'] is None:
            isDamage = True
        
        saveDC = ctx.NUMBER(0)
        if saveDC is not None:
            self.result['saveDC'] = int(saveDC.getText())
        saveType = ctx.ABILITY()
        if saveType is not None:
            self.result['saveType'] = saveType.getText()
        
        if saveDC is not None and saveType is not None:
            damageAverage = ctx.NUMBER(1)
            if damageAverage is not None:
                if isDamage:
                    self.result['damageAverage'] = int(damageAverage.getText())
                else:
                    self.result['plusDamageAverage'] = int(damageAverage.getText())
            damageDice = ctx.DICE()
            if damageDice is not None:
                if isDamage:
                    self.result['damageDice'] = damageDice.getText()
                else:
                    self.result['plusDamageDice'] = damageDice.getText()
            damageType = ctx.DAMAGE_TYPE()
            if damageType is not None:
                if isDamage:
                    self.result['damageType'] = [damageType.getText()]
                else:
                    self.result['plusDamageType'] = [damageType.getText()]

    def enterExtraDamage(self, ctx):
        if self.result['plusDamageDice'] is None and ctx.NUMBER() is not None:
            extraDice = ctx.DICE()
            if extraDice is not None:
                self.result['plusDamageDice'] = extraDice.getText()
                self.result['plusDamageType'] = self.result['damageType']

    # def exitAttack(self, ctx):
    #     extra = ctx.extraText()
    #     if extra is not None:
    #       self.result['extraText'] = extra.getText()

    def wordToNumber(word):
        if word == "one": return 1
        if word == "two": return 2
        if word == "three": return 3
        if word == "four": return 4
        if word == "five": return 5
        if word == "six": return 6
        if word == "seven": return 7
        if word == "eight": return 8
        if word == "nine": return 9
        return None

    def buildCsvHeader():
        return ','.join(['isMelee','isRanged','isWeapon','isSpell','toHitBonus','reach','range','rangeMax', 'numberTargets',
                        'damageAverage','damageDice','damageType',
                        'plusDamageAverage','plusDamageDice','plusDamageType',
                        'twoHandedDamageAverage','twoHandedDamageDice','twoHandedDamageType',
                    ])

    def buildCsv(self):
        return '"' + '","'.join([
            str(self.result['isMelee']),str(self.result['isRanged']),str(self.result['isWeapon']),
            str(self.result['isSpell']),str(self.result['toHitBonus']),str(self.result['reach']),
            str(self.result['range']),str(self.result['rangeMax']),str(self.result['numberTargets']),
            str(self.result['damageAverage']),str(self.result['damageDice']),str(self.result['damageType']),
            str(self.result['plusDamageAverage']),str(self.result['plusDamageDice']),str(self.result['plusDamageType']),
            str(self.result['twoHandedDamageAverage']),str(self.result['twoHandedDamageDice']),str(self.result['twoHandedDamageType'])
        ]) + '"'