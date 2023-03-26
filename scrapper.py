import requests
from bs4 import BeautifulSoup

# send a request to the BBC News homepage and get the HTML content
url = "https://www.reddit.com"
response = requests.get(url)
html_content = response.content

# create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

title = ''
href = ''
all_content = soup.find('div', {'class' : 'Post'})
for content in all_content:
    titles = content.find('h3')
    if titles is not None:
        title = titles.text

    comment_link = content.find('a', {'data-click-id' : 'comments'})
    if comment_link is not None:
        href = comment_link['href']


print(title, href)




