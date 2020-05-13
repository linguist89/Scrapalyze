import string

class analyze:
    
    def __init__(self, contents):
        self.contents = contents
        
        
    def print_all(self,
                  remove_punctuation=False):
        """
        Prints all the elements in the contents in a format that is similar to how the website looks. 
        The purpose is to be able to navigate the layers to determine which elements you need to scrape.
        remove_punctuation (default False): set to True to remove all punctuation as listed in string.punctuation
        """
        if remove_punctuation == False:
            for element in self.contents:
                if not isinstance(element,str):
                    print(element.text.strip())
                else:
                    print(element.strip())
        elif remove_punctuation == True:
            filtered_contents = self.remove_punctuation(self.contents)
            for element in filtered_contents:
                if not isinstance(element,str):
                    print(element.text.strip())
                else:
                    print(element.strip())
          
                
    def tokenize(self,
                 vocab=False,
                 remove_punctuation=True,
                 remove_stopwords=True):
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
        if remove_stopwords == True:
            tokenized_contents = self.remove_stopwords(tokenized_contents)
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
                if not isinstance(e, str):
                    e = e.text
                for char in e:
                    if char not in string.punctuation:
                        temp_string += char
                filtered_list.append(temp_string)
            return filtered_list
        
    def remove_stopwords(self,
                         temp_contents):
        """
        Removes all the stopwords from a string or a list.
        """
        stopwords = {"ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during", "out", "very",
                     "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such", "into", "of", "most",
                     "itself", "other", "off", "is", "s", "am", "or", "who", "as", "from", "him", "each", "the", "themselves", 
                     "until", "below", "are", "we", "these", "your", "his", "through", "don", "nor", "me", "were", "her", "more", 
                     "himself", "this", "down", "should", "our", "their", "while", "above", "both", "up", "to", "ours", "had", "she",
                     "all", "no", "when", "at", "any", "before", "them", "same", "and", "been", "have", "in", "will", "on", "does", 
                     "yourselves", "then", "that", "because", "what", "over", "why", "so", "can", "did", "not", "now", "under", "he",
                     "you", "herself", "has", "just", "where", "too", "only", "myself", "which", "those", "i", "after", "few", "whom",
                     "t", "being", "if", "theirs", "my", "against", "a", "by", "doing", "it", "how", "further", "was", "here", "than"}
           
        if isinstance(temp_contents, str):
            filtered_content = ""
            for word in temp_contents.split():
                if word.lower() not in stopwords:
                    filtered_content += word
            return filtered_content
        elif isinstance(temp_contents, list):
            filtered_list = []
            for e in temp_contents:
                temp_string = ""
                if not isinstance(e, str):
                    e = e.text
                for word in e.split():
                    if word.lower() not in stopwords:
                        temp_string += word
                filtered_list.append(temp_string)
            filtered_list = [e for e in filtered_list if e]
            return filtered_list 
        
        