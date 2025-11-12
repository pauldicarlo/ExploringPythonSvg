'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: paul.dicarlo@gmail.com
'''
# tests/geometry/test_linesegment.py

import pytest
from sailocus.geometry.point import Point  # direct import works thanks to python_paths
from sailocus.geometry.linesegment import LineSegment  # direct import works thanks to python_paths

# -----------------------------
# Fixtures (if needed)
# -----------------------------

# -----------------------------
# Basic construction & repr
# -----------------------------
def test_line_creation():
    # Simple case where slope would be 1.0
    p1 = Point(1.0, 1.0)
    p2= Point(7.5, 7.5)
    linesegment1 = LineSegment(p1, p2)
    assert linesegment1.point_a.x == 1.0
    assert linesegment1.point_a.y == 1.0
    assert linesegment1.point_b.x == 7.5
    assert linesegment1.point_b.y == 7.5



