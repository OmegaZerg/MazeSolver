from display import Window, Point, Line
import time
class Cell():
    def __init__(self, window: Window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__bot_left = -1
        self.__bot_right = -1
        self.__top_left = -1
        self.__top_right = -1
        self.__center = -1
        self.__win = window

    def draw(self, bot_left: Point, bot_right: Point, top_left: Point, top_right: Point):
        if not self.__win:
            return
        self.__bot_left = bot_left
        self.__bot_right = bot_right
        self.__top_left = top_left
        self.__top_right = top_right
        self.__center = Point((self.__top_left.x_coordinate + self.__top_right.x_coordinate)/2,(self.__top_left.y_coordinate + self.__bot_left.y_coordinate)/2)
        if self.has_left_wall:
            self.__win.draw_line(Line(self.__bot_left, self.__top_left))
        if self.has_right_wall:
            self.__win.draw_line(Line(self.__bot_right, self.__top_right))
        if self.has_bottom_wall:
            self.__win.draw_line(Line(self.__bot_left, self.__bot_right))
        if self.has_top_wall:
            self.__win.draw_line(Line(self.__top_left, self.__top_right))

    def draw_move(self, to_cell, undo=False):
        if not self.__win:
            return
        path = Line(self.__center, to_cell.__center)
        if undo == False:
            self.__win.draw_line(path, "red")
        else:
            self.__win.draw_line(path, "gray")
        

class Maze():
    def __init__(self, x1: float, y1: float, num_rows: int, num_cols: int, cell_size_x: float, cell_size_y: float, window: Window = None, draw_speed: float = 0.05):
        self.__cells = []
        self.__x1 = x1 #x, y maze start position
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = window
        self.__draw_speed = draw_speed
        self.__create_cells()

    def __create_cells(self):
        rows = []
        for i in range(self.__num_cols):
            row = []
            for j in range(self.__num_rows):
                row.append(Cell(self.__win))
            rows.append(row)
        self.__cells = rows
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i: int, j: int):
        if not self.__win:
            return
        x1 = self.__x1 + (i * self.__cell_size_x)
        x2 = x1 + self.__cell_size_x
        y1 = self.__y1 + (j * self.__cell_size_y)
        y2 = y1 + self.__cell_size_y
        self.__cells[i][j].draw(Point(x1, y2), Point(x2, y2), Point(x1, y1), Point(x2, y1))
        self.__animate()

    def __animate(self):
        if not self.__win:
            return
        self.__win.redraw()
        time.sleep(self.__draw_speed)