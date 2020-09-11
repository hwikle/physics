from unittest import TestCase
from physics.physlib import *
import numpy as np

class TestCoreLib(TestCase):

    def test_Point_raises_TypeError_when_passed_nonarray(self):
        with self.assertRaises(TypeError):
            pt = Point(3, (1,2,3))

    def test_Point_raises_ValueError_on_array_with_mismatched_dimension(self):
        with self.assertRaises(ValueError):
            pt = Point(2, np.array([1,2,3]))

if __name__ == '__main__':
    unittest.main()
