import copy

from node import Node


class HashTable:
    def __init__(self):
        self.capacity = 10
        self.size = 0
        self.items = [None] * self.capacity

    def hash(self, key):
        hashsum = 0
        for character in str(key):
            hashsum += ord(character)
        return hashsum % self.capacity

    def rehash(self):
        self.capacity *= 2
        new_items = [None] * self.capacity
        for index in range(self.capacity // 2):
            node = self.items[index]
            while node is not None:
                new_index = self.hash(node.key)
                new_node = new_items[new_index]

                if new_node is None:
                    new_items[new_index] = Node(node.key)
                else:
                    new_prev = new_node
                    while new_node is not None:
                        new_prev = new_node
                        new_node = new_node.next

                    new_prev.next = Node(node.key)

                node = node.next
        self.items = [None] * (self.capacity//2)
        self.items = new_items

    def insert(self, key):
        index = self.hash(key)
        node = self.items[index]
        if node is None:
            self.items[index] = Node(key)
            self.size += 1
        else:
            prev = node
            while node is not None:
                if prev.key == key:
                    return
                prev = node
                node = node.next
            prev.next = Node(key)
            self.size += 1

        if self.size / self.capacity >= 0.7:
            self.rehash()

        return index

    def get_pos(self, key):
        index = self.hash(key)
        node = self.items[index]
        position = 1
        while node is not None and node.key != key:
            node = node.next
            position += 1
        if node is None:
            return -1
        return position
