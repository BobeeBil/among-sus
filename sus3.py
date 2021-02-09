from numpy import random

code = ""
word = "" # AAEACDBB or AAAFCDBB
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

c1_ = 0.5; c1b = 0.2; c1g = 0.2; c1ch = 0.07; c1sh = 0.03
c1 = random.choice(t1, p=[c1_, c1b, c1g, c1ch, c1sh])

if c1 == "A":
    c2a = 1.0; c2o = 0.0
elif c1 == "B" or c1 == "C":
    c2a = 0.4; c2o = 0.6
elif c1 == "D" or c1 == "E":
    c2a = 0.5; c2o = 0.5
c2 = random.choice(t2, p=[c2a, c2o])

if c1 == "A":
    c3_ = 0.4; c3b = 0.2; c3d = 0.1; c3g = 0.1; c3m = 0.1 ;c3sh = 0.1
elif c1 == "B" or c1 == "C":
    c3_ = 0.4; c3b = 0.2; c3d = 0.03; c3g = 0.3; c3m = 0.03; c3sh = 0.04
elif c1 == "D" or c1 == "E":
    c3_ = 0.3; c3b = 0.2; c3d = 0.1; c3g = 0.2; c3m = 0.1; c3sh = 0.1
c3 = random.choice(t3, p=[c3_, c3b, c3d, c3g, c3m, c3sh])


if c3 == "A":
    c4_ = 0.0; c4b = 0.13; c4d = 0.13; c4f = 0.125; c4g = 0.125
    c4m = 0.125; c4n = 0.125; c4ch = 0.12; c4sh = 0.12
elif c3 == "B":
    c4_ = 0.3; c4b = 0.0; c4d = 0.2; c4f = 0.2; c4g = 0.0
    c4m = 0.2; c4n = 0.0; c4ch = 0.1; c4sh = 0.0 
elif c3 == "C":
    c4_ = 0.4; c4b = 0.0; c4d = 0.0; c4f = 0.0; c4g = 0.0
    c4m = 0.3; c4n = 0.3; c4ch = 0.0; c4sh = 0.0
elif c3 == "D":
    c4_ = 0.3; c4b = 0.0; c4d = 0.0; c4f = 0.2; c4g = 0.0
    c4m = 0.2; c4n = 0.0; c4ch = 0.2; c4sh = 0.1 
elif c3 == "E":
    c4_ = 0.5; c4b = 0.3; c4d = 0.05; c4f = 0.05; c4g = 0.05
    c4m = 0.0; c4n = 0.0; c4ch = 0.0; c4sh = 0.05
elif c3 == "F":
    c4_ = 0.4; c4b = 0.0; c4d = 0.0; c4f = 0.0; c4g = 0.0
    c4m = 0.3; c4n = 0.3; c4ch = 0.0; c4sh = 0.0
c4 = random.choice(t4, p=[c4_, c4b, c4d, c4f, c4g, c4m, c4n, c4ch, c4sh])

if c3 == "A":
    c5a = 0.15; c5i = 0.15; c5o = 0.35; c5u = 0.35
elif c3 == "B":
    c5a = 0.15; c5i = 0.35; c5o = 0.15; c5u = 0.35
elif c3 == "C":
    c5a = 0.15; c5i = 0.2; c5o = 0.3; c5u = 0.35
elif c3 == "D":
    c5a = 0.3; c5i = 0.3; c5o = 0.0; c5u = 0.4
elif c3 == "E":
    c5a = 0.15; c5i = 0.1; c5o = 0.4; c5u = 0.35
elif c3 == "F":
    c5a = 0.2; c5i = 0.0; c5o = 0.4; c5u = 0.4
c5 = random.choice(t5, p=[c5a, c5i, c5o, c5u])

if c5 == "A":
    c6b = 0.0; c6g = 0.4; c6n = 0.2; c6ng = 0.4
elif c5 == "B":
    c6b = 0.0; c6g = 0.1; c6n = 0.2; c6ng = 0.7
elif c5 == "C":
    c6b = 0.2; c6g = 0.4; c6n = 0.0; c6ng = 0.4
elif c5 == "D":
    c6b = 0.1; c6g = 0.3; c6n = 0.3; c6ng = 0.3
c6 = random.choice(t6, p=[c6b, c6g, c6n, c6ng])


if c6 == "D":
    c7_ = 0.55; c7__ = 0.45
else:
    c7_ = 1.0; c7__ = 0.0
c7 = random.choice(t7, p=[c7_, c7__])
if random.choice([1, 2, 3]) == 1 and c7 == "B":
    sus = True

if c7 == "B":
    c8o = 0.0; c8u = 1.0; c8ou = 0.0
else:
    if c6 == "A":
        c8o = 0.3; c8u = 0.4; c8ou = 0.3
    elif c6 == "B":
        c8o = 0.3; c8u = 0.5; c8ou = 0.2
    elif c6 == "C":
        c8o = 0.1; c8u = 0.5; c8ou = 0.4
    if c6 == "D":
        c8o = 0.2; c8u = 0.7; c8ou = 0.1
c8 = random.choice(t8, p=[c8o, c8u, c8ou])



letters = [l1, l2, l3, l4, l5, l6, l7, l8]
types = [t1, t2, t3, t4, t5, t6, t7, t8]
codes = [c1, c2, c3, c4, c5, c6, c7, c8]

for l in letters:
    word += l[types[letters.index(l)].index(codes[letters.index(l)])]
    if letters.index(l) == 5 and sus == True:
        word += "s"
word += "s"

for c in codes:
    code += c
print()
print(code)
print(word)
print()