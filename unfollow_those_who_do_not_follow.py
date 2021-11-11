# -----------------------------
#   USAGE
# -----------------------------
# python start.py 
#
# DESCRIPTION:
# My recipe to automate an instagram account through InstaPy  
# 
# Author: Bryan Laygond
# Website: http://www.laygond.com
# ------------------------------

# Import the necessary packages
from instapy import InstaPy
from instapy import smart_run
import insta_config as config   # Create your own config file

# login credentials
insta_username = config.USERNAME1
insta_password = config.PASSWORD1

# Custom COMMENTS
# https://www.webfx.com/tools/emoji-cheat-sheet/
comments_es = ['Bakansisimo! @{}',
                'BRUTAL!!!! @{}',
                'Proximo CRACK del Circo! @{}']
comments_en = [u'DAMN!!! 🤹 @{}',
                'BRUTAL!!!! Keep it up!@{}',
                'Yo! That\'s NICE! @{}']               

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)


with smart_run(session):		
        #-------------------
        # Relationship Tools
        #-------------------
        '''
        Source -> https://instapy.org/relationship-tools
        live_match: will always load live data from the server
        store_locally: the files will be saved into your logs folder
        '''
        # Log/Save followers and following
        #my_followers = session.grab_followers(username="caic.espol", amount="full", live_match=True, store_locally=True)
        #my_following = session.grab_following(username="caic.espol", amount="full", live_match=True, store_locally=True)

        #-------------------
        # Settings
        #-------------------
        '''
        Source -> https://instapy.org/settings
        sleep_after: is used to put InstaPy to sleep after reaching peak rather than jumping the action 
        sleepyhead: can help to sound more humanly which will wake up a little bit later in a randomly chosen time
        stochastic_flow: every ~hour/day it will generate peaks at close range around your original peaks
        potency_ratio: ratio between followers-following, positive then more followers, negative then more following            
        '''
        # Supervise Peak levels
        session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                                peak_likes_hourly=30,
                                peak_likes_daily=50,
                                peak_comments_hourly=3,
                                peak_comments_daily=5,
                                peak_follows_hourly=15,
                                peak_follows_daily=20,
                                peak_unfollows_hourly=15,
                                peak_unfollows_daily=30,
                                peak_server_calls_hourly=None,
                                peak_server_calls_daily=None)
        # Make sure users do not exceed
        session.set_relationship_bounds(enabled=True,
				potency_ratio=None, 
				delimit_by_numbers=True,
				max_followers=8500,
				max_following=4490,
				min_followers=100,
				min_following=100,
				min_posts=4,
                                max_posts=1000) 
        # Like 80% of images displayed
        session.set_do_like(enabled=True, percentage=80)
        # Dont like pics above 50 likes
        session.set_delimit_liking(enabled=True, max_likes=50, min_likes=None) 
        # Every 4th image will be commented on
        session.set_comments(comments_es)
        session.set_do_comment(enabled=True, percentage=25)
        # Don't comment if post has more than 60 comments
        session.set_delimit_commenting(enabled=True, max_comments=60, min_comments=None)
        # Always skip users without profile pic
        #session.set_skip_users(skip_no_profile_pic=True, no_profile_pic_percentage=100)
        # Exclude these users from any action 
        #session.set_dont_include(["friend1", "friend2", "friend3"])
        # Watch Stories
        # session.set_do_story(enabled = True, percentage = 70, simulate = True)

        
        #-------------------
        # Actions
        #-------------------	
        '''
        Source -> https://instapy.org/actions/
        skip_top_posts: Determines whether the first 9 top posts should be liked or not (default is True)
        There are 4 Unfollow methods available to use:|> customList |> InstapyFollowed |> nonFollowers |> allFollowing
        style: Unfollow First In, First Out (FIFO) or the earliest people you followed (LIFO) or RANDOM
        simulate: True-> send commands to Instagram saying we have watched the stories. False -> perform the exact same action as a human (cliicking on stories, waiting until watching finishes, etc...)
        '''
        # Unfollows people, but only people who do not follow you,
        session.unfollow_users(amount = 100, nonFollowers=True, style="LIFO")	
        # Like 100 videos from hashtag
        session.like_by_tags(["malabares"], amount=100, skip_top_posts=False)#, media='Video')
        # Follow Likers of List
        #session.follow_likers(['user1' , 'user2'], photos_grab_amount = 1, follow_likers_per_photo = 4, randomize=False, sleep_delay=600, interact=False)

        # Remove outgoing unapproved follow requests from private accounts
        #session.remove_follow_requests(amount=200, sleep_delay=600)
       
  