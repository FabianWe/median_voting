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

import operator


class MedianVote(object):
    """Class for a vote in a median voting

    It contains the weight of a voter (default 1) and the value voted for by
    the voter. A vote should have a value >= 0.

    Attributes:
        value (int, float): Value the voter weighted for. value should be >= 0.
        weight (int): Weight of the voter (how many votes a single voter has).
    """

    def __init__(self, value, weight=1):
        self.value = value
        self.weight = weight


class MedianStatistics(object):
    """ A class for retrieving results from a median vote.

    The list of votes must be sorted for these functions to operate correctly.

    Args:
        votes (list of MedianVote): All votes you want results for.
        sorted (bool): Set to true if the list is already sorted according
            to weight in decreasing order. Otherwise the votes get sorted.

    Attributes:
        sorted_votes (list of MedianVote): The list of sorted votes.
    """

    ops = {
        'lt': operator.lt,
        'le': operator.le,
        'gt': operator.gt,
        'ge': operator.ge
    }

    def __init__(self, votes, sorted=False):
        if sorted:
            self.sorted_votes = votes
        else:
            self.sorted_votes = votes
            self.sorted_votes = self.sort_votes()

    @staticmethod
    def sort_votes(votes):
        """ Sorts the votes in decreasing order and returns the result.

        Usually you don't have to sort the elements by yourself, the __init__
        method will take care of this.

        Args:
            votes (list of MedianVote): The votes to sort.

        Returns:
            list of MedianVote: The sorted votes.
        """
        return sorted(votes, key=lambda vote: vote.value, reverse=True)

    def weight_sum(self):
        """ Returns the sum of all weights in the votes list.

        Returns:
            int: The sum of the weights.
        """
        return sum(vote.weight for vote in self.sorted_votes)

    def median(self, votes_required=None):
        """ Computes the median, i.e. the greatest value with a majority.

        You can either specify the number of notes required or let it be the
        half of the weight sum.

        Note:
            For a majority to be reached strictly more votes than
            votes_required are needed. For example: eight voters each with one
            vote, this means we must have more than 4 votes. For 15 votes we
            get that more than seven votes are required, i.e. at least 8.
            That is also the behaviour if you don't specify votes_required.

        Args:
            votes_required (int): The number of votes TODO
        """
        if votes_required is None:
            votes_required = self.weight_sum() // 2
        weight = 0
        for vote in self.sorted_votes:
            weight += vote.weight
            if weight > votes_required:
                return vote.value
        return None
