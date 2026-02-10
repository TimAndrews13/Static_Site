import unittest

from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
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

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )

    def test_multinode_split_links(self):
        node1 = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev)",
            TextType.TEXT,
        )
        node2 = TextNode(
            "This is text with a link [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node1, node2])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )

    def test_multinode_split_images(self):
        node1 = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        node2 = TextNode(
            "This is text with another ![second image](https://i.imgur.com/3elNhQu.png) and some extra text",
            TextType.TEXT,            
        )
        new_nodes = split_nodes_image([node1, node2])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("This is text with another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" and some extra text", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_nolink_split_links(self):
        node = TextNode("This is text without a link", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(new_nodes, [node])

    def test_nolink_split_images(self):
        node = TextNode("This is text without an image", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(new_nodes, [node])

    def test_wrongtype_split_links(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev)", TextType.ITALIC)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(new_nodes, [node])

    def test_wrongtype_split_images(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.BOLD)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(new_nodes, [node])          