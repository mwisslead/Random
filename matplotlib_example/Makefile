all: design.py testmodal.py exprLexer.py exprParser.py exprVisitor.py __main__.py
	python __main__.py

expr%.py: expr.g4
	antlr4 -Dlanguage=Python3 -visitor -no-listener $^

%.py: %.ui
	python -m PyQt5.uic.pyuic $*.ui -o $*.py

clean:
	rm -rf design.py testmodal.py expr*.py expr.tokens exprLexer.tokens __pycache__
