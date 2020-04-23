# Scrapalyze

A module designed to easily scrape and analyze HTML pages. 

# Installation instructions

### If you are using this from your own computer, make sure to have the latest versions of BeautifulSoup, selenium and requests installed.

git clone https://github.com/linguist89/scrapalyze.git  
pip install selenium  
cd scrapalyze  
import Scrapalyze  

### If running from within a Jupyter Notebook or Google Colab then use the following commands:

!git clone https://github.com/linguist89/scrapalyze.git  
!pip install selenium  
%cd scrapalyze  
import Scrapalyze  

# Scrapalyze class

The base scrapalyze class will contain the raw HTML of the website along with methods that give the user the ability to scrape further information based upon element tags or navigation via webdrivers. 

### Example of a Scrapalyze class instantiation

sc = Scrapalyze.Scrapalyze("https://github.com/")

### You can view which element tags are available on the website which can be used for scraping by element 

tags = sc.tag_list  

# Scrapalayze class object (Scrap)

### The Scrap internal methods have been altered, but an updated README is coming soon...



