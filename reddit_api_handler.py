from config import Scrapper

# Local variables
subreddit = 'MachineLearning'  # To be passed via. user interface
post_limit = 10  # Static list count
show_top_comments = False
number_of_comments = 5

scrapper = Scrapper()
reddit = scrapper.initialize_praw()

def get_post(subreddit):
    """
    Get posts under subbreddit using praw
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


def show_post_lists(count, subreddit, type):
    """
    Get top treding post using Beautifulsoap web scrapper
    @param count: Count of the posts
    @param subreddit:
    @param type: Hot, New, Best etc
    @return:
    """
