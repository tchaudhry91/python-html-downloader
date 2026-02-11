# External Dependency <- Should be autoinstalled with pipreqs. 
# Requirements.txt deliberately omitted
import requests
import sys
import json
params = json.load(sys.stdin)
resp = requests.get(params.url)
print(resp.text)
