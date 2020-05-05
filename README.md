# Scrapalyze

A module designed to easily scrape and analyze HTML pages. 

# Installation instructions

### If you are using this from your own computer, make sure to have the latest versions of BeautifulSoup, selenium and requests installed.

git clone https://github.com/linguist89/scrapalyze.git  
pip install selenium  
cd scrapalyze  
import Scrapalyze  

### Running in Google Colab
!git clone https://github.com/linguist89/scrapalyze.git  
!pip install selenium  
%cd scrapalyze  
import Scrapalyze  

### Running on your own PC in Jupyter Notebook
### Important: run the first three lines only once. Otherwise it will keep cloning the git and creating nested folders each time your run the code.

!git clone https://github.com/linguist89/scrapalyze.git  
!pip install selenium  
%cd scrapalyze  
import Scrapalyze


# Scrapalyze class

The base scrapalyze class will contain the raw HTML of the website along with methods that give the user the ability to scrape further information based upon element tags or navigation via webdrivers. 

### Scrapalyze class instantiation
Scrapalyze scrapes the entire HTML of a website using BeautifulSoup. The class instance, in this case "sc", has class methods which are used to further scrape elements in a more specific way. The results of these scrapes are elements in themselves (they are individually called "Scrap") and have their own internal methods.

sc = Scrapalyze.Scrapalyze("https://github.com/", fast=True, show_stats=True)

Scrapalyze arguments:  
fast: boolean (default is True). Set this to False if you want to investigate how the site is scraped. If you already know which elements you want to scrape then set it to True.  
show_stats: boolean (default is True). This will display rough statistics when scraping specific elements i.e. how many HTML elements are in the Scrap, how many layers are in the HTML tree, etc. Set this to False if you don't need to see the stats.  


### Finding what to scrape - tag_list
You can view which element tags are present on the website that can be used for scraping by element. It would benefit you to know some HTML in order to find which elements you want to scrape, but mainly just looking at the HTML code of the website and finding the element will be sufficient. The tag_list simply makes navigation easier.  

tags = sc.tag_list  

### Scraping links from the initial website
If you want to scrape the links from the website use the scrape_links method (see the example below). This method contains parameters that filter which websites it will return.  

sc.scrape_links(filter_links=['github']) # This will scrape will links that contain with word 'github'  

You can also use regular expression by changing the regex parameter to True.  

sc.scrape_links(filter_links=['^https'], regex=True) # This will scrape only links that begin with 'https'  



# Scrapalayze class object (Scrap)

Scraps are class objects that are instantiated from the results of a Scrapalyze method. They methods that for filtering, formatting and analyzing the data passed in as arguments (this is called the Scrap's contents). Following is an example of creating an instance of a Scrap class:  

article = sc.scrape_by_element(element='article')



### Displaying the stats of a Scrap and displaying the contents
The stats property displays the number of HTML elements inside the Scrap's contents. If Scrap was instantiated with fast=False then it will also display the number of layers present in the Scrap's contents.

article.stats # This will display the stats
article.contents # The output of this is a list

## Scraping embedded layers
The embedded layers in a Scrap object refers to the structure of an HTML document's tree layout. Each layer would be equivalent to a subdirectory or branch within the HTML document layout.  

### Slow scrape
Slow scraping simply means that the method will scrape all the layers of the Scrap's contents. This method is automatically called when the Scrap class is instantiated with the fast parameter set to False. It can however be manually called if the need arises.  

article.slow_scrape_embedded_layers()  

The results are contained in a dictionary. The layer number is the key and the value is a tuple: first element is a list of the tags in the layer and the second element are all the BeautifulSoup elements in the layer. The following is an example:  

first_layer_elements = article.embedded_layers[1][1] # This will be a list of BeautfilSoup elements

### Filter embedded layers
It's useful to have a section of HTML scraped, but for most projects the internal elements of that section need to be further filtered. A Scrap method called filter_embedded_layers can help with this task. The result is a list of BeautifulSoup elements. Here are some examples:

article.filter_embedded_layers(layer=3, specify=['p']) # This will scrape all the p elements from layer 3

article.filter_embedded_layers(layer=3, specify=['h1'])[0].text # This will display the text of the first h1 element in layer 3




