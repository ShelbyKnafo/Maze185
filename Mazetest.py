import unittest
from Maze import *


class testMaze (unittest .TestCase) :
    def setUp (self) :
        # this checks for a Maze Class
        self.m=Maze()

    def testMazeExists(self):
        pass


    def testScreenExists(self) :
        assert type(self.m) == Maze

unittest.main (exit=False)


