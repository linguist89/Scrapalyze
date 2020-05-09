import nltk

class analyze:
    
    def __init__(self, contents):
        self.contents = contents
        
        
    def print_all(self):
        """
        Prints all the elements in the contents in a format that is similar to how the website looks. 
        The purpose is to be able to navigate the layers to determine which elements you need to scrape.
        """
        for element in self.contents:
            if not isinstance(element,str):
                print(element.text.strip())
            else:
                print(element.strip())
                
    def tokenize(self,
                 vocab=False):
        """
        Tokenizes the contents and outputs as a 2-d list with each sentence a list of tokens.
        vocab (default False): set to True to get a list of all vocab items.
        """
        tokens_list = []
        for element in self.contents:
            if not isinstance(element,str):
                tokens_list.append(element.text.split())
            else:
                tokens_list.append(element.split())
        if vocab == False:
            return [l for l in tokens_list if l]
        elif vocab == True:
            return list(set([subl for l in tokens_list for subl in l]))