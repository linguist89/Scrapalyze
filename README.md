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
### Running a method such as scrape_by_element returns a Scrapalyze object called a Scrap In these two examples, the variables "title" and "p" are Scrap classes which contain their own internal methods

## Create Scrap two scrap objects ("p" and "title")

title = sc.scrape_by_element(element="title")  
p = sc.scrape_by_element(element='p')   


## Print text of those objects

#This will print the text of the title of the website without any formatting  
print(title.clean())

#This removes the punctuation and prints the text of the first p element (i.e. p[0])  
print(p.clean(remove_punct=True))

#This removes the punctuation, tokenizes the sentence and prints each word of the second p element (i.e. p[1])  
print(p.clean(i=2, remove_punct=True, tokenize=True))

#This removes the punctuation, makes all letters lowercase and prints the text of the third p element (i.e. p[2])  
print(p.clean(i=3, remove_punct=True, lower=True))



