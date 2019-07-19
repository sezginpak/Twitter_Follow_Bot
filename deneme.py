import sqlite3
from config import bot_settings, oauth_configure
import tweepy
auth = tweepy.OAuthHandler(oauth_configure['CONSUMER_API_KEY'], oauth_configure['CONSUMER_API_SECRET_KEY'])
auth.set_access_token(oauth_configure['ACCESS_TOKEN'], oauth_configure['ACCESS_TOKEN_SECRET'])

api = tweepy.API(auth)
# api.get_user(screen_name="SumruOzden").following

conn=sqlite3.connect(bot_settings['YOUR_USERNAME']+".db")

cur=conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS 'users2' (id, username, follow_status, recent)")
