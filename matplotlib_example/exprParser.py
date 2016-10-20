# Generated from expr.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\r")
        buf.write("&\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\5\2\23\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\7\2!\n\2\f\2\16\2$\13\2\3\2\2\3\2\3")
        buf.write("\2\2\4\3\2\5\6\3\2\7\b,\2\22\3\2\2\2\4\5\b\2\1\2\5\6\7")
        buf.write("\3\2\2\6\7\5\2\2\2\7\b\7\4\2\2\b\23\3\2\2\2\t\n\7\b\2")
        buf.write("\2\n\23\5\2\2\6\13\f\7\13\2\2\f\r\7\3\2\2\r\16\5\2\2\2")
        buf.write("\16\17\7\4\2\2\17\23\3\2\2\2\20\23\7\f\2\2\21\23\7\13")
        buf.write("\2\2\22\4\3\2\2\2\22\t\3\2\2\2\22\13\3\2\2\2\22\20\3\2")
        buf.write("\2\2\22\21\3\2\2\2\23\"\3\2\2\2\24\25\f\n\2\2\25\26\t")
        buf.write("\2\2\2\26!\5\2\2\13\27\30\f\t\2\2\30\31\t\3\2\2\31!\5")
        buf.write("\2\2\n\32\33\f\b\2\2\33\34\7\t\2\2\34!\5\2\2\t\35\36\f")
        buf.write("\7\2\2\36\37\7\n\2\2\37!\5\2\2\b \24\3\2\2\2 \27\3\2\2")
        buf.write("\2 \32\3\2\2\2 \35\3\2\2\2!$\3\2\2\2\" \3\2\2\2\"#\3\2")
        buf.write("\2\2#\3\3\2\2\2$\"\3\2\2\2\5\22 \"")
        return buf.getvalue()


class exprParser ( Parser ):

    grammarFileName = "expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'/'", "'*'", "'+'", "'-'", 
                     "'^'", "'%'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "NUM", "WS" ]

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
    ID=9
    NUM=10
    WS=11

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

        def expr(self):
            return self.getTypedRuleContext(exprParser.ExprContext,0)

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
            self.op = None # Token
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
            self.op = None # Token
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
            self.state = 16
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
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
                self.match(exprParser.T__5)
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
                self.state = 12
                self.match(exprParser.T__1)
                pass

            elif la_ == 4:
                localctx = exprParser.NumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 14
                self.match(exprParser.NUM)
                pass

            elif la_ == 5:
                localctx = exprParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 15
                self.match(exprParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 32
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 30
                    self._errHandler.sync(self);
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = exprParser.MuldivContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 18
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 19
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==exprParser.T__2 or _la==exprParser.T__3):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 20
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = exprParser.AddsubContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 21
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 22
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==exprParser.T__4 or _la==exprParser.T__5):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 23
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = exprParser.ExpoContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 24
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 25
                        self.match(exprParser.T__6)
                        self.state = 26
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = exprParser.ModContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 27
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 28
                        self.match(exprParser.T__7)
                        self.state = 29
                        self.expr(6)
                        pass

             
                self.state = 34
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
         




