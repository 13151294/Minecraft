Level = int(input("\033[38;2;255;255;255mEnter Level : "))
Exp = 0
ExpNextLevel = 7
Plus = 2
k = 3
for i in range(Level):
    if i % 15 == 0 and i > 0:
        Plus += k
        k += 1
    Exp += ExpNextLevel
    ExpNextLevel += Plus
Number1 = len("{} Level Exp Required : {}.".format(Level, Exp))
print("\033[38;2;0;255;0m~"*(Number1//2),"Answer","~"*(Number1//2),"\033[38;2;255;255;255m")
Number2 = len("~"*(Number1+8))
print("{} Level Exp Required : {}.".format(Level, Exp).center(Number2))
print("{} Level Exp Diff is {}.".format(Level, ExpNextLevel - Plus ).center(Number2))
print("{} Level Exp Diff is {}.".format(Level+1, ExpNextLevel).center(Number2))
print("\033[38;2;0;255;0m~"*(Number1+7))
