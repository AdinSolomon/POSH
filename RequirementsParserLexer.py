# Generated from RequirementsParser.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\6\r\\\n\r\r\r")
        buf.write("\16\r]\3\r\3\r\3\16\3\16\3\16\3\16\2\2\17\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\3")
        buf.write("\2\6\3\2C\\\3\2\62;\4\2KKVV\5\2\13\f\17\17\"\"\2e\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\3\35\3\2\2\2\5\37\3\2\2\2\7!\3\2\2\2\t%\3\2\2\2\13\'")
        buf.write("\3\2\2\2\r*\3\2\2\2\17\66\3\2\2\2\218\3\2\2\2\23:\3\2")
        buf.write("\2\2\25<\3\2\2\2\27>\3\2\2\2\31[\3\2\2\2\33a\3\2\2\2\35")
        buf.write("\36\7*\2\2\36\4\3\2\2\2\37 \7+\2\2 \6\3\2\2\2!\"\7c\2")
        buf.write("\2\"#\7p\2\2#$\7f\2\2$\b\3\2\2\2%&\7.\2\2&\n\3\2\2\2\'")
        buf.write("(\7q\2\2()\7t\2\2)\f\3\2\2\2*+\7]\2\2+,\7O\2\2,-\7k\2")
        buf.write("\2-.\7p\2\2./\7\"\2\2/\60\7I\2\2\60\61\7t\2\2\61\62\7")
        buf.write("c\2\2\62\63\7f\2\2\63\64\7g\2\2\64\65\7<\2\2\65\16\3\2")
        buf.write("\2\2\66\67\7_\2\2\67\20\3\2\2\289\t\2\2\29\22\3\2\2\2")
        buf.write(":;\t\3\2\2;\24\3\2\2\2<=\t\4\2\2=\26\3\2\2\2>?\7*\2\2")
        buf.write("?@\7E\2\2@A\7c\2\2AB\7p\2\2BC\7\"\2\2CD\7d\2\2DE\7g\2")
        buf.write("\2EF\7\"\2\2FG\7v\2\2GH\7c\2\2HI\7m\2\2IJ\7g\2\2JK\7p")
        buf.write("\2\2KL\7\"\2\2LM\7E\2\2MN\7q\2\2NO\7p\2\2OP\7e\2\2PQ\7")
        buf.write("w\2\2QR\7t\2\2RS\7t\2\2ST\7g\2\2TU\7p\2\2UV\7v\2\2VW\7")
        buf.write("n\2\2WX\7{\2\2XY\7+\2\2Y\30\3\2\2\2Z\\\t\5\2\2[Z\3\2\2")
        buf.write("\2\\]\3\2\2\2][\3\2\2\2]^\3\2\2\2^_\3\2\2\2_`\b\r\2\2")
        buf.write("`\32\3\2\2\2ab\7\2\2\3bc\3\2\2\2cd\b\16\2\2d\34\3\2\2")
        buf.write("\2\4\2]\3\b\2\2")
        return buf.getvalue()


class RequirementsParserLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    LETTER = 8
    DIGIT = 9
    SPECIAL_DIGIT = 10
    CONCURRENCY = 11
    WHITESPACE = 12
    END_OF_FILE = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'and'", "','", "'or'", "'[Min Grade:'", "']'", 
            "'(Can be taken Concurrently)'" ]

    symbolicNames = [ "<INVALID>",
            "LETTER", "DIGIT", "SPECIAL_DIGIT", "CONCURRENCY", "WHITESPACE", 
            "END_OF_FILE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "LETTER", "DIGIT", "SPECIAL_DIGIT", "CONCURRENCY", "WHITESPACE", 
                  "END_OF_FILE" ]

    grammarFileName = "RequirementsParser.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


