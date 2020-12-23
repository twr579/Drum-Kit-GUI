from tkinter import Button, Entry, Label, Tk, StringVar
import pyglet
import webbrowser

# The parent class of the program. Contains key bindings and buttons for all
# drum sounds, entry and submit button for YouTube searches, and functions for
# playing acoustic drum sounds, changing between acoustic and electric, and
# opening YouTube links.
class DrumKit:
    def __init__(self, master):

        # Each key is bound to a function to play a specific drum sound.
        master.bind('a', lambda event: self.snare())
        master.bind('s', lambda event: self.snare())
        master.bind('d', lambda event: self.kick())
        master.bind('f', lambda event: self.htom())
        master.bind('g', lambda event: self.mtom())
        master.bind('h', lambda event: self.ltom())
        master.bind('j', lambda event: self.crash())
        master.bind('k', lambda event: self.ophat())
        master.bind('l', lambda event: self.ophat())
        master.bind('o', lambda event: self.clhat())
        master.bind('p', lambda event: self.clhat())
        master.bind('n', lambda event: self.ride())
        master.bind('m', lambda event: self.ride())

        # Buttons for switching between acoustic and electric drums.
        self.acoustic = Button(drums,text="Acoustic",fg="black",width=10,
        command=lambda: self.setAcoustic(drums)).place(x=300,y=80)

        self.electric = Button(drums,text="Electric",fg="black",width=10,
        command=lambda: self.setElectric(drums)).place(x=400,y=80)

        # Buttons with labels corresponding to the key which will play the same
        # drum sound.
        self.a = Button(drums,text="a",fg="black",width=2,height=1,
        command=lambda: self.snare()).place(x=90,y=230)

        self.s = Button(drums,text="s",fg="black",width=2,height=1,
        command=lambda: self.snare()).place(x=120,y=230)

        self.d = Button(drums,text="d",fg="black",width=2,height=1,
        command=lambda: self.kick()).place(x=210,y=230)

        self.f = Button(drums,text="f",fg="black",width=2,height=1,
        command=lambda: self.htom()).place(x=300,y=230)

        self.g = Button(drums,text="g",fg="black",width=2,height=1,
        command=lambda: self.mtom()).place(x=390,y=230)

        self.h = Button(drums,text="h",fg="black",width=2,height=1,
        command=lambda: self.ltom()).place(x=480,y=230)

        self.j = Button(drums,text="j",fg="black",width=2,height=1,
        command=lambda: self.crash()).place(x=570,y=230)

        self.k = Button(drums,text="k",fg="black",width=2,height=1,
        command=lambda: self.ophat()).place(x=660,y=230)

        self.l = Button(drums,text="l",fg="black",width=2,height=1,
        command=lambda: self.ophat()).place(x=690,y=230)

        self.o = Button(drums,text="o",fg="black",width=2,height=1,
        command=lambda: self.clhat()).place(x=660,y=155)

        self.p = Button(drums,text="p",fg="black",width=2,height=1,
        command=lambda: self.clhat()).place(x=690,y=155)

        self.n = Button(drums,text="n",fg="black",width=2,height=1,
        command=lambda: self.ride()).place(x=660,y=305)

        self.m = Button(drums,text="m",fg="black",width=2,height=1,
        command=lambda: self.ride()).place(x=690,y=305)

        # The base for the YouTube search link. The video title searched for
        # via the entry function will be appended to this url.
        self.url = "https://www.youtube.com/results?search_query="

        # Variable storing YouTube search title.
        self.s = StringVar()

        # Entry bar in GUI.
        self.entry = Entry(drums,textvariable=self.s,
        width=15)
        self.entry.place(x=320,y=152)

        # Button to submit YouTube search and open link.
        self.submit = Button(drums,text="Search",
        command=lambda: self.search(self.url, self.s)).place(x=420,y=150)

    # Functions for each drum sound effect (acoustic). Calls functions from the
    # Pyglet library.

    # Snare drum
    def snare(self):
        snare = pyglet.media.load('sounds/snare.wav', streaming=False)
        snare.play()

    # Kick drum
    def kick(self):
        kick = pyglet.media.load('sounds/kick.wav', streaming=False)
        kick.play()

    # High tom drum
    def htom(self):
        htom = pyglet.media.load('sounds/htom.wav', streaming=False)
        htom.play()

    # Mid tom drum
    def mtom(self):
        mtom = pyglet.media.load('sounds/mtom.wav', streaming=False)
        mtom.play()

    # Low tom drum
    def ltom(self):
        ltom = pyglet.media.load('sounds/ltom.wav', streaming=False)
        ltom.play()

    # Crash cymbal
    def crash(self):
        crash = pyglet.media.load('sounds/crash.wav', streaming=False)
        crash.play()

    # Open hi-hat
    def ophat(self):
        ophat = pyglet.media.load('sounds/ophat.wav', streaming=False)
        ophat.play()

    # Closed hi-hat
    def clhat(self):
        clhat = pyglet.media.load('sounds/clhat.wav', streaming=False)
        clhat.play()

    # Ride cymbal
    def ride(self):
        ride = pyglet.media.load('sounds/ride.wav', streaming=False)
        ride.play()

    # Changes class to acoustic drumkit.
    def setAcoustic(self, tk):
        self = ADrumKit(tk)

    # Changes class to electric drumkit.
    def setElectric(self, tk):
        self = EDrumKit(tk)

    # Searches for video using the webbrowser library. Replaces spaces in
    # search with '+'
    def search(self, url, s):
        s = s.get()
        s = s.replace(' ', '+')
        url += s
        webbrowser.open(url,new=1)

        # Reset entry box
        self.entry.destroy()
        self.entry = Entry(drums,textvariable=self.s,
        width=15)
        self.entry.place(x=320,y=152)

# Acoustic drumkit class. Shares all attributes with its parent class.
class ADrumKit(DrumKit):
    pass

# Electric drumkit class. Shares __init__, setAcoustic, setElectric, and
# search functions, but drum functions will play electric drum sound
# effects.
class EDrumKit(DrumKit):

    # Functions for each drum sound effect (electric). Calls functions from the
    # Pyglet library.
    def snare(self):
        snare = pyglet.media.load('sounds/e_snare.wav', streaming=False)
        snare.play()

    def kick(self):
        kick = pyglet.media.load('sounds/e_kick.wav', streaming=False)
        kick.play()

    def htom(self):
        htom = pyglet.media.load('sounds/e_htom.wav', streaming=False)
        htom.play()

    def mtom(self):
        mtom = pyglet.media.load('sounds/e_mtom.wav', streaming=False)
        mtom.play()

    def ltom(self):
        ltom = pyglet.media.load('sounds/e_ltom.wav', streaming=False)
        ltom.play()

    def crash(self):
        crash = pyglet.media.load('sounds/e_crash.wav', streaming=False)
        crash.play()

    def ophat(self):
        ophat = pyglet.media.load('sounds/e_ophat.wav', streaming=False)
        ophat.play()

    def clhat(self):
        clhat = pyglet.media.load('sounds/e_clhat.wav', streaming=False)
        clhat.play()

    def ride(self):
        ride = pyglet.media.load('sounds/e_ride.wav', streaming=False)
        ride.play()

# Create a new Tk GUI from the DrumKit parent class
drums = Tk()
dk = DrumKit(drums)

# Title and dimensions of GUI
drums.title("Drummer")
drums.geometry("800x400")

# Labels
instructions = Label(drums,text="Use the keyboard to drum!",fg="black",
font=("Helvetica",20)).place(x=230,y=10)

switch = Label(drums,text="Switch between acoustic and electric drums!",
fg="black",font=("Helvetica",10)).place(x=260,y=50)

search = Label(drums,text="Type a song name to search on YouTube and play along!",
fg="black",font=("Helvetica",10)).place(x=230,y=120)

snare = Label(drums,text="Snare",fg="black",
font=("Helvetica",10)).place(x=95,y=200)

kick = Label(drums,text="Kick",fg="black",
font=("Helvetica",10)).place(x=205,y=200)

htom = Label(drums,text="High Tom",fg="black",
font=("Helvetica",10)).place(x=285,y=200)

mtom = Label(drums,text="Mid Tom",fg="black",
font=("Helvetica",10)).place(x=375,y=200)

ltom = Label(drums,text="Low Tom",fg="black",
font=("Helvetica",10)).place(x=465,y=200)

crash = Label(drums,text="Crash",fg="black",
font=("Helvetica",10)).place(x=560,y=200)

ophat = Label(drums,text="Open Hi-Hat",fg="black",
font=("Helvetica",10)).place(x=650,y=200)

clhat = Label(drums,text="Closed Hi-Hat",fg="black",
font=("Helvetica",10)).place(x=645,y=125)

ride = Label(drums,text="Ride",fg="black",
font=("Helvetica",10)).place(x=670,y=275)

# Run Tkinter application
drums.mainloop()
