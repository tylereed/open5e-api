# Generated from ./SavingThrow.g4 by ANTLR 4.13.2
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
        4,1,32,206,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,42,8,1,1,
        1,1,1,1,1,1,2,5,2,48,8,2,10,2,12,2,51,9,2,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,5,5,68,8,5,10,5,12,5,71,9,
        5,1,6,1,6,1,6,3,6,76,8,6,1,6,1,6,1,6,1,7,1,7,1,7,3,7,84,8,7,1,7,
        1,7,1,7,3,7,89,8,7,1,7,1,7,1,7,5,7,94,8,7,10,7,12,7,97,9,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,112,8,8,1,8,1,
        8,3,8,116,8,8,1,8,3,8,119,8,8,1,8,5,8,122,8,8,10,8,12,8,125,9,8,
        1,8,1,8,1,8,1,8,1,8,1,8,3,8,133,8,8,1,8,1,8,3,8,137,8,8,1,8,1,8,
        1,8,3,8,142,8,8,1,8,3,8,145,8,8,1,8,3,8,148,8,8,1,8,1,8,1,8,3,8,
        153,8,8,1,8,1,8,1,8,3,8,158,8,8,1,8,1,8,1,8,3,8,163,8,8,1,9,3,9,
        166,8,9,1,9,1,9,1,9,1,9,5,9,172,8,9,10,9,12,9,175,9,9,1,9,3,9,178,
        8,9,1,9,1,9,3,9,182,8,9,1,10,4,10,185,8,10,11,10,12,10,186,1,10,
        4,10,190,8,10,11,10,12,10,191,1,11,1,11,1,12,4,12,197,8,12,11,12,
        12,12,198,1,13,4,13,202,8,13,11,13,12,13,203,1,13,6,49,69,186,191,
        198,203,0,14,0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,11,1,0,2,2,1,
        0,28,28,1,0,9,11,1,0,15,16,3,0,4,4,12,12,18,18,2,0,4,4,12,12,2,0,
        12,12,20,21,1,0,24,24,2,0,9,11,17,17,1,0,14,14,2,0,18,18,25,25,219,
        0,28,1,0,0,0,2,30,1,0,0,0,4,49,1,0,0,0,6,52,1,0,0,0,8,59,1,0,0,0,
        10,69,1,0,0,0,12,72,1,0,0,0,14,80,1,0,0,0,16,104,1,0,0,0,18,165,
        1,0,0,0,20,184,1,0,0,0,22,193,1,0,0,0,24,196,1,0,0,0,26,201,1,0,
        0,0,28,29,3,2,1,0,29,1,1,0,0,0,30,31,3,10,5,0,31,32,5,28,0,0,32,
        33,5,1,0,0,33,34,5,26,0,0,34,35,3,4,2,0,35,36,5,2,0,0,36,41,3,6,
        3,0,37,42,5,3,0,0,38,42,5,4,0,0,39,40,5,5,0,0,40,42,3,8,4,0,41,37,
        1,0,0,0,41,38,1,0,0,0,41,39,1,0,0,0,42,43,1,0,0,0,43,44,3,26,13,
        0,44,45,5,0,0,1,45,3,1,0,0,0,46,48,8,0,0,0,47,46,1,0,0,0,48,51,1,
        0,0,0,49,50,1,0,0,0,49,47,1,0,0,0,50,5,1,0,0,0,51,49,1,0,0,0,52,
        53,5,26,0,0,53,54,5,6,0,0,54,55,5,27,0,0,55,56,5,7,0,0,56,57,3,18,
        9,0,57,58,5,8,0,0,58,7,1,0,0,0,59,60,5,26,0,0,60,61,5,6,0,0,61,62,
        5,27,0,0,62,63,5,7,0,0,63,64,3,18,9,0,64,65,5,8,0,0,65,9,1,0,0,0,
        66,68,8,1,0,0,67,66,1,0,0,0,68,71,1,0,0,0,69,70,1,0,0,0,69,67,1,
        0,0,0,70,11,1,0,0,0,71,69,1,0,0,0,72,75,3,20,10,0,73,76,3,14,7,0,
        74,76,3,16,8,0,75,73,1,0,0,0,75,74,1,0,0,0,76,77,1,0,0,0,77,78,3,
        26,13,0,78,79,5,0,0,1,79,13,1,0,0,0,80,81,7,2,0,0,81,83,5,26,0,0,
        82,84,5,12,0,0,83,82,1,0,0,0,83,84,1,0,0,0,84,88,1,0,0,0,85,86,5,
        13,0,0,86,87,5,27,0,0,87,89,5,7,0,0,88,85,1,0,0,0,88,89,1,0,0,0,
        89,90,1,0,0,0,90,91,3,18,9,0,91,95,5,8,0,0,92,94,3,22,11,0,93,92,
        1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,98,1,0,0,0,
        97,95,1,0,0,0,98,99,5,14,0,0,99,100,5,26,0,0,100,101,5,12,0,0,101,
        102,5,28,0,0,102,103,7,3,0,0,103,15,1,0,0,0,104,105,5,17,0,0,105,
        106,5,26,0,0,106,107,5,12,0,0,107,108,5,28,0,0,108,132,7,3,0,0,109,
        118,7,4,0,0,110,112,5,12,0,0,111,110,1,0,0,0,111,112,1,0,0,0,112,
        113,1,0,0,0,113,119,5,19,0,0,114,116,5,12,0,0,115,114,1,0,0,0,115,
        116,1,0,0,0,116,117,1,0,0,0,117,119,5,9,0,0,118,111,1,0,0,0,118,
        115,1,0,0,0,119,133,1,0,0,0,120,122,3,24,12,0,121,120,1,0,0,0,122,
        125,1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,126,1,0,0,0,125,
        123,1,0,0,0,126,127,5,25,0,0,127,128,7,5,0,0,128,129,7,6,0,0,129,
        130,5,31,0,0,130,131,5,12,0,0,131,133,5,10,0,0,132,109,1,0,0,0,132,
        123,1,0,0,0,133,134,1,0,0,0,134,136,5,26,0,0,135,137,5,12,0,0,136,
        135,1,0,0,0,136,137,1,0,0,0,137,141,1,0,0,0,138,139,5,13,0,0,139,
        140,5,27,0,0,140,142,5,7,0,0,141,138,1,0,0,0,141,142,1,0,0,0,142,
        144,1,0,0,0,143,145,3,18,9,0,144,143,1,0,0,0,144,145,1,0,0,0,145,
        147,1,0,0,0,146,148,5,8,0,0,147,146,1,0,0,0,147,148,1,0,0,0,148,
        162,1,0,0,0,149,150,5,22,0,0,150,152,5,26,0,0,151,153,5,12,0,0,152,
        151,1,0,0,0,152,153,1,0,0,0,153,157,1,0,0,0,154,155,5,13,0,0,155,
        156,5,27,0,0,156,158,5,7,0,0,157,154,1,0,0,0,157,158,1,0,0,0,158,
        159,1,0,0,0,159,160,3,18,9,0,160,161,5,8,0,0,161,163,1,0,0,0,162,
        149,1,0,0,0,162,163,1,0,0,0,163,17,1,0,0,0,164,166,5,23,0,0,165,
        164,1,0,0,0,165,166,1,0,0,0,166,167,1,0,0,0,167,181,5,29,0,0,168,
        169,7,5,0,0,169,170,5,12,0,0,170,172,5,29,0,0,171,168,1,0,0,0,172,
        175,1,0,0,0,173,171,1,0,0,0,173,174,1,0,0,0,174,177,1,0,0,0,175,
        173,1,0,0,0,176,178,7,5,0,0,177,176,1,0,0,0,177,178,1,0,0,0,178,
        179,1,0,0,0,179,180,5,18,0,0,180,182,5,29,0,0,181,173,1,0,0,0,181,
        182,1,0,0,0,182,19,1,0,0,0,183,185,8,7,0,0,184,183,1,0,0,0,185,186,
        1,0,0,0,186,187,1,0,0,0,186,184,1,0,0,0,187,189,1,0,0,0,188,190,
        8,8,0,0,189,188,1,0,0,0,190,191,1,0,0,0,191,192,1,0,0,0,191,189,
        1,0,0,0,192,21,1,0,0,0,193,194,8,9,0,0,194,23,1,0,0,0,195,197,8,
        10,0,0,196,195,1,0,0,0,197,198,1,0,0,0,198,199,1,0,0,0,198,196,1,
        0,0,0,199,25,1,0,0,0,200,202,9,0,0,0,201,200,1,0,0,0,202,203,1,0,
        0,0,203,204,1,0,0,0,203,201,1,0,0,0,204,27,1,0,0,0,27,41,49,69,75,
        83,88,95,111,115,118,123,132,136,141,144,147,152,157,162,165,173,
        177,181,186,191,198,203
    ]

class SavingThrowParser ( Parser ):

    grammarFileName = "SavingThrow.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "' Saving Throw: DC '", "' Failure: '", 
                     "'.'", "','", "' plus '", "' ('", "') '", "' damage'", 
                     "'take '", "'takes '", "'deals '", "' '", "'('", "', or half damage with a successful DC '", 
                     "' save'", "' saving throw'", "'DC '", "' or '", "'taking '", 
                     "' a '", "' the '", "' and '", "'points of '", "'takes damage'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ON_A_FAILURE", "NUMBER", "DICE", "ABILITY", 
                      "DAMAGE_TYPE", "COMMA_SPACE", "TARGET_TYPE", "TEXT" ]

    RULE_forcedSavingThrow = 0
    RULE_forcedSavingThrow2024 = 1
    RULE_preFailure2024 = 2
    RULE_damage2024 = 3
    RULE_plusDamage2024 = 4
    RULE_preAbility = 5
    RULE_forcedSavingThrow2014 = 6
    RULE_damageThenSave = 7
    RULE_savingThrow = 8
    RULE_damageType = 9
    RULE_preText = 10
    RULE_preHalfSuccess = 11
    RULE_preFailure = 12
    RULE_postText = 13

    ruleNames =  [ "forcedSavingThrow", "forcedSavingThrow2024", "preFailure2024", 
                   "damage2024", "plusDamage2024", "preAbility", "forcedSavingThrow2014", 
                   "damageThenSave", "savingThrow", "damageType", "preText", 
                   "preHalfSuccess", "preFailure", "postText" ]

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
    T__23=24
    ON_A_FAILURE=25
    NUMBER=26
    DICE=27
    ABILITY=28
    DAMAGE_TYPE=29
    COMMA_SPACE=30
    TARGET_TYPE=31
    TEXT=32

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ForcedSavingThrowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forcedSavingThrow2024(self):
            return self.getTypedRuleContext(SavingThrowParser.ForcedSavingThrow2024Context,0)


        def getRuleIndex(self):
            return SavingThrowParser.RULE_forcedSavingThrow

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForcedSavingThrow" ):
                listener.enterForcedSavingThrow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForcedSavingThrow" ):
                listener.exitForcedSavingThrow(self)




    def forcedSavingThrow(self):

        localctx = SavingThrowParser.ForcedSavingThrowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_forcedSavingThrow)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.forcedSavingThrow2024()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForcedSavingThrow2024Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def preAbility(self):
            return self.getTypedRuleContext(SavingThrowParser.PreAbilityContext,0)


        def ABILITY(self):
            return self.getToken(SavingThrowParser.ABILITY, 0)

        def NUMBER(self):
            return self.getToken(SavingThrowParser.NUMBER, 0)

        def preFailure2024(self):
            return self.getTypedRuleContext(SavingThrowParser.PreFailure2024Context,0)


        def damage2024(self):
            return self.getTypedRuleContext(SavingThrowParser.Damage2024Context,0)


        def postText(self):
            return self.getTypedRuleContext(SavingThrowParser.PostTextContext,0)


        def EOF(self):
            return self.getToken(SavingThrowParser.EOF, 0)

        def plusDamage2024(self):
            return self.getTypedRuleContext(SavingThrowParser.PlusDamage2024Context,0)


        def getRuleIndex(self):
            return SavingThrowParser.RULE_forcedSavingThrow2024

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForcedSavingThrow2024" ):
                listener.enterForcedSavingThrow2024(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForcedSavingThrow2024" ):
                listener.exitForcedSavingThrow2024(self)




    def forcedSavingThrow2024(self):

        localctx = SavingThrowParser.ForcedSavingThrow2024Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_forcedSavingThrow2024)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.preAbility()
            self.state = 31
            self.match(SavingThrowParser.ABILITY)
            self.state = 32
            self.match(SavingThrowParser.T__0)
            self.state = 33
            self.match(SavingThrowParser.NUMBER)
            self.state = 34
            self.preFailure2024()
            self.state = 35
            self.match(SavingThrowParser.T__1)
            self.state = 36
            self.damage2024()
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 37
                self.match(SavingThrowParser.T__2)
                pass
            elif token in [4]:
                self.state = 38
                self.match(SavingThrowParser.T__3)
                pass
            elif token in [5]:
                self.state = 39
                self.match(SavingThrowParser.T__4)
                self.state = 40
                self.plusDamage2024()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 43
            self.postText()
            self.state = 44
            self.match(SavingThrowParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreFailure2024Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SavingThrowParser.RULE_preFailure2024

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreFailure2024" ):
                listener.enterPreFailure2024(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreFailure2024" ):
                listener.exitPreFailure2024(self)




    def preFailure2024(self):

        localctx = SavingThrowParser.PreFailure2024Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_preFailure2024)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 46
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==2:
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 51
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Damage2024Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(SavingThrowParser.NUMBER, 0)

        def DICE(self):
            return self.getToken(SavingThrowParser.DICE, 0)

        def damageType(self):
            return self.getTypedRuleContext(SavingThrowParser.DamageTypeContext,0)


        def getRuleIndex(self):
            return SavingThrowParser.RULE_damage2024

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDamage2024" ):
                listener.enterDamage2024(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDamage2024" ):
                listener.exitDamage2024(self)




    def damage2024(self):

        localctx = SavingThrowParser.Damage2024Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_damage2024)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(SavingThrowParser.NUMBER)
            self.state = 53
            self.match(SavingThrowParser.T__5)
            self.state = 54
            self.match(SavingThrowParser.DICE)
            self.state = 55
            self.match(SavingThrowParser.T__6)
            self.state = 56
            self.damageType()
            self.state = 57
            self.match(SavingThrowParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlusDamage2024Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(SavingThrowParser.NUMBER, 0)

        def DICE(self):
            return self.getToken(SavingThrowParser.DICE, 0)

        def damageType(self):
            return self.getTypedRuleContext(SavingThrowParser.DamageTypeContext,0)


        def getRuleIndex(self):
            return SavingThrowParser.RULE_plusDamage2024

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlusDamage2024" ):
                listener.enterPlusDamage2024(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlusDamage2024" ):
                listener.exitPlusDamage2024(self)




    def plusDamage2024(self):

        localctx = SavingThrowParser.PlusDamage2024Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_plusDamage2024)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(SavingThrowParser.NUMBER)
            self.state = 60
            self.match(SavingThrowParser.T__5)
            self.state = 61
            self.match(SavingThrowParser.DICE)
            self.state = 62
            self.match(SavingThrowParser.T__6)
            self.state = 63
            self.damageType()
            self.state = 64
            self.match(SavingThrowParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreAbilityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABILITY(self, i:int=None):
            if i is None:
                return self.getTokens(SavingThrowParser.ABILITY)
            else:
                return self.getToken(SavingThrowParser.ABILITY, i)

        def getRuleIndex(self):
            return SavingThrowParser.RULE_preAbility

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreAbility" ):
                listener.enterPreAbility(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreAbility" ):
                listener.exitPreAbility(self)




    def preAbility(self):

        localctx = SavingThrowParser.PreAbilityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_preAbility)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 66
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==28:
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 71
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForcedSavingThrow2014Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def preText(self):
            return self.getTypedRuleContext(SavingThrowParser.PreTextContext,0)


        def postText(self):
            return self.getTypedRuleContext(SavingThrowParser.PostTextContext,0)


        def EOF(self):
            return self.getToken(SavingThrowParser.EOF, 0)

        def damageThenSave(self):
            return self.getTypedRuleContext(SavingThrowParser.DamageThenSaveContext,0)


        def savingThrow(self):
            return self.getTypedRuleContext(SavingThrowParser.SavingThrowContext,0)


        def getRuleIndex(self):
            return SavingThrowParser.RULE_forcedSavingThrow2014

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForcedSavingThrow2014" ):
                listener.enterForcedSavingThrow2014(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForcedSavingThrow2014" ):
                listener.exitForcedSavingThrow2014(self)




    def forcedSavingThrow2014(self):

        localctx = SavingThrowParser.ForcedSavingThrow2014Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_forcedSavingThrow2014)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.preText()
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 11]:
                self.state = 73
                self.damageThenSave()
                pass
            elif token in [17]:
                self.state = 74
                self.savingThrow()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 77
            self.postText()
            self.state = 78
            self.match(SavingThrowParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DamageThenSaveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(SavingThrowParser.NUMBER)
            else:
                return self.getToken(SavingThrowParser.NUMBER, i)

        def damageType(self):
            return self.getTypedRuleContext(SavingThrowParser.DamageTypeContext,0)


        def ABILITY(self):
            return self.getToken(SavingThrowParser.ABILITY, 0)

        def DICE(self):
            return self.getToken(SavingThrowParser.DICE, 0)

        def preHalfSuccess(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SavingThrowParser.PreHalfSuccessContext)
            else:
                return self.getTypedRuleContext(SavingThrowParser.PreHalfSuccessContext,i)


        def getRuleIndex(self):
            return SavingThrowParser.RULE_damageThenSave

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDamageThenSave" ):
                listener.enterDamageThenSave(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDamageThenSave" ):
                listener.exitDamageThenSave(self)




    def damageThenSave(self):

        localctx = SavingThrowParser.DamageThenSaveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_damageThenSave)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 81
            self.match(SavingThrowParser.NUMBER)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 82
                self.match(SavingThrowParser.T__11)


            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 85
                self.match(SavingThrowParser.T__12)
                self.state = 86
                self.match(SavingThrowParser.DICE)
                self.state = 87
                self.match(SavingThrowParser.T__6)


            self.state = 90
            self.damageType()
            self.state = 91
            self.match(SavingThrowParser.T__7)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589918206) != 0):
                self.state = 92
                self.preHalfSuccess()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
            self.match(SavingThrowParser.T__13)
            self.state = 99
            self.match(SavingThrowParser.NUMBER)
            self.state = 100
            self.match(SavingThrowParser.T__11)
            self.state = 101
            self.match(SavingThrowParser.ABILITY)
            self.state = 102
            _la = self._input.LA(1)
            if not(_la==15 or _la==16):
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


    class SavingThrowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(SavingThrowParser.NUMBER)
            else:
                return self.getToken(SavingThrowParser.NUMBER, i)

        def ABILITY(self):
            return self.getToken(SavingThrowParser.ABILITY, 0)

        def DICE(self, i:int=None):
            if i is None:
                return self.getTokens(SavingThrowParser.DICE)
            else:
                return self.getToken(SavingThrowParser.DICE, i)

        def damageType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SavingThrowParser.DamageTypeContext)
            else:
                return self.getTypedRuleContext(SavingThrowParser.DamageTypeContext,i)


        def ON_A_FAILURE(self):
            return self.getToken(SavingThrowParser.ON_A_FAILURE, 0)

        def TARGET_TYPE(self):
            return self.getToken(SavingThrowParser.TARGET_TYPE, 0)

        def preFailure(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SavingThrowParser.PreFailureContext)
            else:
                return self.getTypedRuleContext(SavingThrowParser.PreFailureContext,i)


        def getRuleIndex(self):
            return SavingThrowParser.RULE_savingThrow

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSavingThrow" ):
                listener.enterSavingThrow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSavingThrow" ):
                listener.exitSavingThrow(self)




    def savingThrow(self):

        localctx = SavingThrowParser.SavingThrowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_savingThrow)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(SavingThrowParser.T__16)
            self.state = 105
            self.match(SavingThrowParser.NUMBER)
            self.state = 106
            self.match(SavingThrowParser.T__11)
            self.state = 107
            self.match(SavingThrowParser.ABILITY)
            self.state = 108
            _la = self._input.LA(1)
            if not(_la==15 or _la==16):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 109
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 266256) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 118
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 111
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==12:
                        self.state = 110
                        self.match(SavingThrowParser.T__11)


                    self.state = 113
                    self.match(SavingThrowParser.T__18)
                    pass

                elif la_ == 2:
                    self.state = 115
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==12:
                        self.state = 114
                        self.match(SavingThrowParser.T__11)


                    self.state = 117
                    self.match(SavingThrowParser.T__8)
                    pass


                pass

            elif la_ == 2:
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8556118014) != 0):
                    self.state = 120
                    self.preFailure()
                    self.state = 125
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 126
                self.match(SavingThrowParser.ON_A_FAILURE)
                self.state = 127
                _la = self._input.LA(1)
                if not(_la==4 or _la==12):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 128
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3149824) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 129
                self.match(SavingThrowParser.TARGET_TYPE)
                self.state = 130
                self.match(SavingThrowParser.T__11)
                self.state = 131
                self.match(SavingThrowParser.T__9)
                pass


            self.state = 134
            self.match(SavingThrowParser.NUMBER)
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 135
                self.match(SavingThrowParser.T__11)


            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 138
                self.match(SavingThrowParser.T__12)
                self.state = 139
                self.match(SavingThrowParser.DICE)
                self.state = 140
                self.match(SavingThrowParser.T__6)


            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 143
                self.damageType()


            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 146
                self.match(SavingThrowParser.T__7)


            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 149
                self.match(SavingThrowParser.T__21)
                self.state = 150
                self.match(SavingThrowParser.NUMBER)
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 151
                    self.match(SavingThrowParser.T__11)


                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 154
                    self.match(SavingThrowParser.T__12)
                    self.state = 155
                    self.match(SavingThrowParser.DICE)
                    self.state = 156
                    self.match(SavingThrowParser.T__6)


                self.state = 159
                self.damageType()
                self.state = 160
                self.match(SavingThrowParser.T__7)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DamageTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DAMAGE_TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(SavingThrowParser.DAMAGE_TYPE)
            else:
                return self.getToken(SavingThrowParser.DAMAGE_TYPE, i)

        def getRuleIndex(self):
            return SavingThrowParser.RULE_damageType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDamageType" ):
                listener.enterDamageType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDamageType" ):
                listener.exitDamageType(self)




    def damageType(self):

        localctx = SavingThrowParser.DamageTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_damageType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 164
                self.match(SavingThrowParser.T__22)


            self.state = 167
            self.match(SavingThrowParser.DAMAGE_TYPE)
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 173
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 168
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==12):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 169
                        self.match(SavingThrowParser.T__11)
                        self.state = 170
                        self.match(SavingThrowParser.DAMAGE_TYPE) 
                    self.state = 175
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4 or _la==12:
                    self.state = 176
                    _la = self._input.LA(1)
                    if not(_la==4 or _la==12):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 179
                self.match(SavingThrowParser.T__17)
                self.state = 180
                self.match(SavingThrowParser.DAMAGE_TYPE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreTextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SavingThrowParser.RULE_preText

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreText" ):
                listener.enterPreText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreText" ):
                listener.exitPreText(self)




    def preText(self):

        localctx = SavingThrowParser.PreTextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_preText)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 183
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==24:
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 186 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

            self.state = 189 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 188
                    _la = self._input.LA(1)
                    if _la <= 0 or (((_la) & ~0x3f) == 0 and ((1 << _la) & 134656) != 0):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 191 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreHalfSuccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SavingThrowParser.RULE_preHalfSuccess

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreHalfSuccess" ):
                listener.enterPreHalfSuccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreHalfSuccess" ):
                listener.exitPreHalfSuccess(self)




    def preHalfSuccess(self):

        localctx = SavingThrowParser.PreHalfSuccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_preHalfSuccess)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            _la = self._input.LA(1)
            if _la <= 0 or _la==14:
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


    class PreFailureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ON_A_FAILURE(self, i:int=None):
            if i is None:
                return self.getTokens(SavingThrowParser.ON_A_FAILURE)
            else:
                return self.getToken(SavingThrowParser.ON_A_FAILURE, i)

        def getRuleIndex(self):
            return SavingThrowParser.RULE_preFailure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreFailure" ):
                listener.enterPreFailure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreFailure" ):
                listener.exitPreFailure(self)




    def preFailure(self):

        localctx = SavingThrowParser.PreFailureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_preFailure)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 195
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==18 or _la==25:
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 198 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostTextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SavingThrowParser.RULE_postText

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostText" ):
                listener.enterPostText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostText" ):
                listener.exitPostText(self)




    def postText(self):

        localctx = SavingThrowParser.PostTextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_postText)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 200
                    self.matchWildcard()

                else:
                    raise NoViableAltException(self)
                self.state = 203 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





