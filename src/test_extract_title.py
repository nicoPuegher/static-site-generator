import unittest
from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = "# Hello"
        self.assertEqual(extract_title(md), "Hello")

    def test_extract_title_with_spaces(self):
        md = "#    Hello World   "
        self.assertEqual(extract_title(md), "Hello World")

    def test_no_title(self):
        md = "## Subtitle only"
        with self.assertRaises(Exception):
            extract_title(md)


if __name__ == "__main__":
    unittest.main()
