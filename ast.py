from visitor import Visitor

class AST:
    def __init__(self,name): #constructeur
        self.name = name

    def accept(self, visitor, arg):
        nom = self.__class__.__name__
        nomMethode = getattr(visitor, "visit" + nom)
        nomMethode(self, arg)

class Racine(AST):
    def __init__(self):
        self.includes = []
        self.raccourcis = []
        self.main = []

    def __str__(self):
    	print("+++ AST +++")
        string = "Ast"
        for include in self.includes :
        	string = string + "\n {0}".format(include)
        for raccourci in self.raccourcis :
        	string = string + "\n {0}".format(raccourci)
        string = string + "\n {0}".format(self.main)
        return string

class Prgm(AST):
    def __init__(self):
        self.instruct = []

class Declaration(AST):
    def __init__(self):
        self.type = None
