import unittest
from pathlib import Path

from compythertools.funcs import replace_with_json
from compythertools.funcs import marker


class TestStringMethods(unittest.TestCase):

    def test_jsonfile(self):
        '''
        Testing replace_with_json function with sample data.
        '''
        self._sampleInput = Path('tests/samplefiles/sample_input.txt')
        self._sampleOutput = Path('tests/samplefiles/sample_output.txt')
        self._sampleJson = Path('tests/samplefiles/sample_data.json')
        self._newFile = Path('tests/samplefiles/test_output.txt')

        replace_with_json(
            self._sampleInput,
            self._newFile,
            self._sampleJson
        )

        with open(self._sampleOutput, 'r') as file1, \
                open(self._newFile, 'r') as file2:

            self.assertEquals(
                file1.read(),
                file2.read()
            )

    def test_marker(self):
        '''
        Testing marker function.
        '''

        self._unmarkedStrings = [
            'Winter', 'Spring', 'Summer', 'Autumn'
        ]
        self._markeredStrings = [
            '<:Winter:>', '<:Spring:>', '<:Summer:>', '<:Autumn:>'
        ]
        self.assertEquals(
            self._markeredStrings,
            list(map(marker, self._unmarkedStrings))
        )


if __name__ == '__main__':
    unittest.main()
