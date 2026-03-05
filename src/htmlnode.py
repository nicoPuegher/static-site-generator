class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        res = ""
        if self.props:
            for key, value in self.props.items():
                res += f' {key}="{value}"'
        return res

    def __eq__(self, other):
        equal_tag = self.tag == other.tag
        equal_value = self.value == other.value
        equal_children = self.children == other.children
        equal_props = self.props == other.props
        return equal_tag and equal_value and equal_children and equal_props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
