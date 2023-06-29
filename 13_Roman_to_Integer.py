import unittest

class Solution:
    def romanToInt(self, s):
        if not (1 <= len(s) <= 15):
            raise ValueError("s must have length between 1 and 15")
        
        if not isinstance(s, str):
            raise TypeError("s must be a string")
        
        roman_to_int = {
            'I': 1, 'V': 5,
            'X': 10, 'L': 50,
            'C': 100, 'D': 500,
            'M': 1000
        }

        valid_values = roman_to_int.keys()
        for char in s:
            if char not in valid_values:
                raise ValueError("s must be one of {}".format(valid_values))

        result_array = []
        for char in reversed(s):
            char_rst = roman_to_int[char]
            if not len(result_array):
                pass
            else:
                if char_rst >= result_array[-1]:
                    pass
                else:
                    char_rst = -char_rst
            result_array.append(char_rst)
        result = sum(result_array)

        if not 1 <= result <= 3999:
            raise ValueError("Result must be between 1 and 3999, your result is {}".format(result))
        
        return result

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # 異常檢查
    def test_romanToInt_1_length_error(self):
        self.assertRaises(ValueError, self.solution.romanToInt, "")  # 長度小於1
        self.assertRaises(ValueError, self.solution.romanToInt, "IIIIIIIIIIIIIIII")  # 長度大於15

    def test_romanToInt_1_value_error(self):
        self.assertRaises(ValueError, self.solution.romanToInt, "A")

    def test_romanToInt_1_type_error(self):
        self.assertRaises(TypeError, self.solution.romanToInt, 1)

    def test_romanToInt_1_result_error(self):
        self.assertRaises(ValueError, self.solution.romanToInt, "MMMMCMXCIV") # 4994

    # testcase
    def test_romanToInt_III(self):
        result = self.solution.romanToInt("III")
        self.assertEqual(result, 3)

    def test_romanToInt_IV(self):
        result = self.solution.romanToInt("IV")
        self.assertEqual(result, 4)

    def test_romanToInt_IX(self):
        result = self.solution.romanToInt("IX")
        self.assertEqual(result, 9)

    def test_romanToInt_LVIII(self):
        result = self.solution.romanToInt("LVIII")
        self.assertEqual(result, 58)

    def test_romanToInt_MCMXCIV(self):
        result = self.solution.romanToInt("MCMXCIV")
        self.assertEqual(result, 1994)


if __name__=="__main__":
    unittest.main(
        failfast=True,  # 啓用 failfast 選項
        verbosity=2
    )

    # import sys
    # sys.argv.append("-h")
    # print(sys.argv)
    # unittest.main(argv=sys.argv)
