from textnode import TextType, TextNode, text_node_to_html_node
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from block_to_block_type import block_to_block_type, BlockType
from markdown_to_blocks import markdown_to_blocks
from text_to_textnodes import text_to_textnodes


def markdown_to_html_node(markdown):
    #Convert Markdown into Blocks
    blocks = markdown_to_blocks(markdown)

    #Create Empty list to append all html_nodes to
    children_nodes = []

    #Loop over Each Block in Blocks:
    for block in blocks:
        blocktype = block_to_block_type(block)

    #Create new HTMLNode with proper data based on Block Type
        #If BlockType is a CODE
        if blocktype == BlockType.CODE:
            block = block.removeprefix("```").removesuffix("```").removeprefix("\n")
            text_node = TextNode(block, TextType.TEXT)
            html_node = text_node_to_html_node(text_node)
            html_node = ParentNode(tag="code", children=[html_node], props=None)
            html_node = ParentNode(tag="pre", children=[html_node], props=None)
        
        #If BlockType is a HEADING
        elif blocktype == BlockType.HEADING:
            count = 0
            for char in block:
                if char == "#":
                    count += 1
                else:
                    break
            count = 6 if count > 6 else count
            block = block.removeprefix(count * "#").removeprefix(" ")
            html_node = ParentNode(tag=f"h{count}", children=text_to_children(block), props=None)

        #If BlockType is a QUOTE
        elif blocktype == BlockType.QUOTE:
            lines = block.split("\n")
            lines = [line.removeprefix("> ").removeprefix(">") for line in lines]
            block = " ".join(lines)
            html_node = ParentNode(tag="blockquote", children=text_to_children(block), props=None)

        #If BlockType is an UNORDERD_LIST
        elif blocktype == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            lines = [ParentNode(tag="li", children=text_to_children(line.removeprefix("- ").removeprefix("* "))) for line in lines]
            html_node = ParentNode(tag="ul", children=lines, props=None)

        #If BlockType is an ORDERED_LIST
        elif blocktype == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            li_list = []
            for i, line in enumerate(lines, start=1):
                li = ParentNode(tag=f"li", children=text_to_children(line.removeprefix(f"{i}. ")))
                li_list.append(li)
            html_node = ParentNode(tag="ol", children=li_list, props=None)

        #If BlockType is a PARAGRAPH    
        elif blocktype == BlockType.PARAGRAPH:
            block = block.replace("\n", " ")
            html_node = ParentNode(tag="p", children=text_to_children(block), props=None)
        
        children_nodes.append(html_node)
    
    parent_node = ParentNode(tag="div", children=children_nodes)
    
    return parent_node

#Helper funciton to Create Children HTML_Nodes for each block in markdown_to_html_node
def text_to_children(text):
    #Convert text to List of Text Nodes
    text_nodes = text_to_textnodes(text)
    #List Comprehension to convert each text_node in text_nodes into a new list of html_nodes
    html_nodes = [text_node_to_html_node(text_node) for text_node in text_nodes]

    return html_nodes
