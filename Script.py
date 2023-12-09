from pytube import YouTube
from tkinter import filedialog 
# -*- coding: utf-8 -*-
print("𝐄𝐙𝐙𝐄𝐋𝐃𝐄𝐈𝐍")
url_input = input("Please Enter Your URL : ")
all_streams = YouTube(url_input).streams.all()
v=-1
for i in all_streams:
    v+=1
    print(str(v)+" : "+str(i))
stm_input = int(input("Pleas Choose The Suitable Stream : "))
print("Please Choose Directery To Save : ")
folder_name = filedialog.askdirectory()
choice = all_streams[stm_input].download(folder_name)
print("Download Complete.............................")