oauth_configure = {
    "CONSUMER_API_KEY": "",
    "CONSUMER_API_SECRET_KEY": "",
    "ACCESS_TOKEN": "",
    "ACCESS_TOKEN_SECRET": "",
}

bot_settings = {
    "YOUR_USERNAME": "",
    "FOLLOW_TIME": 240,  # --> INTEGER
    "UNFOLLOW_TIME": 240,  # --> INTEGER
    "FOLLOW_PER_DAY": None,
    "UNFOLLOW_PER_DAY": None,
    "USER_MAX_FOLLOW": 500,  # --> INTEGER
    "USER_MIN_FOLLOW": 250,  # --> INTEGER
    "USER_GET_LIST_MAX": 20,  # --> INTEGER
    "USER_RESOURCES_LIST": [],
    "USER_DEFAULT_FOLLOW": [

    ],
    "USER_BLACKLIST": [
        "",
        "",
    ],
    "FOLLOW_RECENT_FEED": True,
    "END_AT_H": 2,  # --> INTEGER if not sleep please 'None'
    "END_AT_M": 30,  # --> INTEGER if not sleep please 'None'
    "START_AT_H": 9,  # --> INTEGER if not sleep please 'None'
    "START_AT_M": 30,  # --> INTEGER if not sleep please 'None'
}



import sqlite3
import tweepy

auth = tweepy.OAuthHandler(oauth_configure['CONSUMER_API_KEY'], oauth_configure['CONSUMER_API_SECRET_KEY'])
auth.set_access_token(oauth_configure['ACCESS_TOKEN'], oauth_configure['ACCESS_TOKEN_SECRET'])

api = tweepy.API(auth)


conn=sqlite3.connect(bot_settings['YOUR_USERNAME']+".db", timeout=15)
















#
