import sys
import getopt

class Solution:
    #56 ms
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if 2 > length:
            return length
        sdict = {}
        lenmax = startpoint = 0
        for i, c in enumerate(s):
            if c in sdict and (sdict[c] + 1) > startpoint:
                startpoint = sdict[c] + 1
            newlen = i - startpoint + 1
            lenmax = lenmax if lenmax > newlen else newlen
            sdict[c] = i
        return  lenmax

    def lengthOfLongestSubstring64(self, s: str) -> int:
        length = len(s)
        if 2 > length:
            return length

        lenmax = curr = 1
        while (curr < length):
            c = s[curr]
            if c in s[0:curr]:
                lenmax = lenmax if lenmax > curr else curr
                headcut = s.find(c) + 1
                s = s[headcut:]
                length -= headcut
                curr -= headcut
            curr += 1
        return  lenmax if lenmax > curr else curr

    #84 ms
    def lengthOfLongestSubstring1(self, s):
        oldmax = newmax = curr = 0
        length = len(s)
        while (curr < length):
            c = s[curr]
            if c in s[0:curr]:
                headcut = s.find(c) + 1
                s = s[headcut:]
                length -= headcut
                oldmax = curr
                curr -= headcut
            else:
                curr += 1
                newmax = max(newmax, oldmax, curr)
        return newmax

    def lengthOfLongestSubstring2(self, s):
        headmax = i = 0
        length = len(s)
        while (curr < length):
            c = s[curr]
            curr += 1
            if c in s[0:curr-1]:
                headcut = s.find(c) + 1
                if headmax < curr-1:
                    headmax = curr-1
                s = s[headcut:]
                length -= headcut
                curr = 0
            else:
                headmax = max(headmax, curr)
        return headmax

def process(args):
    s = Solution()
    print(s.lengthOfLongestSubstring("tmmzuxt"))

def main(argv = [__name__]):
    opts, args = getopt.getopt( argv[1:], "h", ["help"])
    process(args)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
