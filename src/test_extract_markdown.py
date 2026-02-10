import unittest

from extract_markdown import extract_markdown_images, extract_markdown_links

class TestMarkdownExtract(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual(
            [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")],
            matches
        )

    def test_empty_list_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is just normal text with no image"
        )
        self.assertListEqual([], matches)

    def test_empty_list_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with **bold** words and _italic_ words"
        )
        self.assertListEqual([], matches)       