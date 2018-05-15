"""This is a one-line docstring of a module."""


class MyLibrary(object):
    """Demonstrate the result of different test library scope settings."""

    ROBOT_LIBRARY_SCOPE = 'TEST CASE'

    def __init__(self):
        """Constructor of MyLibrary."""
        self.count = 0

    def get_count_value(self):
        """Accumulate count."""
        self.count = self.count + 1
        return self.count
