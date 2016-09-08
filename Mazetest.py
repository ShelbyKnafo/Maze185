import unittest
from Maze import *


class testMaze (unittest .TestCase) :
    def setUp (self) :
        # this checks for a Maze Class
        self.m=Maze()

    def testScreenExists(self) :
        assert type(self.m) == Maze

if __name__=="__main__":
    unittest.main (exit=False)
