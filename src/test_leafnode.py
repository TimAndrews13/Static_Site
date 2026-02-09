import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p",  "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Philadelphia Eagles", {"href": "https://www.philadelphiaeagles.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.philadelphiaeagles.com">Philadelphia Eagles</a>')

    def test_leaf_to_html_image(self):
        node = LeafNode("img", "Eagles Win Super Bowl LIX!", {"src": "https://media.cnn.com/api/v1/images/stellar/prod/ap25041134230829-20250210040541141.jpg?c=original", "alt": "Eagles hoist Lombardi"})
        self.assertEqual(node.to_html(), '<img src="https://media.cnn.com/api/v1/images/stellar/prod/ap25041134230829-20250210040541141.jpg?c=original" alt="Eagles hoist Lombardi">Eagles Win Super Bowl LIX!</img>')

if __name__ =="__main__":
    unittest.main()