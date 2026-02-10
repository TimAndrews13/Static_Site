from textnode import TextType, TextNode

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
            if len(sections[i]) == "":
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
                
                