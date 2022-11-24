import keyword  # importing the 'keyword' library
print("This is the list of keywords in Python 3.10.6")
print(keyword.kwlist)  # prints the list of keywords
print()
print("Is \'and\' a keyword?")  # \' is an "escape sequence" to print the character " ' "
print(keyword.iskeyword('and'))  # checks whether 'and' is a keyword
print("As can be seen, \'and\' is a keyword?")
print("What about \'Optimus Prime\'?")
print(keyword.iskeyword('Optimus Prime'))  # checks whether 'Optimus Prime' is a keyword
print("Apparently not")
