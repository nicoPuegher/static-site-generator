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

    def test_value_eq(self):
        node = HTMLNode("h1", "Hello, World!", [], {"class": "title"})
        node2 = HTMLNode("h1", "Goodbye, World!", [], {"class": "title"})
        self.assertNotEqual(node, node2)

    def test_children_eq(self):
        child = HTMLNode("p", "My paragraph")
        child2 = HTMLNode("span", "My span")
        node = HTMLNode("h1", "Hello, World!", [child, child2], {"class": "title"})
        node2 = HTMLNode("h1", "Hello, World!", [child], {"class": "title"})
        self.assertNotEqual(node, node2)

    def test_props_eq(self):
        node = HTMLNode("h1", "Hello, World!", [], {"class": "title"})
        node2 = HTMLNode("h1", "Hello, World!", [], {"class": "paragraph"})
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
