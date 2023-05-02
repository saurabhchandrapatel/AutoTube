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



import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("HH8wG1gSXq0Ag6vQjhgZcJXov", "8A6vj1euc2BnriOTLK7QiZSL5Wymt2xu9wpHYOQP4JihePyIlV")
auth.set_access_token("2258745854-KaLHv8q0PuFXxQumdO04D7Wl3j0UAdlOKCxJJqR", "PcyBW1xtBuRRSoPaR9B1jb8SyPu4vks5tNc4i28nUyKwo")
 



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
            
            BE MY FRIEND:
             🌍Check my website / blog: https://blog.aktel.in
 

        '''

        keywords = """
             #shorts #memesoftheday #memes #meme #dankmemes #funnymemes #memesdaily #edgymemes #dankmeme #offensivememes #dailymemes #fortnitememes #memestagram #spicymemes #funnymeme #memepage #memer #btsmemes #memelord #animememes #memez #tiktokmemes #memesespañol #memesespañol #nichememes #dankmemesdaily #edgymeme #memeaccount #kpopmemes #bestmemes #spongebobmemes #darkmemes #nichememe #wholesomememes #memestar #relatablememes #stolenmemes #nicememe #instamemes #memesrlife #pubgmemes #memesbrasil
            """

        video_data = {
            "file": "/tmp/video.mp4",
            "title": title,
            "description": description+keywords,
            "keywords": keywords.replace(" #", ", "),
            "privacyStatus":"public",
        }
        time.sleep(60 * 1)
        UploadVedioObj = UploadVedio()
        id = UploadVedioObj.upload(video_data)
        print(id)
        api = tweepy.API(auth) 
        api.update_status("https://www.youtube.com/shorts/"+str(id))
    return "ko"

def lambda_handler(event, context):    
    upload_video_status = True
    daily = False
    out = main(upload_video_status)
    return { 
        'message' : out
    }



lambda_handler("", "") 