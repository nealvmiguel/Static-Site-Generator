import unittest

from src.textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_equal_nodes_are_equal(self):
        actual_node = TextNode("This is a text node", TextType.BOLD)
        expected_node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(actual_node, expected_node)

    def ttest_different_text_not_equal(self):
        actual_node = TextNode("This is a text node", TextType.BOLD)
        expected_node = TextNode("This is a different node", TextType.BOLD)
        self.assertNotEqual(actual_node, expected_node)
        
    def test_url_presence_affects_equality(self):
        actual_node = TextNode("this is a text node", TextType.LINK, "https://www.boot.dev")
        expected_node = TextNode("this is a text node", TextType.LINK)
        self.assertNotEqual(actual_node, expected_node)
        
    def test_different_types_not_equal(self):
        actual_node = TextNode("this is a text node", TextType.BOLD)
        expected_node = TextNode("this is a text node", TextType.LINK)
        self.assertNotEqual(actual_node, expected_node)
    
    def test_identical_nodes_with_urls_are_equal(self):
        actual_node = TextNode("this is a text node", TextType.LINK,  "https://www.boot.dev")
        expected_node = TextNode("this is a text node", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(actual_node, expected_node)
        
    def test_different_urls_not_equal(self):
        actual_node = TextNode("this is a text node", TextType.LINK,  "https://www.boot.dev")
        expected_node = TextNode("this is a text node", TextType.LINK, "https://scrimba.com/home")
        self.assertNotEqual(actual_node,expected_node)
    
    def test_urls_none(self):
        actual_node = TextNode("this is a text node", TextType.LINK, None)
        expected_node = TextNode("this is a text node", TextType.LINK, None)
        self.assertEqual(actual_node, expected_node)
        
    
    def test_text_node_to_html_node_text(self):
        node = TextNode("Hello, world!", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        assert html_node.tag == None
        assert html_node.value == "Hello, world!"
        assert html_node.props == {}
        
    def test_text_node_to_html_node_bold(self):
        node = TextNode("Hello, world!", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        assert html_node.tag == "b"
        assert html_node.value == "Hello, world!"
        assert html_node.props == {}
        
    def test_text_node_to_html_node_italic(self):
        node = TextNode("Hello, world!", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        assert html_node.tag == "i"
        assert html_node.value == "Hello, world!"
        assert html_node.props == {}
        
    def test_text_node_to_html_node_code(self):
        node = TextNode("hello_world", TextType.CODE)
        html_node = text_node_to_html_node(node)
        assert html_node.tag == "code"
        assert html_node.value == "hello_world"
        assert html_node.props == {}
    
    def test_text_node_to_html_node_link(self):
        node = TextNode("click me!", TextType.LINK, "google.com")
        html_node = text_node_to_html_node(node)
        assert html_node.tag == "a"
        assert html_node.value == "click me!"
        assert html_node.props == {"href":"google.com"}
    
    def test_text_node_to_html_node_image(self):     
        node = TextNode("alt text here", TextType.IMAGE, "image_url.png")
        html_node = text_node_to_html_node(node)
        assert html_node.tag == "img"
        assert html_node.value == ""  # images have empty string value
        assert html_node.props == {
            "src": "image_url.png",
            "alt": "alt text here"
        }    
        
        

        
        
if __name__ == "__main__":
    unittest.main() 