from textnode import TextNode, TextType
from copy_directory import copy_directory
from generate_page import generate_page, generate_pages_recursive
import os

def main():
    text_node = TextNode("This is some anchor text", TextType.LINK, url='https://www.boot.dev')
    print(text_node)

    #copy static directory to public directory
    copy_directory("static", "public")

    #Generate Pages
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()