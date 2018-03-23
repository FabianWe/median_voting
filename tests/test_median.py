# -*- coding: utf-8 -*-

# MIT License
#
# Copyright (c) 2018 Fabian Wenzelmann
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from median_voting import *
import pytest
import sys


def test_median_one():
    v1 = MedianVote(200, 4)
    v2 = MedianVote(1000, 3)
    v3 = MedianVote(700, 2)
    v4 = MedianVote(500, 2)

    stat = MedianStatistics([v1, v2, v3, v4])
    assert stat.median() == 500


def test_median_two():
    v1 = MedianVote(0, 1)
    v2 = MedianVote(150, 2)
    v3 = MedianVote(200, 3)

    stat = MedianStatistics([v1, v2, v3])
    assert stat.median() == 150


if __name__ == '__main__':
    pytest.main(sys.argv)
