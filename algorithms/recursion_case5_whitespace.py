'''
This program delete whitespases and tab characters from string
'''

def remove(string):
    # base case
    if not string:
        return "This is not a string"
    # recursive case
    if string[0] == '\t' or string[0] == " ":
        return remove(string[1:])
    else:
        return string[0] + remove(string[1:])

text = remove(input('Enter the string: '))
print(text)