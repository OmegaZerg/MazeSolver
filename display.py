from tkinter import Tk, BOTH, Canvas

class Point():
    def __init__(self, x: float, y: float):
        self.x_coordinate = x
        self.y_coordinate = y

class Line():
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(self.point1.x_coordinate, self.point1.y_coordinate, self.point2.x_coordinate, self.point2.y_coordinate, fill=fill_color, width=2)

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

    def draw_line(self, line: Line, fill_color: str="black"):
        line.draw(self.__canvas, fill_color)

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        print("Window Closed.")

    def close(self):
        self.__is_running = False
        

