all: matplotlib_example/design.py matplotlib_example/testmodal.py matplotlib_example/exprLexer.py matplotlib_example/exprParser.py matplotlib_example/exprVisitor.py matplotlib_example/__main__.py
	python -m matplotlib_example

matplotlib_example/expr%.py: data/expr.g4
	cd data && antlr4 -Dlanguage=Python3 -visitor -no-listener expr.g4 -o ../matplotlib_example

matplotlib_example/%.py: data/%.ui
	cd data && python -m PyQt5.uic.pyuic $*.ui -o ../matplotlib_example/$*.py

clean:
	rm -rf matplotlib_example/design.py matplotlib_example/testmodal.py matplotlib_example/expr*.py matplotlib_example/*tokens matplotlib_example/__pycache__ matplotlib_example/*.pyc
