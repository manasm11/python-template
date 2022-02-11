import unittest


class TestMain(unittest.TestCase):
    def test_main_exists(self):
        from index import main

        assert main
