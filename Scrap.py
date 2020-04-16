import nltk

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
        """
        Stats is a property fuction that outputs statistics about the element you scraped.
        """
        print("The length of your scrap_list is: " + str(len(self.scrap_list)))
        
    # Display the article as it was scraped
    def display(self):
        """
        Display prints each entry in the scrap_list.
        """
        for entry in self.scrap_list:
            print(entry)
            
    # Display all the tags within the scraped tag
    @property
    def internal_tags(self):       
        """
        Internal tags is a property function that outputs the name of the tags within the element that you scraped.
        Use internal_scrape to further refine your scrapes.
        """
        tag_list = []
        for element in self.scrap_list:
            for token in element:
                if not isinstance(token, str):
                    tag_list.append(token.name)
        tag_list = sorted(list(set(tag_list)))
        return tag_list
    
    # Scrape internally based upon internal tags
    def internal_scrape(self, element):
        """
        Scrape the internal elements from a scrap_list.
        This will ouput them as a list with each element of scrap_list returning either a result or none.
        Best used after looking at results of internal_tags.
        """
        iscrape = []
        for scrap in self.scrap_list:
            iscrape.append(scrap.find(element))
        
        return iscrape
    
    # Removes a single newline character from the string
    def clean(self, 
              i=0,
             remove_punct=False,
             tokenize=False,
             lower=False):
        """
        remove_punct: default False. If set to True, removes punctuation from the text of the scraped element. 
        tokenize: default False. If set to True, returns the text as a list of tokens.
        lower: default False. If set to True, returns the tokens all in lower case.
        If set to false, ouputs only the text of the element without any formatting.
        """
        # Remove punctuation from scrap_list element's text
        if remove_punct == True:
            words = nltk.word_tokenize(self.scrap_list[i].text)
            if tokenize == True:
                if lower == True:
                    new_words = [word.lower() for word in words if word.isalnum()]
                else:                  
                    new_words = [word for word in words if word.isalnum()]
            else:
                new_words = ' '.join([word for word in words if word.isalnum()])
            return new_words
        else:
            return self.scrap_list[i].text
        
        

        
    
    