import praw

# Static credentials variables
CLIENT_ID = 'vXaDMPsCx7IV-Nu97QBKcg'
CLIENT_SECRET = 'xf2hv2gDIae2Ljbi7Jn7sSqU-HDoSg'
USER_AGENT = 'post-webscrapper'

# Build reddit object
reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT)

# Local variables
subreddit = 'MachineLearning'  # To be passed via. user interface
post_limit = 10  # Static list count
show_top_comments = False
number_of_comments = 5


def get_post(subreddit):
    """
    @param subreddit: Name of subreddit
    @return: Post details in JSON
    """
    hot_posts = reddit.subreddit(subreddit).hot(limit=post_limit)
    posts = []
    for post in hot_posts:
        post_title = post.title
        post_id = post.id
        post_permalink = 'https://www.reddit.com' + post.permalink
        post_detail = {'id': post_id, 'title': post_title, 'permalink': post_permalink}
        posts.append(post_detail)
    return {'posts': posts}

