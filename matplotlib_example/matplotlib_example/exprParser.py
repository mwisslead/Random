# Generated from expr.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\16")
        buf.write("\63\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\7\2\21\n\2\f\2\16\2\24\13\2\3\2\3\2\3\2\3\2\5\2")
        buf.write("\32\n\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\"\n\2\3\2\3\2\3\2")
        buf.write("\3\2\5\2(\n\2\3\2\3\2\3\2\3\2\7\2.\n\2\f\2\16\2\61\13")
        buf.write("\2\3\2\2\3\2\3\2\2\2<\2\31\3\2\2\2\4\5\b\2\1\2\5\6\7\3")
        buf.write("\2\2\6\7\5\2\2\2\7\b\7\4\2\2\b\32\3\2\2\2\t\n\7\t\2\2")
        buf.write("\n\32\5\2\2\6\13\f\7\f\2\2\f\r\7\3\2\2\r\22\5\2\2\2\16")
        buf.write("\17\7\13\2\2\17\21\5\2\2\2\20\16\3\2\2\2\21\24\3\2\2\2")
        buf.write("\22\20\3\2\2\2\22\23\3\2\2\2\23\25\3\2\2\2\24\22\3\2\2")
        buf.write("\2\25\26\7\4\2\2\26\32\3\2\2\2\27\32\7\r\2\2\30\32\7\f")
        buf.write("\2\2\31\4\3\2\2\2\31\t\3\2\2\2\31\13\3\2\2\2\31\27\3\2")
        buf.write("\2\2\31\30\3\2\2\2\32/\3\2\2\2\33\34\f\n\2\2\34\35\7\5")
        buf.write("\2\2\35.\5\2\2\n\36!\f\t\2\2\37\"\7\6\2\2 \"\7\7\2\2!")
        buf.write("\37\3\2\2\2! \3\2\2\2\"#\3\2\2\2#.\5\2\2\n$\'\f\b\2\2")
        buf.write("%(\7\b\2\2&(\7\t\2\2\'%\3\2\2\2\'&\3\2\2\2()\3\2\2\2)")
        buf.write(".\5\2\2\t*+\f\7\2\2+,\7\n\2\2,.\5\2\2\b-\33\3\2\2\2-\36")
        buf.write("\3\2\2\2-$\3\2\2\2-*\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/\60")
        buf.write("\3\2\2\2\60\3\3\2\2\2\61/\3\2\2\2\b\22\31!\'-/")
        return buf.getvalue()


class exprParser ( Parser ):

    grammarFileName = "expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'^'", "'*'", "'/'", "'+'", 
                     "'-'", "'%'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "NUM", "WS" ]

    RULE_expr = 0

    ruleNames =  [ "expr" ]

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
    ID=10
    NUM=11
    WS=12

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(exprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub" ):
                return visitor.visitSub(self)
            else:
                return visitor.visitChildren(self)


    class ModContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMod" ):
                return visitor.visitMod(self)
            else:
                return visitor.visitChildren(self)


    class FuncContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.funcname = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprParser.ExprContext,i)

        def ID(self):
            return self.getToken(exprParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)


    class NegateContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(exprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegate" ):
                return visitor.visitNegate(self)
            else:
                return visitor.visitChildren(self)


    class NumContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(exprParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)


    class AddsubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.ADD = None # Token
            self.MINUS = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddsub" ):
                return visitor.visitAddsub(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(exprParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class ExpoContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpo" ):
                return visitor.visitExpo(self)
            else:
                return visitor.visitChildren(self)


    class MuldivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.MUL = None # Token
            self.DIV = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMuldiv" ):
                return visitor.visitMuldiv(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = exprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = exprParser.SubContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 3
                self.match(exprParser.T__0)
                self.state = 4
                self.expr(0)
                self.state = 5
                self.match(exprParser.T__1)
                pass

            elif la_ == 2:
                localctx = exprParser.NegateContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 7
                self.match(exprParser.T__6)
                self.state = 8
                self.expr(4)
                pass

            elif la_ == 3:
                localctx = exprParser.FuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                localctx.funcname = self.match(exprParser.ID)
                self.state = 10
                self.match(exprParser.T__0)
                self.state = 11
                self.expr(0)
                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==exprParser.T__8:
                    self.state = 12
                    self.match(exprParser.T__8)
                    self.state = 13
                    self.expr(0)
                    self.state = 18
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 19
                self.match(exprParser.T__1)
                pass

            elif la_ == 4:
                localctx = exprParser.NumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 21
                self.match(exprParser.NUM)
                pass

            elif la_ == 5:
                localctx = exprParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                self.match(exprParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 45
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 43
                    self._errHandler.sync(self);
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = exprParser.ExpoContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 25
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 26
                        self.match(exprParser.T__2)
                        self.state = 27
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = exprParser.MuldivContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 28
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 31
                        token = self._input.LA(1)
                        if token in [exprParser.T__3]:
                            self.state = 29
                            localctx.MUL = self.match(exprParser.T__3)

                        elif token in [exprParser.T__4]:
                            self.state = 30
                            localctx.DIV = self.match(exprParser.T__4)

                        else:
                            raise NoViableAltException(self)

                        self.state = 33
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = exprParser.AddsubContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 37
                        token = self._input.LA(1)
                        if token in [exprParser.T__5]:
                            self.state = 35
                            localctx.ADD = self.match(exprParser.T__5)

                        elif token in [exprParser.T__6]:
                            self.state = 36
                            localctx.MINUS = self.match(exprParser.T__6)

                        else:
                            raise NoViableAltException(self)

                        self.state = 39
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = exprParser.ModContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 40
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 41
                        self.match(exprParser.T__7)
                        self.state = 42
                        self.expr(6)
                        pass

             
                self.state = 47
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         




