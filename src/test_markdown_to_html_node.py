import unittest

from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quote_block(self):
        md = """
> This is a quote block
> May Thy Knife Chip and Shatter
> My Arrakis, My Dune
> Quotes from Dune
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote block May Thy Knife Chip and Shatter My Arrakis, My Dune Quotes from Dune</blockquote></div>"
        )

    def test_heading1_block(self):
        md = """# This is Heading 1

## This is Heading 2

### This is Heading 3

#### This is Heading 4

##### This is Heading 5

###### This is Heading 6

####### This is also Heading 6
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is Heading 1</h1><h2>This is Heading 2</h2><h3>This is Heading 3</h3><h4>This is Heading 4</h4><h5>This is Heading 5</h5><h6>This is Heading 6</h6><p>####### This is also Heading 6</p></div>"
        )

    def test_unordered_list_block(self):
        md = """
- List Item 1
- List Item 2
- List Item 3
- List Item 4
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>List Item 1</li><li>List Item 2</li><li>List Item 3</li><li>List Item 4</li></ul></div>"
        )

    def test_ordered_list_block(self):
        md = """
1. List Item 1
2. List Item 2
3. List Item 3
4. List Item 4
5. List Item 5
6. List Item 6
7. List Item 7
8. List Item 8
9. List Item 9
10. List Item 10
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>List Item 1</li><li>List Item 2</li><li>List Item 3</li><li>List Item 4</li><li>List Item 5</li><li>List Item 6</li><li>List Item 7</li><li>List Item 8</li><li>List Item 9</li><li>List Item 10</li></ol></div>"
        )

    def test_multiple_blocks(self):
        md = """
# Heading

This is a paragraph.

* Item 1
* Item 2
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading</h1><p>This is a paragraph.</p><ul><li>Item 1</li><li>Item 2</li></ul></div>"
        )
