import unittest
canUnlockAll = __import__('0-lockboxes').canUnlockAll


class TestLockboxes(unittest.TestCase):
    def test_basic_case(self):
        boxes = [[1], [2], [0], []]
        self.assertNotEqual(canUnlockAll(boxes), True)

    def test_some_boxes_cannot_be_unlocked(self):
        boxes = [[1], [2], [0], []]
        self.assertFalse(canUnlockAll(boxes))

    def test_circular_dependency(self):
        boxes = [[1], [0, 2], [1]]
        self.assertTrue(canUnlockAll(boxes))

    def test_empty_lockboxes(self):
        boxes = [[], [], []]
        self.assertFalse(canUnlockAll(boxes))

    def test_complex_interconnected_lockboxes(self):
        boxes = [[1, 2], [3], [4], [2, 5], [6], [
            7], [8], [9], [7], [10, 11], [12], []]
        self.assertTrue(canUnlockAll(boxes))

    def test_lockboxes_with_no_keys(self):
        boxes = [[], [], [], []]
        self.assertFalse(canUnlockAll(boxes))


if __name__ == "__main__":
    unittest.main()
    all()
