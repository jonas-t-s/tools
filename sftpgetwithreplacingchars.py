import os.path

import pysftp
from tqdm import tqdm

PASSWORD = ""
USERNAME =""
SSHHOST= ""

SOURCEDIR=""
TARGETDIR=""
ILLEGALCHARS=":"
REPLACEMENTCHARS= "_"

with pysftp.Connection(host=SSHHOST, username=USERNAME, password=PASSWORD) as sftp:
    for file in tqdm(sftp.listdir(SOURCEDIR)):
        basename = file
        for index, char in enumerate(ILLEGALCHARS):
            if char in basename:
                basename= basename.replace(char, REPLACEMENTCHARS[index])

        sftp.get(SOURCEDIR + file, TARGETDIR + basename)
