from antlr4 import *
from .AttackListener import AttackListener

class AttackActionListener(AttackListener):
    def __init__(self):
        super().__init__()
        self.result = {
            'isMelee': False,
            'isRanged': False,
            'isWeapon': False,
            'isSpell': False,
            'toHitBonus': 0,
            'reach': None,
            'range': None,
            'rangeMax': None,
            'numberTargets': 0,
            'damageAverage': None,
            'damageDice': None,
            'damageType': None
        }

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
        targets = ctx.NUMBER_TEXT()
        if targets is not None:
            self.result['numberTargets'] = AttackActionListener.wordToNumber(targets.getText())

    def enterDamage(self, ctx):
        damageAverage = ctx.NUMBER()
        if damageAverage is not None:
            self.result['damageAverage'] = int(damageAverage.getText())
        damageDice = ctx.DICE()
        if damageDice is not None:
            self.result['damageDice'] = damageDice.getText()
        damageType = ctx.DAMAGE_TYPE()
        if damageType is not None:
            self.result['damageType'] = damageType.getText()
    
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
        return ','.join(['isMelee','isRanged','isWeapon','isSpell','toHitBonus','reach','range','rangeMax',
                         'numberTargets','damageAverage','damageDice','damageType'])

    def buildCsv(self):
        return ','.join([
            str(self.result['isMelee']),str(self.result['isRanged']),str(self.result['isWeapon']),
            str(self.result['isSpell']),str(self.result['toHitBonus']),str(self.result['reach']),
            str(self.result['range']),str(self.result['rangeMax']),str(self.result['numberTargets']),
            str(self.result['damageAverage']),str(self.result['damageDice']),str(self.result['damageType'])
        ])