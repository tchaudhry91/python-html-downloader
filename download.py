# External Dependency <- Should be autoinstalled with pipreqs. 
# Requirements.txt deliberately omitted
import requests
import sys

resp = requests.get(sys.argv[1])
print(resp.text)
