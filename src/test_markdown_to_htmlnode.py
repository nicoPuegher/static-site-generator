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


if __name__ == "__main__":
    unittest.main()
