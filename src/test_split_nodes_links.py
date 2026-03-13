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

    def test_split_multiple_links(self):
        node = TextNode(
            "Go to [Google](https://google.com) and [YouTube](https://youtube.com)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        self.assertEqual(
            [
                TextNode("Go to ", TextType.TEXT),
                TextNode("Google", TextType.LINK, "https://google.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("YouTube", TextType.LINK, "https://youtube.com"),
            ],
            new_nodes,
        )

    def test_split_link_at_start(self):
        node = TextNode(
            "[Boot](https://boot.dev) is great",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        self.assertEqual(
            [
                TextNode("Boot", TextType.LINK, "https://boot.dev"),
                TextNode(" is great", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_link_at_end(self):
        node = TextNode(
            "Visit [Boot](https://boot.dev)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        self.assertEqual(
            [
                TextNode("Visit ", TextType.TEXT),
                TextNode("Boot", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes,
        )

    def test_split_no_links(self):
        node = TextNode(
            "Just plain text",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        self.assertEqual([node], new_nodes)

    def test_split_link_non_text_node(self):
        node = TextNode(
            "already a link",
            TextType.LINK,
            "https://example.com",
        )

        new_nodes = split_nodes_link([node])

        self.assertEqual([node], new_nodes)

    def test_split_links_with_text_between(self):
        node = TextNode(
            "Start [A](url1) middle [B](url2) end",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        self.assertEqual(
            [
                TextNode("Start ", TextType.TEXT),
                TextNode("A", TextType.LINK, "url1"),
                TextNode(" middle ", TextType.TEXT),
                TextNode("B", TextType.LINK, "url2"),
                TextNode(" end", TextType.TEXT),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
