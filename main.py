import random, time, threading, sys
import tweepy

import sqlite3
from tool import ToolFunc



class Beck(ToolFunc):
    """docstring for Beck."""

    def __init__(self, arg=None):
        super(Beck, self).__init__()
        self.arg = arg
        self.follow_event = threading.Event()
        self.unfollow_event = threading.Event()
        self.users_db_event = threading.Event()
        self.c = c

        self.follow_list = []
        self.follow_list_byID = []
        self.fol_li_byID = []
        self.unfollow_list_byID = []

        self.follow_count = 0
        self.start_followers = self.api.me().followers_count

        self.bot_sleep()
        self.db_check()



    def database_commit(self):
        time.sleep(2)
        for i in self.follow_list:
            self.cur.execute("""UPDATE users
    	                               SET follow_status=:follow_status,username=:username
    	                               WHERE id=:id;""", {'follow_status': i.following, 'username': i.screen_name, 'id': i.id_str})
        self.c.conn.commit()

    def get_follow_list(self):
        if len(self.c.bot_settings['USER_RESOURCES_LIST'])==0:
            print("'USER_RESOURCES_LIST' list cannot be empty.")
            exit()
        for i in self.api.followers(screen_name=random.choice(self.c.bot_settings['USER_RESOURCES_LIST']), count=self.c.bot_settings['USER_GET_LIST_MAX']):
            self.GetFollowListCur.execute("SELECT id=(?) FROM users", (i.id_str, ))
            if self.GetFollowListCur.fetchall()[0][0]==1:
                continue
            else:
                self.follow_list.append(i)
        for i in self.follow_list:
            self.follow_list_byID.append(i.id_str)

    def follow_user_byID(self):
        for i in self.follow_list_byID:
            if not self.following_check(i):
                try:
                    self.api.get_user(user_id=i).follow()
                    self.follow_count+=1
                except tweepy.TweepError as e:
                    if (e.api_code==420) or (e.api_code==429):
                        self.rate_limit_sleep = (1*60*60)
                        time.sleep(self.rate_limit_sleep)
                        self.rate_limit_sleep=0
                        continue
                self.unfollow_list_byID.append(i)
                self.fol_li_byID.append(i)
            else:
                continue
            time.sleep(self.c.bot_settings['FOLLOW_TIME'])
        self.database_commit()
        self.follow_list.pop()
        self.follow_list_byID.pop()
        self.follow_event.set()


    def unfollow_user_byID(self):
        time.sleep(self.c.bot_settings['UNFOLLOW_TIME'])
        for i in self.unfollow_list_byID:
            if self.rate_limit_sleep!=0:
                time.sleep(self.rate_limit_sleep)
            status = self.api.get_user(user_id=i)
            if status.following:
                try:
                    status.unfollow()
                except tweepy.RateLimitError as e:
                    print('RateLimitError' + e.api_code)
                except tweepy.TweepError as e:
                    print('TweepError' + e.api_code)
            else:
                continue
            time.sleep(self.c.bot_settings['UNFOLLOW_TIME'])
        self.unfollow_list_byID.pop()
        self.unfollow_event.set()

    def users_db_into(self):
        for i in self.fol_li_byID:
            try:
                self.cur.execute("INSERT INTO users VALUES (?, ?)", (i, self.api.get_user(user_id=i).screen_name))
            except sqlite3.OperationalError as e:
                print(e)
            time.sleep(15)
        self.users_db_event.set()
























#
