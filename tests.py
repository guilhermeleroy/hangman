from unittest import TestCase
from unittest import mock

import io
import sys

from main import *

class TestWordLetters(TestCase):
    def test_common_word(self):
        word = 'batata'
        word_letters = get_letters_in_word(word)
        self.assertEqual(len(word_letters), 3)

    def test_word_sorting(self):
        word = 'uoiea'
        word_letters = get_letters_in_word(word)
        self.assertEqual(word_letters, ['a', 'e', 'i', 'o', 'u'])

    def test_uppercase_out(self):
        word = 'Jaca'
        word_letters = get_letters_in_word(word)
        self.assertEqual(word_letters, ['a', 'c'])

    def test_hifen_word(self):
        word = 'a-b-c'
        word_letters = get_letters_in_word(word)
        self.assertEqual(len(word_letters), 3)

class TestDisplayedWord(TestCase):
    def test_empty_used_letters(self):
        used_letters = []
        word = 'alfa'

        #transforma a saida na tela numa variavel de retorno
        output = io.StringIO()
        sys.stdout = output
        display_word(word, used_letters)
        sys.stdout = sys.__stdout__

        self.assertEqual(output.getvalue(), '_ _ _ _ \n\n')

    def test_upperletter_word(self):
        used_letters = ['l']
        word = 'AlFa'
        output = io.StringIO()
        sys.stdout = output
        display_word(word, used_letters)
        sys.stdout = sys.__stdout__

        self.assertEqual(output.getvalue(), 'A l F _ \n\n')

    def test_hifen_word_display(self):
        used_letters = []
        word = 'a-b'
        output = io.StringIO()
        sys.stdout = output
        display_word(word, used_letters)
        sys.stdout = sys.__stdout__

        self.assertEqual(output.getvalue(), '_ - _ \n\n')

    def test_complete_used_letters(self):
        used_letters = ['a', 'f', 'l']
        word = 'alfa'
        output = io.StringIO()
        sys.stdout = output
        display_word(word, used_letters)
        sys.stdout = sys.__stdout__

        self.assertEqual(output.getvalue(), 'a l f a \n\n')

class TestAttempts(TestCase):
    #Utiliza um mock para simular input do usuário
    @mock.patch('main.input', create = True)
    def test_number_attempts_ok(self, mocked_input):
        mocked_input.side_effect = ['5']
        result = get_num_attempts()
        self.assertEqual(result, 5)

    @mock.patch('main.input', create = True)
    def test_number_attempts_lesser(self, mocked_input):
        with self.assertRaises(Exception):
            mocked_input.side_effect = ['0']
            get_num_attempts()

    @mock.patch('main.input', create = True)
    def test_number_attempts_greater(self, mocked_input):
        with self.assertRaises(Exception):
            mocked_input.side_effect = ['11']
            get_num_attempts()

