import random, time, threading, sys
import tweepy
import datetime

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

        self.th1 = False
        self.th2 = False

        self.follow_list = []
        self.follow_list_byID = []
        self.fol_li_byID = []
        self.unfollow_list_byID = []

        self.follow_count = 0
        self.start_followers = self.api.me().followers_count

        print("Start Followers: {}".format(self.start_followers))

        self.rate_limit_sleep = 0
        self.tour = 0

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
        print('Current Follow: {} --> Hour: {}, Minute: {}, Second: {}'.format(self.follow_count, time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec))
        for j in range(1, 2):
            u_n = random.choice(self.c.bot_settings['USER_RESOURCES_LIST'])
            try:
                for i in self.api.followers(screen_name=u_n, count=self.c.bot_settings['USER_GET_LIST_MAX']):
                    self.GetFollowListCur.execute("SELECT id FROM users WHERE id=:id", {'id': i.id_str})
                    fet = self.GetFollowListCur.fetchall()
                    if len(fet)==0:
                        self.follow_list.append(i)
                    elif len(fet)!=0:
                        continue
            except tweepy.TweepError as e:
                print(e)
                print('ERROR! code : {}'.format(e.api_code))
                time.sleep(500)
            except tweepy.RateLimitError as e:
                print(e)
                time.sleep(500)
            time.sleep(30)

        for i in self.follow_list:
            self.follow_list_byID.append(i.id_str)
        print("Follow list len: {}".format(len(self.follow_list_byID)))

    def follow_user_byID(self):
        if self.follow_list_byID==[]:
            self.th1 = True
            return
        for i in self.follow_list_byID:
            if not self.following_check(i):
                try:
                    usr = self.api.get_user(user_id=i)
                    usr.follow()
                    print('{} Follow: {} --> Hour: {}, Minute: {}, Second: {}'.format(usr.screen_name, self.follow_count, time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec))
                    self.follow_count+=1
                    self.users_db_into_one(i)
                except tweepy.TweepError as e:
                    if (e.api_code==420) or (e.api_code==429):
                        self.rate_limit_sleep = (1*60*60)
                        time.sleep(self.rate_limit_sleep)
                        self.rate_limit_sleep=0
                        continue
                    elif (e.api_code==50):
                        print(e)
                        continue
                    else:
                        print('undefined error by TweepError)
                except:
                    print('undefined error')
                self.unfollow_list_byID.append(i)
                self.fol_li_byID.append(i)
            else:
                continue
            time.sleep(self.c.bot_settings['FOLLOW_TIME'])
        self.database_commit()
        self.follow_list.pop()
        self.follow_list_byID.pop()
        self.th1 = True


    def unfollow_user_byID(self):
        if self.unfollow_list_byID==[]:
            self.th2 = True
            return
        time.sleep(self.c.bot_settings['UNFOLLOW_TIME'])
        for i in self.unfollow_list_byID:
            if self.rate_limit_sleep!=0:
                time.sleep(self.rate_limit_sleep)
            try:
                status = self.api.get_user(user_id=i)
            except tweepy.TweepError as e:
                if (e.api_code==50):
                    continue
            if status.following:
                try:
                    status.unfollow()
                    print('{} Unfollow: {} --> Hour: {}, Minute: {}, Second: {}'.format(status.screen_name, self.follow_count, time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec))
                except tweepy.RateLimitError as e:
                    print('RateLimitError' + e.api_code)
                except tweepy.TweepError as e:
                    if (e.api_code==50):
                        continue
                    print('TweepError' + e.api_code)
            else:
                continue
            time.sleep(self.c.bot_settings['UNFOLLOW_TIME'])
        self.unfollow_list_byID.pop()
        self.th2 = True


    def users_db_into_one(self, id=None):
        if id==None: return False
        data = self.api.get_user(user_id=id)
        stat = data.following
        if stat:
            self.cur.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (id, data.screen_name, stat, True))
        else:
            self.cur.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (id, data.screen_name, stat, False))

        self.c.conn.commit()






















#
