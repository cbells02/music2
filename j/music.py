from tkinter import Tk, Label, Button
from tkinter.filedialog import askdirectory
import pygame
import os
from mutagen.id3 import ID3


pygame.init()

listofsong = []

index = 0


def directorychooser():
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            realdir = os.path.realpath(files)
            audio = ID3(realdir)

            listofsong.append(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listofsong[0])


directorychooser()




class MyGUI:
    def __init__(self, master):
        self.master = master
        master.title("my music App")

        self.label = Label(master, text="the GUI")
        self.label.pack()

        self.greet_button = Button(master, text="play music", command=self.play)
        self.greet_button.pack()

        self.greet_button = Button(master, text="pause", command=self.pause)
        self.greet_button.pack()

        self.greet_button = Button(master, text="unpause", command=self.unpause)
        self.greet_button.pack()

        self.greet_button = Button(master, text="next", command=self.nextsong)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def play(self):
        pygame.mixer.music.load(listofsong[index])
        pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()


    def unpause(self):
        pygame.mixer.music.unpause()

    def nextsong(self):
        global index
        index += 1
        while index <=listofsong:
            try:
                pygame.mixer.music.load(listofsong[index])
                pygame.mixer.music.play()
                pass
            except IndexError:
                print("opppppps")






'''
       global index
        index += 1
        if index <= len(listofsong):
            pygame.mixer.music.load(listofsong[index])
            pygame.mixer.music.play()
        elif index > len(listofsong):

            index = 0
            pygame.mixer.music.load(listofsong[index])
            pygame.mixer.music.play()

'''

root = Tk()
my_gui = MyGUI(root)
root.mainloop()

#for the next song make a exception for the error and have it play the first song in the index#
#make a better GUI#
