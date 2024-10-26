import pandas as pd
import subprocess
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import secrets
NUMTESTS = int(10000000)
minnumber = 1
maxnumber = 100
numbers = np.zeros(maxnumber-minnumber+1)
for i in range(NUMTESTS):
    #Choose stuff
    numbers[secrets.SystemRandom().randint(minnumber,maxnumber)-minnumber] +=1 
numbers /= NUMTESTS
numbers *= maxnumber-minnumber
sns.lineplot(numbers)
plt.show()
from collections import Counter
occurances = Counter(numbers)
counts = occurances.values()

print(occurances)
print(f"AVG {np.average(numbers)}")
print(f"MIN {np.min(numbers)}")
print(f"MAX {np.max(numbers)}")
print(f"Stdv {np.std(numbers)}")

print(f"Count-AVG: {np.average(numbers)}")
print(f"Count-Min: {np.min(numbers)}")
print(f"Count-max: {np.max(numbers)}")
print(f"Count-std: {np.std(numbers)}")
