import sys
import getopt

class Solution:
    def convert(self, s, numRows) :
        remain = len(s)
        if remain < 2 or remain <= numRows or numRows < 2:
            return s

        zigzag = [""] * numRows
        pattern = numRows * 2 - 2

        while remain >= pattern :
            for i in range(numRows) :
                if i == 0 or i == numRows - 1:
                    zigzag[i] += s[i]
                else :
                    zigzag[i] += s[i] + s[pattern-i]
            s = s[pattern:]
            remain -= pattern
        else :
            for i in range(remain) :
                if i < numRows:
                    zigzag[i] += s[i]
                else :
                    zigzag[pattern - i] += s[i]

        return ''.join(zigzag)

    def reverse0(self, x: int) -> int:
        limit = 2**31
        if x >= limit or x < -limit :
            return 0

        neg, s = 1, list(str(-x)) if x < 0 else 0, list(str(x))

        n = len(s)
        for i in range(n//2) :
            s[i], s[n-1-i] = s[n-1-i], s[i]

        x = -int(''.join(s)) if neg else int(''.join(s))

        return (0 if x >= limit or x < -limit else x)

    def reverse1(self, x: int) -> int:
        limit = 2147483648 #2**31
        if x >= limit or x < -limit :
            return 0

        neg = 1 if x < 0 else 0

        s = str(-x) if neg else str(x)
        x = -int(s[::-1]) if neg else int(s[::-1])

        return (0 if x >= limit or x < -limit else x)

    def reverse(self, x: int) -> int:
        limit = 2**31
        if x >= limit or x < -limit or x == 0:
            return 0

        if x < 0:
            x = -x
            neg = 1
        else:
            neg = 0

        digit = x % 10
        ret = 0
        while x != 0 :
            if  ret <= limit // 10:
                ret = ret*10 + digit
            else :
                return 0
            x = x // 10
            digit = x % 10
        return -ret if neg else ret

def process(args) :
    s = Solution()
    print(s.convert("PAYPALISHIRING", 4))
    print("PINALSIGYAHRPI")
    print(s.reverse(1463847412))
    print("----------")


def main(argv = [__name__]) :
    opt, args = getopt.getopt(argv[1:], "h", ["help"])
    process(args)

if __name__ == "__main__" :
    sys.exit(main(sys.argv))
