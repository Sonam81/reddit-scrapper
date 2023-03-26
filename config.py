import praw

# Static credentials variables
CLIENT_ID = '9HTI4YX0Ihyxzph4fAlRgA'
CLIENT_SECRET = 'tctPR9XUh7igfSgX13au99marGEmLA'
USER_AGENT = 'webscrapy'


class Scrapper:

    def initialize_praw(self):
        reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT)
        return reddit
