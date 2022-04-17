import unittest
import sys
from src import web_reader

class TestWebReader(unittest.TestCase):
    def test_create(url: str):
        new_web_reader=web_reader.CourseWebReader(url)
        new_web_reader.print_classnames()

if __name__ == '__main__':
    unittest.main(sys.argv[1])
