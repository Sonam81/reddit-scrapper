import requests
from bs4 import BeautifulSoup

# send a request to reddit.com

def list_popular(url):

    post_title = ''
    posts = []
    response = requests.get(url)
    html_content = response.content

    # create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")
    post_permalink = ''
    all_content = soup.find_all('div', {'class' : 'Post'})

    for content in all_content:
        titles = content.find('h3')
        if titles is not None:
            post_title = titles.text

        comment_link = content.find('a', {'data-click-id' : 'comments'})
        if comment_link is not None:
            post_permalink = comment_link['href']

        post_id = post_permalink[post_permalink.find('/comments/') + 10:]
        post_id = post_id[0: post_id.find('/')]

        post_permalink = 'https://www.reddit.com' + post_permalink
        post_detail = {
            'id': post_id,
            'title': post_title,
            'permalink': post_permalink
        }
        posts.append(post_detail)
        print(post_title, post_permalink,"permalink")
    return posts

