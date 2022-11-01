from HashTable import HashTable


class SymbolTable:
    def __init__(self):
        self.symbolTable = HashTable()

    def add(self, key):
        self.symbolTable.insert(key)

    def find_pos(self, key):
        return self.symbolTable.get_pos(key)
