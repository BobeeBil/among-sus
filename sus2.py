import random

l1 = ["g", "b", "d", "k"]
h1 = ["A", "B", "C", "D"]
l2 = ["m", "n", "g", "b", "d", "k", "p"]
h2 = ["A", "B", "C", "D", "E", "F", "G"]
l3 = ["ng", "g"]
h3 = ["A", "B"]
l4 = ["b", "g"]
h4 = ["A", "B"]

t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11 = "", "", "", "", "", "", "", "", "", "", ""

s1 = ""
s2 = ""
s3 = ""
se = ""

r = random.randint(1, 3)
if r == 1 or r == 2:
	t1 = "A"
	t2 += "/"
else:
	t1 = "B"
	r = random.randint(0, len(l1) - 1)
	t2 = h1[r]
	s1 += l1[r]

r = random.randint(1, 3)
if r == 1 or r == 2:
    t3 = "A"
    s1 += "a"
else:
    t3 = "B"
    s1 += "o"

r = random.randint(0, len(l2) - 1)
t4 = h2[r]
s2 += l2[r]

r = random.randint(1, 2)
if r == 1:
    t5 = "A"
    s2 += "u"
else:
    t5 = "B"
    s2 += "o"

r = random.randint(0, len(l3) - 1)
t6 = h3[r]
s2 += l3[r]

r = random.randint(1, 8)
if r == 1 or r == 2:
    t7 = "B"
    s2 += " "
elif r == 4:
    t7 = "C"
    s2 += " s"
else:
    t7 = "A"

r = random.randint(1, 15)
if r == 1:
    t9 = "B"
    r = random.randint(1, 2)
    if r == 1:
        t10 = "A"
        s3 += "a"
    else:
        t10 = "B"
    r = random.randint(0, len(l4) - 1)
    t11 = h4[r]
    s3 += l4[r]

else:
    t9 = "A"
    t10 = "/"
    t11 = "/"

r = random.randint(1, 6)
if r == 1 or r == 2 or r ==  3:
    t8 = "A"
    s3 += "u"
elif r == 4 or r == 5:
    t8 = "B"
    s3 += "o"
else:
    t8 = "C"
    s3 += "a"
s3 += "s"

type = t1 + t2 + t3 + "-" + t4 + t5 + t6 + "-" + t7 + t8 + "-"  + t9 + t10 + t11
word = s1 + s2 + se + s3
print()
print(type)
print(word)
print()