# Generated from expr.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .exprParser import exprParser
else:
    from exprParser import exprParser

# This class defines a complete generic visitor for a parse tree produced by exprParser.

class exprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by exprParser#sub.
    def visitSub(self, ctx:exprParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#mod.
    def visitMod(self, ctx:exprParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#func.
    def visitFunc(self, ctx:exprParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#negate.
    def visitNegate(self, ctx:exprParser.NegateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#num.
    def visitNum(self, ctx:exprParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#addsub.
    def visitAddsub(self, ctx:exprParser.AddsubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#id.
    def visitId(self, ctx:exprParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#expo.
    def visitExpo(self, ctx:exprParser.ExpoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#muldiv.
    def visitMuldiv(self, ctx:exprParser.MuldivContext):
        return self.visitChildren(ctx)



del exprParser