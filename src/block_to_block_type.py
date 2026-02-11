from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(markdown):
    #strip markdown just in case
    markdown = markdown.strip()
    #split markdown by each newline
    lines = markdown.split('\n')

    #check for code block:
    if markdown.startswith("```\n") and markdown.endswith("\n```"):
        return BlockType.CODE

    #check for header: Example "# Heading 1"
    if len(lines) == 1 and (markdown.startswith("# ") or markdown.startswith("## ") or markdown.startswith("### ") or markdown.startswith("#### ") or markdown.startswith("##### ") or markdown.startswith("###### ")):
        return BlockType.HEADING

    #Check for quote block:
    quote_bool = all(line.startswith(">") for line in lines)
    if quote_bool:
        return BlockType.QUOTE

    #Check for unorderd list:
    unordered_bool = all(line.startswith("- ") for line in lines)
    if unordered_bool:
        return BlockType.UNORDERED_LIST

    #Check for orderd list:
    ordered_bool = True
    for i, line in enumerate(lines, start=1):
        if not line.startswith(f"{i}. "):
            ordered_bool = False
            break
    if ordered_bool:
        return BlockType.ORDERED_LIST
    
    #Return Paragraph if no conditions met
    return BlockType.PARAGRAPH