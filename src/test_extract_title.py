import unittest

from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_equal(self):
        md = """# This is the Title

I am descibing how to do something

1. Step 1
2. Step 2
3. Step 3
"""
        self.assertEqual(extract_title(md), "This is the Title")

    def text_extract_title_exception(self):
        md = """List of Programming Languages

-Python
-GoLang
-C
-SQL        
"""
        self.assertRaises(Exception, extract_title, md)

    def text_extract_title_different_line(self):
        md = """Here is a website
    
# ESPN

Sports Covered:

- Football
- Basketball
- Baseball
- Soccer
- Hockey
"""
        self.assertEqual(extract_title(md), "ESPN")
