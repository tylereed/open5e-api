import sys
from antlr4 import *
from .AttackLexer import AttackLexer
from .AttackParser import AttackParser
from .AttackActionListener import AttackActionListener

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
    
    if listener.result['isWeapon'] or listener.result['isSpell']:
        return listener.buildCsv()
    else:
        return None

def main(argv):

    print(AttackActionListener.buildCsvHeader())
    with open(argv[1]) as fp:
        for line in fp:
            parsed = parseAttack(line)
            print(parsed)

if __name__ == '__main__':
    main(sys.argv)