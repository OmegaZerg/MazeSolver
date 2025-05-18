from display import Window, Point, Line
from maze import Cell

def main():
    win = Window(800, 600)
    point1, point2 = Point(100.5, 250), Point(300, 320.8)
    line = Line(point1, point2)
    win.draw_line(line, "black")

    cell1 = Cell(win)
    cell1.has_right_wall = False
    cell1.draw(Point(100, 100), Point(200, 100), Point(100, 200), Point(200, 200))

    cell2 = Cell(win)
    cell2.has_left_wall = True
    cell2.draw(Point(200, 100), Point(300, 100), Point(200, 200), Point(300, 200))

    cell1.draw_move(cell2, True)
    
    win.redraw()
    win.wait_for_close()

if __name__ == "__main__":
    main()