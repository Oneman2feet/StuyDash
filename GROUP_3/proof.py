import urllib2
from bs4 import BeautifulSoup

url='http://allrecipes.com/Recipe/Homemade-Mac-and-Cheese/Detail.aspx?src=rotd'

result = urllib2.urlopen(url).read()
soup = BeautifulSoup(result)
#print (soup.prettify())


def ingredients(recipe):
    """
    Gets a list of all the ingredients in any given recipe
    """
    soup = BeautifulSoup(urllib2.urlopen(recipe).read())
    
    a = soup.findAll(True, {'class':"ingredient-name"})
    b = []
    for item in a:
        b.append(str(item.contents[0]))
    return b

"""
print ingredients('http://allrecipes.com/recipe/brownie-frosting/detail.aspx?event8=1&prop24=SR_Title&e11=brownies&e8=Quick%20Search&event10=1&e7=Home%20Page')
I removed the unneccessary parameters from the URL to make it easier to use
with future code, but I'll keep the long one commented in case we need it
in the future. -Brian
"""
print ingredients("http://allrecipes.com/recipe/brownie-frosting/detail.aspx")

#Tried functionality of shortened URL with other recipe, seems to work great
print ingredients("http://allrecipes.com/recipe/vegan-cupcakes/detail.aspx")
