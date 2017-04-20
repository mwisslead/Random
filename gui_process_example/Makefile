all: gui_process/design.py  gui_process/__main__.py
	python -m gui_process

gui_process/%.py: resources/%.ui
	cd resources && python -m PyQt5.uic.pyuic $*.ui -o ../gui_process/$*.py

clean:
	rm -rf gui_process/design.py gui_process/__pycache__ gui_process/*.pyc build dist gui_process.egg-info
