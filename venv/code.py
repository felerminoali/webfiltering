#import re #import our regex module
from bs4 import BeautifulSoup

def cleanMe(html):
    soup = BeautifulSoup(html, "html.parser") # create a new bs4 object from the html data loaded
    for script in soup(["script", "style"]): # remove all javascript and stylesheet code
        script.extract()
    # get text
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text

def createDataset(siteRmoved):

    with open(siteRmoved, 'r') as myfile:
        htmlFile = myfile.read()
    cleaned = cleanMe(htmlFile)

    filename = siteRmoved.split(".")[0]+".txt"
    with open(filename, 'wb') as f:
        f.write(cleaned.encode('utf8'))
    #self.log('Saved file %s' % filename)
    pass

sitelist = ['data.html','data1.html']
while len(sitelist)>0:
    siteRemoved = sitelist.pop()
    createDataset(siteRemoved)