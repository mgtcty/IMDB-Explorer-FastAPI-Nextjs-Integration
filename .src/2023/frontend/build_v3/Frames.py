from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Canvas, Entry, Button, PhotoImage, font
from functools import partial
import backend


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_1 = OUTPUT_PATH / Path(r"assets\frame4")
ASSETS_PATH_2 = OUTPUT_PATH / Path(r"assets\frame3")
ASSETS_PATH_3 = OUTPUT_PATH / Path(r"assets\frame2")
ASSETS_PATH_4 = OUTPUT_PATH / Path(r"assets\frame1")
ASSETS_PATH_5 = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets_frame1(path: str) -> Path:
    return ASSETS_PATH_1 / Path(path)


def relative_to_assets_frame2(path: str) -> Path:
    return ASSETS_PATH_2 / Path(path)


def relative_to_assets_frame3(path: str) -> Path:
    return ASSETS_PATH_3 / Path(path)


def relative_to_assets_frame4(path: str) -> Path:
    return ASSETS_PATH_4 / Path(path)


def relative_to_assets_frame5(path: str) -> Path:
    return ASSETS_PATH_5 / Path(path)


class Frame1:
    def __init__(self, parent, switch_frame):
        self.parent = parent
        self.switch_frame = switch_frame

        self.frame = Canvas(
            self.parent,
            bg="#394867",
            height=1024,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.frame.place(x=0, y=0)
        self.image_1 = PhotoImage(file=relative_to_assets_frame1("image_1.png"))
        self.canvas_image_1 = self.frame.create_image(720.0, 512.0, image=self.image_1)

        self.image_2 = PhotoImage(file=relative_to_assets_frame1("image_2.png"))
        self.canvas_image_2 = self.frame.create_image(721.0, 514.0, image=self.image_2)

        self.image_3 = PhotoImage(file=relative_to_assets_frame1("image_3.png"))
        self.canvas_image_3 = self.frame.create_image(721.0, 618.0, image=self.image_3)

        self.button1_image = PhotoImage(file=relative_to_assets_frame1("button_1.png"))
        self.button1 = Button(
            self.frame,
            image=self.button1_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.switch_to_frame2,
            relief="flat"
        )
        self.button1.place(x=462.0, y=639.0, width=495.0, height=147.0)

    def switch_to_frame2(self):
        self.frame.pack_forget()
        self.switch_frame.show_frame2()


class Frame2:
    def __init__(self, parent, switch_frame):
        self.id = None
        self.role = None

        # initialize the director and actor
        self.director = 0
        self.actor = 1

        self.parent = parent
        self.switch_frame = switch_frame
        self.frame = Canvas(
            self.parent,
            bg="#394867",
            height=1024,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.frame.place(x=0, y=0)

        self.image_1 = PhotoImage(file=relative_to_assets_frame2("image_1.png"))
        self.canvas_image_1 = self.frame.create_image(720.0, 512.0, image=self.image_1)

        self.image_2 = PhotoImage(file=relative_to_assets_frame2("image_2.png"))
        self.canvas_image_2 = self.frame.create_image(721.0, 514.0, image=self.image_2)

        self.image_3 = PhotoImage(file=relative_to_assets_frame2("image_3.png"))
        self.canvas_image_3 = self.frame.create_image(724.0, 620.0, image=self.image_3)

        self.button1_image = PhotoImage(file=relative_to_assets_frame2("button_1.png"))
        self.button1 = Button(
            self.frame,
            image=self.button1_image,
            borderwidth=0,
            highlightthickness=0,
            command=partial(self.switch_to_frame3, self.director),
            relief="flat"
        )
        self.button1.place(x=730.0, y=635.0, width=450.0, height=120.0)

        self.button2_image = PhotoImage(file=relative_to_assets_frame2("button_2.png"))
        self.button2 = Button(
            self.frame,
            image=self.button2_image,
            borderwidth=0,
            highlightthickness=0,
            command=partial(self.switch_to_frame3, self.actor),
            relief="flat"
        )
        self.button2.place(x=224.0, y=635.0, width=450.0, height=120.0)

    def switch_to_frame3(self, role):
        self.id = backend.get_actor_director(role)
        self.role = role
        self.frame.pack_forget()
        self.switch_frame.show_frame3()

    def get_id(self):
        return self.id, self.role


class Frame3:
    def __init__(self, parent, switch_frame):
        self.name = None
        self.birth = 'null'
        self.movie_id = None
        self.movie_name = None

        self.parent = parent
        self.switch_frame = switch_frame
        
        self.frame = Canvas(self.parent, bg="#394867", height=1024, width=1440, bd=0, highlightthickness=0,
                            relief="ridge")
        self.frame.place(x=0, y=0)

        self.image_1 = PhotoImage(file=relative_to_assets_frame3("image_1.png"))
        self.canvas_image_1 = self.frame.create_image(720.0, 512.0, image=self.image_1)

        self.image_2 = PhotoImage(file=relative_to_assets_frame3("image_2.png"))
        self.canvas_image_2 = self.frame.create_image(721.0, 514.0, image=self.image_2)

        self.image_3 = PhotoImage(file=relative_to_assets_frame3("image_3.png"))
        self.canvas_image_3 = self.frame.create_image(722.0, 610.0, image=self.image_3)

        self.image_4 = PhotoImage(file=relative_to_assets_frame3("image_4.png"))
        self.canvas_image_4 = self.frame.create_image(716.0, 785.0, image=self.image_4)

        self.button1_image = PhotoImage(file=relative_to_assets_frame3("button_1.png"))
        self.button_1 = Button(self.frame, image=self.button1_image, borderwidth=0, highlightthickness=0,
                               command=self.switch_to_frame4)
        self.button_1.place(x=651.0, y=723.0, width=200.0, height=100.0)

        self.button2_image = PhotoImage(file=relative_to_assets_frame3("button_2.png"))
        self.button_2 = Button(self.frame, image=self.button2_image, borderwidth=0, highlightthickness=0,
                               command=self.switch_to_frame5)
        self.button_2.place(x=879.0, y=723.0, width=400.0, height=100.0)
        custom_font = font.Font(size=35)
        self.entry_1 = Entry(
            font=custom_font,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=182.0,
            y=385.0,
            width=1094.0,
            height=69.0
        )
        self.entry_2 = Entry(
            font=custom_font,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=183.0,
            y=573.0,
            width=1094.0,
            height=69.0
        )
        self.image_5 = PhotoImage(
            file=relative_to_assets_frame3("image_5.png"))
        self.canvas_image_5 = self.frame.create_image(
            271.0,
            343.0,
            image=self.image_5
        )

        self.image_6 = PhotoImage(
            file=relative_to_assets_frame3("image_6.png"))
        self.canvas_image_6 = self.frame.create_image(
            454.0,
            526.0,
            image=self.image_6
        )
        self.hide = False  # Track if widgets are hidden or not
     
    def switch_to_frame5(self):
        try:
            self.name, birth = self.entry_1.get(), self.entry_2.get()
            if birth.strip() == '':
                self.birth = 'null'
            elif type(birth) == str:
                self.birth = int(birth)

            self.movie_id = backend.get_highest_movie_id()
            self.frame.pack_forget()
            if not self.hide:
                self.hide_widgets()  # Hide the widgets if not already hidden
            self.switch_frame.show_frame5()
        except ValueError:
            print("Invalid input. Please enter a valid birth.")

    def switch_to_frame4(self):
        try:
            self.name, birth = self.entry_1.get(), self.entry_2.get()
            if birth.strip() == '':
                self.birth = 'null'
            elif type(birth) == str:
                self.birth = int(birth)

            self.frame.pack_forget()
            if not self.hide:
                self.hide_widgets()  # Hide the widgets if not already hidden
            self.switch_frame.show_frame4()
        except ValueError:
            print("Invalid input. Please enter a valid birth.")

    def get_name_birth(self):
        return self.name, self.birth

    def get_movie_id(self):
        return self.movie_id

    def reshow_widgets(self):
        if self.hide:
            self.show_widgets()  # Show the widgets if hidden

    def hide_widgets(self):
        self.entry_1.place_forget()
        self.entry_2.place_forget()
        self.hide = True

    def show_widgets(self):
        self.entry_1.place(
            x=182.0,
            y=385.0,
            width=1094.0,
            height=69.0
        )
        self.entry_2.place(
            x=183.0,
            y=573.0,
            width=1094.0,
            height=69.0
        )
        self.hide = False


class Frame4:
    
    def __init__(self, parent, switch_frame):
        self.movie_id = None
        self.movie_name = None
        self.ratings = None
        self.votes = None
        self.year = 'null'
        self.parent = parent
        self.switch_frame = switch_frame
    
        self.frame = Canvas(self.parent, bg="#394867", height=1024, width=1440, bd=0, highlightthickness=0,
                            relief="ridge")
        self.frame.place(x=0, y=0)
        self.button1_image = PhotoImage(
            file=relative_to_assets_frame4("button_1.png"))
        self.button1 = Button(
            image=self.button1_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.switch_to_frame5,
            relief="flat"
        )
        self.button1.place(
            x=513.0,
            y=759.0,
            width=400.0,
            height=100.0
        )
        self.image_1 = PhotoImage(
            file=relative_to_assets_frame4("image_1.png"))
        self.canvas_image_1 = self.frame.create_image(
            720.0,
            512.0,
            image=self.image_1
        )
        self.image_2 = PhotoImage(
            file=relative_to_assets_frame4("image_2.png"))
        self.canvas_image_2 = self.frame.create_image(
            721.0,
            514.0,
            image=self.image_2
        )
        custom_font = font.Font(size=35)
        self.entry_1 = Entry(
            font=custom_font,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=189.0,
            y=595.0,
            width=313.0,
            height=97.0
        )
        self.entry_2 = Entry(
            font=custom_font,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=569.0,
            y=595.0,
            width=313.0,
            height=97.0
        )
        self.entry_3 = Entry(
            font=custom_font,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_3.place(
            x=937.0,
            y=595.0,
            width=313.0,
            height=97.0
        )
        self.entry_4 = Entry(
            font=custom_font,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_4.place(
            x=176.0,
            y=404.0,
            width=1100.0,
            height=69.0
        )
        self.image_3 = PhotoImage(
            file=relative_to_assets_frame4("image_3.png"))
        self.canvas_image_3 = self.frame.create_image(
            722.0,
            618.0,
            image=self.image_3
        )
        self.hidden = False  # Track if widgets are hidden or not

    def switch_to_frame5(self):
        # Convert the input values to the expected types
        self.movie_id = backend.get_highest_movie_id()
        self.movie_name = self.entry_4.get()

        # check if the input value contains only spaces or is empty
        if self.movie_name.strip() == '':
            raise ValueError("Invalid input. Please enter a movie title.")

        # check if the input value contains float or string on the rating and votes respectively
        try:
            self.ratings = float(self.entry_2.get())
            self.votes = int(self.entry_3.get())
            year = self.entry_1.get()
            if year.strip() == '':
                self.year = 'null'
            elif type(year) == str:
                self.year = int(year)

            self.frame.pack_forget()
            if not self.hidden:
                self.hide_widgets()  # Hide the widgets if not already hidden
            self.switch_frame.show_frame5()
        except ValueError:
            print("Invalid input. Please enter a float for rating and integer for votes and year.")

    def get_movie_data(self):
        self.movie_id = backend.get_highest_movie_id()
        self.movie_name = self.entry_4.get()
        self.ratings = float(self.entry_2.get())
        self.votes = int(self.entry_3.get())
        return self.movie_id, self.movie_name, self.ratings, self.votes, self.year

    def reshow_widgets(self):
        if self.hidden:
            self.show_widgets()  # Show the widgets if hidden

    def hide_widgets(self):
        self.entry_1.place_forget()
        self.entry_2.place_forget()
        self.entry_3.place_forget()
        self.entry_4.place_forget()
        self.button1.place_forget()
        self.hidden = True

    def show_widgets(self):
        self.entry_1.place(
            x=189.0,
            y=595.0,
            width=313.0,
            height=97.0
        )
        self.entry_2.place(
            x=569.0,
            y=595.0,
            width=313.0,
            height=97.0
        )
        self.entry_3.place(
            x=937.0,
            y=595.0,
            width=313.0,
            height=97.0
        )
        self.entry_4.place(
            x=176.0,
            y=404.0,
            width=1100.0,
            height=69.0
        )
        self.button1.place(
            x=513.0,
            y=759.0,
            width=400.0,
            height=100.0
        )
        self.hidden = False


class Frame5:
    def __init__(self, parent, switch_frame):
        self.parent = parent
        self.switch_frame = switch_frame
        self.frame = Canvas(self.parent, bg="#394867", height=1024, width=1440, bd=0, highlightthickness=0,
                            relief="ridge")
        self.frame.place(x=0, y=0)
        self.image_1 = PhotoImage(
            file=relative_to_assets_frame5("image_1.png"))
        self.canvas_image_1 = self.frame.create_image(
            720.0,
            512.0,
            image=self.image_1
        )

        self.image_2 = PhotoImage(
            file=relative_to_assets_frame5("image_2.png"))
        self.canvas_image_2 = self.frame.create_image(
            721.0,
            514.0,
            image=self.image_2
        )

        self.image_3 = PhotoImage(
            file=relative_to_assets_frame5("image_3.png"))
        self.canvas_image_3 = self.frame.create_image(
            721.0,
            617.0,
            image=self.image_3
        )

        self.button1_image = PhotoImage(
            file=relative_to_assets_frame5("button_1.png"))
        self.button_1 = Button(
            image=self.button1_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.switch_to_frame1,
            relief="flat"
        )
        self.button_1.place(
            x=263.0,
            y=661.0,
            width=900.0,
            height=100.0
        )

    def switch_to_frame1(self):

        self.frame.pack_forget()
        self.switch_frame.show_frame1()
