from facebook_scraper import get_posts

for post in get_posts('nintendo', pages=3):
  print(post['text'][:50])


# twitter api seems to be broken rn, will look into fixing later