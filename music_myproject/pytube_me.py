from pytube import YouTube
import my_que
from my_que import insert_data

def on_complete(stream,file_path):
    print(stream)
    #print(file_path) 
    insert_data(file_path)


def on_progress(stream,chunk,bytes_remaining):
    print(100 - (bytes_remaining / stream.filesize * 100))
def vid_info(url):
    vid_me = YouTube(url)
    vid_length = vid_me.length
    return vid_me.title

def vid_download(url):
    yt = YouTube(url,on_complete_callback= on_complete,on_progress_callback =on_progress)
    t = yt.streams.filter(only_audio = True)
    print("downloading.......")
    t[0].download('/musics')
