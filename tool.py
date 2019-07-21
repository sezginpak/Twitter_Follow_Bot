import config as c

class ToolFunc(object):
    def __init__(self):
        self.c = c
        self.cur = self.c.conn.cursor()
        self.ToolCur = self.c.conn.cursor()
        self.GetFollowListCur = self.c.conn.cursor()
        self.api = self.c.api


    def following_check(self, id=None):
        if id==None: return False
        self.ToolCur.execute("SELECT (id=?) FROM users", (id, ))
        if self.ToolCur.fetchall()[0][0]==1:
            return True
        return False

    def db_check(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS 'users' (id, username, follow_status, recent)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS 'default_user' (screen_name)")
        self.c.conn.commit()

    def bot_sleep(self):
        hour = abs(self.c.bot_settings['START_AT_H'] - self.c.bot_settings['END_AT_H'])
        minute = abs(self.c.bot_settings['START_AT_M'] - self.c.bot_settings['END_AT_M'])
        self.bot_sleep_time = (hour*60*60 + minute*60)

    def current_status(self):
        me = self.api.me()
        stat = [self.follow_count, me.followers_count, me.friends_count]
        print("")
        print("Bot Started Follow Count: {}".format(stat[0]))
        print("Current Followers: {}".format(stat[1]))
        print("Current Follow: {}".format(stat[2]))
