from display import Window, Point, Line
class Cell():
    def __init__(self, window: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, bot_left: Point, bot_right: Point, top_left: Point, top_right: Point):
        self.__bot_left = bot_left
        self.__bot_right = bot_right
        self.__top_left = top_left
        self.__top_right = top_right
        if self.has_left_wall:
            self.__win.draw_line(Line(self.__bot_left, self.__top_left))
        if self.has_right_wall:
            self.__win.draw_line(Line(self.__bot_right, self.__top_right))
        if self.has_bottom_wall:
            self.__win.draw_line(Line(self.__bot_left, self.__bot_right))
        if self.has_top_wall:
            self.__win.draw_line(Line(self.__top_left, self.__top_right))