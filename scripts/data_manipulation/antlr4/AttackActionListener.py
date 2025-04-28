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
        'numberTargets': 0,
        'damageAverage': 0,
        'damageDice': 0,
        'damageType': ''
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

    def buildCsvHeader():
        return ','.join(['isMelee','isRanged'])

    def buildCsv(self):
        return ','.join([str(self.result['isMelee']),str(self.result['isRanged'])])