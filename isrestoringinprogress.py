"""
This file does check how far the restoration process of a full bucket in aws s3 is.
"""
import json
import subprocess

bucket = ""
files = subprocess.check_output(["aws", "s3", "ls", "s3://" + bucket, "--recursive"]).decode("utf-8").split("\n")

index = int(len(files)/2)
intervallength = int(len(files)/2)

for i in range(0,len(files)):
    file = files[index].split(" ")[-1]
    if intervallength < 1:
        break

    head = subprocess.check_output(["aws", "s3api", "head-object", "--bucket", bucket, "--key", file])
    js = json.loads(head)

    restore = js["Restore"]
    if 'ongoing-request="false"' in restore:
        index += intervallength/2
    else:
        index -= intervallength/2
    index = int(index)
    intervallength /= 2
    intervallength = int(intervallength)


print(index)
