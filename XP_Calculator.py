CurrentlyLevel = int(input("\033[38;2;255;255;255mEnter Currently Level : "))
TargetLevel = int(input("\033[38;2;255;255;255mEnter Target Level : "))
def XpCal(level):
    Xp = 0
    Plus = 7
    PlusAppend = 2
    k = 3
    for i in range(level):
        if i % 15 == 0 and i > 0:
            PlusAppend += k
            k += 1 
        Xp += Plus
        Plus += PlusAppend
    return Xp
print("\033[38;2;255;255;0mXp Required :", XpCal(TargetLevel) - XpCal(CurrentlyLevel), "\033[38;2;255;255;255m")
