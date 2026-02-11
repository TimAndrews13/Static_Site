def markdown_to_blocks(markdown):
    #Split markdown text by whitespce
    blocks = markdown.split("\n\n")
    #use list comprehension to remove empty blocks
    blocks = [block for block in blocks if block]
    #strip each block of leading and trailing whitespce
    for i in range(len(blocks)):
        blocks[i] = blocks[i].strip()
    
    return blocks