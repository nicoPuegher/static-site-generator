import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "This is my title", {"class": "title"})
        self.assertEqual(node.to_html(), '<h1 class="title">This is my title</h1>')


if __name__ == "__main__":
    unittest.main()
