import string
from collections import Counter

class analyze:
    
    def __init__(self, contents):
        self.contents = contents
        
        
    def print_all(self,
                  remove_punctuation=False,
                  remove_stopwords=False,
                  make_lowercase=False,
                  sw='default',
                  custom_stopwords=[]):
        """
        Prints all the elements in the contents in a format that is similar to how the website looks. 
        The purpose is to be able to navigate the layers to determine which elements you need to scrape.
        
        remove_punctuation (default False): set to True to remove all punctuation as listed in string.punctuation
        remove_stopwords (default False): set to True to remove all stopwords from the contents based upon the list of NLTK stopwords.
        sw: three options default, edit and new. 
            Default will use the stopwords available in the script. 
            Edit will add (to the current stopwords) whichever stopwords are included as a list in the custom_stopwords argument.
            New will only include the stopwords which are contained in the custom_stopwords list.
        custom_stopwords (default empty list): add list of stopwords and set the sw parameter to edit or new.
        """
        if self.contents == "There are no more layers":
            return self.contents
        printable_contents = []
        if remove_punctuation == False:
            for element in self.contents:
                if not element:
                    break
                if not isinstance(element,str):
                    printable_contents.append(element.text.strip() + " ")
                else:
                    printable_contents.append(element.strip() + " ")
        elif remove_punctuation == True:
            filtered_contents = self.remove_punctuation(self.contents)
            for element in filtered_contents:
                if not isinstance(element,str):
                    printable_contents.append(element.text.strip())
                else:
                    printable_contents.append(element.strip())
                    
        if remove_stopwords == True:
            printable_contents = self.remove_stopwords(printable_contents,
                                                       sw,
                                                       custom_stopwords)
        if make_lowercase == True:
            printable_contents = self.make_lowercase(printable_contents)
            
        if isinstance(printable_contents, str):
            print(printable_contents)
        elif isinstance(printable_contents, list):
            for e in printable_contents:
                print(e)
                
    def tokenize(self,
                 vocab=False,
                 vocab_count=False,
                 remove_punctuation=False,
                 remove_stopwords=False,
                 make_lowercase=False,
                 sw='default',
                 custom_stopwords=[]):
        """
        Tokenizes the contents and outputs as a 2-d list with each sentence a list of tokens.
        vocab (default False): set to True to get a list of all vocab items instead of the 2-d list of tokenized sentences.
        vocab_count (default False): set both vocab and vocab_count to True to get a vocab list with the counts of each unique item. 
        
        remove_punctuation (default False): set to True to remove all punctuation as listed in string.punctuation
        remove_stopwords (default False): set to True to remove all stopwords from the contents based upon the list of NLTK stopwords.
        make_lowercase (default False): set to True to make all characters lowercase. 
        sw: three options default, edit and new. 
            Default will use the stopwords available in the script. 
            Edit will add (to the current stopwords) whichever stopwords are included as a list in the custom_stopwords argument.
            New will only include the stopwords which are contained in the custom_stopwords list.
        custom_stopwords (default empty list): add list of stopwords and set the sw parameter to edit or new.
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
            if isinstance(tokenized_contents,str):
                tokenized_contents = self.remove_punctuation(tokenized_contents)
            else:
                new_contents = []
                for element in tokenized_contents:                    
                    temp_contents = self.remove_punctuation(element)
                    new_contents.append(temp_contents)
                tokenized_contents = new_contents
                
        if remove_stopwords == True:
            tokenized_contents = self.remove_stopwords(tokenized_contents,
                                                       sw,
                                                       custom_stopwords)
        if make_lowercase == True:
            tokenized_contents = self.make_lowercase(tokenized_contents)
  
        if vocab_count == True and vocab == True:
            tokenized_contents = list(Counter(tokenized_contents).items())
            return sorted(tokenized_contents,key=lambda x: x[1], reverse=True)
        else:   
            return tokenized_contents
        
    def remove_punctuation(self,
                           temp_contents):
        """
        Removes all the punctuation from a string or a list.
        Punctuation list comes from string.punctuation
        """
        if isinstance(temp_contents, str):
            filtered_content = ""
            for char in temp_contents:
                if char not in string.punctuation:
                    filtered_content += char
            return filtered_content
        elif isinstance(temp_contents, list):
            filtered_list = []
            for e in temp_contents:
                if e:
                    temp_string = ""                
                    if not isinstance(e, str):
                        e = e.text
                    for char in e:
                        if char not in string.punctuation:
                            temp_string += char
                    filtered_list.append(temp_string)
            return filtered_list
        
    def remove_stopwords(self,
                         temp_contents,
                         sw,
                         custom_stopwords):
        """
        Removes all the stopwords from a string or a list.
        sw: three options default, edit and new. 
            Default will use the stopwords available in the script. 
            Edit will add (to the current stopwords) whichever stopwords are included as a list in the custom_stopwords argument.
            New will only include the stopwords which are contained in the custom_stopwords list.
        custom_stopwords (default empty list): add list of stopwords and set the sw parameter to edit or new.
        """
        
        stopwords = {"ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during", "out","very",
                     "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such", "into",
                     "of","most","itself", "other", "off", "is", "s", "am", "or", "who", "as", "from", "him", "each", "the",
                     "themselves","until", "below", "are", "we", "these", "your", "his", "through", "don", "nor", "me", "were", 
                     "her", "more","himself", "this", "down", "should", "our", "their", "while", "above", "both", "up", "to", 
                     "ours", "had", "she", "all", "no", "when", "at", "any", "before", "them", "same", "and", "been", "have", 
                     "in", "will", "on", "does", "yourselves", "then", "that", "because", "what", "over", "why", "so", "can", 
                     "did", "not", "now", "under", "he", "you", "herself", "has", "just", "where", "too", "only", "myself", 
                     "which", "those", "i", "after", "few", "whom","t", "being", "if", "theirs", "my", "against", "a", "by", 
                     "doing", "it", "how", "further", "was", "here", "than"}
        if sw != 'default':
            custom_stopwords = [word.lower() for word in custom_stopwords]
            if sw == 'edit':
                stopwords = set(list(stopwords) + custom_stopwords)
            elif sw == 'new':
                stopwords = set(custom_stopwords)

        if isinstance(temp_contents, str):
            filtered_content = ""
            for word in temp_contents.split():
                if word.lower() not in stopwords:
                    filtered_content += word + " "
            return filtered_content
        elif isinstance(temp_contents, list):
            filtered_list = []
            for e in temp_contents:
                temp_string = ""
                temp_list = []
                if not isinstance(e, list):
                    if not isinstance(e, str):
                        e = e.text
                    for word in e.split():
                        if word.lower() not in stopwords:
                            temp_string += word + " "
                    filtered_list.append(temp_string)
                elif isinstance(e, list):
                    for word in e:
                        if word.lower() not in stopwords:
                            temp_list.append(word)
                    filtered_list.append(temp_list)
            filtered_list = [e for e in filtered_list if e]
            return filtered_list 
        
    def make_lowercase(self,
                       temp_contents):
        """
        Converts all the characters in the contents to lowercase.
        """
        if isinstance(temp_contents, str):
            filtered_content = temp_contents.lower()
            return filtered_content
        elif isinstance(temp_contents, list):
            filtered_list = []
            for e in temp_contents:
                if isinstance(e, str):
                    temp = e.lower()
                elif isinstance(e, list):
                    temp = [word.lower() for word in e]                        
                filtered_list.append(temp)
            return filtered_list
        
        