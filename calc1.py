
INTEGER, PLUS, EOF, MINUS = 'INTEGER', 'PLUS', 'EOF', 'MINUS'

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value
        
    def __str__(self):
        return f'Token ({self.type}, {repr(self.value)})'
    
    
class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None
    
    def error(self):
        raise Exception('Error parsing input')
    
    def get_next_token(self):
        text = self.text
        
        if self.pos > len(text) -1:
            return Token(EOF, None)
        
        while text[self.pos] == ' ':
            self.pos += 1
        
        current_char = text[self.pos]
        
        digit = ''
        while current_char.isdigit():
            digit += current_char
            self.pos += 1
            if self.pos > len(text) -1:
                break
            current_char = text[self.pos]
            
        if digit:
            token = Token(INTEGER, int(digit))
            return token
        
        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token
        
        if current_char == '-':
            token = Token(MINUS, current_char)
            self.pos += 1
            return token
        
        self.error()
        
    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()
    
    def expr(self):
        self.current_token = self.get_next_token()
        
        left = self.current_token
        self.eat(INTEGER)
        
        op = self.current_token
        if self.current_token.type in ['PLUS', 'MINUS']:
            self.eat(self.current_token.type)
        
        right = self.current_token
        self.eat(INTEGER)
        
        if op.type == 'PLUS':
            result = left.value + right.value
        elif op.type == 'MINUS':
            result = left.value - right.value
        else:
            self.error()

        return result

def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()
        