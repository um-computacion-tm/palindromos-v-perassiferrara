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

    def test_aa_espaciado(self):
        resultado = is_palindrome('a a')
        self.assertEqual(resultado, True)

    def test_ab_espaciado(self):
        resultado = is_palindrome('a b')
        self.assertEqual(resultado, False)

    def test_aCa_espaciado(self):
        resultado = is_palindrome('aC a')
        self.assertEqual(resultado, True)

    def test_aCs_espaciado(self):
        resultado = is_palindrome('a Cs')
        self.assertEqual(resultado, False)

    def test_ABBA_espaciado(self):
        resultado = is_palindrome(' AB BA')
        self.assertEqual(resultado, True)

    def test_ABCA_espaciado(self):
        resultado = is_palindrome('ABC A ')
        self.assertEqual(resultado, False)

    def test_ABCBA_espaciado(self):
        resultado = is_palindrome('AB CB A')
        self.assertEqual(resultado, True)

    def test_ABCCBA_espaciado(self):
        resultado = is_palindrome('A BC C BA')
        self.assertEqual(resultado, True)

    def test_ZBCCBA_espaciado(self):
        resultado = is_palindrome(' ZB CCB A ')
        self.assertEqual(resultado, False)

    def test_neuquen_espaciado(self):
        result = is_palindrome('ne uq ue n')
        self.assertEqual(result, True)

    def test_neuqueM_espaciado(self):
        resultado = is_palindrome('neu que M')
        self.assertEqual(resultado, False)

if __name__ == "__main__":
    unittest.main()