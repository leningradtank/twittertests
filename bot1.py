import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("uPBDslYCyQ9HbpX2VFZDRgVvu", "y84eMnuYIjf0IymL9OzBsP0qkX3eidcCzCapoyJt5DVxDQ3OS2")
auth.set_access_token("1302423402007887878-NSgDYnVwMMRTIOABrvdP75iNjJsW98", "DRNJDMm6nIn6MJViZXjinFAzYJ49soxFXhcZXXVjGZU0N")

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("I love Twitter")