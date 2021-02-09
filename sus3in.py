from numpy import random

sus = False
l1 = ["", "b", "g", "ch", "sh"]
t1 = ["A", "B", "C", "D", "E"]
l2 = ["a", "o"]
t2 = ["A", "B"]
l3 = ["", "b", "d", "g", "m", "sh"]
t3 = ["A", "B", "C", "D", "E", "F"]

l4 = ["", "b", "d", "f", "g", "m", "n", "ch", "sh"]
t4 = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
l5 = ["a","i", "o", "u"]
t5 = ["A", "B", "C", "D"]
l6 = ["b", "g", "n", "ng"]
t6 = ["A", "B", "C", "D"]

l7 = ["", " "]
t7 = ["A", "B"]
l8 = ["o", "u", "ou"]
t8 = ["A", "B", "C"]

while True:
    word = ""
    try:
        CODE = input("INPUT CODE: ")
    except EOFError:
        continue
    c1, c2, c3, c4 = CODE[0], CODE[1], CODE[2], CODE[3]
    c5, c6, c7, c8 = CODE[4], CODE[5], CODE[6], CODE[7]

    letters = [l1, l2, l3, l4, l5, l6, l7, l8]
    types = [t1, t2, t3, t4, t5, t6, t7, t8]
    codes = [c1, c2, c3, c4, c5, c6, c7, c8]

    for l in letters:
        word += l[types[letters.index(l)].index(codes[letters.index(l)])]
        if letters.index(l) == 5 and sus == True:
            word += "s"
    word += "s"

    print(word)
    print()