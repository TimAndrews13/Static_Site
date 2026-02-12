from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type

def extract_title(markdown):
    #Convert Markdown to Blocks
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block[0:2] == "# ":
            return block.removeprefix("# ")
    raise Exception("No H1 Header Present in Markdown")
