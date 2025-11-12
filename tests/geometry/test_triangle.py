'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: paul.dicarlo@gmail.com
'''
# tests/geometry/test_triangle.py

import pytest
from sailocus.geometry.point import Point  # direct import works thanks to python_paths
from sailocus.geometry.triangle import Triangle  # direct import works thanks to python_paths

# -----------------------------
# Fixtures (if needed)
# -----------------------------

# -----------------------------
# Basic construction & repr
# -----------------------------
def test_triangle():
    p1 = Point(0.0, 0.0)
    p2 = Point(20, 20)
    p3 = Point(40, 40)

    tr1 = Triangle(p1, p2, p3)