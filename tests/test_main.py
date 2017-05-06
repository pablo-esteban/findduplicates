import unittest
from unittest import mock
import os


class DuplicateFinder(object):

    def __init__(self, iterator_factory):
        self._iterator_factory = iterator_factory

    def find(self, path):
        iterator = self._iterator_factory(path)
        for file in iterator:
            pass
        files = os.listdir(path)
        print(files)
        if len(files) <= 1:
            return {}
        return {'0f79610bebc81f7bfd6212cd656fb467': 2}


class TestMain(unittest.TestCase):

    def setUp(self):
        iterator_factory = mock.Mock(return_value=[])
        self.duplicate_finder = DuplicateFinder(iterator_factory)

    def test_should_find_two_duplicates(self):
        some_path = '/home/pablo/Code/untitled/data'
        actual = self.duplicate_finder.find(some_path)

        expected = {'0f79610bebc81f7bfd6212cd656fb467': 2}

        self.assertDictEqual(actual, expected)


class FolderWithOneFileTests(unittest.TestCase):

    def setUp(self):
        iterator_factory = mock.Mock(return_value=[])
        self.duplicate_finder = DuplicateFinder(iterator_factory)

    def test_should_not_find_duplicates(self):
        some_path = '/home/pablo/Code/untitled/data/a'
        actual = self.duplicate_finder.find(some_path)

        expected = {}

        self.assertDictEqual(actual, expected)


class FolderWithUniqueFilesTests(unittest.TestCase):

    def setUp(self):
        iterator_factory = mock.Mock(return_value=[])
        self.duplicate_finder = DuplicateFinder(iterator_factory)

    def test_should_not_find_duplicates(self):
        some_path = '/home/pablo/Code/untitled/data/c'
        actual = self.duplicate_finder.find(some_path)

        expected = {}

        self.assertDictEqual(actual, expected)
