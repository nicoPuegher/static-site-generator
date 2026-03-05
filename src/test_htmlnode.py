import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("h1", "Hello, World!", [], {"class": "title"})
        node2 = HTMLNode("h1", "Hello, World!", [], {"class": "title"})
        self.assertEqual(node, node2)

    def test_tag_eq(self):
        node = HTMLNode("h1", "Hello, World!", [], {"class": "title"})
        node2 = HTMLNode("h2", "Hello, World!", [], {"class": "title"})
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
