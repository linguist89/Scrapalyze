# A Scrap is an object from a Scrapalyze method
class Scrap:
    
    # Initializes the scrap with the list scraped from the Scrapalyze class
    def __init__(self, scrap_list):
        self.scrap_string = scrap_list[0].text
        self.scrap_list = scrap_list
    
    # Removes a single newline character from the string
    def clean(self, permanent=False):
        """Set permanent to True to make changes permanent to string.
        Default is set to False."""
        if permanent == True:
            self.scrap_string = self.scrap_string.replace("\n","") 
        else:
            return self.scrap_string.replace("\n","")
 