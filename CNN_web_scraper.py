# This is a program that scrapes the title, updated date, byline of a article
import requests
from bs4 import BeautifulSoup

# gets url from user and request html from website
url = str(input("Please enter CNN URL: "))
response = requests.get(url)

# Parse the html to get the content we want
soup = BeautifulSoup(response.text, 'html.parser')
article_title = soup.title
article_author = soup.find(class_ ='byline__name')
article_date = soup.find('div', class_ ='timestamp')
# article contents are 
article_contents = soup.find_all('p', class_ ='paragraph inline-placeholder')


print(f"Title: {article_title.text}")
print(f"\nAuthor: {article_author.text}")
print(f"\nUpdated Date: {article_date.text}")
for num in article_contents:
    print(f"\n{num.text}")


# Writes the article into a tect file
with open('CNN_article.txt', 'w') as i:
    i.write(f"Title: {article_title.text}")
    i.write(f"\nAuthor: {article_author.text}")
    i.write(f"\nUpdated Date: {article_date.text}")

    for num in article_contents:
        i.write(f"\n{num.text}")