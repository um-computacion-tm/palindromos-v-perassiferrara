import unittest


def is_palindrome(unstring):
    unstring = unstring.replace(' ', '')
    index2 = -1
    for index1 in range(len(unstring)):
        if unstring[index1] != unstring[index2]:
            return False
        else:
            index2 -= 1
    return True


class Test(unittest.TestCase):

    def test_a(self):
        resultado = is_palindrome('a')
        self.assertEqual(resultado, True)

    def test_aa(self):
        resultado = is_palindrome('aa')
        self.assertEqual(resultado, True)

    def test_ab(self):
        resultado = is_palindrome('ab')
        self.assertEqual(resultado, False)

    def test_aCa(self):
        resultado = is_palindrome('aCa')
        self.assertEqual(resultado, True)

    def test_aCs(self):
        resultado = is_palindrome('aCs')
        self.assertEqual(resultado, False)

    def test_ABBA(self):
        resultado = is_palindrome('ABBA')
        self.assertEqual(resultado, True)

    def test_ABCA(self):
        resultado = is_palindrome('ABCA')
        self.assertEqual(resultado, False)

    def test_ABCBA(self):
        resultado = is_palindrome('ABCBA')
        self.assertEqual(resultado, True)

    def test_ABCCBA(self):
        resultado = is_palindrome('ABCCBA')
        self.assertEqual(resultado, True)

    def test_ZBCCBA(self):
        resultado = is_palindrome('ZBCCBA')
        self.assertEqual(resultado, False)

    def test_neuquen(self):
        resultado = is_palindrome('neuquen')
        self.assertEqual(resultado, True)

    def test_neuqueM(self):
        resultado = is_palindrome('neuqueM')
        self.assertEqual(resultado, False)

    def test_neuquen_espaciado(self):
        result = is_palindrome('ne uq ue n')
        self.assertEqual(result, True)
    
if __name__ == "__main__":
    unittest.main()