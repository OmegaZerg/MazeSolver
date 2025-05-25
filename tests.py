import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
    def test_maze_new_position(self):
        num_cols = 3
        num_rows = 8
        m1 = Maze(10, 10, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
    def test_maze_break_enter_exit(self):
        num_cols = 7
        num_rows = 7
        m1 = Maze(5, 5, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._Maze__cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._Maze__cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )
    def test_reset_cells_visited(self):
        num_cols = 7
        num_rows = 7
        m1 = Maze(5, 5, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._Maze__cells[0][0].visited,
            False,
        )

if __name__ == "__main__":
    unittest.main()