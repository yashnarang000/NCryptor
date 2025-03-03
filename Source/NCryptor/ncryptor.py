#IMPORT
import re # Import Regex

class NCrypt:
    def __init__(self, code_dict, allowed_characters, separator):
        self.codes = code_dict
        self.allowed_characters = allowed_characters
        self.separator = separator

    
    def encrypt(self, simple):
        i = 0
        simple_list = []
        simple = simple.lower() # Convert the simple text into lowercase
        simple = re.sub(fr"{self.allowed_characters}","", simple) # Limiting simple text to allowed characters only (Use Regular Expressions here. Refer https://www.dataquest.io/wp-content/uploads/2019/03/python-regular-expressions-cheat-sheet.pdf for more info.)
        while i<len(simple):
            simple_list.append(simple[i]) # Appending each character to 'simple_list' as an item
            i = i+1
    
        complex_list = []
        for k in simple_list:
            complex_list.append(self.codes[k]) # Appending the codes of the characters to 'complex_list'
        complexx = self.separator.join(complex_list) # Joining the items of the 'complex_list' to make 'complexx' string (codes of each character are separated by the separator)
        return complexx
    
    def c2s(self, comvalue):
        simkeys = list(self.codes.keys()) # 'simkeys' is a list containing all dictionary keys
        comvalues = list(self.codes.values()) # 'comvalues' is a list containing all dictionary values
        com_index = comvalues.index(comvalue) # Takes the value as input and gives the index number as output
        simvalue = simkeys[com_index] # Takes 'com_index' index number and returns the item value (key)
        return simvalue

    def decrypt(self, complexx):
        complex_list = complexx.split(self.separator) # Splits the given code into valid dictionary values using the separator
        simple_list = []
        com_length = len(complex_list)
        i = 0
        while i < com_length:
            simple_list.append(self.c2s(complex_list[i])) #Appending the keys of 'complex_list' from the dictionary
            i=i+1
        simple = "".join(simple_list) #Merging the 'simple_list' into a 'simple' string
        return simple

