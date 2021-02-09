import random

CODE = "A/A-BBA-AA-A//"
CODE = input("INPUT CODE: ")

t1 = CODE[0]
t2 = CODE[1]
t3 = CODE[2]
t4 = CODE[4]
t5 = CODE[5]
t6 = CODE[6]
t7 = CODE[8]
t8 = CODE[9]
t9 = CODE[11]
t10 = CODE[12]
t11 = CODE[13]

word = ""

l1 = ["g", "b", "d", "k"]
h1 = ["A", "B", "C", "D"]
l2 = ["m", "n", "g", "b", "d", "k", "p"]
h2 = ["A", "B", "C", "D", "E", "F", "G"]
l3 = ["ng", "g"]
h3 = ["A", "B"]
l4 = ["b", "g"]
h4 = ["A", "B"]

if t1 == "B":
    word += l1[h1.index(t2)]

if t3 == "A":
    word += "a"
elif t3 == "B":
    word += "o"

word += l2[h2.index(t4)]

if t5 == "A":
    word += "u"
elif t5 == "B":
    word += "o"

word += l3[h3.index(t6)]

if t7 == "B":
    word += " "
elif t7 == "C":
    word == " s"

if t9 == "B":
    if t10 == "A":
        word += "a"
    word += l4[h4.index[t11]]

if t8 == "A":
    word += "u"
elif t8 == "B":
    word += "o"
elif t8 == "C":
    word += "a"
word += "s"

print(word)