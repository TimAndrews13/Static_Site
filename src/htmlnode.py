

class HTMLNode():
    def __init__(self, tag: str | None = None, value: str | None = None, children: list | None = None, props: dict | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Child classes will override this method to render themselves as HTML")

    def props_to_html(self):
        html_string = ""
        if self.props is None or len(self.props) == 0:
            return html_string
        for key, prop in self.props.items():
            html_string += f'{key}="{prop}" '
        html_string = html_string.strip()
        return html_string

    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"
