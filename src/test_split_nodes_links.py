import unittest

from textnode import TextType, TextNode
from split_nodes_links import split_nodes_link


class TestSplitNodesLinks(unittest.TestCase):
    def test_split_single_link(self):
        node = TextNode(
            "Click [here](https://example.com)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        self.assertEqual(
            [
                TextNode("Click ", TextType.TEXT),
                TextNode("here", TextType.LINK, "https://example.com"),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
