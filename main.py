import feedparser

def inp():
    url = input("Enter the URL:")
    return url

def get_feed(url):
    d = feedparser.parse(url)
    title = d.feed.title
    des = d.feed.description
    link = d.feed.link
    return title,des,link

url = inp()
title,des,link=get_feed(url)

print(f"Title: {title}")
print(f"Description: {des}")
print(f"Link: {link}")