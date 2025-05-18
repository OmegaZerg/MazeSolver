from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.title("Maze Stuff") 
        self.__canvas = Canvas(self.__root, height=self.__height, width=self.__width, bg="white")
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        print("Window Closed.")

    def close(self):
        self.__is_running = False
        