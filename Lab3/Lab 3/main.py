from SymbolTable import SymbolTable
from Scanner import *
from PIF import PIF
from HashTable import HashTable

if __name__ == '__main__':
    pif = PIF()
    st = SymbolTable()
    fileName = input("File name: ")

    index = 0
    for elem in allThree:
        print(index, elem)
        index += 1

    lineNr = 0
    with open(fileName, 'r') as file:
        for line in file:
            lineNr += 1
            for element in split_Line(line):
                if element in separators or element in operators or element in reservedWords:
                    continue
                elif is_id(element):
                    if st.find_pos(element) == -1:
                        st.add(element)
                elif is_const(element):
                    if st.find_pos(element) == -1:
                        st.add(element)
                else:
                    raise Exception('Lexical error, token: ' + element + ' at line ' + str(lineNr))
    file.close()

    with open(fileName, "r") as file:
        for line in file:
            for element in split_Line(line):
                if element in separators or element in operators or element in reservedWords:
                    if element != ' ':
                        pif.add(find_pos(element), -1)
                elif is_id(element):
                    pif.add("id", (st.symbolTable.hash(element), st.find_pos(element)))
                elif is_const(element):
                    pif.add("constant", (st.symbolTable.hash(element), st.find_pos(element)))
    file.close()

    f = open("st.out", "w")
    f.write("{:<15} {:<15} \n".format("Bucket", "Values"))
    index = 0
    while index < st.symbolTable.capacity:
        node = st.symbolTable.items[index]
        if node is not None:
            prev = st.symbolTable.items[index]
            values = []
            while node is not None:
                values.append(node.key)
                prev = node
                node = node.next
            f.write("{:<15} {:<15} \n".format(index, str(values)))
        index += 1
    f.close()

    f = open("pif.out", "w")
    f.write("{:<15} {:<15} \n".format("Token", "ST_Position"))
    for element in pif.content:
        f.write("{:<15} {:<15} \n".format(element[0], str(element[1])))
    f.close()
