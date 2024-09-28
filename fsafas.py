number = 38
txt = f"Number: {38}"

class printClass:

    def __init__(self, text):
        
        self.text = text

    def printText(self):

        print(self.text)

number = 45

pC = printClass(txt)

pC.printText()