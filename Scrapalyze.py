from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  

class Scrapalyze:
    def __init__(self, url):
        self.url = url
        self.get_tag_list()
        
    # Get a list of the documents HTML tags
    def get_tag_list(self):
        """
        Create a list of tags from all the unique tags in the document.
        This is useful for navigation purpose and getting an overview of what tags are in the document.
        """
        # Get the soup
        agent = {"User-Agent":"Mozilla/5.0"}
        response = requests.get(self.url, headers=agent)
        soup = bs(response.text, 'lxml')
        
        # Creates a list of all the tags in the HTML, sorts them and outputs the resutling list.
        page_list = list(soup.descendants)
        self.tag_list = []
        for token in page_list:
            if not isinstance(token, str):
                self.tag_list.append(token.name)
        self.tag_list = sorted(list(set(self.tag_list)))
        return self.tag_list
        
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
        # Get the soup
        agent = {"User-Agent":"Mozilla/5.0"}
        response = requests.get(self.url, headers=agent)
        soup = bs(response.text, 'lxml')

        # Set the kwargs defaults to empty strings (so that they can pass the logic tests if the user doesn't enter values)
        kwargs.setdefault('element',"")
        kwargs.setdefault('attribute_type',"")
        kwargs.setdefault('attribute_content',"")
            

        # Options to search for a specific element with or without attributes specificed
        # Returns as default
        if kwargs['element']:
            if kwargs['attribute_type']:
                find_object = soup.findAll(kwargs['element'],attrs={kwargs['attribute_type']:kwargs['attribute_content']})
                return Scrap(find_object)
            else:
                find_object = soup.findAll(kwargs['element'])
                return Scrap(find_object)
        else:
            return soup


    # Single scrape of a website through using xpath
    def scrape_by_css(self, **kwargs):
        """
        Scrapes website self.url and returns a parsed HTML document.
        The search is done through css selector as opposed to the single_scrape which
        searches by using elements and attributes. The results will be contained in a list.

        **kwargs:  
        css_selector: change to whichever object you are searching for.
        """
        # Get the soup
        agent = {"User-Agent":"Mozilla/5.0"}
        response = requests.get(self.url, headers=agent)
        soup = bs(response.text, 'lxml')

        # Set the kwargs defaults to empty strings (so that they can pass the logic tests if the user doesn't enter values)
        kwargs.setdefault('css_selector',"")


        # Find object based on css selector otherwise return soup
        if kwargs['css_selector']:
            try:
                find_object = soup.select(kwargs['css_selector'])
            except:
                find_object = "Cannot find the object. Check your css_selector."
            return find_object
        else:
            return soup


    # Scrape all the links from a page based upon specified criteria
    def scrape_links(self, **kwargs):
        """
        Scrapes self.url and returns all the links on that website.
        Keyword arguments can be passed to specify which part of the website should be scraped
        for urls. The results will be contained in a list.

        **kwargs:
        element: change to whichever element you are searching for in the soup.

        attribute_type: change to whichever attribute_type you are searching for in the soup.

        attribute_content: change to whichever attribute_content you are searching for in the soup.
        """
        # Get soup
        agent = {"User-Agent":"Mozilla/5.0"}
        response = requests.get(self.url, headers=agent)
        soup = bs(response.text, 'lxml')

        # Set the kwargs defaults to empty strings (so that they can pass the logic tests if the user doesn't enter values)
        kwargs.setdefault('element',"")
        kwargs.setdefault('attribute_type',"")
        kwargs.setdefault('attribute_content',"")

        # Get links to specific elements on a page
        # If left blank then it will scrape all the links from that page
        if kwargs['element'] and kwargs['attribute_type']:
            element = scrape_element(self.url, 
                                     element=kwargs['element'], 
                                     attribute_type=kwargs['attribute_type'],
                                     attribute_conent=kwargs['attribute_content'])
        elif kwargs['element']:
            element = scrape_element(self.url, element=kwargs['element'])
        else:
            element = scrape_element(self.url)
        try:
            links_list = element.findAll('a')
            links_list = [link.get('href') for link in links_list]
        except:
            links_list = "There was an error."
        return links_list

    # Remotely enter input into a search box or click a link then scrape the resulting page.
    def scrape_selenium_css(self, **kwargs):
        """
        Creates a webdriver, navigates to self.url, finds element by css_selector and
        passes key as an argument to the send_keys function. Returns the resulting page as a soup.
        The results will be contained in a list.
        **kwargs:
        css_selector: default is empty string

        key: default is empty string

        headless: True/False whether you want the webdriver to be headless. Default is True.

        """
        # Set the kwargs defaults to empty strings (so that they can pass the logic tests if the user doesn't enter values)
        kwargs.setdefault('css_selector',"")
        kwargs.setdefault('key',"")
        kwargs.setdefault('action_type',"")
        kwargs.setdefault('headless', True)

        # Launch the webdriver which in this case is a chromedriver
        # Headless feature if you don't want the window to appear
        if kwargs['headless'] == True:        
            chrome_options = Options()  
            chrome_options.add_argument("--headless")         
            driver = webdriver.Chrome("chromedriver.exe", options=chrome_options)
        else:
            driver = webdriver.Chrome("chromedriver.exe")
        driver.get(self.url)

        if kwargs['action_type'] == "search":
            # Search for the element and insert the specified key
            elem = driver.find_element_by_css_selector(kwargs['css_selector'])
            elem.clear()
            elem.send_keys(kwargs['key'])
            elem.send_keys(Keys.RETURN)
        elif kwargs['action_type'] == "click_link":
            # Click on a link and navigate to that page.
            elem = driver.find_element_by_css_selector(kwargs['css_selector'])
            elem.click()

        # Creates a soup of the page and returns the whole soup
        page_soup = bs(driver.page_source, 'lxml')
        driver.close()
        return page_soup