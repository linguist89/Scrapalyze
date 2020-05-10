import string

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
                 vocab=False,
                 remove_punctuation=True):
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
            tokenized_contents = [l for l in tokens_list if l]
        elif vocab == True:
            tokenized_contents = list(set([subl for l in tokens_list for subl in l]))
        if remove_punctuation == True:
            tokenized_contents = self.remove_punctuation(tokenized_contents)
        return tokenized_contents
        
    def remove_punctuation(self,
                           temp_contents):
        """
        Removes all the punctuation from a string or a list.
        """
        if isinstance(temp_contents, str):
            filtered_content = ""
            for char in temp_contents:
                if char not in string.puntuation:
                    filtered_content += char
            return filtered_content
        elif isinstance(temp_contents, list):
            filtered_list = []
            for e in temp_contents:
                temp_string = ""
                for char in e:
                    if char not in string.punctuation:
                        temp_string += char
                filtered_list.append(temp_string)
            return filtered_list
            
        
        
        