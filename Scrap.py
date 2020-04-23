import nltk

# A Scrap is an object from a Scrapalyze method
class Scrap:
    """
    A Scrap is a class that contains specific methods for formatting the results of Scrapalyze methods.
    """
    
    # Initializes the scrap with the list scraped from the Scrapalyze class
    def __init__(self, contents):
        self.contents = contents
        self.scrape_embedded_elements()
        self.num_layers = self.number_of_embedded_layers()
    
    # Display standard statistics for the Scrap
    @property
    def stats(self):
        """
        Stats is a property fuction that outputs statistics about the element you scraped.
        """
        # Length of contents
        print("Contents length is: {}".format(len(self.contents)))   
        
        # Number of embedded layers
        print("The number of embedded layers is: {}".format(self.num_layers))
        
    
    # Display the article as it was scraped
    def raw(self):
        """
        Display prints each entry in the contents.
        """
        for entry in self.contents:
            print(entry)
            
    # Display all the tags within the scraped tag
    @property
    def internal_tags(self):       
        """
        Internal tags is a property function that outputs the name of the tags within the element that you scraped.
        Use internal_scrape to further refine your scrapes.
        """
        tag_list = []
        for element in self.contents:
            for token in element:
                if not isinstance(token, str):
                    tag_list.append(token.name)
        tag_list = sorted(list(set(tag_list)))
        return tag_list
    
    # Determine the number of layers embedded elements in the contents
    def number_of_embedded_layers(self):
        i = 1
        end = 1
        while i == end:
            end = self.scrape_embedded_elements(layer=i)[2]
            i += 1
        return end
            
    # Scrap tags based upon their layers of embedding
    def scrape_embedded_elements(self, 
                                 layer = 1):
        """
        Iterates through the contents of the initiliazed list.
        Extracts all embedded tags and element for easy internal navigation.
        """
        contents = self.contents
        end = 1
        for i in range(layer):
            layer_tags = []
            layer_elements = []
            for element in contents:
                if not isinstance(element, str):
                    for child in list(element.children):
                        layer_tags.append(child.name)
                        layer_elements.append(child)
                layer_tags = list(set(layer_tags))
                later_elements = list(set(layer_elements))
            contents = layer_elements
            if contents != []:
                end = i
            else:
                layer_elements = "There are no more layers"
                layer_tags = "There are no more layers"
        return layer_tags,layer_elements,end
    
    # Print the scraped embedded elements
    def embedded_scrapes(self, 
                         layer=1, 
                         specify=[],
                         tags_elements=1):
        """
        Returns the elements or tags of an embedded layer.
        layer: default 1. Displays the first layer of elements. 
        Each increment represents 1 layer i.e. 3 is the third layer of embedded elements.
        specify: default empyt list. Add any HTML tags in the list to display only those elements.
        tags_elements: default 1. Change to 0 if you want to return tags instead of full elements.
        """        
        scrape_results = []
        if not isinstance(self.scrape_embedded_elements(layer=layer)[tags_elements], str):
            for element in self.scrape_embedded_elements(layer=layer)[tags_elements]:
                if specify != []:
                    for s in specify:
                        if element.name == s:
                            scrape_results.append(element)
                else:
                    scrape_results.append(element)
            return scrape_results
        else:
            return self.scrape_embedded_elements(layer=layer)[tags_elements]
                                        
        
    
    # Filter out any unwanted elements in the contents
    def filter_contents(self,
                        exclude=[],
                       permanent=False):
        """
        This contains the contents of the initial scrape.
        permanent: default False. Set to true to make the changes permanent.
        """
        if exclude:
            for token in self.contents:
                for child in token.children:
                    for e in exclude:
                        if child.name != e and child.name != None:
                            print(child.name)
                            print(e)
                            print("========")
        else:
            return self.contents
        
            
    
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
        # Remove punctuation from contents element's text
        if remove_punct == True:
            words = nltk.word_tokenize(self.contents[i].text)
            if tokenize == True:
                if lower == True:
                    new_words = [word.lower() for word in words if word.isalnum()]
                else:                  
                    new_words = [word for word in words if word.isalnum()]
            else:
                if lower == True:
                    new_words = ' '.join([word.lower() for word in words if word.isalnum()])
                else:                  
                    new_words = ' '.join([word for word in words if word.isalnum()])                
            return new_words
        else:
            return self.contents[i].text
        
        

        
    
    