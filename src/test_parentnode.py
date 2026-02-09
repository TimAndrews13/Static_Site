import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span",  "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )

    def test_to_html_with_grandchildren_props(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node], props={"class": "highlight", "style": "color: red"})
        parent_node = ParentNode("div", [child_node], props={"style": "margin-top: 10px"})
        self.assertEqual(
            parent_node.to_html(),
            '<div style="margin-top: 10px"><span class="highlight" style="color: red"><b>grandchild</b></span></div>'
        )


if __name__ =="__main__":
    unittest.main()