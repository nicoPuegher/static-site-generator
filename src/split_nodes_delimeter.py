from textnode import TextType


def split_nodes_delimeter(old_nodes, delimeter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimeter)

        if len(parts) % 2 == 0:
            raise Exception("Invalid markdown: missing closing delimeter")

    return new_nodes
