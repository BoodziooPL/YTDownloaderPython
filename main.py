import tkinter
import customtkinter
from pytube import YouTube
from moviepy.editor import *

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        audio_stream = ytObject.streams.filter(only_audio=True).first()
        title.configure(text=ytObject.title, text_color='green')
        # mp4 download
        audio_file = f"{ytObject.title}.mp4"
        audio_stream.download(filename=audio_file)

        # from mp4 to mp3
        audio = AudioFileClip(audio_file)
        audio.write_audiofile(f"{ytObject.title}.mp3")
        audio.close()
        
        # deleting mp4
        os.remove(audio_file)
        finishLabel.configure(text='Done')
    except:
        finishLabel.configure(text="Download Failed!", text_color='red')

# Settings GUI
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme('blue')

# Frame APP
app = customtkinter.CTk()
app.geometry("500x200")
app.title("Youtube downloader")

# UI Elements
title = customtkinter.CTkLabel(app, text="Paste Youtube Link")
title.pack(padx = 10,pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=300, height = 30)
link.pack()

# Finish Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Download
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx = 20, pady=10)
# Start app
app.mainloop()