from markdown_to_blocks import markdown_to_blocks
from parentnode import ParentNode
from leafnode import LeafNode
from textnode import text_node_to_html_node
from text_to_textnodes import text_to_textnodes


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    children = []

    for block in blocks:
        block_type = _block_type(block)

        if block_type == "paragraph":
            text = " ".join(block.split())
            children.append(
                ParentNode(
                    "p",
                    _text_to_children(text),
                )
            )

        elif block_type == "heading":
            level = len(block.split(" ")[0])
            text = block[level + 1 :]
            children.append(
                ParentNode(
                    f"h{level}",
                    _text_to_children(text),
                )
            )

        elif block_type == "code":
            code_content = block.strip("`")
            if code_content.startswith("\n"):
                code_content = code_content[1:]

            code_node = LeafNode("code", code_content)
            children.append(ParentNode("pre", [code_node]))

        elif block_type == "quote":
            lines = block.split("\n")
            cleaned = "\n".join(line.lstrip("> ").rstrip() for line in lines)
            children.append(
                ParentNode(
                    "blockquote",
                    _text_to_children(cleaned),
                )
            )

        elif block_type == "unordered_list":
            items = []
            for line in block.split("\n"):
                item_text = line.lstrip("- ").strip()
                items.append(ParentNode("li", _text_to_children(item_text)))
            children.append(ParentNode("ul", items))

    return ParentNode("div", children)


def _text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]


def _block_type(block):
    if block.startswith("#"):
        return "heading"

    if block.startswith("```") and block.endswith("```"):
        return "code"

    if block.startswith(">"):
        return "quote"

    if block.startswith("- "):
        return "unordered_list"

    if _is_ordered_list(block):
        return "ordered_list"

    return "paragraph"


def _is_ordered_list(block):
    lines = block.split("\n")
    for i, line in enumerate(lines, start=1):
        if not line.startswith(f"{i}. "):
            return False
    return True
