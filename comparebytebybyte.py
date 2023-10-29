"""
INPUT: OUTPUT OF HEXDUMP of File
"""
FILE1LOC = "corr.hex"
FILE2LOC = "false.hex"

file1 = open(FILE1LOC, "r")
file2 = open(FILE2LOC, "r")

lines2 = file2.readlines()
count = 0
for index, line1 in enumerate(file1.readlines()):
    try:
        if lines2[index] == line1:
            continue
        else:
            count += 1
            continue
            print(f"line {index} does not match.")
            print(f"line in file 1: {line1}")
            print(f"line in file 2: {lines2[index]}")
    except:
        break
print(count)