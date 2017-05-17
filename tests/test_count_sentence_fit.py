from unittest import TestCase


class TestCount_sentence_fit(TestCase):
    def test_count_sentence_fit(self):
        try:
            from build import count_sentence_fit
        except ImportError:
            self.assertFalse("no function found")

        self.assertRaises(TypeError, count_sentence_fit,
                          None, None, None)

        self.assertRaises(ValueError, count_sentence_fit,
                          'abc', rows=-1, cols=-1)

        sentence = ["hello", "world"]
        expected = 1
        self.assertEqual(count_sentence_fit(sentence, rows=2, cols=8),
                         expected)

        sentence = ["a", "bcd", "e"]
        expected = 2
        self.assertEqual(count_sentence_fit(sentence, rows=3, cols=6),
                         expected)

        sentence = ["I", "had", "apple", "pie"]
        expected = 1
        self.assertEqual(count_sentence_fit(sentence, rows=4, cols=5),
                         expected)
