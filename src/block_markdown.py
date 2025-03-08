# from textnode import TextNode, TextType



def markdown_to_blocks(markdown):
    # Split the markdown into blocks using double newlines
    blocks = markdown.strip().split("\n\n")
    # Now we need to clean up each block and remove empty ones...
    
    print(blocks)
    
    # Return our list of blocks
    return blocks


markdown_to_blocks("""
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
""")