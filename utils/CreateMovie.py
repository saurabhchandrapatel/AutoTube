from moviepy.editor import *
import random
import os
import moviepy.editor as mpe
dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def GetDaySuffix(day):
    if day == 1 or day == 21 or day == 31:
        return "st"
    elif day == 2 or day == 22:
        return "nd"
    elif day == 3 or day == 23:
        return "rd"
    else:
        return "th"

# dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
dir_path = "/opt/python"
music_path = os.path.join(dir_path, "Music/")

def add_return_comment(comment):
    need_return = 30
    new_comment = ""
    return_added = 0
    return_added += comment.count('\n')
    for i, letter in enumerate(comment):
        if i > need_return and letter == " ":
            letter = "\n"
            need_return += 30
            return_added += 1
        new_comment += letter
    return new_comment, return_added
        

class CreateMovie():

    @classmethod
    def CreateMP4(cls, post_data):

        clips = []

        # introName = ''
        # videos = []
        # if introName != '':
        #     introVid = VideoFileClip("./" + introName)
        #     videos.append(introVid)
        #     duration += introVid.duration
        # template_path = '.\\data\\template.png'
        # clip_with_green = ImageSequenceClip([template_path], durations=[12])
        # clips.append(clip) 

        for post in post_data:
            if "gif" not in post['image_path']:
                clip = ImageSequenceClip([post['image_path']], durations=[12])
                clips.append(clip)
            else:
                clip = VideoFileClip(post['image_path'])
                clip_lengthener = [clip] * 60
                clip = concatenate_videoclips(clip_lengthener)
                clip = clip.subclip(0,12)
                clips.append(clip)
        
        # After we have out clip.
        clip = concatenate_videoclips(clips)
        # Hack to fix getting extra frame errors??
        clip = clip.subclip(0,60)
        colors = ['yellow', 'LightGreen', 'LightSkyBlue', 'LightPink4', 'SkyBlue2', 'MintCream','LimeGreen', 'WhiteSmoke', 'HotPink4']
        colors = colors + ['PeachPuff3', 'OrangeRed3', 'silver']
        random.shuffle(colors)
        text_clips = []
        notification_sounds = []
        for i, post in enumerate(post_data):
            return_comment, return_count = add_return_comment(post['Best_comment'])
            # bg_color='yellow',
            txt = TextClip(return_comment, font='Calibri',   fontsize=25, color="black", bg_color='yellow', stroke_color="black", align='center', stroke_width=.02)
            # txt = TextClip(return_comment, font='Calibri',fontsize=38, color="black", size=(600, 500) , method="caption",align="west",)
            txt = txt.on_color(col_opacity=.3)
            # txt = txt.set_position((10,500))
            txt = txt.set_position(("center", 550)) 
            txt = txt.set_start((0, 3 + (i * 12))) # (min, s)
            txt = txt.set_duration(7)
            txt = txt.crossfadein(0.5)
            txt = txt.crossfadeout(0.5)
            txt = txt.margin(10)
            text_clips.append(txt)

            return_comment, _ = add_return_comment(post['best_reply'])
            # txt = TextClip(return_comment, font='Courier',fontsize=38, color=colors.pop(), bg_color='yellow')
            txt = TextClip(return_comment, font='Calibri',fontsize=25,   color="black",bg_color='yellow', stroke_color="black", align='center', stroke_width=.02)
            txt = txt.on_color(col_opacity=.3)
            # txt = txt.set_position((15,585 + (return_count * 50)))
            #txt = txt.set_position("center", "bottom")
            txt = txt.set_position(("center", 635 + (return_count * 50) ))    
            txt = txt.set_start((0, 5 + (i * 12))) # (min, s)
            txt = txt.set_duration(7)
            txt = txt.crossfadein(0.5)
            txt = txt.crossfadeout(0.5)
            txt = txt.margin(10)
            text_clips.append(txt)

            notification = AudioFileClip(os.path.join(music_path, f"notification.mp3"))
            notification = notification.set_start((0, 3 + (i * 12)))
            notification_sounds.append(notification)

            notification = AudioFileClip(os.path.join(music_path, f"notification.mp3"))
            notification = notification.set_start((0, 5 + (i * 12)))
            notification_sounds.append(notification)
        
        music_file = os.path.join(music_path, f"music{random.randint(0,4)}.mp3")
        music = AudioFileClip(music_file)
        music = music.set_start((0,0))
        music = music.volumex(.4)
        music = music.set_duration(59)
        new_audioclip = CompositeAudioClip([music]+notification_sounds)
        clip.write_videofile(f"video_clips.mp4", fps = 24)
        clip = VideoFileClip("video_clips.mp4",audio=False)
        clip = CompositeVideoClip([clip] + text_clips)
        clip.audio = new_audioclip
        clip.write_videofile("/tmp/video.mp4", fps = 24)

        if os.path.exists(os.path.join(dir_path, "video_clips.mp4")):
            os.remove(os.path.join(dir_path, "video_clips.mp4"))
        else:
            print(os.path.join(dir_path, "video_clips.mp4"))

# if __name__ == '__main__':

#     createMovie = CreateMovie()
#     post_data_item1 = {}
#     post_data_item1['title'] = 'Okkey' 
#     post_data_item1['image_path'] = ".\\data\\03092023\\1.jpg"
#     post_data_item1['Best_comment'] = ["hi this is"]
#     post_data_item1['best_reply'] = ["hi this is"]

#     # post_data_item2 = {}
#     # post_data_item2['title'] = 'Okkey' 
#     # post_data_item2['image_path'] = ".\\data\\03092023\\2.jpg"
#     # post_data_item2['Best_comment'] = ["hi this is"]
#     # post_data_item2['best_reply'] = ["hi this is"]


#     post_data = []
#     post_data.append(post_data_item1)
#     # post_data.append(post_data_item2)

#     createMovie.CreateMP4(post_data)

#     print(TextClip.list('color'))