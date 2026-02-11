import unittest

from block_to_block_type import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_heading_block(self):
        md = "### This is a header"
        self.assertEqual(BlockType.HEADING, block_to_block_type(md))

    def test_code_block(self):
        md = '''```
        Here is some code 
        blah blah blah
        x = y
```
'''
        self.assertEqual(BlockType.CODE, block_to_block_type(md))

    def test_quote_block(self):
        md = '''>I think therefor I am
>I have become death, the destroyer of worlds
> I'm walking here!
> May thy knife chip and shatter
'''
        self.assertEqual(BlockType.QUOTE, block_to_block_type(md))

    def test_unordered_list_block(self):
        md = '''
- Jalen Hurts
- AJ Brown
- Quinyon Mitchell
- Jalen Carter
- Devonta Smith
- Cooper DeJean
'''
        self.assertEqual(BlockType.UNORDERED_LIST, block_to_block_type(md))

    def test_ordered_list_block(self):
        md = '''1. Bananas
2. Olives
3. Avocados
4. Lettuce
5. Tomato'''
        self.assertEqual(BlockType.ORDERED_LIST, block_to_block_type(md))

    def test_paragraph_block(self):
        md = ''' I would like boot dev to help me get a programming job some time this year.
        I think it has been very helpful in making me eel more comfortable in Python.
        I am looking forward to learning GoLang.
        '''
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(md))