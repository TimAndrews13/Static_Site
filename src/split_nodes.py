from textnode import TextType, TextNode
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError(f'invalid markdown, delimiter "{delimiter}" not closed')

        # Even index will be a TextNode, Odd index will be Text Type of Delimiter
        for i in range(len(sections)):
            #check if string value is empty
            if sections[i] == "":
                continue
            #if index is an odd number, than new node is TextType of delimiter
            if i % 2 != 0:
                new_node = TextNode(sections[i], text_type)
                new_nodes.append(new_node)
            #if index is an even number or zero, than new node is TextType of TEXT
            else:
                new_node = TextNode(sections[i], TextType.TEXT)
                new_nodes.append(new_node)
    
    return new_nodes


#Helper function to split images and links
def split_nodes_generic(old_nodes, extract_func, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
            
        # 1. Use the passed-in extraction function
        items = extract_func(node.text)
        if not items:
            new_nodes.append(node)
            continue

        remaining_text = node.text
        for item in items:
            # 2. Determine the markdown string based on the TextType
            # Images have a leading '!', links do not
            prefix = "!" if text_type == TextType.IMAGE else ""
            split_value = f"{prefix}[{item[0]}]({item[1]})"
            
            sections = remaining_text.split(split_value, 1)
            
            # Add the text before the item (if any)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            
            # 3. Add the new specialized node using the passed-in text_type
            new_nodes.append(TextNode(item[0], text_type, item[1]))
            
            remaining_text = sections[1]
        
        # Add any remaining text after the last item
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
            
    return new_nodes
                
#Call Helper Funciton in both split_nodes_image and split_nodes_link
def split_nodes_image(old_nodes):
    return split_nodes_generic(old_nodes, extract_markdown_images, TextType.IMAGE)


def split_nodes_link(old_nodes):
    return split_nodes_generic(old_nodes, extract_markdown_links, TextType.LINK)