import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_prop_to_html(self):
        node = HTMLNode(tag="a", value="An image for display", props={"href": "https://www.google.com", "target": "_blank"})
        result = node.props_to_html()
        self.assertEqual(result, 'href="https://www.google.com" target="_blank"')

    def test_prop_to_html_2(self):
        node = HTMLNode(tag="p", value="test paragraph", props={"p": "Here is a unit test for props", "href": "https://boots.dev", "target": "_learning"})
        result = node.props_to_html()
        self.assertEqual(result, 'p="Here is a unit test for props" href="https://boots.dev" target="_learning"')

    #def bold_prop_to_html(self):
    #    node = HTMLNode(tag="b", value="these words eventually will be bold", props={"p": "this text will eventually be bold", "b": "eventually", "i": "will be bold"})
    #    result = node.props_to_html()
    #    self.assertEqual(result, 'p="this text will eventually be bold" b="eventually", i="will be bold"')


if __name__ =="__main__":
    unittest.main()