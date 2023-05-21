from tkinter import Tk
from Frames import Frame1, Frame2, Frame3, Frame4, Frame5
from backend import insert_information


class MainApp:
    def __init__(self, main_root):
        # initialize the inputs to the table
        self.id = None
        self.role = None
        self.name = None
        self.movie_id = None
        self.movie_name = 'NO MOVIE'
        self.ratings = 0.0
        self.votes = 0
        self.birth = 'null'
        self.movie_year = 'null'

        # declare the frames
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

    def collecting_inserting_data(self):
        # get the user's information
        self.id, self.role = self.frame2.get_id()
        self.name, self.birth = self.frame3.get_name_birth()
        print("id: {}\nrole: {}\nname: {}\nbirth: {}\n".format(self.id, self.role, self.name, self.birth))
        # if they have a movie get the data
        if self.movie_id == self.frame3.get_movie_id():
            self.movie_id, self.movie_name, self.ratings, self.votes, self.movie_year = self.frame4.get_movie_data()
            '''print("\n\nid: {} as type {}\nname: {} as type {}\nyear: {} as type {}\nratings: {} as type {}\n"
                  "votes: {} as type {}".format(self.movie_id, type(self.movie_id), self.movie_name,
                                                type(self.movie_name), self.movie_year, type(self.movie_year),
                                                self.ratings, type(self.ratings), self.votes, type(self.votes)))'''
        else:
            self.movie_id = self.frame3.get_movie_id()
            '''print("\n\nid: {} as type {}\nname: {} as type {}\nyear: {} as type {}\nratings: {} as type {}\n"
                  "votes: {} as type {}".format(self.movie_id, type(self.movie_id), self.movie_name,
                                                type(self.movie_name), self.movie_year, type(self.movie_year),
                                                self.ratings, type(self.ratings), self.votes, type(self.votes)))'''
        if self.birth == 'null':
            self.birth = None
        if self.movie_year == 'null':
            self.movie_year = None
        # insert all information got
        insert_information(role=self.role, a_d_id=self.id, name=self.name, movie_id=self.movie_id,
                           movie_name=self.movie_name, ratings=self.ratings, votes=self.votes, 
                           movie_year=self.movie_year, birth=self.birth)

        # re-initialize the data
        self.id = None
        self.role = None
        self.name = None
        self.movie_id = None
        self.movie_name = 'NO MOVIE'
        self.ratings = 0.0
        self.votes = 0
        self.birth = 'null'
        self.movie_year = 'null'

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
        self.collecting_inserting_data()
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
