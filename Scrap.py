# A Scrap is an object from a Scrapalyze method
class Scrap:
    """
    A Scrap is a class that contains specific methods for formatting the results of Scrapalyze methods.
    """
    
    # Initializes the scrap with the list scraped from the Scrapalyze class
    def __init__(self, scrap_list):
        self.scrap_list = scrap_list
    
    # Display standard statistics for the Scrap
    @property
    def stats(self):
        print("The length of your scrap_list is: " + str(len(self.scrap_list)))
    
    # Removes a single newline character from the string
    def clean(self, i=0, permanent=False):
        """Set permanent to True to make changes permanent to string.
        Default is set to False."""
        if permanent == True:
            self.scrap_list[i].text = self.scrap_list[i].text.replace("\n","").strip() 
        else:
            return self.scrap_list[i].text.replace("\n","").strip()
    