import sys
import getopt

class Solution:
    def isPalindrome64(self, x: int) -> bool:
        if x < 0 : return False
        if x <10: return True

        original = x
        palindrome = 0

        while x > 9 :
            palindrome = palindrome * 10 + x % 10
            x = x // 10
        else :
            palindrome = palindrome * 10 + x

        return palindrome == original

    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x > 0) : return False
        if x < 10: return True

        revert = 0
        while x > revert :
            revert = revert * 10 + x % 10
            x = x // 10

        return revert == x or x == revert // 10

def process(args) :
    s = Solution()
    print(s.isPalindrome(120))

def main( argv = [__name__] ) :
    opt, args = getopt.getopt(argv[1:], "h", ["help"])
    process(args)

if __name__ == "__main__" :
    sys.exit(main(sys.argv))
