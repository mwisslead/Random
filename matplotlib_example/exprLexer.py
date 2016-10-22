# Generated from expr.g4 by ANTLR 4.5.3
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\16")
        buf.write("K\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3")
        buf.write("\t\3\t\3\n\3\n\3\13\3\13\7\13\60\n\13\f\13\16\13\63\13")
        buf.write("\13\3\f\7\f\66\n\f\f\f\16\f9\13\f\3\f\3\f\6\f=\n\f\r\f")
        buf.write("\16\f>\3\f\6\fB\n\f\r\f\16\fC\5\fF\n\f\3\r\3\r\3\r\3\r")
        buf.write("\2\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\31\16\3\2\6\4\2C\\c|\5\2\62;C\\c|\3\2\62;\4\2\13")
        buf.write("\13\"\"O\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3")
        buf.write("\33\3\2\2\2\5\35\3\2\2\2\7\37\3\2\2\2\t!\3\2\2\2\13#\3")
        buf.write("\2\2\2\r%\3\2\2\2\17\'\3\2\2\2\21)\3\2\2\2\23+\3\2\2\2")
        buf.write("\25-\3\2\2\2\27E\3\2\2\2\31G\3\2\2\2\33\34\7*\2\2\34\4")
        buf.write("\3\2\2\2\35\36\7+\2\2\36\6\3\2\2\2\37 \7`\2\2 \b\3\2\2")
        buf.write("\2!\"\7,\2\2\"\n\3\2\2\2#$\7\61\2\2$\f\3\2\2\2%&\7-\2")
        buf.write("\2&\16\3\2\2\2\'(\7/\2\2(\20\3\2\2\2)*\7\'\2\2*\22\3\2")
        buf.write("\2\2+,\7.\2\2,\24\3\2\2\2-\61\t\2\2\2.\60\t\3\2\2/.\3")
        buf.write("\2\2\2\60\63\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\26\3")
        buf.write("\2\2\2\63\61\3\2\2\2\64\66\t\4\2\2\65\64\3\2\2\2\669\3")
        buf.write("\2\2\2\67\65\3\2\2\2\678\3\2\2\28:\3\2\2\29\67\3\2\2\2")
        buf.write(":<\7\60\2\2;=\t\4\2\2<;\3\2\2\2=>\3\2\2\2><\3\2\2\2>?")
        buf.write("\3\2\2\2?F\3\2\2\2@B\t\4\2\2A@\3\2\2\2BC\3\2\2\2CA\3\2")
        buf.write("\2\2CD\3\2\2\2DF\3\2\2\2E\67\3\2\2\2EA\3\2\2\2F\30\3\2")
        buf.write("\2\2GH\t\5\2\2HI\3\2\2\2IJ\b\r\2\2J\32\3\2\2\2\b\2\61")
        buf.write("\67>CE\3\b\2\2")
        return buf.getvalue()


class exprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    ID = 10
    NUM = 11
    WS = 12

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'^'", "'*'", "'/'", "'+'", "'-'", "'%'", "','" ]

    symbolicNames = [ "<INVALID>",
            "ID", "NUM", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "ID", "NUM", "WS" ]

    grammarFileName = "expr.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


