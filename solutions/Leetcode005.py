import sys
import getopt

class Solution:
    def longestPalindrome0(self, s):
        print(s)
        n = len(s)
        if n < 2 :
            return n

        parlList = []

        lognest = 1

        longest = 2 if s[0] == s[1] else 1
        substr = s[0:longest]
        parlList.append((longest, substr))

        mid = 1
        while mid < n - 1 :
            even, i = 0, 0
            while (mid - i) >= 0 and (mid + 1 + i) <= n - 1 :
                if s[mid - i] == s[mid + 1 + i] :
                    even += 2
                    print("even:", even, mid, i, mid-i, mid+i+2, s[mid-i:mid+i+2])
                    i += 1
                else :
                    break

            odd, j = 1, 1
            while (mid - j) >= 0 and (mid + j) <= n - 1 :
                if s[mid - j] == s[mid + j]:
                    odd += 2
                    print("odd:", odd, mid, i, mid-i-1, mid+i, s[mid-j: mid+j+1])
                    j += 1
                else:
                    break

            if even > odd :
                print(mid, i)
                substr = s[mid-i+1 : mid+i+1]
                parlList.append((even, substr))
            else :
                substr = s[mid-j+1: mid+j]
                parlList.append((odd, substr))

            mid += 1

        longest = 2 if s[n - 1] == s[n - 2] else 1
        parlList.append((longest, s[n-longest:]))

        return parlList

    def longestPalindrome1(self, s):
        n = len(s)
        if n < 2 :
            return s

        longest, mid = 0, 0

        mid = n // 2 if n % 2 else (n-1) // 2
        # to the right
        while mid < n :
            even, i, odd, j = 0, 0, 1, 1
            while (mid - i) >= 0 and (mid + 1 + i) <= n - 1 and s[mid - i] == s[mid + 1 + i] :
                even += 2
                i += 1

            while (mid - j) >= 0 and (mid + j) <= n - 1 and s[mid - j] == s[mid + j]:
                odd += 2
                j += 1

            if even > odd :
                if even > longest :
                    longest = even
                    substr = s[mid-i+1 : mid+i+1]
            else :
                if odd > longest :
                    longest = odd
                    substr = s[mid-j+1: mid+j]

            if mid + i + 1 < n and mid + j < n :
                mid += 1
            else :
                break

        # to the left
        if longest < n :
            mid = n // 2 if n % 2 else (n-1) // 2
            while mid >= 0:
                even, i, odd, j = 0, 0, 1, 1
                while (mid - i) >= 0 and (mid + 1 + i) <= n - 1 and s[mid - i] == s[mid + 1 + i] :
                    even += 2
                    i += 1

                while (mid - j) >= 0 and (mid + j) <= n - 1 and s[mid - j] == s[mid + j]:
                    odd += 2
                    j += 1

                if even > odd :
                    if even > longest :
                        longest = even
                        substr = s[mid-i+1 : mid+i+1]
                else :
                    if odd > longest :
                        longest = odd
                        substr = s[mid-j+1: mid+j]

                if mid - j >= 0 and mid - i >= 0 :
                    mid -= 1
                else :
                    break

        return substr

    def longestPalindrome2(self, s):
        n = len(s)
        if n < 2 :
            return s

        longest, substr = 1, s[0]

        mid = n // 2 if n % 2 else (n-1) // 2
        # to the right
        cur = mid
        while cur < n :
            i, j = 0, 1
            while (cur - i) >= 0 and (cur + 1 + i) <= n - 1 and s[cur - i] == s[cur + 1 + i]:
                i += 1
            even = i * 2

            while (cur - j) >= 0 and (cur + j) <= n - 1 and s[cur - j] == s[cur + j]:
                j += 1
            odd = 1 + (j-1)*2

            if even > odd and even > longest:
                    longest = even
                    substr = s[cur-i+1 : cur+i+1]
            elif odd > longest :
                    longest = odd
                    substr = s[cur-j+1: cur+j]

            if cur + i + 1 < n and cur + j < n :
                cur += 1
            else :
                break

        # to the left
        cur = min( mid - 1, cur - i + 1, cur - j + 1)
        right = longest // 2
        while cur >= right:
            i , j = 0 , 1
            while (cur - i) >= 0 and (cur + 1 + i) <= n - 1 and s[cur - i] == s[cur + 1 + i]:
                i += 1
            even = i * 2

            while (cur - j) >= 0 and (cur + j) <= n - 1 and s[cur - j] == s[cur + j]:
                j += 1
            odd = j*2 - 1

            if even > odd :
                if even > longest :
                    longest = even
                    substr = s[cur-i+1 : cur+i+1]
            else :
                if odd > longest :
                    longest = odd
                    substr = s[cur-j+1: cur+j]

            if cur - j >= 0 and cur - i >= 0 :
                cur -= 1
            else :
                break

        return substr

    def findPalindrome148(self, s, n, pos):
        i, j = 0, 1
        while i <= pos and (pos + 1 + i) <= n - 1 and s[pos - i] == s[pos + 1 + i]:
            i += 1
        even = i * 2

        while j <= pos and (pos + j) <= n - 1 and s[pos - j] == s[pos + j]:
            j += 1
        odd = 1 + (j-1)*2

        if even > odd :
            return even, s[pos-i+1 : pos+i+1]
        else :
            return odd, s[pos-j+1: pos+j]

    def longestPalindrome148(self, s):
        n = len(s)
        if n < 2 :
            return s

        longest, substr = 1, s[0]

        mid = n // 2 if n % 2 else (n-1) // 2
        right = mid
        left = mid-1
        half = 1
        while right + half < n or left >= half:
            if right + half <= n :
                pallen, palstr = self.findPalindrome148(s, n, right)
                if pallen > longest : longest, substr = pallen, palstr
                half = longest // 2
                right += 1
            if left >= half :
                pallen, palstr = self.findPalindrome148(s, n, left)
                if pallen > longest : longest, substr = pallen, palstr
                half = longest // 2
                left -= 1

        return substr

    def findPalindrome(self, s, n, pos):
        i, j = 0, 1
        while i <= pos and (pos + 1 + i) <= n - 1 and s[pos - i] == s[pos + 1 + i]:
            i += 1
        while j <= pos and (pos + j) <= n - 1 and s[pos - j] == s[pos + j]:
            j += 1

        j -= 1

        if i > j :
            return i*2 , s[pos-i+1 : pos+i+1]
        else :
            return j*2+1, s[pos-j: pos+j+1]

    def longestPalindrome(self, s):
        n = len(s)
        if n < 2 :
            return s
        longest, substr = 1, s[0]
        right = n // 2 if n % 2 else (n-1) // 2
        left = right - 1
        half = 0
        while right + half < n or left >= half:
            if left >= half :
                palLen, palstr = self.findPalindrome(s, n, left)
                if  palLen > longest :
                    longest, substr = palLen, palstr
                    half = longest // 2
                left -= 1
            if right + half < n :
                palLen, palstr = self.findPalindrome(s, n, right)
                if  palLen > longest :
                    longest, substr = palLen, palstr
                    half = longest // 2
                right += 1

        return substr

def process(args):
    s = Solution()
    print(s.longestPalindrome0("ccd"))
    print("---------")
    print(s.longestPalindrome("baadc"))


def main(argv = [__name__]):
    opt, args = getopt.getopt(argv[1:], "h", "help")
    process(args)

if __name__ == "__main__" :
    sys.exit(main(sys.argv))
