from random import shuffle

lbld = ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "O", "P", "R", "S", "T", "U", "V", "W", "X"]
shuffle(lbld)
cbld = []
a = 0
while a < 6 :
    cbld.append(lbld[0])
    lbld = ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "O", "P", "R", "S", "T", "U", "V", "W", "X"]
    if "B" in cbld :
        lbld.remove("B")
        lbld.remove("J")
        lbld.remove("M")
    if "C" in cbld :
        lbld.remove("C")
        lbld.remove("F")
        lbld.remove("I")
    if "D" in cbld :
        lbld.remove("E")
        lbld.remove("D")
        lbld.remove("R")
    if "E" in cbld :
        lbld.remove("E")
        lbld.remove("D")
        lbld.remove("R")
    if "F" in cbld :
        lbld.remove("F")
        lbld.remove("C")
        lbld.remove("I")
    if "G" in cbld :
        lbld.remove("G")
        lbld.remove("L")
        lbld.remove("V")
    if "H" in cbld :
        lbld.remove("H")
        lbld.remove("S")
        lbld.remove("U")
    if "I" in cbld :
        lbld.remove("I")
        lbld.remove("C")
        lbld.remove("F")
    if "J" in cbld :
        lbld.remove("J")
        lbld.remove("B")
        lbld.remove("M")
    if "K" in cbld :
        lbld.remove("K")
        lbld.remove("P")
        lbld.remove("W")
    if "L" in cbld :
        lbld.remove("L")
        lbld.remove("G")
        lbld.remove("V")
    if "M" in cbld :
        lbld.remove("M")
        lbld.remove("B")
        lbld.remove("J")
    if "O" in cbld :
        lbld.remove("O")
        lbld.remove("X")
        lbld.remove("T")
    if "P" in cbld :
        lbld.remove("P")
        lbld.remove("K")
        lbld.remove("W")
    if "R" in cbld :
        lbld.remove("R")
        lbld.remove("D")     
        lbld.remove("E")
    if "S" in cbld :
        lbld.remove("S")
        lbld.remove("H")
        lbld.remove("U")
    if "T" in cbld :
        lbld.remove("T")
        lbld.remove("O")
        lbld.remove("X")
    if "U" in cbld :
        lbld.remove("U")
        lbld.remove("H")
        lbld.remove("S")
    if "V" in cbld :
        lbld.remove("V")
        lbld.remove("G")
        lbld.remove("L")
    if "W" in cbld :
        lbld.remove("W")
        lbld.remove("K")
        lbld.remove("P")
    if "X" in cbld :
        lbld.remove("X")
        lbld.remove("T")
        lbld.remove("O")
    shuffle(lbld)
    a = a + 1

print(cbld)

lbld = ["A", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X"]
shuffle(lbld)
abld = []
a = 0
while a < 10 :
    abld.append(lbld[0])
    lbld = ["A", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X"]
    if "A" in abld :
        lbld.remove("A")
        lbld.remove("M")
    if "C" in abld :
        lbld.remove("C")
        lbld.remove("E") 
    if "D" in abld :
        lbld.remove("D")
        lbld.remove("Q")
    if "E" in abld :
        lbld.remove("E")
        lbld.remove("C")
    if "F" in abld :
        lbld.remove("F")
        lbld.remove("L")
    if "G" in abld :
        lbld.remove("G")
        lbld.remove("U")
    if "H" in abld :
        lbld.remove("H")
        lbld.remove("R")
    if "J" in abld :
        lbld.remove("J")
        lbld.remove("P")
    if "K" in abld :
        lbld.remove("K")
        lbld.remove("V")
    if "L" in abld :
        lbld.remove("L")
        lbld.remove("F")
    if "M" in abld :
        lbld.remove("M")
        lbld.remove("A")
    if "N" in abld :
        lbld.remove("N")
        lbld.remove("T")
    if "O" in abld :
        lbld.remove("O")
        lbld.remove("W")
    if "P" in abld :
        lbld.remove("P")
        lbld.remove("J")
    if "Q" in abld :
        lbld.remove("Q")
        lbld.remove("D")
    if "R" in abld :
        lbld.remove("R")
        lbld.remove("H")
    if "S" in abld :
        lbld.remove("S")
        lbld.remove("X")
    if "T" in abld :
        lbld.remove("T")
        lbld.remove("N")
    if "U" in abld :
        lbld.remove("U")
        lbld.remove("G")
    if "V" in abld :
        lbld.remove("V")
        lbld.remove("K")
    if "W" in abld :
        lbld.remove("W")
        lbld.remove("O")
    if "X" in abld :
        lbld.remove("X")
        lbld.remove("S")
    shuffle(lbld)
    a = a + 1

print(abld)