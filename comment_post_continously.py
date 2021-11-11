# -----------------------------
#   USAGE
# -----------------------------
# python comment_post_continously.py 
#
# DESCRIPTION:
# Comment on a post continously. In my case i want to tag
# three of my followers on each comment to increase my chances
# of winning a price.
#
# Author: Bryan Laygond
# Website: http://www.laygond.com
# ------------------------------

# Import the necessary packages
from instapy import InstaPy
from instapy import smart_run
import insta_config as config   # Create your own config file
import random
import time
import json
import os

# login credentials
insta_username = config.USERNAME2
insta_password = config.PASSWORD2

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

# Comment Parameter Settings
batch_size = 3      # number of people to tag per comment
base_comment ="YA ESTOY PARTICIPANDO "
url_post = "https://www.instagram.com/p/CVl1dJGjn7r/"


with smart_run(session):		
    #-------------------
    # Relationship Tools
    #-------------------
    '''
    Source -> https://instapy.org/relationship-tools
    live_match: will always load live data from the server
    store_locally: the files will be saved into your logs folder
    '''
    # Get followers
    my_followers = session.grab_followers(username=insta_username, amount="full", live_match=True, store_locally=True)
    #my_followers = json.load(open(os.path.expanduser('~')+'/InstaPy/logs/'+insta_username+'/relationship_data/'+insta_username+'/followers/10-11-2021~20~31.json'))
    #my_followers = ['jguerrero3383', 'raves.raves', 'avecescindy', 'cia.tager', 'kondrez', 'bybanner_brest', 'cdut_izyum', 'domenica.mov', 'milicent210', 'mathletas', '_jose.fuentes_', 'kuimin.tattoopiercing', 'a67_leds', 'marionthiers31', 'rico_gran_ceviche_', 'celularescursos5', 'dome_renteria', 'gkaizer.musico', 'cuoriintrentino', 'eksu1rpcgm', 'meueuisabella', 'john_acro_dancer', 'serdeluz1811', 'ifemasters', 'oscar_terrazas420', 'kleine_nata09', 'ashirson_gymantics_coach', 'anthonyggv10', 'shadow_player_666', 'fundacionunida_ong', 'takana.kendama']
    

    #-------------------
    # Settings
    #-------------------
    '''
    Source -> https://instapy.org/settings
    sleep_after: is used to put InstaPy to sleep after reaching peak rather than jumping the action 
    sleepyhead: can help to sound more humanly which will wake up a little bit later in a randomly chosen time
    stochastic_flow: every ~hour/day it will generate peaks at close range around your original peaks
    '''
    # Supervise Peak levels
    session.set_quota_supervisor(enabled=True, sleep_after=["comments"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                            peak_comments_hourly=20,
                            peak_comments_daily=100)
    session.set_do_like(enabled=True, percentage=100)
    session.set_do_comment(enabled=True, comment_liked_photo= True, percentage=100)


    #-------------------
    # Actions
    #-------------------
    '''
    Source -> https://instapy.org/actions/
    '''
    random.shuffle(my_followers)
    for offset in range(0, len(my_followers), batch_size):
        batch_samples = my_followers[offset:offset+batch_size]
        if len(batch_samples) == 3:
            my_comment = base_comment + " ".join(['@'+sample for sample in batch_samples])
            session.set_comments([my_comment])
            session.interact_by_URL([url_post]) # this takes around 42 seconds
            time.sleep(random.randint(0,13))    # wait some time randomly in between comments
