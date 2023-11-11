import requests
import os
responsev4 = requests.get('https://www.cloudflare.com/ips-v4/')
responsev6 = requests.get('https://www.cloudflare.com/ips-v6/')

for response in [responsev4, responsev6]:
    for ip in response.content.decode().split('\n'):
        os.system(f"ufw allow to any port 443 from {ip}")