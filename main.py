import os
# pip install path.py
import posixpath
def with_moviepy(filename):
    from moviepy.editor import VideoFileClip
    clip = VideoFileClip(filename)
    duration       = clip.duration
    fps            = clip.fps
    width, height  = clip.size
    duration_s = duration * 0.5
    duration_e = duration_s + 30
    return duration_s, duration_e

def cutter(file_name):
    clip_name = "clip_"+os.path.basename(file_name)
    from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
    # ffmpeg_extract_subclip("full.mp4", start_seconds, end_seconds, targetname="cut.mp4")
    ffmpeg_extract_subclip(file_name, duration_s, duration_e, targetname=clip_name)

db = []
i = 0
while i ==0 :
    path = str(input('input path here'))

    path = path.replace('"','')

    path = path.replace(os.sep,posixpath.sep)
    if path == "e":
        break
    else:
        db.append(path)
print(db)



for path in db:
    duration_s, duration_e = with_moviepy(path)
    cutter(path)



k = input("press enter to close")







