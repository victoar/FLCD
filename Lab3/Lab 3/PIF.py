class PIF:
    def __init__(self):
        self.content = []

    def add(self, code, st_pos):
        self.content.append((code, st_pos))

    def __str__(self):
        return str(self.content)
