from textnode import TextNode, TextType
from copy_directory import copy_directory
from generate_page import generate_page, generate_pages_recursive
import os
import sys

def main():
    text_node = TextNode("This is some anchor text", TextType.LINK, url='https://www.boot.dev')
    print(text_node)

    #Set Basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    #copy static directory to docs directory
    copy_directory("static", "docs")

    #Generate Pages Recursively
    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    main()