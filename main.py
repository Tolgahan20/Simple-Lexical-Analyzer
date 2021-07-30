import enum #importing enum library
import time

class Tokens(enum.Enum): #Tokens class is created with related attributes
    INTEGER = 'INTEGER'
    FLOAT = 'FLOAT'
    ID = 'ID'
    BITWISE_OR = 'BITWISE_OR'
    LOGICAL_OR = 'LOGICAL_OR'
    BITWISE_AND = 'BITWISE_AND'
    LOGICAL_AND = 'LOGICAL_AND'
    FOR = 'FOR'
    WHILE = 'WHILE'
    IF = 'IF'
    ELSE = 'ELSE'
    ERROR = 'ERROR'


class Node:
    def __init__(self, token, value=None):
        self.token = token
        if value is None:
            self.value = ""
        else:
            self.value = value


words = []
store = []

#reserved words such as for,while,else are stored in list
reservedWords = [Tokens.FOR, Tokens.WHILE, Tokens.IF, Tokens.ELSE] 
exit = True #The program will run until we want

def readfile(): #readfile function is for reading a file from our computer to get the input
    f = open("lab2.txt", "r")
    for x in f:
        for y in x.split(' '):
            words.append(y)



def checkint(n): #function to decide if the input is an integer or not
    try: #try - except blocks are written to prevent unwanted termination of the program
        int(n)
        return True
    except ValueError: #this is the expecting error while checking
        return False


def checkfloat(n): #function to decide if the input is an float or not
    try: #try - except blocks are written to prevent unwanted termination of the program
        float(n)
        return True
    except ValueError: #this is the expected error while checking
        return False


def lex(): #function to find and save the inputs
    for i, x in enumerate(words): 
        if checkint(x): #if the input is integer, the input will be saved as type: integer
            node = Node(Tokens.INTEGER, x)
            store.append(node)
        elif checkfloat(x): #if the input is float, the input will be saved as type: float
            node = Node(Tokens.FLOAT, words[i])
            store.append(node)
        elif words[i] == '&': #if the input is bitwise and, the input and will be saved as type: bitwise and
            node = Node(Tokens.BITWISE_AND)
            store.append(node)
        elif words[i] == '&&': #if the input is logical and, the input and will be saved as type: logical and
            node = Node(Tokens.LOGICAL_AND)
            store.append(node)
        elif words[i] == '|': #if the input is bitwise or, the input or will be saved as type: bitwise or
            node = Node(Tokens.BITWISE_OR)
            store.append(node)
        elif words[i] == '||': #if the input is logical or, the input or will be saved as type: logical or
            node = Node(Tokens.LOGICAL_OR)
            store.append(node)
        elif words[i] == 'for': #if the input is  for, the input will be saved as type: for
            node = Node(Tokens.FOR)
            store.append(node)
        elif words[i] == 'while': #if the input is  while, the input will be saved as type: while
            node = Node(Tokens.WHILE)
            store.append(node)
        elif words[i] == 'if': #if the input is if, the input will be saved as type: if
            node = Node(Tokens.IF)
            store.append(node)
        elif words[i] == 'else': #if the input is else, the input will be saved as type: input
            node = Node(Tokens.ELSE)
            store.append(node)
        elif checkint(x[0]): #if the input is unknown type, the integer will be saved as type: unknown
            node = Node(Tokens.ERROR, words[i])
            store.append(node)
        else: #if the input is in reserved words list, the integer will be saved as type: reservedword
            if words[i] in reservedWords:
                node = Node(Tokens.ID, reservedWords.index(words[i]))
                store.append(node)
            else:
                reservedWords.append(words[i])
                node = Node(Tokens.ID, len(reservedWords) - 1)
                store.append(node)

    x = len(store) #Showing the number of elements read from the file
    print(str(x) + ' Elements Read')


def showtable(): #this is the function to show the table of symbols
    for i, x in enumerate(store):
        if store[i].token == Tokens.INTEGER:   #if the input is an integer, the line below will run
            print('<token=' + store[i].token.value + ', integer_value:' + store[i].value + '>')
        elif store[i].token == Tokens.FLOAT:   #if the input is a float, the line below will run

            print('<token=' + store[i].token.value + ', float_value:' + store[i].value + '>')
        elif store[i].token == Tokens.BITWISE_AND:  #if the input is bitwise and, the line below will run

            print('<token=' + store[i].token.value + '>')
        elif store[i].token == Tokens.LOGICAL_AND:  #if the input is logical and, the line below will run

            print('<token=' + store[i].token.value + '>')
        elif store[i].token == Tokens.BITWISE_OR:   #if the input is bitwise or, the line below will run

            print('<token=' + store[i].token.value + '>')
        elif store[i].token == Tokens.LOGICAL_OR:   #if the input is logical or, the line below will run

            print('<token=' + store[i].token.value + '>')
        elif store[i].token == Tokens.FOR:    #if the input is a reserved word for, the line below will run

            print('<token=' + store[i].token.value + '>')
        elif store[i].token == Tokens.WHILE:  #if the input is a reserved word while, the line below will run

            print('<token=' + store[i].token.value + '>')
        elif store[i].token == Tokens.IF:     #if the input is a reserved word if, the line below will run

            print('<token=' + store[i].token.value + '>')
        elif store[i].token == Tokens.ELSE:   #if the input is a reserved word else, the line below will run

            print('<token=' + store[i].token.value + '>')
        elif store[i].token == Tokens.ERROR:  #if the input is not in a certain type, the line below will run

            print('<token=' + store[i].token.value + ', unrecognised_string=\"' + store[i].value + '\">')
        else:  #if the input is not in any type defined above, the line below will run
            print('<token=' + store[i].token.value + ', index:' + str(store[i].value) + '>')


def showmenu(): #function to show the menu to the user
    readfile() #readfile function is automatically running to read input from the .txt file

    #Creating Menu Interface and Taking input from the menu
    print("""\nMENU: 
    1. Call lex()
    2. Show Symbol Table
    3. Exit""")

    index = input("Choose Your Instuction: ")

    if index == "1": #If the user enters "1", the lex function will run
        print("Lex Function is Running...")
        time.sleep(0.5)
        lex()
    elif index == "2": #If the user enters "2", the showtable function will run
        print("Showing the Table...")
        time.sleep(0.5)
        showtable()
    elif index == "3": #If the user enters "3", the program will terminate
        global exit
        print("The Program is Terminating")
        time.sleep(0.4)
        exit = False #this is where the program terminates
    
    else: #If the user entered an undefined operation, the message will be printed
        print("Invalid Operation!")


while exit: #Program will run until we ask it to stop
    showmenu()
