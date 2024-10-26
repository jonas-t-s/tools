import os
import argparse
import os
import argparse
import hashlib


def get_file_size(file_path):
    return os.path.getsize(file_path)


def get_file_hash(file_path, algorithm):
    h = hashlib.new(algorithm)
    with open(file_path, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser(description='Get file size and hashes.')

    args = parser.parse_args()
    numfound = 0
    totalnums = 0
    notfound =0
    from concurrent.futures import ThreadPoolExecutor


    def process_file(root_file):
        root, file = root_file
        if search_file(f"{root}/{file}"):
            return True
        else:
            return False
    with ThreadPoolExecutor() as executor:
        root_files = [(root, file) for root, dirs, files in os.walk("/home/jonas/Clouds/googledrive/Pictures")
                      if "/run" not in root for file in files]
        totalnums = len(root_files)
        results = executor.map(process_file, root_files)

    numfound = sum(results)
    notfound = totalnums - numfound

    print(f"Found: {numfound}")
    print(f"not Found: {notfound}")
    print(f"totla: {totalnums}")
def search_file(filepath):
    file_size = get_file_size(filepath)
    md5_sum = get_file_hash(filepath, 'md5')
    sha256_sum = get_file_hash(filepath, 'sha256')
    for root, dirs, files in os.walk("/home/jonas/Pictures"):
        if "/run" in root:
            continue
        for name in files:
            try:
                if get_file_size(root + "/" + name) == file_size:
                    if get_file_hash(root + "/" + name, 'md5') == md5_sum and get_file_hash(root + "/" + name,
                                                                                            'sha256') == sha256_sum and not root in filepath:
                        return True
            except FileNotFoundError:
                continue
    return False
    print(f'File size: {file_size}')
    print(f'MD5: {md5_sum}')
    print(f'SHA256: {sha256_sum}')


if __name__ == "__main__":
    main()