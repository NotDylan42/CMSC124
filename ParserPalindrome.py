class PalindromeParser:
    def __init__(self, strLine:str) -> None:
        self.__strLine = strLine.replace(" ","").lower()
        self.__strLineRev = self.__strLine[::-1]
        self.__currentChar = None
        self.__currentPosition = -1
        self.__isError = False
        self.next_Char()

    def match(self, char):
        return self.__currentChar == char

    def next_Char(self):
        self.__currentPosition += 1

        if self.__currentPosition >= len(self.__strLine):
            self.__currentChar = '$'
        else:
            self.__currentChar = self.__strLine[self.__currentPosition]    

    def curr_expression(self):
        if self.__currentChar.isalpha() and self.match(self.__strLineRev[self.__currentPosition]):
            self.next_Char()
            self.curr_expression()

    def start(self):
        self.curr_expression()

        if not self.match('$') or (self.match('$') and self.__currentPosition < len(self.__strLine)-1):
            self.__isError = True

        return (True if not self.__isError else False)
