from textnode import TextNode, TextType
from copy_directory import copy_directory

def main():
    text_node = TextNode("This is some anchor text", TextType.LINK, url='https://www.boot.dev')
    print(text_node)

    copy_directory("static", "public")

if __name__ == "__main__":
    main()