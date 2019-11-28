

class Line():
    """The string"""
    def __init__(self):
        self.string = ""

    def get_string(self):
        return self.string

    def set_string(self, string):
        if self.verification(string):
            self.string = string

    def verification(self, string):
        result = False
        if len(string) == 9:
            for char in string:
                if char == '1' or char == '0':
                    result = True
                else:
                    print("Error! The string should contain only the characters \"1\" or \"0\". ")
                    result = False
                    break
        else:
            print("Error! The string length must be 9.")
            result = False
        return result

    def get_quentity_one(self):
        quentity = 0
        for char in self.string:
            if char == '1':
                quentity += 1
        return quentity

    def get_length(self):
        return len(self.string)
