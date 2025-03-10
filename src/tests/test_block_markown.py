import unittest
from src.block_markdown import markdown_to_blocks

class TestBlockMarkdown(unittest.TestCase):
    
    def test_markdown_to_blocks(self):
        markdown = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        
    def test_markdown_two_consecutive_newlines(self):
        markdown = """
    This is **bolded** paragraph


    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
        
        blocks = markdown_to_blocks(markdown)
        
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ]
        )
        
    def test_markdown_one_block(self):
        markdown = """
        This is **bolded** paragraph
        """
        
        blocks = markdown_to_blocks(markdown)
        
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph"
            ]
            )
        
    def test_markdown_empty(self):
        markdown = ""
        
        blocks = markdown_to_blocks(markdown)
        
        self.assertEqual(
            blocks,
            []
        )
        
    def test_markdown_internal_newlines(self):
        markdown = """
    This is a paragraph that
    spans multiple lines. Even though there's a newline character
    after "that" and "lines.", it's still just one paragraph block
    because there are no blank lines between them.

    This is a new paragraph block because there's a blank line above it.
    """
        
        blocks = markdown_to_blocks(markdown)
        
        self.assertEqual(
            blocks,
            [
                "This is a paragraph that\nspans multiple lines. Even though there's a newline character\nafter \"that\" and \"lines.\", it's still just one paragraph block\nbecause there are no blank lines between them.",
                "This is a new paragraph block because there's a blank line above it."
            ]
        )