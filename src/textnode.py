from src.html_node import LeafNode


from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
            

def text_node_to_html_node(text_node):
    if not isinstance(text_node.text_type, TextType):
        raise ValueError(f"Unrecognized text type: {text_node.text_type}")
    
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text, {})
        
        case TextType.BOLD:
            return LeafNode("b", text_node.text, {})
        
        case TextType.ITALIC:
            return LeafNode('i', text_node.text, {})
        
        case TextType.LINK:
            props = {"href": text_node.url}
            return LeafNode('a', text_node.text, props)
            
        case TextType.CODE:
            return LeafNode('code', text_node.text, {})    
            
        case TextType.IMAGE:
            
            props = {"src": text_node.url,
                    "alt": text_node.text,
                    
                    }
            return LeafNode('img', "", props)
        
        case _:
            raise ValueError(f"Unhandled TextType: {text_node.text_type}")

        
        



