from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    #initialize with one TextNode in a list
    nodes = [TextNode(text, TextType.TEXT)]
    #call split_nodes_delimter for Bold on nodes list
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    #call split_nodes_delimter for Italic on nodes list
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    #call split_nodes_delimiter for Code Block on nodes list
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    #call split_nodes_image on nodes list
    nodes = split_nodes_image(nodes)
    #call split_nodes_link on nodes list
    nodes = split_nodes_link(nodes)

    return nodes