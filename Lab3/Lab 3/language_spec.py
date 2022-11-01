separators = ['[', ']', '{', '}', '(', ')', ';', ' ', ':', '\n', '\t', '\"']
operators = ['+', '-', '*', '/', '%', '<', '<=', '=', '>=', '>',
             '>>', '<<', '==', '&&', '||', '!', '!=', '&', '~',
             '|', '^', '+=', '++', '--', ',']
reservedWords = ['pe_lista', 'daca_merge', 'daca_nu', 'doresc', 'spune', 'da_i_sa_mearga']
allThree = separators + operators + reservedWords


def find_pos(elem):
    index = 0
    for elememt in allThree:
        if elem == elememt:
            return index
        index += 1