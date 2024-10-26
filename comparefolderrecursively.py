import concurrent.futures
import hashlib
import os




def calculate_md5(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        return hashlib.md5(data).hexdigest()


def md5_all_files(directory):
    md5s = list()
    filepaths = list()
    sizes = set()
    threadpoolexecutor = concurrent.futures.ThreadPoolExecutor()
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            if os.path.isfile(filepath):
                md5s.append(calculate_md5(filepath))
                filepaths.append(filepath)
                sizes.add(os.path.getsize(filepath))
    return filepaths, md5s, sizes

print("Calculating A")
afiles, Ahashes, sizes = md5_all_files("/home/jonas/Clouds/googledrive/Pictures")  # Replace with your folder path

# bfiles, Bhashes = md5_all_files("/home/jonas/Pictures")
seenhashes = list()
seenfiles = list()
seenorigfiles = list()
for file, hash in zip(afiles, Ahashes):
    for foldername, subfolders, filenames in os.walk("/home/jonas/Pictures"):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            if len(seenorigfiles) >= len(afiles):
                    break
            if os.path.isfile(filepath):
                if not os.path.getsize(filepath) in sizes:
                    continue
                md5sum = calculate_md5(filepath)
                if md5sum in Ahashes:
                    seenhashes.append(md5sum)
                    seenfiles.append(filepath)
                    seenorigfiles.append(afiles[Ahashes.index(md5sum)])

print(f"The e following files have the same hash:\n")
for hash, origfile, newfile in zip(seenhashes, seenorigfiles, seenfiles):
    print(f"{origfile} -> {newfile}")
print("The following files have no match:")
for file, hash in zip(afiles, Ahashes):
    if (file not in seenorigfiles) and hash not in seenhashes:
        print(file)
