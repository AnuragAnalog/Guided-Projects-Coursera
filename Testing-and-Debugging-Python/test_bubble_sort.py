
import random
import unittest
import bubblesort as bt

class Test_TestValue(unittest.TestCase):
    def test_sample(self):
        testList = [4, 3, 2, 1]
        expectedList = testList.copy()
        expectedList.sort()
        actualList = bt.bubbleSort(testList)

        self.assertEqual(actualList, expectedList)

    def test_empty(self):
        testList = []
        expectedList = testList.copy()
        expectedList.sort()
        actualList = bt.bubbleSort(testList)

        self.assertEqual(actualList, expectedList)

    def test_presorted(self):
        testList = [1, 2, 3, 4]
        expectedList = testList.copy()
        expectedList.sort()
        actualList = bt.bubbleSort(testList)

        self.assertEqual(actualList, expectedList)

    def test_negatives(self):
        testList = [-4, -3, -2, -1]
        expectedList = testList.copy()
        expectedList.sort()
        actualList = bt.bubbleSort(testList)

        self.assertEqual(actualList, expectedList)

    def test_random(self):
        testList = [random.randint(0, 20) for i in range(4)]
        expectedList = testList.copy()
        expectedList.sort()
        actualList = bt.bubbleSort(testList)

        self.assertEqual(actualList, expectedList)