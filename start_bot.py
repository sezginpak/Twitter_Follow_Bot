import main
import threading, time, sys
import signal

def signal_handler(signal, frame):
    app.users_db_into()
    app.current_status()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

app = main.Beck()

# app.get_follow_list()
# app.follow_user_byID()
# app.users_db_into()

while True:

    app.get_follow_list()

    app.follow_event.clear()
    app.unfollow_event.clear()
    app.users_db_event.clear()

    threading.Thread(target=app.follow_user_byID).run()
    app.follow_event.wait()
    app.users_db_into()
    threading.Thread(target=app.unfollow_user_byID).run()


    app.users_db_event.wait()

    time.sleep(5)



    if time.localtime().tm_hour == app.c.bot_settings['END_AT_H'] and time.localtime().tm_minute == app.c.bot_settings['END_AT_M']:
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

app.users_db_into()
app.current_status()
sys.exit(0)
