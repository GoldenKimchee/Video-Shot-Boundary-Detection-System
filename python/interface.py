# interface.py
# Program to set up the interface.

from tkinter import *
from PIL import ImageTk, Image
import glob, math, os
from program import program

# Main app.
class interface(Frame):
    # Constructor
    def __init__(self, master):

        self.program = program()
        self.frame_width = 500
        self.frame_height = 400
        self.frame_imgs = []

        # Check for pre-exisiting frames. If there are no frames, it will generate them.
        frames_present = self.check_frame_imgs()
        
        # If there are frames present in frame_imgs, ask the user if they want to re-extract the
        # frames or skip extraction.
        if (frames_present):
            self.ask_conversion()
        
        # Ask user how intensity bins should be loaded
        self.program.ask_intensity_bins()
        
        # Generate SD values
        self.program.generate_sd()
        
        # Calculate thresholds from SD values
        self.program.set_thresholds()
        
        # Calculate start and end frames with Twin-comparison based approach
        self.program.find_frames()
        
        # Print the sets of (Cs, Ce) and (Fs, Fe).
        self.program.frame_sets()

        print("Now loading interface...")

        # Populate self.frame_imgs so they appear in Listbox
        self.populate_frame_imgs()
        
        # Generate cut's start and end frames 
        self.program.generate_frame_imgs()

        # Generate window
        Frame.__init__(self, master)
        self.master = master

        # Create Main frame.
        self.mainFrame = Frame(master)
        self.mainFrame.columnconfigure(0, weight=1)
        self.mainFrame.columnconfigure(1, weight=5)
        self.mainFrame.rowconfigure(0, weight=1)
        self.mainFrame.pack(fill='both', expand=True)
        
        # Create label that shows frames
        img = Image.open('default.jpg')
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
        for infile in (glob.glob('frame_imgs/*.jpg')):
            im = Image.open(infile)

            # Resize to fit the frame
            imResize = im.resize((self.frame_width, self.frame_height), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(imResize)

            # Add the images to the list.
            self.frame_imgs.append(photo)

    # Check if the 'frame_imgs' folder has any pre-existing frames
    def check_frame_imgs(self):
        # Locate frame_imgs folder that stores the frames
        dirname = os.path.dirname(__file__)
        path = os.path.join(dirname, 'frame_imgs')

        # Getting the list of directories
        dir = os.listdir(path)
  
        # Checking if the list is empty or not
        if len(dir) == 0:  
            print("There are no pre-existing frame images.")
            print("Frame images will now be extracted into 'frame_imgs' folder")

            self.program.extract_frames()
            return False

        else:
            return True
    
    def ask_conversion(self):
        convert = input("Convert from pre-existing frames? (y/n) ")

        while True:
            convert = convert.lower()
            if (convert == "n"):
                self.program.extract_frames()
                self.program.get_dimensions()
                break
            elif (convert == "y"):
                self.program.convert_to_pil_imgs()
                self.program.get_dimensions
                break
            convert = input("Please enter y or n ")
        
        print("Done with image conversions.")

# Executable section.
if __name__ == '__main__':
    root = Tk()
    root.title('Video Shot Boundary Detection App')
    root.resizable(0, 0)

    imageViewer = interface(root)

    root.mainloop()