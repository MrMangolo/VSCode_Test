import argparse

class AllArgs:
    #Pastebin Key
    key = None

    #Set Vars to Arguments
    def parseArgs(self):
        parser = argparse.ArgumentParser(description="This is a Pastebin Scraper. It scrapes all new Pastes at the time it's getting started. Go to https://pastebin.com/api_scraping_faq and Whitelist you IP to use the Scraper.")
        parser._action_groups.pop()
        #required = parser.add_argument_group("Required arguments")
        #optional = parser.add_argument_group("Optional arguments")
        #required.add_argument("-k", "--key", help="Input pastebin key", required=True)
        #args = parser.parse_args()
        #self.key = args.key