from display import Window, Point, Line

def main():
    win = Window(800, 600)
    point1, point2 = Point(100.5, 250), Point(300, 320.8)
    line = Line(point1, point2)
    win.draw_line(line, "black")
    win.redraw()

    win.wait_for_close()

if __name__ == "__main__":
    main()