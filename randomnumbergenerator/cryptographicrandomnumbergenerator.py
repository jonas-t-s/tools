import secrets
"""
Just some fun stuff for getting random numbers from the systemrandom number generator
"""
firstpossiblenumber = 1
lastpossiblenumber = 5
numberofuniquerandomnumbers = 1

sysrandom = secrets.SystemRandom()
randomnumbers = []
for i in range(numberofuniquerandomnumbers):
    r = sysrandom.randint(firstpossiblenumber, lastpossiblenumber)
    while r in randomnumbers:
        r = sysrandom.randint(firstpossiblenumber, lastpossiblenumber)
    randomnumbers.append(r)

randomnumbers.sort()
print(randomnumbers)

