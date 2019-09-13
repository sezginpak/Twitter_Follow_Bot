import main
import threading, time, sys
import signal

def signal_handler(signal, frame):
    app.current_status()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

app = main.Beck()

# app.get_follow_list()
# app.follow_user_byID()
# app.users_db_into()


while True:

    app.get_follow_list()
    app.th1 = False
    app.th2 = False


    th1 = threading.Thread(target=app.follow_user_byID)
    th1.run()
    while app.th1==False:
        time.sleep(app.c.bot_settings['FOLLOW_TIME'])

    th2 = threading.Thread(target=app.unfollow_user_byID)
    th2.run()
    while app.th2==False:
        time.sleep(app.c.bot_settings['UNFOLLOW_TIME'])



    time.sleep(5)



    if time.localtime().tm_hour == app.c.bot_settings['END_AT_H'] and time.localtime().tm_min == app.c.bot_settings['END_AT_M']:
        time.sleep(app.bot_sleep_time)
        print("""
            Start Followers: {}
            Current Followers: {}
            """.format(app.start_followers, app.api.me().followers_count))
        if len(app.unfollow_list_byID)!=0:
            app.unfollow_user_byID()
        app.follow_list=[]
        app.follow_list_byID=[]
        app.fol_li_byID=[]
        app.unfollow_list_byID=[]

    app.current_status()

app.current_status()
sys.exit(0)
