import unittest
import numpy as np
import pandas as pd
from Project import *
import matplotlib.pyplot as plt

class TestProject(unittest.TestCase):

    def test_q1(self):
        plot_polynomial()

    def test_q2(self):
        plot_compare_functions()

    def test_q3(self):
        plot_array_from_txt("data/array_sample.txt")

    def test_q4(self):
        plot_monthly_temperature("data/temperature.csv")

    def test_q5(self):
        plot_scatter_from_csv("data/scatter.csv")

    def test_q6(self):
        plot_heatmap("data/matrix.txt")

    def test_q7(self):
        self.assertIsNotNone(is_invertible("data/invertible.txt"))

    def test_q8(self):
        A = np.loadtxt("data/orthogonalA.txt")
        B = np.loadtxt("data/orthogonalB.txt")
        are_orthogonal(A, B)

    def test_q9(self):
        plot_surface()

    def test_q10(self):
        animate_sine_wave()

if __name__ == "__main__":
    unittest.main()
