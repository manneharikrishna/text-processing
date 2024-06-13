import unittest
from cigniti_data import cigdata_paragraph

class TestCigdataParagraph(unittest.TestCase):

    def test_cigdata_paragraph(self):
        # input data and width from cigniti
        paragraph = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."
        page_width = 20

        expected_output = [
            "This   is  a  sample",
            "text      but      a",
            "complicated  problem",
            "to  be solved, so we",
            "are adding more text",
            "to   see   that   it",
            "actually      works."
        ]

        output = cigdata_paragraph(paragraph, page_width)

        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()

