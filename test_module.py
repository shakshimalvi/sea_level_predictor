import unittest
from sea_level_predictor import draw_plot


class SeaLevelPredictorTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ax = draw_plot()

    def test_plot_title(self):
        self.assertEqual(self.ax.get_title(), "Rise in Sea Level")

    def test_plot_labels(self):
        self.assertEqual(self.ax.get_xlabel(), "Year")
        self.assertEqual(self.ax.get_ylabel(), "Sea Level (inches)")

    def test_number_of_lines(self):
        self.assertEqual(len(self.ax.lines), 2)

    def test_number_of_scatter_points(self):
        self.assertEqual(len(self.ax.collections), 1)

    def test_first_line_extends_to_2050(self):
        x_data = self.ax.lines[0].get_xdata()
        self.assertEqual(x_data[-1], 2050)

    def test_second_line_starts_at_2000(self):
        x_data = self.ax.lines[1].get_xdata()
        self.assertEqual(x_data[0], 2000)

    def test_second_line_extends_to_2050(self):
        x_data = self.ax.lines[1].get_xdata()
        self.assertEqual(x_data[-1], 2050)


if __name__ == "__main__":
    unittest.main()