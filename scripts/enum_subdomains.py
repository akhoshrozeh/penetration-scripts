import requests
import sys

if len(sys.argv) != 2:
    print("Enter a domain to enumerate.")
    exit(1)

subdom_list = open("../wordlists/subdomains.txt").read()
subdoms = subdom_list.splitlines()

target_domain = sys.argv[1]


for subdom in subdoms:
    # create the http url
    subdom_url = f"http://{subdom}.{target_domain}"

    try:
        requests.get(subdom_url)

    except requests.ConnectionError:
        pass

    else:
        print("Valid subdomain. URL: ", subdom_url)
