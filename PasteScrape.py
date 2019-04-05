import argparse
import requests
import re
import sys
import json
from src.argparser import AllArgs

#
arguments = AllArgs()
arguments.parseArgs()

class PasteLists:
    latest_Entry = dict()
    new_List = None

def testAccess():
    print("Testing whitelisted ip...")
    r = requests.get("https://scrape.pastebin.com/api_scraping.php")
    z = re.match("YOUR IP: \d+.\d+.\d+.\d+ DOES NOT HAVE ACCESS.", r.text)
    if(z):
        sys.exit("Please whitelist your Ip")
    else:
        print("Whitelist: OK")

testAccess()

def getPasteList():
    r = requests.get("https://scrape.pastebin.com/api_scraping.php")
    PasteLists.new_List = json.loads(r.text)
    if(PasteLists.new_List[-1] not in PasteLists.latest_Entry):
        print("ITS NOT IN IT")
    else:
        PasteLists.latest_Entry = PasteLists.new_List[-1]
    
