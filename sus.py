import random as r

c1 = ["b", "d", "g", "m", "n"] # AM
c2 = ["b", "d", "g", "l", "t"] # EXTRA 1
c3 = ["b", "d", "g", "k", "l", "t"] # EXTRA 2
c4 = ["b", "g", "m", "n"] # ONG 
c5 = ["b", "c", "g"] # US
v = ["a", "e", "o", "u"] # VOWELS
word = ""

# DECIDE TYPE
num = r.randint(1, 8)
if 1 <= num <= 4:
    type = "A"
elif 5 <= num <=7:
    type = "B"
else:   
    type = "C"

# CREATE STRING
s1, s2, s3, s4, s5 = "", "", "", "", ""

# SYLLABLE 1
t1 = r.randint(1, 4)
if t1 == 1:
    num = r.randint(1, 3)
    if num == 1 or num == 2:
        s1 += "a"
    else:
        s1 += "o"
elif t1 == 2:
    s1 += c1[r.randint(0, len(c1) - 1)]
    num = r.randint(1, 8)
    if 1 <= num <= 4:
        s1 += "a"
    elif 5 <= num <= 7:
        s1 += "o"
    else:
        s1 += "u"
elif t1 == 3:
    num = r.randint(1, 8)
    if 1 <= num <= 4:
        s1 += "a"
    elif 5 <= num <= 7:
        s1 += "o"
    else:
        s1 += "u"
    s1 += c1[r.randint(0, len(c1) - 1)]
else:
    s1 += c1[r.randint(0, len(c1) - 1)]
    num = r.randint(1, 8)
    if 1 <= num <= 4:
        s1 += "a"
    elif 5 <= num <= 7:
        s1 += "o"
    else:
        s1 += "u"
    s1 += c1[r.randint(0, len(c1) - 1)]

# SYLLABLE 4
t4 = r.randint(1, 3)
if t4 == 1:
    s4 += c4[r.randint(0, len(c4) - 1)]
    num = r.randint(1, 14)
    if 1 <= num <= 4:
        s4 += "u"
    elif 5 <= num <= 8:
        s4 += "o"
    elif 9 <= num <= 11:
        s4 += "a"
    else:
        s4 += "i"
elif t4 == 2:
    num = r.randint(1, 14)
    if 1 <= num <= 4:
        s4 += "u"
    elif 5 <= num <= 8:
        s4 += "o"
    elif 9 <= num <= 11:
        s4 += "a"
    else:
        s4 += "i"
    s4 += c4[r.randint(0, len(c4) - 1)]
else:
    s4 += c4[r.randint(0, len(c4) - 1)]
    num = r.randint(1, 14)
    if 1 <= num <= 4:
        s4 += "u"
    elif 5 <= num <= 8:
        s4 += "o"
    elif 9 <= num <= 11:
        s4 += "a"
    else:
        s4 += "i"
    s4 += c4[r.randint(0, len(c4) - 1)]

# SYLLABLE 5
t5 = r.randint(1, 2)
if t5 == 1:
    num = r.randint(1, 7)
    if 1 <= num <= 4:
        s5 += "u"
    elif 5 <= num <= 7:
        s4 += "o"
    s5 += "s"
else:
    c5.append("ng")
    s5 += c5[r.randint(0, len(c5) - 1)]
    num = r.randint(1, 7)
    if 1 <= num <= 4:
        s5 += "u"
    elif 5 <= num <= 7:
        s4 += "o"
    s5 += "s"

if type == "B" or type == "C":
    # SYLLABLE 2
    t2 = r.randint(1, 8)
    if 1 <= t2 <= 4:
        s2 += v[r.randint(0, len(v) - 1)]
    elif 5 <= t2 <= 6:
        s2 += c2[r.randint(0, len(c2) - 1)]
        s2 += v[r.randint(0, len(v) - 1)]
    else:
        s2 += v[r.randint(0, len(v) - 1)]
        s2 += c2[r.randint(0, len(c2) - 1)]

if type == "C":
    # SYLLABLE 3
    t3 = r.randint(1, 8)
    if 1 <= t3 <= 4:
        s3 += v[r.randint(0, len(v) - 1)]
    elif 5 <= t3 <= 6:
        s3 += c3[r.randint(0, len(c3) - 1)]
        s3 += v[r.randint(0, len(v) - 1)]
    else:
        s3 += v[r.randint(0, len(v) - 1)]
        s3 += c3[r.randint(0, len(c3) - 1)]

word = s1 + s2 + s3 + s4 + s5
print(word)