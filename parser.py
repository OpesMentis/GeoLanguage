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
		self.expect('main')
		self.expect('l_acc')
		while (self.showNext().kind != 'r_acc'):
			self.parseInstruction()
		self.expect('r_acc')

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

	def parseInstruction(self):
		print("Parse instruction")
		if self.showNext().kind in ["pnt", "vect", "line", "seg", "ang", "scal", "string"]:
			self.parseDeclaration()
		#elif self.showNext().kind == 'ident':
			#self.parseAffectation()
		else:
			print ("GOSH! Parsing error for Instruction ligne : ", self.showNext().pos)
			sys.exit(0)

	def parseDeclaration(self):
		print ("Parse declaration")
		if self.showNext().kind == 'pnt':
			self.parseDeclPnt()
		elif self.showNext().kind == 'line':
			self.parseDeclLine()
		elif self.showNext().kind == 'vect':
			self.parseDeclVect()
		elif self.showNext().kind == 'seg':
			self.parseDeclSeg()
		elif self.showNext().kind == 'scal':
			self.parseDeclScal()
		elif self.showNext().kind == 'string':
			self.parseDeclString()
		else:
			print ("GOSH! Parsing error for Declaration ligne : ", self.showNext().pos)
			sys.exit(0)

	def parseDeclPnt(self):
		print ("Parse declaration point")
		self.expect('pnt')
		self.expect('ident')
		if self.showNext().kind != 'excl':
			self.expect('colon')
			self.parseObjPnt()
		self.expect('excl')

	def parseDeclLine(self):
		print ("Parse declaration line")
		self.expect('line')
		self.expect('ident')
		if self.showNext().kind != 'excl':
			self.expect('colon')
			self.parseObjLine()
		self.expect('excl')

	def parseDeclVect(self):
		print ("Parse declaration vector")
		self.expect('vect')
		self.expect('ident')
		if self.showNext().kind != 'excl':
			self.expect('colon')
			self.parseObjVect()
		self.expect('excl')

	def parseDeclSeg(self):
		print ("Parse declaration segment")
		self.expect('seg')
		self.expect('ident')
		if self.showNext().kind != 'excl':
			self.expect('colon')
			self.parseObjSeg()
		self.expect('excl')

	def parseDeclScal(self):
		print ("Parse declaration scalaire")
		self.expect('scal')
		self.expect('ident')
		if self.showNext().kind != 'excl':
			self.expect('colon')
			self.parseObjScal()
		self.expect('excl')

	def parseDeclString(self):
		print ('Parse declaration string')
		self.expect('string')
		self.expect('ident')
		if self.showNext().kind != 'excl':
			self.expect('colon')
			self.parseObjString()
		self.expect('excl')

	def parseInstPnt(self):
		print ('Parse instanciation point')
		self.expect('pnt')
		self.expect('l_par')
		self.parseObjScal()
		self.expect('comma')
		self.parseObjScal()
		self.expect('r_par')

	def parseInstLine(self):
		print ('Parse instanciation ligne')
		self.expect('line')
		self.expect('l_par')
		self.parseObjPnt()
		self.expect('comma')
		self.parseObjPnt()

	def parseInstVect(self):
		print ('Parse instanciation vector')
		self.expect('vect')
		self.expect('l_par')
		self.parseObjScal()
		self.expect('comma')
		self.parseObjScal()
		self.expect('r_par')

	def parseInstSeg(self):
		print ('Parse instanciation segment')
		self.expect('seg')
		self.expect('l_par')
		self.parseObjPnt()
		self.expect('comma')
		self.parseObjPnt()
		self.expect('r_par')

	def parseObjPnt(self):
		print ('Parse objet point')
		if self.showNext().kind == 'pnt':
			self.parseInstPnt()
		elif self.showNext().kind == 'ident':
			self.expect('ident')
		else:
			print ("GOSH! Parsing error for ObjPoint ligne : ", self.showNext().pos)
			sys.exit(0)

	def parseObjLine(self):
		print ('Parse objet line')
		if self.showNext().kind == 'line':
			self.parseInstLine()
		elif self.showNext().kind == 'ident':
			self.expect('ident')
		else:
			print ("GOSH! Parsing error for ObjLine ligne : ", self.showNext().pos)
			sys.exit(0)

	def parseObjVect(self):
		print ('Parse objet vector')
		if self.showNext().kind == 'vect':
			self.parseInstVect()
		elif self.showNext().kind == 'ident':
			self.expect('ident')
		else:
			print ("GOSH! Parsing error for ObjVect ligne : ", self.showNext().pos)
			sys.exit(0)

	def parseObjSeg(self):
		print ('Parse objet segment')
		if self.showNext().kind == 'seg':
			self.parseInstSeg()
		elif self.showNext().kind == 'ident':
			self.expect('ident')
		else:
			print ("GOSH! Parsing error for ObjSeg ligne : ", self.showNext().pos)
			sys.exit(0)

	def parseObjScal(self):
		print('Parse objet scalaire')
		if self.showNext().kind == 'ident':
			self.acceptIt()
		elif self.showNext().kind in ['minus', 'plus', 'l_par', 'nb']:
			self.parseOperation()
		else:
			print ("GOSH! Parsing error for ObjScal ligne : ", self.showNext().pos)
			sys.exit(0)

	def parseObjString(self):
		print('Parse objet string')
		if self.showNext().kind == 'ch':
			self.expect('ch')
		elif self.showNext().kind == 'ident':
			self.expect('ident')
		else:
			print ("GOSH! Parsing error for ObjString ligne : ", self.showNext().pos)
			sys.exit(0)

	def parseOperation(self):
		print ("Parse operation")
		self.parseTerm()
		while (self.showNext().kind in ['minus', 'plus']):
			self.acceptIt()
			self.parseTerm()

	def parseTerm(self):
		print ('Parse term')
		self.parseFactor()
		while (self.showNext().kind in ['multi', 'divi', 'mod', 'pow']):
			self.acceptIt()
			self.parseFactor()

	def parseFactor(self):
		print ('Parse factor')
		if self.showNext().kind == 'minus':
			self.acceptIt()
		self.parsePrimary()

	def parsePrimary(self):
		print ('Parse primary')
		if self.showNext().kind == 'ident':
			self.acceptIt()
		elif self.showNext().kind == 'nb':
			self.acceptIt()
		elif self.showNext().kind == 'l_par':
			self.acceptIt()
			self.parseOperation()
			self.expect('r_par')

if __name__ == '__main__':
    parser = Parser()
    parser.parsePrgm(sys.argv[1])
