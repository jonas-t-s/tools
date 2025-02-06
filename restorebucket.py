"""
Interruptable aws s3 restore from glacier for ten days.
"""

import math
import subprocess
import threading
from concurrent.futures import ThreadPoolExecutor

import numpy as np
from tqdm import tqdm

bucket = ""
files = subprocess.check_output(["aws", "s3", "ls", "s3://" + bucket, "--recursive"]).decode("utf-8").split("\n")
index = int(len(files)/2)
intervallength = int(len(files)/2)
z = 0
heads= np.zeros(len(files))
head = subprocess.check_output(["aws", "s3api", "head-object", "--bucket", bucket, "--key", files[0].split(" ")[-1]])
print(head)
exit(0)
if "Restore" in head.decode("utf-8"):
    index = 0
    print(head)
    exit(0)
skipindex = []
for i in range(0,len(files)):
    file = files[index].split(" ")[-1]
    if intervallength < 1:
        break
    try:
        head = subprocess.check_output(["aws", "s3api", "head-object", "--bucket", bucket, "--key", file])
        # heads[i] = head
        if "Restore" in head.decode("utf-8"):
            index += intervallength/2
        else:
            index -= intervallength/2

        intervallength /= 2
        intervallength = int(intervallength)
        index = int(math.ceil(index))
        if index in skipindex:
            index +=1
    except Exception as e:
        print(e)
lock = threading.Lock()
errorsfile = open("errors.txt", "a")
def run_subprocess(command):
    try:
        result = subprocess.run(command,
                       check=True,
                       capture_output=True,
                       text=True)
    except subprocess.CalledProcessError as e:
        lock.acquire()
        print(command, file=errorsfile)
        print(e.stdout, file=errorsfile)
        print(e.stderr, file=errorsfile)
        lock.release()


commands = []
max_workers = 2
queue = []
executor = ThreadPoolExecutor(max_workers=max_workers)
for idx, line in tqdm(enumerate(files)):
    if idx < index:
        continue
    file = line.split(" ")[-1]
    executor.submit(run_subprocess, ["aws", "s3api", "restore-object", "--restore-request", '{"Days":10,"GlacierJobParameters":{"Tier":"Bulk"}}', "--bucket", bucket, "--key", file])

executor.shutdown()
exit()
