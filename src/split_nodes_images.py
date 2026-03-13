from textnode import TextType, TextNode
from extract_markdown import extract_markdown_images


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)

        if not images:
            new_nodes.append(node)
            continue

        for alt_text, url in images:
            markdown = f"![{alt_text}]({url})"
            parts = text.split(markdown, 1)

            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))

            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))

            text = parts[1]

        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes
