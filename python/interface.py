# interface.py
# Program to set up the interface.

from tkinter import *
from PIL import ImageTk, Image
import glob, math, os
import program

# Main app.
class interface(Frame):
    # Constructor.
    def __init__(self, master):

        Frame.__init__(self, master)
        self.master = master
        self.program = program
        self.intenCode = []#program.get_intenCode()
        self.frame_imgs = [] #self.program.fetch_frame_imgs
        self.frame_width = 500
        self.frame_height = 400
        self.populate_frame_imgs()

        # Create Main frame.
        self.mainFrame = Frame(master)
        self.mainFrame.columnconfigure(0, weight=1)
        self.mainFrame.columnconfigure(1, weight=5)
        self.mainFrame.rowconfigure(0, weight=1)
        self.mainFrame.pack(fill='both', expand=True)
        
        # Create label that shows frames
        img = Image.open('frame_imgs/default.png')
        img = img.resize((self.frame_width, self.frame_height), Image.ANTIALIAS)
        self.chosen_frame = ImageTk.PhotoImage(img)
        self.frameLabel = Label(self.mainFrame, width=500, bg="black", image=self.chosen_frame)
        self.frameLabel.grid(column=1, row=0, sticky=NS, padx=10, pady=10)
        
        # Create frame chooser frame.
        self.listFrame = Frame(self.mainFrame, bg="black", width=50, height=400)
        self.listFrame.grid(column=0, row=0, sticky=NS, padx=10, pady=10)
        self.listFrame.columnconfigure(0, weight=1)
        
        # Layout frame listbox.
        self.listScrollbar = Scrollbar(self.listFrame)
        self.listScrollbar.pack(side=LEFT, fill=BOTH)
        self.list = Listbox(self.listFrame,
                            yscrollcommand=self.listScrollbar.set,
                            selectmode=BROWSE,
                            height=25)
        for i in range(len(self.frame_imgs)):
            self.list.insert(i, "Frame " + str(i + 1))
        self.list.pack(side=TOP)
        self.list.activate(1)
        self.list.bind('<<ListboxSelect>>', self.update_preview)
        self.listScrollbar.config(command=self.list.yview)
    
        # Button to press play to play the frame's corresponding shot
        self.play_button = Button(master, bg="gray", text="Play", fg="white", padx=8, pady=5)
        self.play_button.pack(side=BOTTOM, pady=8)
    
        
    # Event "listener" for listbox change.
    def update_preview(self, event):
        selected_frame_index = self.list.curselection()[0]
        self.chosen_frame = self.frame_imgs[selected_frame_index]
        self.frameLabel.configure(image=self.chosen_frame)
    
    # Read in all frame images from the folder frame_imgs, then convert to
    # a image that can be presented in tkinter
    def populate_frame_imgs(self):
        # Add each frame into self.frame_imgs
        for infile in (glob.glob('frame_imgs/*.png')):
            im = Image.open(infile)

            # Resize to fit the frame
            imResize = im.resize((self.frame_width, self.frame_height), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(imResize)

            # Add the images to the list.
            self.frame_imgs.append(photo)

# Executable section.
if __name__ == '__main__':
    root = Tk()
    root.title('Video Shot Boundary Detection App')
    root.resizable(0, 0)
    
    imageViewer = interface(root)

    root.mainloop()