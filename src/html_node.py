class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
               
        if self.props is None:
            return ""
        
        props_html = ""
        
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)  # correct
    
    def to_html(self):
        if self.value is None:
            raise ValueError("All Leaf Node must have a value")
        
        if self.tag is None:
            return f"{self.value}"

        if self.props:
            props_html = "" 
            
            for key, value in self.props.items():
                props_html += f' {key}="{value}"'
                
            return f'<{self.tag}{props_html}>{self.value}</{self.tag}>'

        return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self,tag,children, props = None):
        super().__init__(tag, None, children, props)  
        self.children = children
        
    def to_html(self):
        if not self.tag:
            raise ValueError("tag is required")
        
        
        if not isinstance(self.children, list) or not self.children:
            raise ValueError("Children is missing")
        
        
        html_children = []
        
        for child in self.children:
            
            html_children.append(child.to_html())
        
        html = "".join(html_children)

        return f"<{self.tag}>{html}</{self.tag}>"
        

                
                

