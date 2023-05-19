from tkinter import Tk
from Frames import Frame1, Frame2, Frame3, Frame4, Frame5

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1440x1024")
        self.root.configure(bg="#394867")
        self.frame5 = Frame5(self.root, self)
        self.frame4 = Frame4(self.root, self)
        self.frame3 = Frame3(self.root, self)
        self.frame2 = Frame2(self.root, self)
        self.frame1 = Frame1(self.root, self)

        self.show_frame1()

    def show_frame1(self):
        self.frame5.frame.pack_forget()
        self.frame3.frame.pack_forget()
        self.frame2.frame.pack_forget()
        self.frame4.frame.pack_forget()
        self.frame1.frame.pack()

    def show_frame2(self):
        self.frame5.frame.pack_forget()
        self.frame3.frame.pack_forget()
        self.frame1.frame.pack_forget()
        self.frame4.frame.pack_forget()
        self.frame2.frame.pack()

    def show_frame3(self):
        self.frame5.frame.pack_forget()
        self.frame1.frame.pack_forget()
        self.frame2.frame.pack_forget()
        self.frame4.frame.pack_forget()
        self.frame3.frame.pack()
    
    def show_frame4(self):
        self.frame5.frame.pack_forget()
        self.frame3.frame.pack_forget()
        self.frame1.frame.pack_forget()
        self.frame2.frame.pack_forget()
        self.frame4.frame.pack()
        self.frame4.reshow_widgets()

    def show_frame5(self):
        self.frame3.frame.pack_forget()
        self.frame2.frame.pack_forget()
        self.frame4.frame.pack_forget()
        self.frame1.frame.pack_forget()
        self.frame5.frame.pack()
    
if __name__ == "__main__":
    root = Tk()
    app = MainApp(root)
    root.resizable(False, False)
    root.mainloop()
