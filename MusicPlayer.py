from pygame import mixer
from tkinter import *
from tkinter import filedialog

c_volume = float(0.5)

def play_song():
    filename = filedialog.askopenfilename(initialdir="C:/",title="Please select a file")
    title = filename.split("/")[-1]
    try:
        mixer.init()
        mixer.music.load(filename)
        mixer.music.set_volume(c_volume)
        mixer.music.play()
        song_title_label.config(text="Now playing : "+str(title),fg="green")
        volume_label.config(fg="green",text="Volume : "+str(c_volume))
    except Exception as e:
        print(e)
        song_title_label.config(text="Error",fg="red")
def reduce_vol():
    try:
        global c_volume
        if c_volume <= 0:
            volume_label.config(fg="red",text="Volume : Muted")
            return
        c_volume -= float(0.1)
        c_volume = round(c_volume,1)
        mixer.music.set_volume(c_volume)
        volume_label.config(fg="green",text="Volume : "+str(c_volume))
    except Exception as e:
        print(e)
        song_title_label.config(text="Track hasn't selected yet !",fg="red")

def increase_vol():
    try:
        global c_volume
        if c_volume >= 1:
            volume_label.config(fg="red",text="Volume : Max")
            return
        c_volume += float(0.1)
        c_volume = round(c_volume,1)
        mixer.music.set_volume(c_volume)
        volume_label.config(fg="green",text="Volume : "+str(c_volume))
    except Exception as e:
        print(e)
        song_title_label.config(text="Track hasn't selected yet !",fg="red")

def pause():
    try:
        mixer.music.pause()
    except Exception as e:
        print(e)
        song_title_label.config(text="Track hasn't selected yet !",fg="red")

def resume():
    try:
        mixer.music.unpause()
    except Exception as e:
        print(e)
        song_title_label.config(text="Track hasn't selected yet !",fg="red")


master = Tk()
master.title("Music Player")
Label(master,text="Music Player",font=("Calibri",15),fg="red").grid(sticky="N",row=0,padx=120)
Label(master,text="Select a music track you would like to play : ",font=("Calibri",12),fg="black").grid(sticky="N",row=1)
Label(master,text="Volume",font=("Calibri",12),fg="black").grid(sticky="N",row=4)
song_title_label = Label(master,font=("Calibri",12))
song_title_label.grid(sticky="N",row=3)
volume_label = Label(master,font=("Calibri",12))
volume_label.grid(sticky="N",row=5)
Button(master,text="Select Song",font=("Calibri",12),command=play_song).grid(row=2,sticky="N")
Button(master,text="Pause",font=("Calibri",12),command=pause).grid(row=3,sticky="E")
Button(master,text="Play",font=("Calibri",12),command=resume).grid(row=3,sticky="W")
Button(master,text="-",font=("Calibri",12),width=5,command = reduce_vol).grid(row=5,sticky="W")
Button(master,text="+",font=("Calibri",12),width=5,command = increase_vol).grid(row=5,sticky="E")
master.mainloop()