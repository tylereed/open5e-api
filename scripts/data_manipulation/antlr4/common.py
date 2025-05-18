
def buildCommonResult():
    return {
        'isMelee': False,
        'isRanged': False,
        'isWeapon': False,
        'isSpell': False,
        'isSave': False,
        'toHitBonus': 0,
        'reach': None,
        'range': None,
        'rangeMax': None,
        'numberTargets': 0,
        'targetType': None,
        'damageAverage': None,
        'damageDice': None,
        'damageType': None,
        'plusDamageAverage': None,
        'plusDamageDice': None,
        'plusDamageType': None,
        'twoHandedDamageAverage': None,
        'twoHandedDamageDice': None,
        'twoHandedDamageType': None,
        'saveDC': None,
        'saveType': None
    }

def getDamageTypesAsList(ctx):
    return map(lambda x: x.getText(), ctx.DAMAGE_TYPE())