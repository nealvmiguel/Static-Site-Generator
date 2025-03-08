import unittest
from src.html_node import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )


    def test_leaf_node(self):
        # Test 1: Basic tag rendering
        node = LeafNode("p", "Hello")
        assert node.to_html() == "<p>Hello</p>"

        # Test 2: Node with no tag
        text_node = LeafNode(None, "Just text")
        assert text_node.to_html() == "Just text"

        # Test 3: Node with properties
        link = LeafNode("a", "Click me!", {"href": "https://boot.dev"})
        assert link.to_html() == '<a href="https://boot.dev">Click me!</a>'


class TestParentNode(unittest.TestCase):
    def test_parentnode_single_leafnode(self):
        parent_none = ParentNode("div", [
            LeafNode("span", "Hello")
            ])
        
        expected_parent = "<div><span>Hello</span></div>"
        
        self.assertEqual(parent_none.to_html(), expected_parent)
        
    def test_parentnode_mutiple_leafnode(self):
        parent_none = ParentNode("div", [
            LeafNode("h2", "Heading2"),
            LeafNode("h3", "Heading3"),
            LeafNode("p", "Hello")
        ])
        
        expected_parent = "<div><h2>Heading2</h2><h3>Heading3</h3><p>Hello</p></div>"
        
        self.assertEqual(parent_none.to_html(), expected_parent)
        
    def test_parentnode_no_tag(self):
        with self.assertRaises(ValueError):
            parent_node = ParentNode(None, [LeafNode("b", "text")])
            parent_node.to_html()

    def test_parentnode_empty_children(self):
        with self.assertRaises(ValueError):
            parent_node = ParentNode("div", [])
            parent_node.to_html()
        
    def test_parentnode_none_children(self):
        with self.assertRaises(ValueError):
            parent_node = ParentNode("div", None)
            parent_node.to_html()
        
    
    def test_parentnode_nested_children(self):
        
        parent_node = ParentNode("div", [
            LeafNode("h2", "Heading2"),
            LeafNode("h3", "Heading3"),
            ParentNode("p", [LeafNode("b", "text")])
        ])
        
        expected_node = "<div><h2>Heading2</h2><h3>Heading3</h3><p><b>text</b></p></div>"
        
        self.assertEqual(parent_node.to_html(), expected_node)
    
    

    
    
        
if __name__ == "__main__":
    unittest.main()







# class TestHTMLNode(unittest.TestCase):
#     def test_htmlnode_no_tag(self):
#         node = HTMLNode(None, "this is a value", None, None)
#         self.assertIsNone(node.tag)
#         self.assertEqual(node.value, "this is a value")
        
#     def test_htmlnode_tag_with_value(self):
#         actual_node = HTMLNode("p", "this is a value", None, None)
#         expected_node = HTMLNode("p", "this is a value", None, None)
#         self.assertEqual(actual_node, expected_node)
        
        

#     def test_htmlnode_tag_with_children(self):
#         # Create child nodes with different structures
#         child1 = HTMLNode("p", "First paragraph", None, {"class": "intro"})
#         child2 = HTMLNode("p", "Second paragraph", None, None)
#         child3 = HTMLNode(None, "Just text", None, None)
        
#         # Create a parent div with these children
#         parent_node = HTMLNode(
#             tag="div",
#             value=None,
#             children=[child1, child2, child3],
#             props={"class": "container"}
#         )
        
#         # Test parent node structure
#         self.assertEqual(parent_node.tag, "div")
#         self.assertIsNone(parent_node.value)
#         self.assertEqual(len(parent_node.children), 3)
        
#         # Test first child (p with props)
#         self.assertEqual(parent_node.children[0].tag, "p")
#         self.assertEqual(parent_node.children[0].value, "First paragraph")
#         self.assertEqual(parent_node.children[0].props, {"class": "intro"})
        
#         # Test second child (p without props)
#         self.assertEqual(parent_node.children[1].tag, "p")
#         self.assertEqual(parent_node.children[1].value, "Second paragraph")
#         self.assertIsNone(parent_node.children[1].props)
        
#         # Test third child (text node)
#         self.assertIsNone(parent_node.children[2].tag)
#         self.assertEqual(parent_node.children[2].value, "Just text")
        
#     def test_props_to_html_none(self):
#         actual_node = HTMLNode(None, None, None, None)
#         self.assertEqual(actual_node.props_to_html(), "")

#     def test_props_to_html_one_prop(self):
#         # test with one property
#         actual_node = HTMLNode(None, None, None, {"href": "https://www.google.com"})
#         self.assertEqual(actual_node.props_to_html(), ' href="https://www.google.com"')
        
#     def test_props_to_html_multiple_props(self):
#         props = {
#             "href": "https://www.boot.dev/tracks/backend",
#             "target": "_blank"
#         }
#         actual_node = HTMLNode(None, None, None, props)
        
#         self.assertEqual(actual_node.props_to_html(), ' href="https://www.boot.dev/tracks/backend" target="_blank"')
    
        
# def __repr__(self):
    
#     return f"HTMLNode(tag={self.tag!r}, value={self.value!r}, children={self.children!r}, props={self.props!r})"

