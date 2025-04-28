# Generated from grammars/Attack.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,33,139,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,38,8,0,1,0,3,0,41,8,0,1,
        0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,3,2,58,
        8,2,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,3,5,72,8,5,1,
        6,3,6,75,8,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,3,7,84,8,7,1,7,1,7,1,8,
        1,8,1,8,1,8,1,9,1,9,3,9,94,8,9,1,9,3,9,97,8,9,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,125,8,12,1,12,
        1,12,3,12,129,8,12,1,13,5,13,132,8,13,10,13,12,13,135,9,13,1,13,
        1,13,1,13,1,133,0,14,0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,3,1,
        0,27,28,1,0,14,15,2,0,7,7,21,21,137,0,28,1,0,0,0,2,47,1,0,0,0,4,
        57,1,0,0,0,6,59,1,0,0,0,8,61,1,0,0,0,10,71,1,0,0,0,12,74,1,0,0,0,
        14,79,1,0,0,0,16,87,1,0,0,0,18,91,1,0,0,0,20,98,1,0,0,0,22,107,1,
        0,0,0,24,116,1,0,0,0,26,133,1,0,0,0,28,29,3,2,1,0,29,30,5,1,0,0,
        30,31,5,2,0,0,31,32,3,8,4,0,32,33,5,3,0,0,33,34,3,10,5,0,34,35,5,
        3,0,0,35,37,3,16,8,0,36,38,5,4,0,0,37,36,1,0,0,0,37,38,1,0,0,0,38,
        40,1,0,0,0,39,41,5,5,0,0,40,39,1,0,0,0,40,41,1,0,0,0,41,42,1,0,0,
        0,42,43,5,2,0,0,43,44,3,18,9,0,44,45,3,26,13,0,45,46,5,0,0,1,46,
        1,1,0,0,0,47,48,3,4,2,0,48,49,5,2,0,0,49,50,3,6,3,0,50,51,5,6,0,
        0,51,3,1,0,0,0,52,58,5,25,0,0,53,58,5,26,0,0,54,55,5,25,0,0,55,56,
        5,7,0,0,56,58,5,26,0,0,57,52,1,0,0,0,57,53,1,0,0,0,57,54,1,0,0,0,
        58,5,1,0,0,0,59,60,7,0,0,0,60,7,1,0,0,0,61,62,5,8,0,0,62,63,5,31,
        0,0,63,64,5,9,0,0,64,9,1,0,0,0,65,72,3,12,6,0,66,72,3,14,7,0,67,
        68,3,12,6,0,68,69,5,7,0,0,69,70,3,14,7,0,70,72,1,0,0,0,71,65,1,0,
        0,0,71,66,1,0,0,0,71,67,1,0,0,0,72,11,1,0,0,0,73,75,5,10,0,0,74,
        73,1,0,0,0,74,75,1,0,0,0,75,76,1,0,0,0,76,77,5,31,0,0,77,78,5,11,
        0,0,78,13,1,0,0,0,79,80,5,12,0,0,80,83,5,31,0,0,81,82,5,13,0,0,82,
        84,5,31,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,85,1,0,0,0,85,86,5,11,
        0,0,86,15,1,0,0,0,87,88,5,32,0,0,88,89,5,2,0,0,89,90,7,1,0,0,90,
        17,1,0,0,0,91,93,3,20,10,0,92,94,3,22,11,0,93,92,1,0,0,0,93,94,1,
        0,0,0,94,96,1,0,0,0,95,97,3,24,12,0,96,95,1,0,0,0,96,97,1,0,0,0,
        97,19,1,0,0,0,98,99,5,16,0,0,99,100,5,2,0,0,100,101,5,31,0,0,101,
        102,5,17,0,0,102,103,5,29,0,0,103,104,5,18,0,0,104,105,5,30,0,0,
        105,106,5,19,0,0,106,21,1,0,0,0,107,108,5,20,0,0,108,109,5,2,0,0,
        109,110,5,31,0,0,110,111,5,17,0,0,111,112,5,29,0,0,112,113,5,18,
        0,0,113,114,5,30,0,0,114,115,5,19,0,0,115,23,1,0,0,0,116,117,7,2,
        0,0,117,118,5,31,0,0,118,119,5,17,0,0,119,120,5,29,0,0,120,121,5,
        18,0,0,121,122,5,30,0,0,122,124,5,19,0,0,123,125,3,22,11,0,124,123,
        1,0,0,0,124,125,1,0,0,0,125,126,1,0,0,0,126,128,5,22,0,0,127,129,
        5,23,0,0,128,127,1,0,0,0,128,129,1,0,0,0,129,25,1,0,0,0,130,132,
        5,33,0,0,131,130,1,0,0,0,132,135,1,0,0,0,133,134,1,0,0,0,133,131,
        1,0,0,0,134,136,1,0,0,0,135,133,1,0,0,0,136,137,5,5,0,0,137,27,1,
        0,0,0,11,37,40,57,71,74,83,93,96,124,128,133
    ]

class AttackParser ( Parser ):

    grammarFileName = "Attack.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "' '", "', '", "','", "'.'", "' Attack'", 
                     "' or '", "'+'", "' to hit'", "'reach '", "' ft.'", 
                     "'range '", "'/'", "'target'", "'targets'", "'Hit:'", 
                     "' ('", "') '", "' damage'", "' plus'", "', or '", 
                     "' if used with two hands'", "' to make a melee attack'", 
                     "<INVALID>", "'Melee'", "'Ranged'", "'Weapon'", "'Spell'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "MARKUP", "MELEE", "RANGED", "WEAPON", "SPELL", "DICE", 
                      "DAMAGE_TYPE", "NUMBER", "NUMBER_TEXT", "TEXT" ]

    RULE_attack = 0
    RULE_attackType = 1
    RULE_meleeRanged = 2
    RULE_weaponSpell = 3
    RULE_toHit = 4
    RULE_distance = 5
    RULE_reach = 6
    RULE_range = 7
    RULE_targets = 8
    RULE_hit = 9
    RULE_damage = 10
    RULE_plusDamage = 11
    RULE_versatileDamage = 12
    RULE_extraText = 13

    ruleNames =  [ "attack", "attackType", "meleeRanged", "weaponSpell", 
                   "toHit", "distance", "reach", "range", "targets", "hit", 
                   "damage", "plusDamage", "versatileDamage", "extraText" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    MARKUP=24
    MELEE=25
    RANGED=26
    WEAPON=27
    SPELL=28
    DICE=29
    DAMAGE_TYPE=30
    NUMBER=31
    NUMBER_TEXT=32
    TEXT=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class AttackContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attackType(self):
            return self.getTypedRuleContext(AttackParser.AttackTypeContext,0)


        def toHit(self):
            return self.getTypedRuleContext(AttackParser.ToHitContext,0)


        def distance(self):
            return self.getTypedRuleContext(AttackParser.DistanceContext,0)


        def targets(self):
            return self.getTypedRuleContext(AttackParser.TargetsContext,0)


        def hit(self):
            return self.getTypedRuleContext(AttackParser.HitContext,0)


        def extraText(self):
            return self.getTypedRuleContext(AttackParser.ExtraTextContext,0)


        def EOF(self):
            return self.getToken(AttackParser.EOF, 0)

        def getRuleIndex(self):
            return AttackParser.RULE_attack

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttack" ):
                listener.enterAttack(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttack" ):
                listener.exitAttack(self)




    def attack(self):

        localctx = AttackParser.AttackContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_attack)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.attackType()
            self.state = 29
            self.match(AttackParser.T__0)
            self.state = 30
            self.match(AttackParser.T__1)
            self.state = 31
            self.toHit()
            self.state = 32
            self.match(AttackParser.T__2)
            self.state = 33
            self.distance()
            self.state = 34
            self.match(AttackParser.T__2)
            self.state = 35
            self.targets()
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 36
                self.match(AttackParser.T__3)


            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 39
                self.match(AttackParser.T__4)


            self.state = 42
            self.match(AttackParser.T__1)
            self.state = 43
            self.hit()
            self.state = 44
            self.extraText()
            self.state = 45
            self.match(AttackParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttackTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def meleeRanged(self):
            return self.getTypedRuleContext(AttackParser.MeleeRangedContext,0)


        def weaponSpell(self):
            return self.getTypedRuleContext(AttackParser.WeaponSpellContext,0)


        def getRuleIndex(self):
            return AttackParser.RULE_attackType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttackType" ):
                listener.enterAttackType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttackType" ):
                listener.exitAttackType(self)




    def attackType(self):

        localctx = AttackParser.AttackTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_attackType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.meleeRanged()
            self.state = 48
            self.match(AttackParser.T__1)
            self.state = 49
            self.weaponSpell()
            self.state = 50
            self.match(AttackParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MeleeRangedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MELEE(self):
            return self.getToken(AttackParser.MELEE, 0)

        def RANGED(self):
            return self.getToken(AttackParser.RANGED, 0)

        def getRuleIndex(self):
            return AttackParser.RULE_meleeRanged

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMeleeRanged" ):
                listener.enterMeleeRanged(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMeleeRanged" ):
                listener.exitMeleeRanged(self)




    def meleeRanged(self):

        localctx = AttackParser.MeleeRangedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_meleeRanged)
        try:
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.match(AttackParser.MELEE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.match(AttackParser.RANGED)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.match(AttackParser.MELEE)
                self.state = 55
                self.match(AttackParser.T__6)
                self.state = 56
                self.match(AttackParser.RANGED)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WeaponSpellContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WEAPON(self):
            return self.getToken(AttackParser.WEAPON, 0)

        def SPELL(self):
            return self.getToken(AttackParser.SPELL, 0)

        def getRuleIndex(self):
            return AttackParser.RULE_weaponSpell

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWeaponSpell" ):
                listener.enterWeaponSpell(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWeaponSpell" ):
                listener.exitWeaponSpell(self)




    def weaponSpell(self):

        localctx = AttackParser.WeaponSpellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_weaponSpell)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            _la = self._input.LA(1)
            if not(_la==27 or _la==28):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ToHitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(AttackParser.NUMBER, 0)

        def getRuleIndex(self):
            return AttackParser.RULE_toHit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToHit" ):
                listener.enterToHit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToHit" ):
                listener.exitToHit(self)




    def toHit(self):

        localctx = AttackParser.ToHitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_toHit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(AttackParser.T__7)
            self.state = 62
            self.match(AttackParser.NUMBER)
            self.state = 63
            self.match(AttackParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DistanceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def reach(self):
            return self.getTypedRuleContext(AttackParser.ReachContext,0)


        def range_(self):
            return self.getTypedRuleContext(AttackParser.RangeContext,0)


        def getRuleIndex(self):
            return AttackParser.RULE_distance

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistance" ):
                listener.enterDistance(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistance" ):
                listener.exitDistance(self)




    def distance(self):

        localctx = AttackParser.DistanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_distance)
        try:
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.reach()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.range_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.reach()
                self.state = 68
                self.match(AttackParser.T__6)
                self.state = 69
                self.range_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReachContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(AttackParser.NUMBER, 0)

        def getRuleIndex(self):
            return AttackParser.RULE_reach

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReach" ):
                listener.enterReach(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReach" ):
                listener.exitReach(self)




    def reach(self):

        localctx = AttackParser.ReachContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_reach)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 73
                self.match(AttackParser.T__9)


            self.state = 76
            self.match(AttackParser.NUMBER)
            self.state = 77
            self.match(AttackParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(AttackParser.NUMBER)
            else:
                return self.getToken(AttackParser.NUMBER, i)

        def getRuleIndex(self):
            return AttackParser.RULE_range

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange" ):
                listener.enterRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange" ):
                listener.exitRange(self)




    def range_(self):

        localctx = AttackParser.RangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_range)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(AttackParser.T__11)
            self.state = 80
            self.match(AttackParser.NUMBER)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 81
                self.match(AttackParser.T__12)
                self.state = 82
                self.match(AttackParser.NUMBER)


            self.state = 85
            self.match(AttackParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TargetsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_TEXT(self):
            return self.getToken(AttackParser.NUMBER_TEXT, 0)

        def getRuleIndex(self):
            return AttackParser.RULE_targets

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTargets" ):
                listener.enterTargets(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTargets" ):
                listener.exitTargets(self)




    def targets(self):

        localctx = AttackParser.TargetsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_targets)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(AttackParser.NUMBER_TEXT)
            self.state = 88
            self.match(AttackParser.T__1)
            self.state = 89
            _la = self._input.LA(1)
            if not(_la==14 or _la==15):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def damage(self):
            return self.getTypedRuleContext(AttackParser.DamageContext,0)


        def plusDamage(self):
            return self.getTypedRuleContext(AttackParser.PlusDamageContext,0)


        def versatileDamage(self):
            return self.getTypedRuleContext(AttackParser.VersatileDamageContext,0)


        def getRuleIndex(self):
            return AttackParser.RULE_hit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHit" ):
                listener.enterHit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHit" ):
                listener.exitHit(self)




    def hit(self):

        localctx = AttackParser.HitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_hit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.damage()
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 92
                self.plusDamage()


            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7 or _la==21:
                self.state = 95
                self.versatileDamage()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DamageContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(AttackParser.NUMBER, 0)

        def DICE(self):
            return self.getToken(AttackParser.DICE, 0)

        def DAMAGE_TYPE(self):
            return self.getToken(AttackParser.DAMAGE_TYPE, 0)

        def getRuleIndex(self):
            return AttackParser.RULE_damage

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDamage" ):
                listener.enterDamage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDamage" ):
                listener.exitDamage(self)




    def damage(self):

        localctx = AttackParser.DamageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_damage)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(AttackParser.T__15)
            self.state = 99
            self.match(AttackParser.T__1)
            self.state = 100
            self.match(AttackParser.NUMBER)
            self.state = 101
            self.match(AttackParser.T__16)
            self.state = 102
            self.match(AttackParser.DICE)
            self.state = 103
            self.match(AttackParser.T__17)
            self.state = 104
            self.match(AttackParser.DAMAGE_TYPE)
            self.state = 105
            self.match(AttackParser.T__18)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlusDamageContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(AttackParser.NUMBER, 0)

        def DICE(self):
            return self.getToken(AttackParser.DICE, 0)

        def DAMAGE_TYPE(self):
            return self.getToken(AttackParser.DAMAGE_TYPE, 0)

        def getRuleIndex(self):
            return AttackParser.RULE_plusDamage

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlusDamage" ):
                listener.enterPlusDamage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlusDamage" ):
                listener.exitPlusDamage(self)




    def plusDamage(self):

        localctx = AttackParser.PlusDamageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_plusDamage)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(AttackParser.T__19)
            self.state = 108
            self.match(AttackParser.T__1)
            self.state = 109
            self.match(AttackParser.NUMBER)
            self.state = 110
            self.match(AttackParser.T__16)
            self.state = 111
            self.match(AttackParser.DICE)
            self.state = 112
            self.match(AttackParser.T__17)
            self.state = 113
            self.match(AttackParser.DAMAGE_TYPE)
            self.state = 114
            self.match(AttackParser.T__18)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VersatileDamageContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(AttackParser.NUMBER, 0)

        def DICE(self):
            return self.getToken(AttackParser.DICE, 0)

        def DAMAGE_TYPE(self):
            return self.getToken(AttackParser.DAMAGE_TYPE, 0)

        def plusDamage(self):
            return self.getTypedRuleContext(AttackParser.PlusDamageContext,0)


        def getRuleIndex(self):
            return AttackParser.RULE_versatileDamage

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVersatileDamage" ):
                listener.enterVersatileDamage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVersatileDamage" ):
                listener.exitVersatileDamage(self)




    def versatileDamage(self):

        localctx = AttackParser.VersatileDamageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_versatileDamage)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            _la = self._input.LA(1)
            if not(_la==7 or _la==21):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 117
            self.match(AttackParser.NUMBER)
            self.state = 118
            self.match(AttackParser.T__16)
            self.state = 119
            self.match(AttackParser.DICE)
            self.state = 120
            self.match(AttackParser.T__17)
            self.state = 121
            self.match(AttackParser.DAMAGE_TYPE)
            self.state = 122
            self.match(AttackParser.T__18)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 123
                self.plusDamage()


            self.state = 126
            self.match(AttackParser.T__21)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 127
                self.match(AttackParser.T__22)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExtraTextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(AttackParser.TEXT)
            else:
                return self.getToken(AttackParser.TEXT, i)

        def getRuleIndex(self):
            return AttackParser.RULE_extraText

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtraText" ):
                listener.enterExtraText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtraText" ):
                listener.exitExtraText(self)




    def extraText(self):

        localctx = AttackParser.ExtraTextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_extraText)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 130
                    self.match(AttackParser.TEXT) 
                self.state = 135
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 136
            self.match(AttackParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





