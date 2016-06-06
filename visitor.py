from ast import *

class Visitor:

    def __init__(self, pp):
        self.pp = pp
        self.indentation = 0

    def indent(self):
        self.indentation += 2

    def desindent(self):
        self.indentation -= 2

    def doIt(self, ast):
        print("+++ VISITOR +++")
        self.visitRacine(ast, None)

    # fonction pour afficher dans le terminal
    def say(self, txt):
        print " " * self.indentation + txt
