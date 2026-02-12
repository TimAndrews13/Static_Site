import os
import shutil

from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
from parentnode import ParentNode

def generate_page(from_path, template_path, dest_path):
    original_cwd = os.getcwd()
    from_path = os.path.join(original_cwd, from_path)
    template_path = os.path.join(original_cwd, template_path)
    dest_path = os.path.join(original_cwd, dest_path)

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    #Read Markdown File from from_path
    f = open(from_path, "r")
    md = f.read()
    f.close()

    #Read Template File from template_path
    f = open(template_path, "r")
    template = f.read()
    f.close()

    #Convert Markdown to HTML
    node = markdown_to_html_node(md)
    html = node.to_html()
    
    #Extract Title from Markdown
    title = extract_title(md)

    #Replce {{ Title }} and {{ Content }} in template.html
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    #Write New HTML file in the dest_path
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(template)