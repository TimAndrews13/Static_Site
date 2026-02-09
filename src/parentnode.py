from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None or self.tag == "":
            raise ValueError("ParentNode must have a tag")
        if self.children is None or len(self.children) == 0:
            raise ValueError("ParentNode must have a children list of HTMLNodes")

        #start html_text for both cases of props and no props
        if self.props is not None:
            props_text = self.props_to_html()
            html_text = f"<{self.tag} {props_text}>"
        else:
            html_text = f"<{self.tag}>"
        
        #Recursively Call to_html() method on childrn
        for child in self.children:
            html_text += child.to_html()
        
        #Append Parent Tag at the end
        html_text += f"</{self.tag}>"
        return html_text

    def __repr__(self):
        return f"tag: {self.tag}, children: {self.children}, props: {self.props}"
