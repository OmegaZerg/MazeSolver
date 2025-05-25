from display import Window, Point, Line
import time
from random import random, choice
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
        self.visited = False
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
        else:
            self.__win.draw_line(Line(self.__bot_left, self.__top_left), "white")
        if self.has_right_wall:
            self.__win.draw_line(Line(self.__bot_right, self.__top_right))
        else:
            self.__win.draw_line(Line(self.__bot_right, self.__top_right), "white")
        if self.has_bottom_wall:
            self.__win.draw_line(Line(self.__bot_left, self.__bot_right))
        else:
            self.__win.draw_line(Line(self.__bot_left, self.__bot_right), "white")
        if self.has_top_wall:
            self.__win.draw_line(Line(self.__top_left, self.__top_right))
        else:
            self.__win.draw_line(Line(self.__top_left, self.__top_right), "white")

    def draw_move(self, to_cell, undo=False):
        if not self.__win:
            return
        path = Line(self.__center, to_cell.__center)
        if undo == False:
            self.__win.draw_line(path, "red")
        else:
            self.__win.draw_line(path, "gray")
        

class Maze():
    def __init__(self, x1: float, y1: float, num_rows: int, num_cols: int, cell_size_x: float, cell_size_y: float, window: Window = None, draw_speed: float = 0.05, seed: float = None):
        self.__cells = []
        self.__x1 = x1 #x, y maze start position
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = window
        self.__draw_speed = draw_speed
        if seed:
            random.seed(seed)
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)

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

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0,0)
        self.__cells[-1][-1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            unvisited_neighboors = []
            #Check up
            new_i = i - 1
            new_j = j
            if 0 <= new_i < self.__num_rows and 0 <= new_j < self.__num_cols:
                if self.__cells[new_i][new_j].visited == False:
                    unvisited_neighboors.append((new_i, new_j))
            #Check down
            new_i = i + 1
            new_j = j
            if 0 <= new_i < self.__num_rows and 0 <= new_j < self.__num_cols:
                if self.__cells[new_i][new_j].visited == False:
                    unvisited_neighboors.append((new_i, new_j))
            #Check Left
            new_i = i
            new_j = j - 1
            if 0 <= new_i < self.__num_rows and 0 <= new_j < self.__num_cols:
                if self.__cells[new_i][new_j].visited == False:
                    unvisited_neighboors.append((new_i, new_j))
            #Check right
            new_i = i
            new_j = j + 1
            if 0 <= new_i < self.__num_rows and 0 <= new_j < self.__num_cols:
                if self.__cells[new_i][new_j].visited == False:
                    unvisited_neighboors.append((new_i, new_j))

            #If neighbors is empty, then we're done and time to draw the maze
            if len(unvisited_neighboors) < 1:
                self.__draw_cell(i, j)
                return
            
            lucky_neighboor = choice(unvisited_neighboors)
            #Moving Up
            if i > lucky_neighboor[0]:
                self.__cells[i][j].has_top_wall = False
                self.__cells[lucky_neighboor[0]][lucky_neighboor[1]].has_bot_wall = False
            #Moving Down
            if i < lucky_neighboor[0]:
                self.__cells[i][j].has_bot_wall = False
                self.__cells[lucky_neighboor[0]][lucky_neighboor[1]].has_top_wall = False
            #Moving Left
            if j > lucky_neighboor[1]:
                self.__cells[i][j].has_left_wall = False
                self.__cells[lucky_neighboor[0]][lucky_neighboor[1]].has_right_wall = False
            #Moving Right
            if j < lucky_neighboor[1]:
                self.__cells[i][j].has_right_wall = False
                self.__cells[lucky_neighboor[0]][lucky_neighboor[1]].has_left_wall = False

            #Move to chosen cell
            self.__break_walls_r(lucky_neighboor[0], lucky_neighboor[1])