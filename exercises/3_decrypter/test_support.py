import unittest
import support


class TestSupportFunctions(unittest.TestCase):
    def setUp(self):
        self.text_array1 = ['Hi!', 'This', 'is', 'a', 'text.']
        self.text_array2 = [
            'hello', 'hello', 'hello', 'is', 'there', 'anybody', 'out',
            'there', 'out', 'there'
        ]
        self.text_array3 = [
            'hello', 'hello', 'hello', 'is', 'there', 'hello', 'anybody',
            'hello', 'out', 'there', 'out', 'there'
        ]
        self.frequencies1 = {'a': 1, 'b': 5, 't': 3, 'z': 2}

    def test_makeLetterDict(self):
        self.assertEqual(
            support.makeLetterDict(), {
                'a': 0,
                'b': 0,
                'c': 0,
                'd': 0,
                'e': 0,
                'f': 0,
                'g': 0,
                'h': 0,
                'i': 0,
                'j': 0,
                'k': 0,
                'l': 0,
                'm': 0,
                'n': 0,
                'o': 0,
                'p': 0,
                'q': 0,
                'r': 0,
                's': 0,
                't': 0,
                'u': 0,
                'v': 0,
                'w': 0,
                'x': 0,
                'y': 0,
                'z': 0
            })

    def test_countLetters(self):
        self.assertEqual(
            support.countLetters(self.text_array1), {
                'a': 1,
                'b': 0,
                'c': 0,
                'd': 0,
                'e': 1,
                'f': 0,
                'g': 0,
                'h': 2,
                'i': 3,
                'j': 0,
                'k': 0,
                'l': 0,
                'm': 0,
                'n': 0,
                'o': 0,
                'p': 0,
                'q': 0,
                'r': 0,
                's': 2,
                't': 3,
                'u': 0,
                'v': 0,
                'w': 0,
                'x': 1,
                'y': 0,
                'z': 0
            })

    def test_getMostPopularKey(self):
        self.assertEqual(support.getMostPopularKey(self.frequencies1), 'b')
        self.assertIn(
            support.getMostPopularKey(support.countLetters(self.text_array1)),
            ['i', 't'])

    def test_getPopularityList(self):
        self.assertEqual(support.getPopularityList(self.frequencies1),
                         ['b', 't', 'z', 'a'])
        self.assertEqual(
            support.getPopularityList(support.countLetters(self.text_array1)),
            [
                'i', 't', 'h', 's', 'a', 'e', 'x', 'b', 'c', 'd', 'f', 'g',
                'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'u', 'v', 'w',
                'y', 'z'
            ])

    def test_cleanText(self):
        text = self.text_array1
        support.cleanText(text)
        self.assertEqual(text, ['hi', 'this', 'is', 'a', 'text'])

    def test_getUniqueWords(self):
        self.assertEqual(
            support.getUniqueWords([
                'hello', 'hello', 'hello', 'is', 'there', 'anybody', 'out',
                'there', 'out', 'there'
            ]), ['hello', 'is', 'there', 'anybody', 'out'])

    def test_getWordFrequencies(self):
        self.assertEqual(support.getWordFrequencies(self.text_array3), {
            'hello': 5,
            'is': 1,
            'there': 3,
            'anybody': 1,
            'out': 2
        })

    def test_getFreqByLen(self):
        frequencies = support.getWordFrequencies(self.text_array3)

        self.assertEqual(support.getFreqByLen(frequencies, 1), {
            'is': 1,
            'anybody': 1
        })
        self.assertEqual(support.getFreqByLen(frequencies, 2), {'out': 2})
        self.assertEqual(support.getFreqByLen(frequencies, 4), {})
