from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
import re
import nltk
nltk.download('punkt')
import scrap_v2

class Scrapalyze:
    def __init__(self, url):
        self.url = url
        self.get_soup(url)
    
    # Create the soup
    def get_soup(self, url):
        # Get the soup
        agent = {"User-Agent":"Mozilla/5.0"}
        response = requests.get(url, headers=agent)
        self.soup = bs(response.text, 'lxml')
        
        
    # Single scrape of a website, but also enables element-level and attribute-level search
    def scrape_by_element(self, **kwargs):
        """
        Scrapes website self.url and returns a parsed HTML document.
        The results will be contained in a list.

        **kwargs:    
        element: change to whichever element you are searching for in the soup.

        attribute_type: change to whichever attribute_type you are searching for in the soup.

        attribute_content: change to whichever attribute_content you are searching for in the soup.

        """
        # Set the kwargs defaults to empty strings (so that they can pass the logic tests if the user doesn't enter values)
        kwargs.setdefault('element',"")
        kwargs.setdefault('attribute_type',"")
        kwargs.setdefault('attribute_content',"")
            

        # Options to search for a specific element with or without attributes specificed
        # Returns as default
        if kwargs['element']:
            if kwargs['attribute_type']:
                find_object = self.soup.find_all(kwargs['element'],attrs={kwargs['attribute_type']:kwargs['attribute_content']})
                return scrap_v2.Scrap(find_object)
            else:
                find_object = self.soup.find_all(kwargs['element'])
                return scrap_v2.Scrap(find_object)
        else:
            return self.soup