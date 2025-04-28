# Generated from grammars/Attack.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AttackParser import AttackParser
else:
    from AttackParser import AttackParser

# This class defines a complete listener for a parse tree produced by AttackParser.
class AttackListener(ParseTreeListener):

    # Enter a parse tree produced by AttackParser#attack.
    def enterAttack(self, ctx:AttackParser.AttackContext):
        pass

    # Exit a parse tree produced by AttackParser#attack.
    def exitAttack(self, ctx:AttackParser.AttackContext):
        pass


    # Enter a parse tree produced by AttackParser#attackType.
    def enterAttackType(self, ctx:AttackParser.AttackTypeContext):
        pass

    # Exit a parse tree produced by AttackParser#attackType.
    def exitAttackType(self, ctx:AttackParser.AttackTypeContext):
        pass


    # Enter a parse tree produced by AttackParser#meleeRanged.
    def enterMeleeRanged(self, ctx:AttackParser.MeleeRangedContext):
        pass

    # Exit a parse tree produced by AttackParser#meleeRanged.
    def exitMeleeRanged(self, ctx:AttackParser.MeleeRangedContext):
        pass


    # Enter a parse tree produced by AttackParser#weaponSpell.
    def enterWeaponSpell(self, ctx:AttackParser.WeaponSpellContext):
        pass

    # Exit a parse tree produced by AttackParser#weaponSpell.
    def exitWeaponSpell(self, ctx:AttackParser.WeaponSpellContext):
        pass


    # Enter a parse tree produced by AttackParser#toHit.
    def enterToHit(self, ctx:AttackParser.ToHitContext):
        pass

    # Exit a parse tree produced by AttackParser#toHit.
    def exitToHit(self, ctx:AttackParser.ToHitContext):
        pass


    # Enter a parse tree produced by AttackParser#distance.
    def enterDistance(self, ctx:AttackParser.DistanceContext):
        pass

    # Exit a parse tree produced by AttackParser#distance.
    def exitDistance(self, ctx:AttackParser.DistanceContext):
        pass


    # Enter a parse tree produced by AttackParser#reach.
    def enterReach(self, ctx:AttackParser.ReachContext):
        pass

    # Exit a parse tree produced by AttackParser#reach.
    def exitReach(self, ctx:AttackParser.ReachContext):
        pass


    # Enter a parse tree produced by AttackParser#range.
    def enterRange(self, ctx:AttackParser.RangeContext):
        pass

    # Exit a parse tree produced by AttackParser#range.
    def exitRange(self, ctx:AttackParser.RangeContext):
        pass


    # Enter a parse tree produced by AttackParser#targets.
    def enterTargets(self, ctx:AttackParser.TargetsContext):
        pass

    # Exit a parse tree produced by AttackParser#targets.
    def exitTargets(self, ctx:AttackParser.TargetsContext):
        pass


    # Enter a parse tree produced by AttackParser#hit.
    def enterHit(self, ctx:AttackParser.HitContext):
        pass

    # Exit a parse tree produced by AttackParser#hit.
    def exitHit(self, ctx:AttackParser.HitContext):
        pass


    # Enter a parse tree produced by AttackParser#damage.
    def enterDamage(self, ctx:AttackParser.DamageContext):
        pass

    # Exit a parse tree produced by AttackParser#damage.
    def exitDamage(self, ctx:AttackParser.DamageContext):
        pass


    # Enter a parse tree produced by AttackParser#plusDamage.
    def enterPlusDamage(self, ctx:AttackParser.PlusDamageContext):
        pass

    # Exit a parse tree produced by AttackParser#plusDamage.
    def exitPlusDamage(self, ctx:AttackParser.PlusDamageContext):
        pass


    # Enter a parse tree produced by AttackParser#versatileDamage.
    def enterVersatileDamage(self, ctx:AttackParser.VersatileDamageContext):
        pass

    # Exit a parse tree produced by AttackParser#versatileDamage.
    def exitVersatileDamage(self, ctx:AttackParser.VersatileDamageContext):
        pass


    # Enter a parse tree produced by AttackParser#extraText.
    def enterExtraText(self, ctx:AttackParser.ExtraTextContext):
        pass

    # Exit a parse tree produced by AttackParser#extraText.
    def exitExtraText(self, ctx:AttackParser.ExtraTextContext):
        pass



del AttackParser