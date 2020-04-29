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



### You can view which element tags are available on the website which can be used for scraping by element 
### It would benefit you to know some HTML in order to find which elements you want to scrape.

tags = sc.tag_list  

# Scrapalayze class object (Scrap)

### The Scrap internal methods have been altered, but an updated README is coming soon...



