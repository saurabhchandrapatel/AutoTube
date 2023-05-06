from yt_config import *
import requests
from datetime import date
import time
from utils.CreateMovie import CreateMovie, GetDaySuffix
from utils.RedditBot import RedditBot
from utils.upload_video import UploadVedio
import tweepy

def main(upload_video_status=False):
    redditbot = RedditBot()     
    upload_token = True
    posts = redditbot.get_posts("memes")
    redditbot.create_data_folder()
    for post in posts:
        redditbot.save_image(post)
    DAY = date.today().strftime("%d")
    DAY = str(int(DAY)) + GetDaySuffix(int(DAY))
    dt_string = date.today().strftime("%A %B") + f" {DAY}"
    CreateMovie.CreateMP4(redditbot.post_data)
    if upload_token and upload_video_status:
        title = f"{redditbot.post_data[0]['title']} - 😅 memes of the day {dt_string}! #memesoftheday"
        description = '''
            #shorts #memes #funnymemes
            Giving you the hottest memes of the day with funny comments!

            '''+title+''' 
        
            video  includes funny memes, internet jokes, and viral clips. videos are popular with a wide range of audiences, particularly younger generations who are more likely to consume and share content on social media.
        
        '''

        keywords = """
             #shorts #memesoftheday #memes #meme #dankmemes #funnymemes #memesdaily #edgymemes #dankmeme #offensivememes #dailymemes #fortnitememes #memestagram #spicymemes #funnymeme #memepage #memer #btsmemes #memelord #animememes #memez #tiktokmemes #memesespañol #memesespañol #nichememes #dankmemesdaily #edgymeme #memeaccount #kpopmemes #bestmemes #spongebobmemes #darkmemes #nichememe #wholesomememes #memestar #relatablememes #stolenmemes #nicememe #instamemes #memesrlife #pubgmemes #memesbrasil
            """

        video_data = {
            "file": os.path.join(DIR_PATH_OUTPUT, "video.mp4"),
            "title": title,
            "description": description+keywords,
            "keywords": keywords.replace(" #", ", "),
            "privacyStatus":"public",
        }
        UploadVedioObj = UploadVedio()
        id = UploadVedioObj.upload(video_data)
        print(id)
        try: 
            auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
            auth.set_access_token(access_token, access_token_secret) 
            api = tweepy.API(auth)
            # api.update_status(video_desc + video_title) 
            api.update_status("https://www.youtube.com/shorts/"+str(id))
        except Exception as e:
            print(e)
            return None

    return "ko"

def lambda_handler(event, context):    
    upload_video_status = True
    daily = False
    Count = 0
    while True:
        Count = Count +1
        try:
            out = main(upload_video_status)
            return { 
                'message' : out
            }
            break;
        except Exception as e:
            print(str(e))
            if Count > 5:
                break;

lambda_handler("", "") 