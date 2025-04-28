# Generated from grammars/Roll.g4 by ANTLR 4.13.2
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
        4,1,5,24,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,3,0,10,8,0,1,0,1,0,
        1,0,3,0,15,8,0,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,0,0,4,0,2,4,6,0,1,
        1,0,2,3,21,0,9,1,0,0,0,2,16,1,0,0,0,4,18,1,0,0,0,6,20,1,0,0,0,8,
        10,3,2,1,0,9,8,1,0,0,0,9,10,1,0,0,0,10,11,1,0,0,0,11,12,5,1,0,0,
        12,14,3,4,2,0,13,15,3,6,3,0,14,13,1,0,0,0,14,15,1,0,0,0,15,1,1,0,
        0,0,16,17,5,4,0,0,17,3,1,0,0,0,18,19,5,4,0,0,19,5,1,0,0,0,20,21,
        7,0,0,0,21,22,5,4,0,0,22,7,1,0,0,0,2,9,14
    ]

class RollParser ( Parser ):

    grammarFileName = "Roll.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'d'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUMBER", "WHITESPACE" ]

    RULE_roll = 0
    RULE_count = 1
    RULE_sides = 2
    RULE_modifier = 3

    ruleNames =  [ "roll", "count", "sides", "modifier" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    NUMBER=4
    WHITESPACE=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RollContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sides(self):
            return self.getTypedRuleContext(RollParser.SidesContext,0)


        def count(self):
            return self.getTypedRuleContext(RollParser.CountContext,0)


        def modifier(self):
            return self.getTypedRuleContext(RollParser.ModifierContext,0)


        def getRuleIndex(self):
            return RollParser.RULE_roll

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoll" ):
                listener.enterRoll(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoll" ):
                listener.exitRoll(self)




    def roll(self):

        localctx = RollParser.RollContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_roll)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 8
                self.count()


            self.state = 11
            self.match(RollParser.T__0)
            self.state = 12
            self.sides()
            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2 or _la==3:
                self.state = 13
                self.modifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CountContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(RollParser.NUMBER, 0)

        def getRuleIndex(self):
            return RollParser.RULE_count

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCount" ):
                listener.enterCount(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCount" ):
                listener.exitCount(self)




    def count(self):

        localctx = RollParser.CountContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_count)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(RollParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SidesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(RollParser.NUMBER, 0)

        def getRuleIndex(self):
            return RollParser.RULE_sides

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSides" ):
                listener.enterSides(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSides" ):
                listener.exitSides(self)




    def sides(self):

        localctx = RollParser.SidesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sides)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(RollParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(RollParser.NUMBER, 0)

        def getRuleIndex(self):
            return RollParser.RULE_modifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModifier" ):
                listener.enterModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModifier" ):
                listener.exitModifier(self)




    def modifier(self):

        localctx = RollParser.ModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_modifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 21
            self.match(RollParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





