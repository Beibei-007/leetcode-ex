# Twelve is written as, XII, which is simply X + II. The number twenty
#  seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest
# from left to right. However, the numeral for four is not IIII.
# Instead, the number four is written as IV. Because the one
# is before the five we subtract it making four.
# The same principle applies to the number nine,
# which is written as IX. There are six instances where subtraction is used:
#
#     I can be placed before V (5) and X (10) to make 4 and 9.
#     X can be placed before L (50) and C (100) to make 40 and 90.
#     C can be placed before D (500) and M (1000) to make 400 and 900.
#
# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
import sys
import getopt

class Solution:
    def intToRoman(self, num: int) -> str:
        if num < 0 or num > 3999 : return ""
        patterns = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        roman = ""

        for u in [1000, 100, 10, 1] :
            digit = num // u
            if digit != 0 :
                k = digit * u
                if digit != 0 :
                    if digit in [9, 5, 4] :
                        roman += patterns[k]
                    elif digit in [6, 7, 8] :
                        roman += patterns[5*u] + patterns[u] * (digit - 5)
                    else :
                        roman += patterns[u] * digit
                num -= k
            if num == 0 : return roman
    def romanToInt64(self, s: str) -> int:
        if s == "" : return 0
        patterns = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9,'V':5, 'IV':4, 'I':1}
        i, ret = 0, 0
        n = len(s)
        while i < n - 1:
            key = s[i:i+2]
            if key not in patterns.keys(): key = s[i]
            ret += patterns[key]
            i += len(key)
        else :
            if i == n - 1 : return ret + patterns[s[i]]
            else : return ret

    # 52ms, 98%
    def romanToInt(self, s: str) -> int:
        if s == "" : return 0
        patterns = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, \
        'L':50, 'XL':40, 'X':10, 'IX':9,'V':5, 'IV':4, 'I':1}
        i, ret = 0, 0
        n = len(s)
        while i < n - 1:
            if (s[i] == 'C' and s[ i + 1 ] in ['D','M']) or \
            (s[i] == 'X' and s[ i + 1 ] in ['C','L'])  or \
            (s[i] == 'I' and s[ i + 1 ] in ['X','V']) :
                key = s[i:i+2]
                i += 2
            else:
                key = s[i]
                i += 1
            ret += patterns[key]
        else :
            if i == n - 1 : return ret + patterns[s[i]]
            else : return ret




def process(args) :
    s = Solution()
    print(s.intToRoman(58))
    print(s.intToRoman(3999))
    print(s.intToRoman(2554))
    print("-----------")
    print(s.romanToInt("LVIII"))
    print(s.romanToInt("MCMXCIV"))
    print(s.romanToInt("CDXCIXIV"))


def main( argv = [__name__] ) :
    opt, args = getopt.getopt(argv[1:], "h", ["help"] )
    process(args)

if __name__ == "__main__" :
    sys.exit(main(sys.argv))
