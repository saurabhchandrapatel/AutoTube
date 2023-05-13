import os
import httplib2
from datetime import date

IG_USERNAME = "saurabh.aktel" 
IG_PASSWORD = ""

d0 = date(2023, 5, 2)
d1 = date.today()
delta = d1 - d0
row = 50 + delta.days

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
if os.name == 'nt':
    IMAGEMAGICK_BINARY = "C:\\Program Files\\ImageMagick-7.0.8-Q16\\magick.exe"
    dir_path = "C:\\tmp"
    dir_path = "."
else:
    IMAGEMAGICK_BINARY = "/usr/bin/convert"
    dir_path = "/tmp"

DIR_PATH = dir_path
DIR_PATH_OUTPUT = os.path.join(DIR_PATH, 'output')
DIR_PATH_IMAGES = os.path.join(DIR_PATH, "image")
DIR_PATH_VIDEOS = os.path.join(DIR_PATH, "video")
DIR_PATH_DB = os.path.join(DIR_PATH, "db")
DIR_PATH_THUMBNAILS = os.path.join(DIR_PATH, "image", "thumbnails")


 
DIR_PATH_FONT = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fonts")
DIR_PATH_DB = os.path.join(os.path.dirname(os.path.realpath(__file__)), "db")
DIR_PATH_MUSIC = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Music")
DB_FILE = os.path.join(DIR_PATH_DB, 'row_db.txt')
DEFAULT_ROW = 10
try:
    os.mkdir(DIR_PATH_OUTPUT)
except:
    ...
try:
    os.mkdir(DIR_PATH_IMAGES)
except:
    ...

try:
    os.mkdir(DIR_PATH_THUMBNAILS)
except:
    ...

try:
    os.mkdir(DIR_PATH_VIDEOS)
except:
    ...
try:
    os.mkdir(DIR_PATH_DB)
except:
    ...
if not os.path.isfile(DB_FILE):
    try:
        file = open(DB_FILE, 'w')
        file.write(str(DEFAULT_ROW))
        file.close()
    except:
        ...



FB_PAGE_ID = "1487996058086830"
FB_PAGE_ACCESS_TOKEN = 'EAAJBzTBWAmIBAAeFLxz1zDha2Pkw99Owf2u4Rt4WPIt7GYoHAKlzvFaZAhWwQSMMKWcPbgI2AjXpqCpd0tfne0wbfoIjUYDDhDNWJU5iK8kBbK7jGEqEn5CtJTkhHZAmUbRme5sr6rWbYfBUT1ndquIlBltbLHecC0zMXcnhPHagCloMYK5PY0mJAQXJAequrzS52yI4oOgTGs52nOqgYcKQ38kBwZD'

FFMPEG_BINARY = os.getenv('FFMPEG_BINARY', 'ffmpeg-imageio')
#IMAGEMAGICK_BINARY = os.getenv('IMAGEMAGICK_BINARY', 'auto-detect') 
START_DATE = '2023'
IG_USERNAME = "saurabh.aktel" 
IG_PASSWORD = ""
IS_VERBOSE = True
MV_LOGGER = None
PIXABAY_API = '856584-785cc0323333f4208cae88f51'  
# we are handling retry logic ourselves.
httplib2.RETRIES = 1

# Maximum number of times to retry before giving up.
MAX_RETRIES = 10

# Always retry when these exceptions are raised.
RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError)

# Always retry when an apiclient.errors.HttpError with one of these status
# codes is raised.
RETRIABLE_STATUS_CODES = [500, 502, 503, 504]
CLIENT_SECRETS_FILE = os.path.join(CURRENT_DIR,"client_secrets.json")
print(CLIENT_SECRETS_FILE)
# This OAuth 2.0 access scope allows an application to upload files to the
# authenticated user's YouTube channel, but doesn't allow other types of access.
YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
YOUTUBE_READ_WRITE_SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# This variable defines a message to display if the CLIENT_SECRETS_FILE is
# missing.
MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:

   %s

with information from the API Console
https://console.developers.google.com/

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
""" % os.path.abspath(os.path.join(os.path.dirname(__file__), CLIENT_SECRETS_FILE))

VALID_PRIVACY_STATUSES = ("public", "private", "unlisted")


def GetDaySuffix(day):
    if day == 1 or day == 21 or day == 31:
        return "st"
    elif day == 2 or day == 22:
        return "nd"
    elif day == 3 or day == 23:
        return "rd"
    else:
        return "th"

DAY = date.today().strftime("%d")
DAY = str(int(DAY)) + GetDaySuffix(int(DAY))
dt_string = date.today().strftime("%A %B") + f" {DAY}"
consumer_key = 'CTgs7JYtqKhVmd3gSAjiH3pND'
consumer_secret = 'mDGOxVYPCbPdP8IY4SGmmJu0t3pyOJQ3pzQ39VrXllxpAiUT7u'
access_token = '98124314-XjBPvLXInqNWo58i52vfp3RZ5vkFfxFzUBXOVXYTl'
access_token_secret = 'g6KxheDo8W0vX4gbicGDSaMyhEqX8UWitNDnDZhhrMIhf'
COLOR_DB = [ 
    ("#E2D1F9","#317773"),
    ("#E2D1F9", "#317773"),
    ("#EE4E34", "#FCEDDA"),
    ("#E2D3F4", "#013DC4"),
    ("#234E70", "#FBF8BE"),
    ("#262223","#DDC6B6"),
    ("#E7D045","#A04EF6"), 
    ("#358597","#F4A896"),
    ("#D2302C","#F7F7F9"),
    ("#F4A950", "#161B21"), 
    ("#295F2D", "#FFE67C"), 
    ("#141A46", "#EC8B5E"),
    ("#8BD8BD", "#243665"), 
    ("#EC4D37", "#1D1B1B"),
    ("#2F3C7E", "#FBEAEB"),
    ('#F96167','#FCE77D'), 
    ("#F9D342", "#292826"), 
    ("#CCF381", "#4831D4"), 
    ("#4A274F" ,"#F0A07C"), 
    ("#EF5455", "#FAD744"), 
    ("#FFF748","#3C1A5B") 
]

# Your Reddit ID & Pass
reddit_username="theblipman"
reddit_password="your_reddit_password"

# Reddit API ID & Key (which you can get from here: https://www.reddit.com/prefs/apps/)
client_id="ZJal5z6xRhWdcs7MLHEMAw"
client_secret="7MI_RkFvd2nDUX8CCLl2TEUBbg4mag"

# Oxford Dictionary application ID & Key (which you can get from here: https://developer.oxforddictionaries.com/)
app_id="your_app_id"
app_key="your_app_key"
user_agent="youtubespatel"


#URL Shortner bitly.com 
"""Package configuration."""

tokens_pool_email= ['vsaurabh.aec@gmail.com', 'vsaurabhaec1', 'vsaurabhaec2', 'vsaurabhaec3'] 
tokens_pool = ['457406ca3a6b1d4c1bc843f38684065dc1b6eb5f','251399feae01c65474d84a78131f0a0784212497','437c850c9a27c431bca01ebbeb2369552d8468bb','9755717c6f3ae34e430c1159c54bb0cdfe5382aa']  # Use your own.
