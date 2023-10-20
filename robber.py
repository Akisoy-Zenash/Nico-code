houses = [2, 16 , 9, 5, 20 , 10, 1]
paire = 0
impaire = 0


for idx, i in enumerate(houses):
    if idx % 2 == 0:
        paire += i
    else:
        impaire += i

if paire > impaire:
    print(f"The max is {paire} starting with the first house and going on one by one")
elif paire < impaire:
    print(f"The max is {impaire} starting with the second house and going on one by one")
else:
    print(f"The max is {paire}, it doesn't matter where u start just go on one by one")