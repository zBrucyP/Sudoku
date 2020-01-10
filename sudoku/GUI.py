import tkinter as tk


class Sudoku_GUI:
    def __init__(self, win_HT=800, win_WT=800,bg_color='#FF9D88'):
        self.window_height = win_HT
        self.window_width = win_WT
        self.bg_color=bg_color

        # build the GUI structure
        self.root = self.build_GUI()

        # launch GUI
        self.root.mainloop()

    def build_GUI(self):
        """
        Composes and returns the top level GUI object
        return: tkinter root object
        """
        # root object, highest point in GUI, window
        GUI = tk.Tk()

        # background to fill in the window
        canvas = tk.Canvas(GUI,
                           height=self.window_height,
                            width=self.window_width,
                             bg=self.bg_color)
        canvas.place(relwidth=1,relheight=1)

        # menubar along top


        # frame for toolbar at top
        toolbar = tk.Frame(GUI, bg='white')
        toolbar.place(relwidth=.8, relheight=.1, relx=.1, rely=.05)

        # frame for game board
        game_board = tk.Frame(GUI, bg='white')
        game_board.place(relwidth=.8, relheight=.8, relx=.1, rely=.2)

        # pack elements to their parents
        #canvas.pack()


        return GUI
