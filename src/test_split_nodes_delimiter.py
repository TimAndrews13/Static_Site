import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TextSplitNodesDelimiter(unittest.TestCase):
    def test_code_blocks(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),
                                    TextNode("code block", TextType.CODE),
                                    TextNode(" word", TextType.TEXT)
                                    ])

    def test_bold_blocks(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),
                                    TextNode("bold", TextType.BOLD),
                                    TextNode(" word", TextType.TEXT)
                                    ])

    def test_italic_blocks(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [TextNode("This is text with an ", TextType.TEXT),
                                    TextNode("italic", TextType.ITALIC),
                                    TextNode(" word", TextType.TEXT)
                                    ])

    def test_excpiton(self):
        node = TextNode("This is text with an _italic word", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, [node], "_", TextType.ITALIC)

    def test_multiple_nodes(self):
        node1 = TextNode("This is text with a **bold** word", TextType.TEXT)
        node2 = TextNode("Here is a **test** for **bold** words", TextType.TEXT)
        node3 = TextNode("I am learning a lot from **Boot Dev**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2, node3], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),
                                    TextNode("bold", TextType.BOLD),
                                    TextNode(" word", TextType.TEXT),
                                    TextNode("Here is a ", TextType.TEXT),
                                    TextNode("test", TextType.BOLD),
                                    TextNode(" for ", TextType.TEXT),
                                    TextNode("bold", TextType.BOLD),
                                    TextNode(" words", TextType.TEXT),
                                    TextNode("I am learning a lot from ", TextType.TEXT),
                                    TextNode("Boot Dev", TextType.BOLD)
                                    ])