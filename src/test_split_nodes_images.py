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

    def test_split_multiple_images(self):
        node = TextNode(
            "Images ![one](1.png) and ![two](2.png)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_image([node])

        self.assertEqual(
            [
                TextNode("Images ", TextType.TEXT),
                TextNode("one", TextType.IMAGE, "1.png"),
                TextNode(" and ", TextType.TEXT),
                TextNode("two", TextType.IMAGE, "2.png"),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
