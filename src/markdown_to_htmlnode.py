from textnode import text_node_to_html_node
from text_to_textnodes import text_to_textnodes


def markdown_to_html_node(markdown):
    pass


def _text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]


def _is_ordered_list(block):
    lines = block.split("\n")
    for i, line in enumerate(lines, start=1):
        if not line.startswith(f"{i}. "):
            return False
    return True
