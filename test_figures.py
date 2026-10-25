import unittest

from circle import area as circle_area, perimeter as circle_perimeter

from square import area as square_area, perimeter as square_perimeter

from triangle import area as tri_area, perimeter as tri_perimeter

from rectangle import area as rect_area, perimeter as rect_perimeter

class testGeometricFigures(unittest.TestCase):

    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(5), 78.54, places=2)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(5), 31.42, places=2)


    def test_square_area(self):
        self.assertEqual(square_area(4), 16)

    def test_square_perimeter(self):
        self.assertEqual(square_perimeter(4), 16)


    def test_tri_area(self):
        self.assertEqual(tri_area(3, 4, 5), 6.0)

    def test_tri_perimeter(self):
        self.assertEqual(tri_perimeter(3, 4, 5), 12)


    def test_rect_area(self):
        self.assertEqual(rect_area(10, 5), 50)

    def test_rect_perimeter(self):
        self.assertEqual(rect_perimeter(10, 5), 30)

    def test_rect_zero_size(self):
        self.assertEqual(rect_area(10, 0), 0)
        self.assertEqual(rect_perimeter(10, 0), 20)

if __name__ == '__main__':
    unittest.main()
