class Solution:
    def romanToInt(self, s: str) -> int:
        symb_val = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        total = 0
        old_value = 0
        for symbol in reversed(s):
            value = symb_val[symbol]
            if value < old_value:
                total -= value
            else:
                total += value
            old_value = value
        return total