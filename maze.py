from display import Window, Point, Line
class Cell():
    def __init__(self, window: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__bot_left = -1
        self.__bot_right = -1
        self.__top_left = -1
        self.__top_right = -1
        self.__win = window

    def draw(self, bot_left: Point, bot_right: Point, top_left: Point, top_right: Point):
        self.__bot_left = bot_left
        self.__bot_right = bot_right
        self.__top_left = top_left
        self.__top_right = top_right
        self.center = Point((self.__top_left.x_coordinate + self.__top_right.x_coordinate)/2,(self.__top_left.y_coordinate + self.__bot_left.y_coordinate)/2)
        if self.has_left_wall:
            self.__win.draw_line(Line(self.__bot_left, self.__top_left))
        if self.has_right_wall:
            self.__win.draw_line(Line(self.__bot_right, self.__top_right))
        if self.has_bottom_wall:
            self.__win.draw_line(Line(self.__bot_left, self.__bot_right))
        if self.has_top_wall:
            self.__win.draw_line(Line(self.__top_left, self.__top_right))

    def draw_move(self, to_cell, undo=False):
        path = Line(self.center, to_cell.center)
        if undo == False:
            self.__win.draw_line(path, "red")
        else:
            self.__win.draw_line(path, "gray")
        