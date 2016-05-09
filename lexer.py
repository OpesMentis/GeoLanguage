import sys
import re

class Token:
    def __init__(self,kind,value,pos):
        self.kind=kind
        self.value=value
        self.pos=pos

class Lexer:
    def __init__(self):
        self.stream = []

    def getStream(self):
        return self.stream

    def setStream(self, val):
        self.stream.append(val)

    def lex(self, lines, token_exprs):
        tokens = []
        ligne = 0
        for characters in lines:
            pos = 0
            ligne += 1
            while pos < len(characters):
                match = None
                for token_expr in token_exprs:
                    pattern, tag = token_expr
                    regex = re.compile(pattern)
                    match = regex.match(characters, pos)
                    if match:
                        text = match.group(0)
                        if tag:
                            token = Token(tag, text, [ligne, pos])
                            tokens = tokens + [token]
                        break
                if not match:
                    print("Illegal character ligne ", ligne,"apres le charactere -", text,"- ( pos",pos,")\n")
                    sys.exit(1)
                else:
                    pos = match.end(0)
        return tokens



    def imp_lex(self, characters):

        token_exprs = [
                (r'[ \n\t]+',               None),
                (r'\{',		               'l_acc'),
                (r'\}',		               'r_acc'),
				(r'\".*\"',                'string'),
                (r'\(',                    'l_par'),
                (r'\)',                    'r_par'),
				(r'\.',                    'dot'),
                (r'\:',                     'colon'),
                (r',',                     'comma'),
                (r'\+',                    'plus'),
                (r'-',                     'minus'),
                (r'\*',                    'multi'),
                (r'/',                     'divi'),
                (r'=',                     'equal'),
                (r'\"',		               'quote'),
				(r'Pnt',                   'pnt'),
				(r'Line',                  'line'),
				(r'Seg',                   'seg'),
				(r'Vect',                  'vect'),
				(r'Ang',                   'ang'),
				(r'print',                 'print'),
				(r'drawnow',               'draw'),
				(r'ext1',                  'attr_pt1'),
                (r'ext2',                  'attr_pt2'),
                (r'x',                     'attr_x'),
                (r'y',                     'attr_y'),
                (r'mes',                   'att_mes'),
                (r'[0-9]+(\.[0-9]+)?',     'scal'),
                (r'[A-Za-z][A-Za-z0-9_]*', 'ident'),
            ]


        return self.lex(characters, token_exprs)

    def tokenize(self, characters):
        print("+++ LEXER +++")
        tokens = self.imp_lex(characters)
        for token in tokens:
            self.stream.append(token)
        for i in self.stream:
            print(i.value, i.kind)
        self.stream = self.stream[::-1]
        return self.stream

    def getNext(self):
        return self.stream.pop()

    def showNext(self):
        return self.stream[-1]

    def lookahead(self, k):
        return self.stream[k]

    def getKind(self):
        return self.stream[1]


if __name__ == '__main__':
    lexer = Lexer()
    filename = sys.argv[1]
    f = open(filename)
    ch = f.readlines()
    f.close()
    lexer.tokenize(ch)
