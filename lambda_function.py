import requests
from datetime import date
import time
from utils.CreateMovie import CreateMovie, GetDaySuffix
from utils.RedditBot import RedditBot
from utils.upload_video import UploadVedio
# import pytrends
# import wikipedia
# import pyttsx3
# from utils.Marketing import publish
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
        video_data = {
            "file": "/tmp/video.mp4",
            "title": f"{redditbot.post_data[0]['title']} - 😅 memes of the day {dt_string}! #memesoftheday",
            "description": "#shorts\nGiving you the hottest memes of the day with funny comments!",
            "keywords":"meme,Dankestmemes , #memesoftheday ",
            "privacyStatus":"public"
        }
        time.sleep(60 * 1)
        UploadVedioObj = UploadVedio()
        id = UploadVedioObj.upload(video_data)
        print(id)
        # if id:
        #     publish(id, whatapp=False, insta=False, tweet=False, telegram=False, fbg=False, wp=False, email=False) 
            # return "ok"
    return "ko"

def lambda_handler(event, context):    
    upload_video_status = True
    daily = False
    out = main(upload_video_status)
    return { 
        'message' : out
    }




# while True:
#     upload_video_status = True
#     daily = False
#     main(upload_video_status)
#     if daily:
#         time.sleep(60 * 60 * 24 - 1)
#     else:
#         break;