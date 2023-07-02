import unittest


class RomanConverter:
    """規則
    1. 羅馬數字通常從左到右, 並按照由大到小的順序表示.
    2. 羅馬數字中的4表示為IV而不是IIII, IV表示 -1 + 5 = 4. 同理9也適用.
    3. 數字27表示為XXVII, 即 XX(20)+ V(5)+ II(2)
    """

    ROMAN_TO_INT_MAPPING = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    INT_TO_ROMAN_MAPPING = [
        ["I", "V", "X"],
        ["X", "L", "C"],
        ["C", "D", "M"],
        ["M", "A", "A"],
    ]

    def romanToInt(self, s: str) -> int:
        """思路
        1. 建立羅馬字轉數字的轉換表。
        2. 將輸入的羅馬字串從低位到高位進行迭代。
        3. 對於每個羅馬字元, 使用轉換表查找對應的數字值。
        4. 如果遇到的羅馬字元比列表中的最後一個大, 表示需要進行減法操作。
        5. 將每個羅馬字元對應的數字值加總得到結果。
        """
        self._check_string_length(s)

        self.check_valid_roman(s)

        result_array = []
        for char in reversed(s):
            char_rst = self.ROMAN_TO_INT_MAPPING[char]
            if not len(result_array):
                pass
            else:
                if char_rst >= result_array[-1]:
                    pass
                else:
                    char_rst = -char_rst
            result_array.append(char_rst)
        result = sum(result_array)

        self._check_integer_range(result)

        return result

    def intToRoman(self, num: int) -> str:
        """概念
        1. 羅馬數字系統每位數由符號x1、x5、x10的組合表示。
        2. 下一組的轉換表, 是通過將符號乘以10表示。如, x10, x50, x100等。
        """
        """思路
        1. 建立數字轉換為羅馬數字的轉換表。
        2. 將輸入的羅馬數字從低位到高位進行迭代。(個位、十位、百位)
        3. 如果數字為9, 將x1和x10組合添加到列表中。
        4. 如果數字大於或等於5, 將第x5和x1重複組合添加到列表中。
        5. 如果數字為4, 將x1和第x5組合添加到列表中。
        6. 對於其他數字小於4, 將x1重複添加到列表中。
        7. 將羅馬數字符號列表反轉並連接為一個字符串。
        """
        self._check_integer_range(num)

        digit_list = [int(digit) for digit in reversed(str(num))]
        roman_symbols = []
        for i in range(len(digit_list)):
            digit = digit_list[i]
            symbols = self.INT_TO_ROMAN_MAPPING[i]

            if digit == 9:
                roman_symbols.append(symbols[0] + symbols[2])
            elif digit >= 5:
                roman_symbols.append(symbols[1] + symbols[0] * (digit - 5))
            elif digit == 4:
                roman_symbols.append(symbols[0] + symbols[1])
            else:
                roman_symbols.append(symbols[0] * digit)
        result = "".join(roman_symbols[::-1])

        return result

    def _check_string_length(self, s: str):
        if not isinstance(s, str):
            raise TypeError("s must be a string")

        if not (1 <= len(s) <= 15):
            raise ValueError("s must have a length between 1 and 15")

    def check_valid_roman(self, s: str):
        valid_values = set(self.ROMAN_TO_INT_MAPPING.keys())
        for char in s:
            if char not in valid_values:
                raise ValueError("s must be one of {}".format(valid_values))

    def _check_integer_range(self, value: int):
        if not isinstance(value, int):
            raise TypeError("value must be an integer")

        if not (1 <= value <= 3999):
            raise ValueError("value must have a value between 1 and 3999")


class TestRomanToInt(unittest.TestCase):
    def setUp(self):
        self.solution = RomanConverter()

    # 異常檢查
    def test_romanToInt_1_length_error(self):
        self.assertRaises(ValueError, self.solution.romanToInt, "")  # 長度小於1
        self.assertRaises(
            ValueError, self.solution.romanToInt, "IIIIIIIIIIIIIIII"
        )  # 長度大於15

    def test_romanToInt_1_value_error(self):
        self.assertRaises(ValueError, self.solution.romanToInt, "A")

    def test_romanToInt_1_type_error(self):
        self.assertRaises(TypeError, self.solution.romanToInt, 1)

    def test_romanToInt_1_result_error(self):
        self.assertRaises(ValueError, self.solution.romanToInt, "MMMMCMXCIV")  # 4994

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


class TestIntToRoman(unittest.TestCase):
    def setUp(self):
        self.solution = RomanConverter()

    # 異常檢查
    def test_intToRoman_1_size_error(self):
        self.assertRaises(ValueError, self.solution.intToRoman, 0)  # 大小小於1
        self.assertRaises(ValueError, self.solution.intToRoman, 4000)  # 大小大於3999

    def test_intToRoman_1_type_error(self):
        self.assertRaises(TypeError, self.solution.intToRoman, "I")

    # testcase
    def test_intToRoman_III(self):
        result = self.solution.intToRoman(3)
        self.assertEqual(result, "III")

    def test_intToRoman_IV(self):
        result = self.solution.intToRoman(4)
        self.assertEqual(result, "IV")

    def test_intToRoman_IX(self):
        result = self.solution.intToRoman(9)
        self.assertEqual(result, "IX")

    def test_intToRoman_LVIII(self):
        result = self.solution.intToRoman(58)
        self.assertEqual(result, "LVIII")

    def test_intToRoman_MCMXCIV(self):
        result = self.solution.intToRoman(1994)
        self.assertEqual(result, "MCMXCIV")  # [5, -1, 100, -10, 1000, -100, 1000]


if __name__ == "__main__":
    # unittest.main(
    #     failfast=True,  # 啓用 failfast 選項
    #     verbosity=2
    # )

    # 創建測試套件
    suite = unittest.TestSuite()
    test_case_1 = unittest.TestLoader().loadTestsFromTestCase(TestRomanToInt)
    test_case_2 = unittest.TestLoader().loadTestsFromTestCase(TestIntToRoman)
    suite.addTest(test_case_1)
    suite.addTest(test_case_2)
    # 創建測試運行器
    runner = unittest.TextTestRunner(failfast=True, verbosity=2)
    runner.run(suite)  # 運行測試

    # import sys
    # sys.argv.append("-h")
    # print(sys.argv)
    # unittest.main(argv=sys.argv)
