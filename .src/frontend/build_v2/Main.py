from tkinter import Tk
from Frames import Frame1, Frame2, Frame3, Frame4, Frame5


class MainApp:
    def __init__(self, main_root):
        self.root = main_root
        self.root.geometry("1440x1024")
        self.root.configure(bg="#394867")
        self.frame5 = Frame5(self.root, self)
        self.frame4 = Frame4(self.root, self)
        self.frame3 = Frame3(self.root, self)
        self.frame2 = Frame2(self.root, self)
        self.frame1 = Frame1(self.root, self)

        self.current_frame = None  # Track the current active frame

        self.show_frame1()

    def show_frame1(self):
        self.hide_current_frame()
        self.frame1.frame.pack()
        self.current_frame = self.frame1

    def show_frame2(self):
        self.hide_current_frame()
        self.frame2.frame.pack()
        self.current_frame = self.frame2

    def show_frame3(self):
        self.hide_current_frame()
        self.frame3.frame.pack()
        self.frame3.reshow_widgets()
        self.current_frame = self.frame3

    def show_frame4(self):
        self.hide_current_frame()
        self.frame4.frame.pack()
        self.frame4.reshow_widgets() 
        self.current_frame = self.frame4

    def show_frame5(self):
        self.hide_current_frame()
        self.frame5.frame.pack()
        self.current_frame = self.frame5

    def hide_current_frame(self):
        if self.current_frame:
            self.current_frame.frame.pack_forget()


if __name__ == "__main__":
    root = Tk()
    app = MainApp(root)
    root.resizable(False, False)
    root.mainloop()
