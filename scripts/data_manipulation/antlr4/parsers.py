import sys
from antlr4 import *

from .AttackLexer import AttackLexer
from .AttackParser import AttackParser
from .AttackActionListener import AttackActionListener
from .RollLexer import RollLexer
from .RollParser import RollParser
from .DamageDiceListener import DamageDiceListener
from .SavingThrowLexer import SavingThrowLexer
from .SavingThrowParser import SavingThrowParser
from .ForcedSavingThrowListener import ForcedSavingThrowListener

def buildCsvHeader():
    return AttackActionListener.buildCsvHeader()

def parseAttack(desc):
    stream = InputStream(desc)
    lexer = AttackLexer(stream)
    stream = CommonTokenStream(lexer)
    parser = AttackParser(stream)
    tree = parser.attack()

    listener = AttackActionListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    
    if listener.result['2014'] or listener.result['2024']:
        return listener.result
    else:
        return None

def parseSavingThrow(desc):
    stream = InputStream(desc)
    lexer = SavingThrowLexer(stream)
    stream = CommonTokenStream(lexer)
    parser = SavingThrowParser(stream)
    tree = parser.forcedSavingThrow()

    listener = ForcedSavingThrowListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    if listener.result['damageAverage'] is not None:
        return listener.result
    else:
        return None

def parseDice(text):
    stream = InputStream(text)
    lexer = RollLexer(stream)
    stream = CommonTokenStream(lexer)
    parser = RollParser(stream)
    tree = parser.roll()

    listener = DamageDiceListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return listener.result

def main(argv):

    print(AttackActionListener.buildCsvHeader())
    with open(argv[1]) as fp:
        for line in fp:
            parsed = parseAttack(line)
            print(parsed)

if __name__ == '__main__':
    main(sys.argv)