# -*- coding: utf-8 -*-
#!/usr/bin/python3

# The maximum possible value for the data set.
MAX_INTEGER_VALUE = 1000

class BasicStats():
    """This class computes basic statistics from a data set of numbers."""

    def __init__(self, data, size):
        """Initializes the BasicStats instance.

        param data A list representing the histogram of the data set.
        param size The total amount of data (not the size of the list but sum of its elements).
        """
        accum = 0
        self._stats = []
        for x in data:
            self._stats.append((x, accum, size - accum - x))
            accum += x

    def less(self, number):
        """Returns the amount of numbers that are less than a particular value.

        param number An integer in the range [0, MAX_INTEGER_VALUE].

        raise ValueError when number is out of range.
        """
        if 0 <= number < MAX_INTEGER_VALUE:
            return self._stats[number][1]
        else:
            raise ValueError(number, 'Parameter value must be in the range [0, {}].'.format(MAX_INTEGER_VALUE))

    def between(self, start_number, end_number):
        """Returns the amount of numbers that are between two particular values.

        param start_number An integer in the range [0, MAX_INTEGER_VALUE].
        param end_number An integer in the range [0, MAX_INTEGER_VALUE].

        raise ValueError when any of the arguments is out of range.
        raise IndexError when start_number > end_number.
        """
        if start_number > end_number:
            raise IndexError((start_number, end_number), 'Invalid range, expression "start_number <= end_number" must be true.')
        elif not (0 <= start_number < MAX_INTEGER_VALUE):
            raise ValueError(start_number, 'Parameter value must be in the range [0, {}].'.format(MAX_INTEGER_VALUE))
        elif not (0 <= end_number < MAX_INTEGER_VALUE):
            raise ValueError(end_number, 'Parameter value must be in the range [0, {}].'.format(MAX_INTEGER_VALUE))
        else:
            return self._stats[start_number][0] + self._stats[start_number][2] - self._stats[end_number][2]

    def greater(self, number):
        """Returns the amount of numbers that are greater than a particular value.

        param number An integer in the range [0, MAX_INTEGER_VALUE].

        raise ValueError when number is out of range.
        """
        if 0 <= number < MAX_INTEGER_VALUE:
            return self._stats[number][2]
        else:
            raise ValueError(number, 'Parameter value must be in the range [0, {}].'.format(MAX_INTEGER_VALUE))

class DataCapture():
    """This class acts as a container of numbers which can be used then for computing basic statistics.
    Values are stored in a histogram format.
    """

    def __init__(self):
        """Initializes DataCapture instance."""

        self._data_container = [0] * MAX_INTEGER_VALUE
        self._total_number_of_values = 0

    def add(self, number):
        """Adds a new value.

        param number An integer in the range [0, MAX_INTEGER_VALUE].

        raise ValueError when number is out if range.
        """
        if 0 <= number < MAX_INTEGER_VALUE:
            self._data_container[number] += 1
            self._total_number_of_values += 1
        else:
            raise ValueError(number, 'Parameter value must be in the range [0, {}].'.format(MAX_INTEGER_VALUE))

    def build_stats(self):
        """Creates and returns a BasicStats instance containing the statistics for the current values."""
        return BasicStats(self._data_container, self._total_number_of_values)
