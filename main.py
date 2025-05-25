from display import Window, Point, Line
from maze import Cell, Maze
import sys

def main():    
    # #----Testing----
    # point1, point2 = Point(100.5, 250), Point(300, 320.8)
    # line = Line(point1, point2)
    # win.draw_line(line, "black")

    # #----Testing2----
    # cell1 = Cell(win)
    # cell1.has_right_wall = False
    # cell1.draw(Point(100, 100), Point(200, 100), Point(100, 200), Point(200, 200))
    # cell2 = Cell(win)
    # cell2.has_left_wall = True
    # cell2.draw(Point(200, 100), Point(300, 100), Point(200, 200), Point(300, 200))
    # cell1.draw_move(cell2, True)

    #----Testing3----
    rows = 10
    columns = 10
    margin = 5 
    window_x = 800
    window_y = 600
    cell_size_x = (window_x - 2 * margin) / columns
    cell_size_y = (window_y - 2 * margin) / rows
    draw_speed = 0.01

    sys.setrecursionlimit(10000)
    win = Window(window_x, window_y)
    maze = Maze(margin, margin, rows, columns, cell_size_x, cell_size_y, win, draw_speed)
    is_solvable =  maze.solve()
    if not is_solvable:
        print("maze can not be solved!")
    else:
        print("maze solved!")
    win.wait_for_close()

if __name__ == "__main__":
    main()