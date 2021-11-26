class DFA_state:
    action = ""
    newState = 0
    def __init__(self, action = "", newState = 0):
        self.action = action
        self.newState = newState

'''                                     Transition table
                                        each element is an object of class DFA_state so we can have action and newstate combined in one table
                                        table is padded so we index from 1 not zero E.g transitionTable[0][] is empty and transtitionTable[x][0] is also empty'''
transitionTable = [
                    [],
                    [[],DFA_state("move",17), DFA_state("move",17), DFA_state("move",2), DFA_state("move",10), DFA_state("move",6), DFA_state("move",7),DFA_state("move",8),DFA_state("move",9),DFA_state("move",11),DFA_state("stuck",0),DFA_state("move",13),DFA_state("move",14),DFA_state("move",16),DFA_state("stuck",0)],
                    [[],DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("move",3), DFA_state("move",4), DFA_state("recognize",0), DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0)],
                    [[],DFA_state("move",3), DFA_state("move",18), DFA_state("move",3), DFA_state("move",3), DFA_state("move",3), DFA_state("move",3),DFA_state("move",3),DFA_state("move",3),DFA_state("move",3),DFA_state("move",3),DFA_state("move",3),DFA_state("move",3),DFA_state("move",16),DFA_state("move",3)],
                    [[],DFA_state("move",4), DFA_state("move",4), DFA_state("move",4), DFA_state("move",5), DFA_state("move",4), DFA_state("move",4),DFA_state("move",4),DFA_state("move",4),DFA_state("move",4),DFA_state("move",4),DFA_state("move",4),DFA_state("move",4),DFA_state("move",4),DFA_state("move",4)],
                    [[],DFA_state("move",4), DFA_state("move",4), DFA_state("move",18), DFA_state("move",5), DFA_state("move",4), DFA_state("move",4),DFA_state("move",4),DFA_state("move",4),DFA_state("move",4),DFA_state("move",4),DFA_state("move",4),DFA_state("move",4),DFA_state("move",4),DFA_state("move",4)],
                    [[],DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0)],
                    [[],DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0)],
                    [[],DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0)],
                    [[],DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0)],
                    [[],DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0)],
                    [[],DFA_state("stuck",0), DFA_state("stuck",0), DFA_state("stuck",0), DFA_state("stuck",0), DFA_state("stuck",0), DFA_state("stuck",0),DFA_state("stuck",0),DFA_state("stuck",0),DFA_state("stuck",0),DFA_state("move",12),DFA_state("stuck",0),DFA_state("stuck",0),DFA_state("stuck",0),DFA_state("stuck",0)],
                    [[],DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0)],
                    [[],DFA_state("stuck",0), DFA_state("stuck",0), DFA_state("stuck",0), DFA_state("stuck",0), DFA_state("stuck",0), DFA_state("stuck",0),DFA_state("stuck",0),DFA_state("stuck",0),DFA_state("stuck",0),DFA_state("stuck",0),DFA_state("stuck",0),DFA_state("move",15),DFA_state("stuck",0),DFA_state("stuck",0)],
                    [[],DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("move",15),DFA_state("move",14),DFA_state("recognize",0),DFA_state("recognize",0)],
                    [[],DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("move",15),DFA_state("recognize",0),DFA_state("recognize",0)],
                    [[],DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("move",16),DFA_state("move",16),DFA_state("recognize",0)],
                    [[],DFA_state("move",17), DFA_state("move",17), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0)],
                    [[],DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0)]
                    ]

tokenTable = {
    1: 'error',
    2: 'div',
    3: 'error',
    4: 'error',
    5: 'error',
    6: 'lparen',
    7: 'rparen',
    8: 'plus',
    9: 'minus',
    10: 'times',
    11: 'error',
    12: 'assign',
    13: 'error',
    14: 'number',
    15: 'number',
    16: 'identifier',
    17: 'whitespace',
    18: 'comment'
}

def charState(c):                       # pass in character returns 1-14 representing char state
    if c == '\t' or c == ' ':
        return 1
    elif c == '\n':
        return 2
    elif c == '/':
        return 3
    elif c == '*':
        return 4
    elif c == '(':
        return 5
    elif c == ')':
        return 6
    elif c == '+':
        return 7
    elif c == '-':
        return 8
    elif c == ':':
        return 9
    elif c == '=':
        return 10
    elif c == '.':
        return 11
    elif c.isdigit():
        return 12
    elif c.isalpha():
        return 13
    else:
        return 14

global unreadChar 
unreadChar = []
EOF = False
fp = None

def scan_main(filename):
    fp = open(filename, 'r')
    token = ""
    list_tokens = []
    while not EOF and token != 'error':
        token = scan(fp)
        list_tokens.append(token)
    if token == 'error':
        print("error")
    fp.close()
    return list_tokens

def scan(fp):
    #code for scan function
    global EOF
    token = "whitespace"
    cur_char = " "
    remembered_chars = ""
    global unreadChar
    while token == 'whitespace' or token == 'comment':                         # base structure setup aka loops and if statements. Contents still need to be added/corrected to structure
        cur_state = 1
        image = ""
        prev_state = 0
        while cur_char != "":
            if not unreadChar:
                cur_char = fp.read(1)
            else:
                cur_char = unreadChar[0]
                unreadChar = unreadChar[1:]
            if cur_char == "":
                EOF = True
                prev_state = cur_state
                return [tokenTable[prev_state],image]
            action = transitionTable[cur_state][charState(cur_char)].action
            if action == "move":
                if cur_state != 0:
                    prev_state = cur_state
                    remembered_chars = ""
                remembered_chars += cur_char
                cur_state = transitionTable[cur_state][charState(cur_char)].newState
            elif action == "recognize":
                token = tokenTable[cur_state]
                if cur_char == ' ' or cur_char == '\n' or cur_char == '\t':
                    pass
                else:
                    unreadChar.append(cur_char)
                break
            elif action == "stuck":
                if prev_state != 0:
                    token = tokenTable[prev_state]
                    break
                else:
                    return "error"
            image += cur_char
    if image.lower() == 'read':
        token = 'read'
    if image.lower() == 'write':
        token = 'write'
    return [token,image]

#------------------------------------------- Parser Function ------------------------------------------------------------
class text_file_store:
    def __init__(self, fp = None) -> None:
        try:
            with open('data.txt', 'r') as file:
                data = file.read().replace('\n', '')
                temp_list = data.split(' ')
                self.data = temp_list
        except:
            self.data = []
        self.index = 0
    
    def read(self, i):
        if i>= len(self.data):
            return ""
        else:
            return self.data[i-1]

class token_list:
    def __init__(self, tokenlist) -> None:
        self.token_list = tokenlist
        self.current_index = 0


tok_list = token_list([])
def main():                             # main function to drive code
    #code for main function
    inp = input("")
    temp = inp.split(" ")
    sp = open(temp[1], 'r')
    global fp
    global file_str
    global tok_list
    fp = sp
    file_str = text_file_store(sp)
    tok_list.token_list = scan_main(temp[1])
    if len(temp) ==2 and temp[0] == "parser":
        program(0)



def program(depth):
    print("<program>")
    if(len(tok_list.token_list) == 0):
        stmt_list(depth + 2)
    elif(tok_list.token_list[tok_list.current_index][0] in ["read","write","identifier"]):
        stmt_list(depth + 2)
    print("</program>")
    pass

def stmt_list(depth):
    indent = " " * depth
    print(indent + "<stmt_list>")
    if(tok_list.current_index>=len(tok_list.token_list)):
        pass
    elif(tok_list.token_list[tok_list.current_index][0] in ["read","write","identifier"]):
        stmt(depth+2), stmt_list(depth+2)
    print(indent + "</stmt_list>")
    pass

def stmt(depth):
    indent = " " * depth
    print(indent + "<stmt>")
    if tok_list.token_list[tok_list.current_index][0] == "read":
        read(depth+2)
        tok_list.current_index += 1
        id(depth+2)
        tok_list.current_index += 1
        pass
    elif tok_list.token_list[tok_list.current_index][0] == "write":
        write(depth+2)
        tok_list.current_index += 1
        expr(depth+2)
        pass
    elif tok_list.token_list[tok_list.current_index][0] == "identifier":
        id(depth+2)
        tok_list.current_index += 1
        equals(depth+2)
        tok_list.current_index += 1
        expr(depth+2)
        pass
    else:
        print("err")
    print(indent + "</stmt>")
    pass

def expr(depth):
    indent = " " * depth
    print(indent + "<expr>")
    if(tok_list.token_list[tok_list.current_index][0] in ["identifier", "number", "lparen"]):
        term(depth+2)
        term_tail(depth+2)
    else:
        print("err")
    print(indent + "</expr>")
    pass

def term(depth):
    indent = " " * depth
    print(indent + "<term>")
    if(tok_list.token_list[tok_list.current_index][0] in ["identifier", "number", "lparen"]):
        factor(depth+2)
        fact_tail(depth+2)
    print(indent + "</term>")
    pass

def term_tail(depth):
    indent = " " * depth
    print(indent + "<term_tail>")
    if (tok_list.current_index>=len(tok_list.token_list)):
        pass
    elif(tok_list.token_list[tok_list.current_index][0] in ["plus", "minus"]):
        add_op(depth+2)
        tok_list.current_index += 1
        term(depth+2)
        term_tail(depth+2)
    elif(tok_list.token_list[tok_list.current_index][0] in ["identifier", "read", "write", "rparen"]):
        pass
    else:
        print("err")
    print(indent + "</term_tail>")
    pass

def factor(depth):
    indent = " " * depth
    print(indent + "<factor>")
    if tok_list.token_list[tok_list.current_index][0] == "identifier":
        id(depth+2)
        tok_list.current_index += 1
        pass
    elif tok_list.token_list[tok_list.current_index][0] == "number":
        number(depth+2)
        tok_list.current_index += 1
        pass
    elif tok_list.token_list[tok_list.current_index][0] == "lparen":
        lparen(depth+2)
        tok_list.current_index += 1
        expr(depth+2)
        rparen(depth+2)
        tok_list.current_index += 1
    print(indent + "</factor>")
    pass

def fact_tail(depth):
    indent = " " * depth
    print(indent + "<fact_tail>")
    if (tok_list.current_index>=len(tok_list.token_list)):
        pass
    elif tok_list.token_list[tok_list.current_index][0] in ["div", "times"]:
        mult_op(depth+2)
        tok_list.current_index += 1
        factor(depth+2)
        fact_tail(depth+2)
    elif tok_list.token_list[tok_list.current_index][0] in ["minus", "plus", "identifier", "read", "write","rparen"]:
        pass
    else:
        print("err")
    print(indent + "</fact_tail>")
    pass

def add_op(depth):
    indentation = " " * depth
    add_op_indent = " " * (depth + 2)
    print(indentation + "<add_op>")
    print(add_op_indent + tok_list.token_list[tok_list.current_index][1])
    print(indentation + "</add_op>")
    pass

def mult_op(depth):
    indentation = " " * depth
    mult_op_indent = " " * (depth + 2)
    print(indentation + "<mult_op>")
    print(mult_op_indent + tok_list.token_list[tok_list.current_index][1])
    print(indentation + "</mult_op>")
    pass

def read(depth):
    indentation = " " * depth
    read_indent = " " * (depth + 2)
    print(indentation + "<read>")
    print(read_indent + "read")
    print(indentation + "</read>")

def write(depth):
    indentation = " " * depth
    read_indent = " " * (depth + 2)
    print(indentation + "<write>")
    print(read_indent + "write")
    print(indentation + "</write>")

def equals(depth):
    indentation = " " * depth
    equals_indent = " " * (depth + 2)
    print(indentation + "<assign>")
    print(equals_indent + ":=")
    print(indentation + "</assign>")

def id(depth):
    indentation = " " * depth
    id_indent = " " * (depth + 2)
    print(indentation + "<id>")
    print(id_indent + tok_list.token_list[tok_list.current_index][1])
    print(indentation + "</id>")

def number(depth):
    indentation = " " * depth
    number_indent = " " * (depth + 2)
    print(indentation + "<number>")
    print(number_indent + tok_list.token_list[tok_list.current_index][1])
    print(indentation + "</number>")

def lparen(depth):
    indentation = " " * depth
    lparen_indent = " " * (depth + 2)
    print(indentation + "<lparen>")
    print(lparen_indent + tok_list.token_list[tok_list.current_index][1])
    print(indentation + "</lparen>")

def rparen(depth):
    indentation = " " * depth
    rparen_indent = " " * (depth + 2)
    print(indentation + "<rparen>")
    print(rparen_indent + tok_list.token_list[tok_list.current_index][1])
    print(indentation + "</rparen>")

main()