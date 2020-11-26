from pytube import YouTube
import os
import shutil
import math
import datetime
import matplotlib

print("Paste in your YouTube video Link")
video_inp = input("")
video = YouTube('%s'%video_inp)

stream = video.streams.first()
