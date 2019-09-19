import sys
import getopt
class Solution:
    def myAtoi0(self, s: str) -> int:
        if s == "" : return 0
        n = len(s)
        start = 0
        while start < n and s[start] == ' ' : start += 1
        if start == n : return 0

        neg = 0
        if s[start] == '-' :
            neg = 1
            start += 1
        elif s[start] == '+' :
            start += 1
        if start == n : return 0

        digits = {str(i):i for i in range(10)}
        if s[start] in digits.keys() :
            limit = 2 ** 31 if neg else (2 ** 31) -1
            ret = 0
            while start < n and s[start] in digits.keys() :
                unit = digits[s[start]]
                if  ret <= (limit - unit) // 10:
                    ret = ret * 10 + unit
                    start += 1
                else :
                    ret = limit
                    break
            if neg : ret = -ret
            return ret
        return 0

    def myAtoi36(self, s: str) -> int:
        s = s.lstrip()
        if s == "" : return 0
        n = len(s)
        start, neg = 0, 0
        if s[start] == '-' :
            neg = 1
            start += 1
        elif s[start] == '+' :
            start += 1
        if start == n : return 0

        digits = {str(i):i for i in range(10)}
        if s[start] in digits.keys() :
            limit = 2 ** 31 if neg else (2 ** 31) -1
            ret = 0
            while start < n and s[start] in digits.keys() :
                unit = digits[s[start]]
                if  ret <= (limit - unit) // 10:
                    ret = ret * 10 + unit
                    start += 1
                else :
                    ret = limit
                    break
            if neg : ret = -ret
            return ret
        return 0

    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if s == "" : return 0

        digits = {str(i):i for i in range(10)}
        if s[0] not in digits.keys() and s[0] != '-' and s[0] != '+': return 0

        n = len(s)
        ret, start = 0 , 0
        while start < n and s[start] not in digits.keys() : start += 1
        if start == n : return ret

        limit = 2 ** 31
        neg = 1 if start > 0 and s[start-1] == "-" else 0
        if not neg :
            limit -= 1

        while start < n and s[start] in digits.keys() :
            unit = digits[s[start]]
            if  ret <= (limit - unit) // 10:
                ret = ret * 10 + unit
                start += 1
            else :
                ret = limit
                break
        if neg : ret = -ret
        return ret

def process(args) :
    s = Solution()
    print(s.myAtoi("42"))
    print(s.myAtoi("words and 981"))
    print(s.myAtoi("4193 with words"))
    print(s.myAtoi("-91283472332"))
    print(s.myAtoi("-2147483648"))
    print(s.myAtoi("2147483648"))

def main(argv = [__name__]) :
    opt, args = getopt.getopt(argv[1:], "h", ["help"])
    process(args)

if __name__ == "__main__" :
    sys.exit(main(sys.argv))
