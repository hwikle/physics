from unittest import TestCase
from physics.core import *
import numpy as np

class TestCoreLib(TestCase):

    def test_Particle_raises_TypeError_when_passed_nonarray(self):
        with self.assertRaises(TypeError):
            pt = Particle(3, (1,2,3))

    def test_Particle_raises_ValueError_on_array_with_mismatched_dimension(self):
        with self.assertRaises(ValueError):
            pt = Particle(2, np.array([1,2,3]))

if __name__ == '__main__':
    unittest.main()
