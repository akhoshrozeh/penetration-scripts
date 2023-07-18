import requests
import sys

if len(sys.argv) != 2:
    print("Enter a domain.")
    exit(1)

target = sys.argv[1]

dirs = open("../wordlists/wordlist2.txt").read()
dir_list = dirs.splitlines()

for dir in dir_list:
    url = f"http://{target}/{dir}.html"

    req = requests.get(url)
    if req.status_code == 404:
        pass
    else:
        print("Valid directory: ", url)


