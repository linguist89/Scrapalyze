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
            
            
    # Removes a single newline character from the string
    def clean(self,
              internal_contents,
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
            words = nltk.word_tokenize(internal_contents)
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
            return internal_contents