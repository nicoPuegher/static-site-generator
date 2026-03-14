import unittest

from markdown_to_htmlnode import markdown_to_html_node


class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = (
            "This is **bolded** paragraph\n"
            "text in a p\n"
            "tag here\n\n"
            "This is another paragraph with _italic_ text and `code` here\n"
        )

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p>"
            "<p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = (
            "```\n"
            "This is text that _should_ remain\n"
            "the **same** even with inline stuff\n"
            "```"
        )

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\n"
            "the **same** even with inline stuff\n"
            "</code></pre></div>",
        )

    def test_headings(self):
        md = "# Heading 1\n\n## Heading 2\n\n### Heading 3"

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div>"
            "<h1>Heading 1</h1>"
            "<h2>Heading 2</h2>"
            "<h3>Heading 3</h3>"
            "</div>",
        )

    def test_blockquote(self):
        md = "> This is a quote with **bold** text"

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div>"
            "<blockquote>This is a quote with <b>bold</b> text</blockquote>"
            "</div>",
        )

    def test_unordered_list(self):
        md = (
            "- Item one with **bold**\n"
            "- Item two with _italic_\n"
            "- Item three with `code`"
        )

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div>"
            "<ul>"
            "<li>Item one with <b>bold</b></li>"
            "<li>Item two with <i>italic</i></li>"
            "<li>Item three with <code>code</code></li>"
            "</ul>"
            "</div>",
        )

    def test_ordered_list(self):
        md = (
            "1. First item\n"
            "2. Second item with **bold**\n"
            "3. Third item with _italic_"
        )

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div>"
            "<ol>"
            "<li>First item</li>"
            "<li>Second item with <b>bold</b></li>"
            "<li>Third item with <i>italic</i></li>"
            "</ol>"
            "</div>",
        )

    def test_full_document(self):
        md = (
            "# Title\n\n"
            "This is a paragraph with **bold** text.\n\n"
            "- Item 1\n"
            "- Item 2\n\n"
            "> A quote here"
        )

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div>"
            "<h1>Title</h1>"
            "<p>This is a paragraph with <b>bold</b> text.</p>"
            "<ul>"
            "<li>Item 1</li>"
            "<li>Item 2</li>"
            "</ul>"
            "<blockquote>A quote here</blockquote>"
            "</div>",
        )


if __name__ == "__main__":
    unittest.main()
