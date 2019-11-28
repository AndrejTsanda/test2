

class Massiv():
    """Massiv"""

    def __init__(self, n):
        self.massiv = ['none'] * n

    def get_massiv(self):
        return self.massiv

    def get_element(self, i):
        return self.massiv[i]

    def set_element(self, i, string):
        self.massiv[i] = string

    def show_massiv(self):
        for s in self.massiv:
            print(s, end=" ")
        print()

    def get_length(self):
        return len(self.massiv)

    def new_massiv(self, string, massiv):
        i = 0
        result = []
        for char in string:
            if char == '1':
                result.append(massiv[i])
            i += 1
        return result
