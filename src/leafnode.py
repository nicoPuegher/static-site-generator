from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNodes must have a value.")

        if self.tag is None:
            return self.value

        combined_props = ""
        if self.props is not None:
            for k, v in self.props.items():
                combined_props += f' {k}="{v}"'

        return f"<{self.tag}{combined_props}>{self.value}</{self.tag}>"
