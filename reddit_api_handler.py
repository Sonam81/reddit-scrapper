from config import Scrapper

scrapper = Scrapper()
reddit = scrapper.initialize_praw()

def get_posts(subreddit, type='top', post_limit=10):
    """
    Get posts under subbreddit using praw
    @param subreddit: Name of subreddit
    @return: Post details in JSON
    """
    return_posts = []

    if type == 'hot':
        all_posts = reddit.subreddit(subreddit).hot(limit=post_limit)
    elif type == 'new':
        all_posts = reddit.subreddit(subreddit).new(limit=post_limit)
    else:
        all_posts = reddit.subreddit(subreddit).top(limit=post_limit)

    for post in all_posts:
        post_title = post.title
        post_id = post.id
        post_permalink = 'https://www.reddit.com' + post.permalink
        post_detail = {'id': post_id, 'title': post_title, 'permalink': post_permalink}
        return_posts.append(post_detail)
    return {'posts': return_posts}

