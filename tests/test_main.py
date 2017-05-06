import unittest
from unittest import mock
import os


class DuplicateFinder(object):

    def __init__(self, iterator_factory, duplicate_detector):
        self._iterator_factory = iterator_factory
        self._duplicate_detector = duplicate_detector

    def find(self, path):
        iterator = self._iterator_factory(path)
        for file in iterator:
            self._duplicate_detector.is_duplicate(file)
        return self._duplicate_detector.duplicates()


class TestMain(unittest.TestCase):

    def setUp(self):
        iterator_factory = mock.Mock(return_value=[])
        duplicate_detector = mock.Mock()
        duplicate_detector.duplicates = mock.Mock(return_value={'0f79610bebc81f7bfd6212cd656fb467': 2})
        self.duplicate_finder = DuplicateFinder(iterator_factory, duplicate_detector)

    def test_should_find_two_duplicates(self):
        some_path = '/home/pablo/Code/untitled/data'
        actual = self.duplicate_finder.find(some_path)

        expected = {'0f79610bebc81f7bfd6212cd656fb467': 2}

        self.assertDictEqual(actual, expected)


class FolderWithOneFileTests(unittest.TestCase):

    def setUp(self):
        iterator_factory = mock.Mock(return_value=[])
        duplicate_detector = mock.Mock()
        duplicate_detector.duplicates = mock.Mock(return_value={})
        self.duplicate_finder = DuplicateFinder(iterator_factory, duplicate_detector)

    def test_should_not_find_duplicates(self):
        some_path = '/home/pablo/Code/untitled/data/a'
        actual = self.duplicate_finder.find(some_path)

        expected = {}

        self.assertDictEqual(actual, expected)


class FolderWithUniqueFilesTests(unittest.TestCase):

    def setUp(self):
        iterator_factory = mock.Mock(return_value=[])
        duplicate_detector = mock.Mock()
        duplicate_detector.duplicates = mock.Mock(return_value={})
        self.duplicate_finder = DuplicateFinder(iterator_factory, duplicate_detector)

    def test_should_not_find_duplicates(self):
        some_path = '/home/pablo/Code/untitled/data/c'
        actual = self.duplicate_finder.find(some_path)

        expected = {}

        self.assertDictEqual(actual, expected)
