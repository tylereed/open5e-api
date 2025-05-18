# Generated from SavingThrow.g4 by ANTLR 4.13.2
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
        4,1,19,65,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,27,8,1,1,1,
        1,1,3,1,31,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,5,2,43,8,
        2,10,2,12,2,46,9,2,1,2,3,2,49,8,2,1,2,1,2,3,2,53,8,2,1,3,4,3,56,
        8,3,11,3,12,3,57,1,4,4,4,61,8,4,11,4,12,4,62,1,4,2,57,62,0,5,0,2,
        4,6,8,0,3,1,0,3,4,2,0,2,2,7,7,1,0,1,1,66,0,10,1,0,0,0,2,15,1,0,0,
        0,4,38,1,0,0,0,6,55,1,0,0,0,8,60,1,0,0,0,10,11,3,6,3,0,11,12,3,2,
        1,0,12,13,3,8,4,0,13,14,5,0,0,1,14,1,1,0,0,0,15,16,5,1,0,0,16,17,
        5,13,0,0,17,18,5,2,0,0,18,19,5,15,0,0,19,26,7,0,0,0,20,27,5,5,0,
        0,21,22,5,6,0,0,22,23,5,17,0,0,23,24,7,1,0,0,24,25,5,18,0,0,25,27,
        5,8,0,0,26,20,1,0,0,0,26,21,1,0,0,0,27,28,1,0,0,0,28,30,5,13,0,0,
        29,31,5,2,0,0,30,29,1,0,0,0,30,31,1,0,0,0,31,32,1,0,0,0,32,33,5,
        9,0,0,33,34,5,14,0,0,34,35,5,10,0,0,35,36,3,4,2,0,36,37,5,11,0,0,
        37,3,1,0,0,0,38,52,5,16,0,0,39,40,5,17,0,0,40,41,5,2,0,0,41,43,5,
        16,0,0,42,39,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,
        48,1,0,0,0,46,44,1,0,0,0,47,49,5,17,0,0,48,47,1,0,0,0,48,49,1,0,
        0,0,49,50,1,0,0,0,50,51,5,12,0,0,51,53,5,16,0,0,52,44,1,0,0,0,52,
        53,1,0,0,0,53,5,1,0,0,0,54,56,8,2,0,0,55,54,1,0,0,0,56,57,1,0,0,
        0,57,58,1,0,0,0,57,55,1,0,0,0,58,7,1,0,0,0,59,61,9,0,0,0,60,59,1,
        0,0,0,61,62,1,0,0,0,62,63,1,0,0,0,62,60,1,0,0,0,63,9,1,0,0,0,7,26,
        30,44,48,52,57,62
    ]

class SavingThrowParser ( Parser ):

    grammarFileName = "SavingThrow.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'DC '", "' '", "'save'", "'saving throw'", 
                     "' taking '", "'. On a failure'", "' a '", "' takes '", 
                     "'('", "') '", "' damage'", "' or '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUMBER", "DICE", "ABILITY", "DAMAGE_TYPE", 
                      "COMMA_SPACE", "TARGET_TYPE", "TEXT" ]

    RULE_forcedSavingThrow = 0
    RULE_savingThrow = 1
    RULE_damageType = 2
    RULE_preText = 3
    RULE_postText = 4

    ruleNames =  [ "forcedSavingThrow", "savingThrow", "damageType", "preText", 
                   "postText" ]

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
    NUMBER=13
    DICE=14
    ABILITY=15
    DAMAGE_TYPE=16
    COMMA_SPACE=17
    TARGET_TYPE=18
    TEXT=19

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

        def preText(self):
            return self.getTypedRuleContext(SavingThrowParser.PreTextContext,0)


        def savingThrow(self):
            return self.getTypedRuleContext(SavingThrowParser.SavingThrowContext,0)


        def postText(self):
            return self.getTypedRuleContext(SavingThrowParser.PostTextContext,0)


        def EOF(self):
            return self.getToken(SavingThrowParser.EOF, 0)

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
            self.state = 10
            self.preText()
            self.state = 11
            self.savingThrow()
            self.state = 12
            self.postText()
            self.state = 13
            self.match(SavingThrowParser.EOF)
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

        def DICE(self):
            return self.getToken(SavingThrowParser.DICE, 0)

        def damageType(self):
            return self.getTypedRuleContext(SavingThrowParser.DamageTypeContext,0)


        def COMMA_SPACE(self):
            return self.getToken(SavingThrowParser.COMMA_SPACE, 0)

        def TARGET_TYPE(self):
            return self.getToken(SavingThrowParser.TARGET_TYPE, 0)

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
        self.enterRule(localctx, 2, self.RULE_savingThrow)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.match(SavingThrowParser.T__0)
            self.state = 16
            self.match(SavingThrowParser.NUMBER)
            self.state = 17
            self.match(SavingThrowParser.T__1)
            self.state = 18
            self.match(SavingThrowParser.ABILITY)
            self.state = 19
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.state = 20
                self.match(SavingThrowParser.T__4)
                pass
            elif token in [6]:
                self.state = 21
                self.match(SavingThrowParser.T__5)
                self.state = 22
                self.match(SavingThrowParser.COMMA_SPACE)
                self.state = 23
                _la = self._input.LA(1)
                if not(_la==2 or _la==7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 24
                self.match(SavingThrowParser.TARGET_TYPE)
                self.state = 25
                self.match(SavingThrowParser.T__7)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 28
            self.match(SavingThrowParser.NUMBER)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 29
                self.match(SavingThrowParser.T__1)


            self.state = 32
            self.match(SavingThrowParser.T__8)
            self.state = 33
            self.match(SavingThrowParser.DICE)
            self.state = 34
            self.match(SavingThrowParser.T__9)
            self.state = 35
            self.damageType()
            self.state = 36
            self.match(SavingThrowParser.T__10)
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

        def COMMA_SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(SavingThrowParser.COMMA_SPACE)
            else:
                return self.getToken(SavingThrowParser.COMMA_SPACE, i)

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
        self.enterRule(localctx, 4, self.RULE_damageType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(SavingThrowParser.DAMAGE_TYPE)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12 or _la==17:
                self.state = 44
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 39
                        self.match(SavingThrowParser.COMMA_SPACE)
                        self.state = 40
                        self.match(SavingThrowParser.T__1)
                        self.state = 41
                        self.match(SavingThrowParser.DAMAGE_TYPE) 
                    self.state = 46
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 47
                    self.match(SavingThrowParser.COMMA_SPACE)


                self.state = 50
                self.match(SavingThrowParser.T__11)
                self.state = 51
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
        self.enterRule(localctx, 6, self.RULE_preText)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 54
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==1:
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 57 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
        self.enterRule(localctx, 8, self.RULE_postText)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 59
                    self.matchWildcard()

                else:
                    raise NoViableAltException(self)
                self.state = 62 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





