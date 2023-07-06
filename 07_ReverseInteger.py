import unittest


class Solution:
    """規則
    1. 給定一個32bit有號整數x, 將數據反轉但是符號不變
    2. 如果反轉后的數值超過32bit有號整數的範圍,回傳0
    3. 假定環境不允許你儲存64bit整數
    """

    def reverse(self, x: int) -> int:
        """思路
        1. 取出數值轉換為字串
        2. 反轉字串, 得到反轉後的數字字串
        3. 將反轉後的數字字串轉換為整數. 並恢復數字的符號
        4. 檢查反轉後的數字是否超出32位有符號整數的範圍. 如果是, 將結果設為0
        5. 誤,這題的精神絕對不是這樣XD

        p.s. 這文章似乎解答了我的問題。函數不是不能用, 重點在於你是否瞭解這個函數背後的邏輯與算法。
        https://hung-yanbin.medium.com/leetcode-%E5%B0%8F%E5%88%86%E4%BA%AB-reverse-integer-b1716d8d8d1a
        """
        # Check if x is within the valid range for a 32-bit signed integer
        if not (-(2**32) <= x <= 2**31 - 1):
            raise ValueError(
                "x must be in the range between -(2 ** 32) and 2 ** 31 - 1"
            )

        # Reverse the absolute value of x as a string
        reversed_str = str(abs(x))[::-1]

        # Convert the reversed string back to an integer
        reversed_num = int(reversed_str)

        # Restore the sign of the reversed number
        result = reversed_num if x >= 0 else -reversed_num

        # Check if the reversed number is within the valid range for a 32-bit signed integer
        if not (-(2**31) <= reversed_num <= 2**31 - 1):
            result = 0

        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # 異常檢查
    def test_reverse_1_check_input_value_error(self):
        self.assertRaises(
            ValueError, self.solution.reverse, (2**31 - 1) + 1
        )  # 輸入大於int32
        self.assertRaises(
            ValueError, self.solution.reverse, -(2**32) - 1
        )  # 輸入小於int32

    def test_reverse_1_check_result_value_error(self):
        result = self.solution.reverse(1123456789)
        self.assertEqual(result, 0)

    # testcase
    def test_reverse_input_123(self):
        result = self.solution.reverse(123)
        self.assertEqual(result, 321)

    def test_reverse_input_123_with_minus(self):
        result = self.solution.reverse(-123)
        self.assertEqual(result, -321)

    def test_reverse_input_120(self):
        result = self.solution.reverse(120)
        self.assertEqual(result, 21)


if __name__ == "__main__":
    unittest.main(failfast=True, verbosity=2)

    # import sys
    # sys.argv.append("-h")
    # print(sys.argv)
    # unittest.main(argv=sys.argv)
