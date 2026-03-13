from textnode import TextNode, TextType

from split_nodes_delimeter import split_nodes_delimeter
from split_nodes_images import split_nodes_image
from split_nodes_links import split_nodes_link


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_delimeter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimeter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimeter(nodes, "_", TextType.ITALIC)

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes
