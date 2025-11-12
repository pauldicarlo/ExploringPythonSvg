'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: paul.dicarlo@gmail.com
'''
# tests/svg/test_svg.py

import pytest
from sailocus.svg import svg  # direct import works thanks to python_paths

# -----------------------------
# Fixtures (if needed)
# -----------------------------

# -----------------------------
# Basic construction & repr
# -----------------------------
def test_svg():
    svg1 = svg.SVG()
    xsvg = svg.SVG()