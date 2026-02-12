# External Dependency <- Should be autoinstalled with pipreqs. 
# Requirements.txt deliberately omitted
import requests
import sys
import json
params = json.load(sys.stdin)
resp = requests.get(params.get("url"))
json.dump({"html_text": resp.text}, sys.stdout)
