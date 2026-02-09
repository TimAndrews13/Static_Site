from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    #Leaf Node class constructor
    def __init__(self, tag=None, value="", props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)


    def to_html(self):
        if self.value is None:
            raise ValueError("All Leaf Nodes must have a value")
        if self.tag is None:
            return self.value
        if self.props is None:
            html_text = f"<{self.tag}>{self.value}</{self.tag}>"
            return html_text
        props_html = self.props_to_html()
        html_text = f'<{self.tag} {props_html}>{self.value}</{self.tag}>'
        return html_text

    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, props: {self.props}"
