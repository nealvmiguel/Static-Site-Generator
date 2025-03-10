
def markdown_to_blocks(markdown):
 # Split the markdown into blocks using double newlines
    blocks = markdown.strip().split("\n\n")
    
    
    cleaned_blocks = []
    
    for block in blocks:
        # Split the block into lines
        lines = block.split("\n")
        # Process each line and remove empty lines
        cleaned_lines = [line.strip() for line in lines if line.strip()]
        # Join the lines back together
        
        cleaned_block = "\n".join(cleaned_lines)
        
        if cleaned_block: 
            cleaned_blocks.append(cleaned_block)
    
   
    # Return our list of blocks
    return cleaned_blocks



markdown_to_blocks("""
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.
This is the second oten oten

- This is the first list item in a list block
- This is a list item
- This is another list item
    """)
