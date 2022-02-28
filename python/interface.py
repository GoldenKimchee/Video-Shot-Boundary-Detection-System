# interface.py
# Program to set up the interface.

from tkinter import *
import math, os
import program

# Main app.
class interface(Frame):
    # Constructor.
    def __init__(self, master):

        Frame.__init__(self, master)
        self.master = master
        self.program = program
        self.intenCode = []#program.get_intenCode()

        # Create Main frame.
        mainFrame = Frame(master)
        mainFrame.columnconfigure(0, weight=1)
        mainFrame.columnconfigure(1, weight=5)
        mainFrame.rowconfigure(0, weight=1)
        mainFrame.pack(fill='both', expand=True)

        # Create video view frame
        videoFrame = Frame(mainFrame, bg="white", width=600, height=400)
        videoFrame.grid(column=1, row=0, sticky=NS, padx=10, pady=10)
        
        # Create frame chooser frame.
        listFrame = Frame(mainFrame, bg="black", width=50, height=400)
        listFrame.grid(column=0, row=0, sticky=NS, padx=10, pady=10)
        listFrame.columnconfigure(0, weight=1)
        
        # Layout frame listbox.
        self.listScrollbar = Scrollbar(listFrame)
        self.listScrollbar.pack(side=LEFT, fill=BOTH)
        self.list = Listbox(listFrame,
                            yscrollcommand=self.listScrollbar.set,
                            selectmode=BROWSE,
                            height=25)
        for i in range(2):
            self.list.insert(i, "Image " + str(i + 1))
        self.list.pack(side=TOP)
        self.list.activate(1)
        self.list.bind('<<ListboxSelect>>', self.update_preview)
        self.listScrollbar.config(command=self.list.yview)
    
        self.play_button = Button(master, bg="gray", text="Play", fg="white", padx=8, pady=5)
        self.play_button.pack(side=BOTTOM, pady=8)
        
        
    def update_preview():
        pass

# Executable section.
if __name__ == '__main__':
    root = Tk()
    root.title('Video Shot Boundary Detection App')
    #root.geometry('900x600')
    root.resizable(0, 0)
    
    imageViewer = interface(root)

    root.mainloop()