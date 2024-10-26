import argparse
import json
import os
import random
import xml
from time import sleep


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfilepath", help="path to the file you want to translate")
    myip = ["65.21.104.25", "2a01:4f9:c012:66db::1"]
    args = parser.parse_args()
    foundips= set()
    tree = xml.etree.ElementTree.parse(args.inputfilepath)
    root = tree.getroot()
    for child in root:
        if child.tag == "record":
            for subchild in child:
                if subchild.tag == "row":
                    for subsubchild in subchild:
                        if subsubchild.tag == "source_ip":
                            if subsubchild.text not in myip:
                                foundips.add(subsubchild.text)
    print(foundips)
    import requests, selenium
    for ip in foundips:
        # print(requests.get(f"https://www.spamhouse.com/ip/{ip}").text)
        # sleep(10)
        dataraw = json.dumps({
            "threat_type": "spam",
            "reason": "This IP is trying to send E-Mails in the name my domain, but fails the DKIM and SPF checks and thus appears in my DMARC reports",
            "source": {
                "object": str(ip)
            }
        })
        with open("./spamhouseapikey.txt", "r") as file:
            authorization = file.read()

        os.system(f"curl -s -H 'Content-Type: application/json' -H 'Authorization: Bearer {authorization}' -d '{dataraw}' https://submit.spamhaus.org/portal/api/v1/submissions/add/ip")
        sleep(100*random.random())
        print("\n")
if __name__ == '__main__':
    main()