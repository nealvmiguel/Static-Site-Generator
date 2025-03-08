import unittest
from src.inline_markdown import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    extract_markdown_links,
    extract_markdown_images,
    text_to_textnodes
)

from src.textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )
        
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
        
    def test_extract_markdown_links(self):
        
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )  
        self.assertListEqual(
            [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches
        )

class TestSplitNodesImgLink(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_node = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_node
        )
        
    def test_split_image_no_image(self):
        node = TextNode("This is a text with no image", TextType.TEXT)
        
        new_node = split_nodes_image([node])
        
        self.assertListEqual([node], new_node)
        
    def test_split_image_beginning(self):
        node = TextNode("![image](https://pin.it/1FI9hchyU) followed by a text", TextType.TEXT)
        
        new_node = split_nodes_image([node])
        
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://pin.it/1FI9hchyU"),
                TextNode(" followed by a text", TextType.TEXT)
            ],
            new_node
        )
    
    def test_split_image_end(self):
        node = TextNode("this is a text and a ![image](https://pin.it/1yipK6pdr)", TextType.TEXT)
        
        new_node = split_nodes_image([node])
        
        self.assertListEqual([
                TextNode("this is a text and a ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://pin.it/1yipK6pdr")
            ], 
            new_node
        )
    
    def test_split_links(self):
        node = TextNode(
            "Check out this [backend site](https://www.boot.dev/tracks/backend) and this [frontend site](https://scrimba.com/home) too!",
            TextType.TEXT
        )

        new_node = split_nodes_link([node])
        
        self.assertListEqual(
            [
                TextNode("Check out this ", TextType.TEXT),
                TextNode("backend site", TextType.LINK, "https://www.boot.dev/tracks/backend"),
                TextNode(" and this ", TextType.TEXT),
                TextNode("frontend site", TextType.LINK, "https://scrimba.com/home"),
                TextNode(" too!", TextType.TEXT)
            ],
            new_node
        )
        
    def test_split_links_no_link(self):
        node = TextNode("This is a text", TextType)
        new_node = split_nodes_link([node])
        
        self.assertListEqual([node], new_node)

    def test_split_links_beginning(self):
        node = TextNode("[backend site](https://www.boot.dev/tracks/backend) check this out and this [frontend site](https://scrimba.com/home) too!", TextType.TEXT)
        
        new_node = split_nodes_link([node])
        
        self.assertListEqual([
                TextNode("backend site", TextType.LINK, "https://www.boot.dev/tracks/backend"),
                TextNode(" check this out and this ", TextType.TEXT),
                TextNode("frontend site", TextType.LINK, "https://scrimba.com/home"),
                TextNode(" too!", TextType.TEXT)
            ], 
            new_node
        )
        
    def test_split_links_end(self):
        node = TextNode("Check this out [backend site](https://www.boot.dev/tracks/backend) and this [frontend site](https://scrimba.com/home)", TextType.TEXT)
        
        new_node = split_nodes_link([node])
        
        self.assertListEqual(
            [
                TextNode("Check this out ", TextType.TEXT),
                TextNode("backend site", TextType.LINK, "https://www.boot.dev/tracks/backend"),
                TextNode(" and this ", TextType.TEXT),
                TextNode("frontend site", TextType.LINK, "https://scrimba.com/home"),
            ],
            new_node
        )


class TestTextToTextNodes(unittest.TestCase):
    
    
    def test_plain_text(self):
        # Test with plain text, no markdown
        text = "Just plain text"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "Just plain text")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
    
    def test_bold_text(self):
        # Test with bold markdown
        text = "This is **bold** text"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[1].text, "bold")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text, " text")
    
    
    def test_italic_text(self):
        text = "This is _italic_ text"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[1].text, "italic")
        self.assertEqual(nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(nodes[2].text, " text")
    
    
    # Add more tests for each markdown feature
    
    def test_code_text(self):
        text = "This is `code` text"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[1].text, "code")
        self.assertEqual(nodes[1].text_type, TextType.CODE)
        self.assertEqual(nodes[2].text, " text")
    
    def test_mixed_markdown(self):
        # Test with multiple markdown features
        text = "This is **bold** and _italic_ and `code`"
        nodes = text_to_textnodes(text)
        # Assert expected results
        self.assertEqual(len(nodes), 6)
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[1].text, "bold")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text, " and ")
        self.assertEqual(nodes[3].text, "italic")
        self.assertEqual(nodes[3].text_type, TextType.ITALIC)
        self.assertEqual(nodes[4].text, " and ")
        self.assertEqual(nodes[5].text, "code")
        self.assertEqual(nodes[5].text_type, TextType.CODE)
        
    def test_links_and_images(self):
        # Test with links and images
        text = "A [link](https://boot.dev) and ![image](image.jpg)"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 4)
        self.assertEqual(nodes[0].text, "A ")
        self.assertEqual(nodes[1].text, "link")
        self.assertEqual(nodes[1].url, "https://boot.dev")
        self.assertEqual(nodes[2].text, " and ")
        self.assertEqual(nodes[3].text, "image")
        self.assertEqual(nodes[3].url, "image.jpg")
        
        
    # def test_empty_string(self):
    
    #     # Test with an empty string
    #     text = ""
    #     if not text:  # If text is empty
    #         return [TextNode("", TextType.TEXT)]
    #     nodes = text_to_textnodes(text)
    #     self.assertEqual(len(nodes), 1)
    #     self.assertEqual(nodes[0].text, "")
    #     self.assertEqual(nodes[0].text_type, TextType.TEXT)
        
    # def test_incomplete_markdown(self):
    #     # Test with incomplete markdown syntax
    #     text = "This has a **bold that doesn't close"
    #     nodes = text_to_textnodes(text)
    #     # Assert that it's handled gracefully (likely as plain text)
    #     self.assertEqual(len(nodes), 1)
    #     self.assertEqual(nodes[0].text, "This has a **bold that doesn't close")
    #     self.assertEqual(nodes[0].text_type, TextType.TEXT)
      
      
    def test_consecutive_markdown(self):
        # Test with markdown elements right next to each other
        text = "**Bold**_Italic_`Code`"
        nodes = text_to_textnodes(text)
        # Assert correct node separation
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "Bold")
        self.assertEqual(nodes[0].text_type, TextType.BOLD)
        self.assertEqual(nodes[1].text, "Italic")
        self.assertEqual(nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(nodes[2].text, "Code")
        self.assertEqual(nodes[2].text_type, TextType.CODE)


if __name__ == "__main__":
    unittest.main()
