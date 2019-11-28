
from Line import *
from Massiv import *

line = Line()
while line.get_string() == "":
    print("Enter string: ", end="")
    line.set_string(input())

massiv = Massiv(line.get_length())
print("Enter Massiv: ")
for i in range(massiv.get_length()):
    print("Enter Massiv[" + str(i) + "] = ", end="")
    massiv.set_element(i, input())

print("Massiv: ")
massiv.show_massiv()

print("Result: ")
for string in massiv.new_massiv(line.get_string(), massiv.get_massiv()):
    print(string, end=" ")


