from ParserPalindrome import PalindromeParser
from ParserExpression import ExpressionParser

def prompt_input(g_setting):
    print(f'(For #{g_setting}) \nInput string: ', end='')
    inputStr = input()
    return inputStr

def main():
    print("MP2: Syntax and Semantics")
    grammar_setting = None

    while grammar_setting != "3":
        print("\nChoose Parsing:\n[1] Expression Parsing\n[2] Palindrome Parsing\n[3] Exit \n")
        print("Input selection: ", end = "")

        input_string = ""
        grammar_setting = input()

        if grammar_setting == "1":
            print("\nType your string. \nType return to go back.\n")
            while input_string != "return":
                input_string = prompt_input(1)
                if input_string == "return":
                    break

                parser = ExpressionParser(input_string)
                if (parser.start()):
                    print("\nThe string is found in the grammar.\n")
                else:
                    print("\nThe string is NOT found in the grammar.\n")

        elif grammar_setting == "2":
            print("\nType your string. \nType return to go back.\n")
            while input_string != "return":
                input_string = prompt_input(2)
                if input_string == "return":
                    break

                parser = PalindromeParser(input_string)
                if (parser.start()):
                    print("\nThe string is a Palindrome.\n")
                else:
                    print("\nThe string is NOT a Palindrome.\n")

        elif grammar_setting == "3":
            break

        else:
            print("INVALID")

main()
