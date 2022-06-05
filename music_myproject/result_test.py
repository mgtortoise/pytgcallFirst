import pytube_me
import my_que
url = input("Enter Url > ")
pytube_me.vid_download(url)
result = my_que.get_data()
print(result)