import unittest

from textnode import TextType, TextNode
from split_nodes_images import split_nodes_image


class TestSplitNodesImages(unittest.TestCase):
    def test_split_single_image(self):
        node = TextNode(
            "Look ![alt](img.png)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_image([node])

        self.assertEqual(
            [
                TextNode("Look ", TextType.TEXT),
                TextNode("alt", TextType.IMAGE, "img.png"),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
