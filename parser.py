from lexer import Lexer
import sys

class Parser:
	def __init__(self):
		self.lexer = Lexer()

	def getLexer(self):
		return self.lexer

	def setLexer(self, val):
		self.lexer = val

	def parsePrgm(self, filename):
		f = open(filename)
		ch = f.readlines()
		self.lexer.tokenize(ch)

		print("+++ PARSER +++")
		while True:
			self.parseInst()

	def expect(self, token_kind):
		next_tok = self.lexer.getNext()
		if next_tok.kind != token_kind:
			print("\nParsing error on line {0} pos {1}".format(next_tok.pos[0], next_tok.pos[1]))
			print("Expecting "+token_kind+", got "+next_tok.kind)
			sys.exit(1)
		return next_tok

	def showNext(self):
		return self.lexer.showNext()

	def acceptIt(self):
		token = self.lexer.getNext()
		return token

	def parseInstPoint(self):
		print ("Parse instanciation point")
		self.expect('pnt')
		self.expect('l_par')
		self.expect('scal')
		self.expect('comma')
		self.expect('scal')
		self.expect('r_par')

	def parseInstLine(self):
		print ("Parse instanciation line")
		self.expect('line')
		self.expect('l_par')
		if self.showNext().kind == 'ident':
			acceptIt()
		elif self.showNext().kind == 'pnt':
			parseInstPoint()
		else:
			 raise ("Parsing error for InstLine ligne : ", self.showNext().pos)
		self.expect('comma')
		if self.showNext().kind == 'ident':
			acceptIt()
		elif self.showNext().kind == 'pnt':
			self.parseInstPoint()
		elif self.showNext().kind == 'vect':
			self.parseInstVector()
		else:
			 raise ("Parsing error for InstLine ligne : ", self.showNext().pos)
		self.expect('r_par')

	def parseInstVector(self):
		print ("Parse instanciation vector")
		self.expect('vect')
		self.expect('l_par')
		self.expect('scal')
		self.expect('comma')
		self.expect('scal')
		self.expect('r_par')

	def parseString(self):
		print ("Parse string")
		self.expect('string')

	def parseScal(self):
		print ("Parse scalar")
		self.expect('scal')

	def parseInst(self):
		print ("Parse instanciation")
		self.expect('ident')
		self.expect('colon')
		if self.showNext().kind == 'pnt':
			self.parseInstPoint()
		elif self.showNext().kind == 'line':
			self.parseInstLine()
		elif self.showNext().kind == 'vect':
			self.parseInstVector()
		elif self.showNext().kind == 'quote':
			self.parseString()
		elif self.showNext().kind == 'scal':
			self.parseScal()
		else:
			raise ("Parsing error for Inst ligne : ", self.showNext().pos)

if __name__ == '__main__':
    parser = Parser()
    parser.parsePrgm(sys.argv[1])
