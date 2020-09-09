import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    consumer_key = os.getenv("uPBDslYCyQ9HbpX2VFZDRgVvu")
    consumer_secret = os.getenv("y84eMnuYIjf0IymL9OzBsP0qkX3eidcCzCapoyJt5DVxDQ3OS2")
    access_token = os.getenv("1302423402007887878-NSgDYnVwMMRTIOABrvdP75iNjJsW98")
    access_token_secret = os.getenv("DRNJDMm6nIn6MJViZXjinFAzYJ49soxFXhcZXXVjGZU0N")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api