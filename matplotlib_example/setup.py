import sys

from setuptools import setup

NAME='matplotlib_example'
VERSION='0.0.0'

ANTLR4='antlr4-python{}-runtime'.format(sys.version_info[0])

setup(
    name=NAME,
    version=VERSION,
    packages=[NAME],
    install_requires=['matplotlib', 'numpy', 'PyQt5', ANTLR4]
)
