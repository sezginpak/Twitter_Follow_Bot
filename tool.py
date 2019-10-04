import config as c
import time
from tweepy.error import RateLimitError

class ToolFunc(object):
    def __init__(self):
        self.c = c
        self.cur = self.c.conn.cursor()
        self.ToolCur = self.c.conn.cursor()
        self.GetFollowListCur = self.c.conn.cursor()
        self.api = self.c.api


    def following_check(self, id=None):
        if id==None: return False
        self.ToolCur.execute("SELECT id FROM users WHERE id=?", (str(id), ))
        res = self.ToolCur.fetchall()
        if len(res)==0:
            return False
        if res[0][0]!='0': return True
        return True

    def db_check(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS 'users' (id, username, follow_status, recent)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS 'default_user' (screen_name)")
        self.c.conn.commit()

    def bot_sleep(self):
        hour = abs(self.c.bot_settings['START_AT_H'] - self.c.bot_settings['END_AT_H'])
        minute = abs(self.c.bot_settings['START_AT_M'] - self.c.bot_settings['END_AT_M'])
        self.bot_sleep_time = (hour*60*60 + minute*60)

    def current_status(self):
        try:
            me = self.api.me()
        except RateLimitError:
            time.sleep(1000)
            me = self.api.me()
        stat = [self.follow_count, me.followers_count, me.friends_count]
        print("")
        print("Bot Started Follow Count: {}".format(stat[0]))
        print("Current Followers: {}".format(stat[1]))
        print("Current Follow: {}".format(stat[2]))
