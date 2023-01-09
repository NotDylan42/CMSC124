class ExpressionParser:
    def __init__(self, strLine) -> None:
        self.__strLine = strLine.replace(" ","")
        self.__currentChar = None
        self.__currentPosition = -1
        self.__isError = False
        self.next_char()

    def match(self, char):
        return self.__currentChar == char

    def next_char(self):
        self.__currentPosition += 1

        if self.__currentPosition >= len(self.__strLine):
            self.__currentChar = '$'
        else:
            self.__currentChar = self.__strLine[self.__currentPosition]

    def curr_expression(self):
        if self.match('('):
            self.next_char()
            self.curr_expression()
            if self.match(')'):
                self.next_char()
            else:
                self.__isError = True
            self.prime_expression()

        elif self.match('~'):
            self.next_char()
            self.curr_expression()
            self.prime_expression()

        elif self.__currentChar in ['x','y','z']:
            self.next_char()
            self.prime_expression()

        else:
            self.__isError = True

    def start(self):
        self.curr_expression()

        if not self.match('$') or (self.match('$') and self.__currentPosition < len(self.__strLine)-1):
            self.__isError = True

        return (True if not self.__isError else False)


    def prime_expression(self):
        if self.__currentChar in ['+','-']:
            self.next_char()
            self.curr_expression()
            self.prime_expression()

        else:
            pass
