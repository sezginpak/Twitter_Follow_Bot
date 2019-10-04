oauth_configure = {
    "CONSUMER_API_KEY": "FfmDppGRW9jr008GttEeSDrJe",
    "CONSUMER_API_SECRET_KEY": "nZHGiEyYTDTQrY7q6fVOZ3VLqBr3ehcpVmEKzg3ZvDTRtOYMU3",
    "ACCESS_TOKEN": "779579582278201344-ceX42fKKYebyDJ7lIna9UYfIbD4Ph7u",
    "ACCESS_TOKEN_SECRET": "9QetlVRE6CMw113btodsIcMmfVm2j6dW0y5E1PN8ah7M3",
}

bot_settings = {
    "YOUR_USERNAME": "sezginpak",
    "FOLLOW_TIME": 240,  # --> INTEGER
    "UNFOLLOW_TIME": 240,  # --> INTEGER
    "FOLLOW_PER_DAY": None,
    "UNFOLLOW_PER_DAY": None,
    "USER_MAX_FOLLOW": 500,  # --> INTEGER
    "USER_MIN_FOLLOW": 250,  # --> INTEGER
    "USER_GET_LIST_MAX": 25,  # --> INTEGER
    "USER_RESOURCES_LIST": ["sivribiber", "tahsinhasoglu", "ProfDemirtas", "tonjukuk", "burakbirakya", "benneizledim", "civaba", "atasozutok", "istetamburasi",
                            "atadogann", "unquale", "kriptoburak", "teyitorg", "ironikadamm", "Overlokcu12", "yavuzsyildiz", "HSevkiTopuz", "huorelensarr", "hocafaktoru", "yineutandik", "turkicmemes", "lordsinov", "unibilgi", "LOmecha"],
    "USER_DEFAULT_FOLLOW": [

    ],
    "USER_BLACKLIST": [
        "goknrkaraa",
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
