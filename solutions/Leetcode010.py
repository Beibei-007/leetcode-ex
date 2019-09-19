import sys
import getopt

class Solution:
    def isMarchCharStar(self,s, p) :
        print(f"Entering isMarchCharStar: s = {s} , p = {p} : ")
        shead, charstar , phead = 0, 2, 2
        slen, plen = len(s), len(p)

        #看看前面多少个重复的字母
        while shead < slen and s[shead] == p[0] :
            shead += 1
        #看看$*后面有多少个相同的字母比如' a*aaaa' 或者" a*a*a*" 需要处理一下
        while phead < plen and (p[phead] == p[0] or p[phead] == '*'):
            if p[phead] == '*' :
                charstar += 2
            phead += 1

        if phead - charstar > shead :  # too many duplicate char after *
            return False
        else :
            if shead == slen :
                print(f"s is all the same as {p[0]} {shead}, {phead}, {plen}")
                if phead == plen :
                    print(p)
                    return True
                else :
                    return self.isMatch(s[shead-1:], p[phead:]) or self.isMatch(s[shead:], p[phead:])
            else :
                print("s is not all the same")
                return self.isMatch(s[shead:], p[phead:])

    def isMatchRest(self, s, p, pnext):
        print(f"Entering isMatchRest: s = {s} , p = {p} : pnext = {pnext}")
        if pnext >= 0 :
            ret = False
            prefix = p[0:pnext]  #len(prefix) = pnext
            snext = s.find(prefix)
            print(f"pnext={pnext}, prefix={prefix}, snext={snext}")
            #print(snext)
            if snext == -1 : return False   # s不包含prefix子串
            while snext != -1 :
                snext += pnext
                ret = ret or self.isMatch(s[snext:], p[pnext:])
                snext = s.find(prefix, snext+1)
                print(f"snext={snext}")
            return ret
        else :
            plen = len(p)
            slen = len(s)
            dotnum = 0
            while dotnum < plen and p[dotnum] == '.' :
                dotnum += 1
            if dotnum == plen :  # '.....'
                return slen >= dotnum
            else :  # '.....$$$$'
                if slen < dotnum - 1 :
                    return False
                else :
                    ret, snext = False, 0
                    while snext < slen - dotnum + 1 :
                        ret = ret or self.isMatch(s[snext:], p)
                        snext += 1
                    return ret

    def isMarchDotStar(self, s, p) :
        print(f"Entering isMarchDotStar: s = {s} , p = {p} : ")
        #First, remove '.*' and all the following '$*'
        p = p[2:]  # Remove.*
        while len(p) > 1 and p[1] == '*' : p = p[2:]
        if p == '' : return True

        dot = p.find('.')
        star = p.find('*')   #star==-1 or star > 1
        plen = len(p)

        if star == -1 : #没有'*'
            if plen > len(s) :
                return False
            else :
                return self.isMarchNoStar(s[:-plen-1:-1], p[::-1])

        if dot == -1 or star < dot:
            return self.isMatchRest(s, p, star - 1)
        else : # 0 <= dot < star
            return self.isMatchRest(s, p, dot - 1 )

    def isMarchNoStar(self, s, p) :
        print(f"Entering isMarchNoStar: s = {s} , p = {p} : ")
        plen = len(p)
        slen = len(s)
        if slen != plen : return False

        dotpos = p.find('.')
        cur = 0
        while dotpos > -1 and cur < slen:
            if s[cur:dotpos] == p[cur:dotpos] :
                cur = dotpos + 1
                dotpos = p.find('.', cur)
            else :
                return False

        return True if s[cur:] == p[cur:] else False

    def isMatch0(self, s: str, p: str) -> bool:
        print(f"Entering isMatch: s = {s} , p = {p} : ")
        if p == '.*' :
            return True
        if p == '' :
            if s == '' :
                return True      # s=p=''
            else :
                #print("p='', s != ''")
                return False    # p='', s != ''
        elif s == '' :
            if len(p) > 1 and p[1] == '*' :
                return self.isMatch(s,p[2:])
            else :
                return False        # s=='', p != ''

        if not s.islower() : return False

        # s > 0 and p > 0 :
        # Let's process the suffix first
        star = p.rfind('*')
        plen, slen = len(p), len(s)
        if star == -1 :
            return self.isMarchNoStar(s, p)   #no *
        if star < plen - 1 :
            suffix = (plen - 1) - star   #length of suffix
            if suffix > slen :
                return False
            else :
                if self.isMarchNoStar(s[:-suffix-1:-1], p[:-suffix-1:-1]) :
                    s = s[:slen - suffix]
                    p = p[:star+1]
                else :
                    return False

        # * is found at p[1] or later
        aheadstar = p.find('*')
        aheadstar -= 1
        dotpos = p.find('.')

        if aheadstar > 0 and (not self.isMarchNoStar(s[0:aheadstar], p[0:aheadstar])):  #check the prefix
            return False

        if p[aheadstar] != '.' :   # not ".*", may be
            return self.isMarchCharStar(s[aheadstar:], p[aheadstar:])
        else : #meet '.*'
            return self.isMarchDotStar(s[aheadstar:], p[aheadstar:])

    def simplePattern(self, p) :
        if len(p) < 2 : return p
        plist =  [chr(i)+'*' for i in range(97,123)]

        for sp in plist :
            p = p.replace(sp, sp[0].upper())

        p = p.replace('.*', '$')

        i, j = 0, 1
        pnew = ''
        while j < len(p) :
            #p[i]is lower, record it
            if p[i].islower() or p[i] == '.' :
                pnew += p[i]
                i = j
            #p[i] is $, record it and ignore the following upper and $s
            elif p[i] == '$' and p[j] != '$' and not p[j].isupper() :
                pnew += p[i]
                i = j
            else :  #p[i].isupper(),
                if p[j] == '$' :  #skip it if following by $
                    i = j
                elif p[j] != p[i] :  #record it following by other upper or lower
                    pnew += p[i]
                    i = j
            j += 1
        else :  #i 永远都小于j，当j==plen 时，最后一个p[i]还没有放进新的pattern
            pnew += p[i]
        return pnew

    def findMustHave0(self, p) :
        must = []
        j, start = 0, 0
        while j < len(p) :
            if p[j].islower() or p[j] == '.' :
                if j == 0 or p[j-1].isupper() or p[j-1] == '$' : start = j
                j += 1
                if j == len(p): must.append(p[start:j])
            else :
                print("start, j, p[j] = ", start, j, p[j])
                if (j > 0 and (p[j-1].islower() or p[j-1] == '.') ):
                    must.append(p[start:j])
                j += 1
        return must

    def findMustHave(self, p) :
        must = []
        j, start = 0, 0
        mlen = 0
        while j < len(p) :
            if p[j].islower() :
                if j == 0 or p[j-1].isupper() or p[j-1] == '$':
                    start = j
                elif p[j-1] == '.' :
                    #print("appending previous dot")
                    must.append(p[start:j])
                    mlen += (j - start)
                    start = j
                j += 1
                if j == len(p):
                    #print("appending last lower")
                    must.append(p[start:j])
                    mlen += (j - start)
            elif p[j] == '.' :
                if j == 0 or p[j-1].isupper() or p[j-1] == '$':
                    start = j
                elif p[j-1].islower() :
                    #print("appending previous lower")
                    must.append(p[start:j])
                    mlen += (j - start)
                    start = j
                j += 1
                if j == len(p):
                    #print("appending last dot")
                    must.append(p[start:j])
                    mlen += (j - start)
            else :
                #print("start, j, p[j] = ", start, j, p[j])
                if j > 0 and (p[j-1].islower() or p[j-1] == '.') :
                    #print("appending others")
                    must.append(p[start:j])
                    mlen += (j - start)
                j += 1

        return must, mlen

    def slicePattern(self, p) :
        must = []
        j, start = 0, 0
        mlen = 0
        while j < len(p) :
            if p[j].islower() :
                if j == 0 or not p[j-1].islower():
                    start = j
                if not p[j-1].islower() :
                    #print("appending previous dot")
                    must.append(p[start:j])
                    mlen += (j - start)
                    start = j
                j += 1
                if j == len(p):
                    #print("appending last lower")
                    must.append(p[start:j])
                    mlen += (j - start)
            elif p[j] == '.' :
                if j == 0 or p[j-1].isupper() or p[j-1] == '$':
                    start = j
                elif p[j-1].islower() :
                    #print("appending previous lower")
                    must.append(p[start:j])
                    mlen += (j - start)
                    start = j
                j += 1
                if j == len(p):
                    #print("appending last dot")
                    must.append(p[start:j])
                    mlen += (j - start)
            else :
                #print("start, j, p[j] = ", start, j, p[j])
                if j > 0 and (p[j-1].islower() or p[j-1] == '.') :
                    #print("appending others")
                    must.append(p[start:j])
                    mlen += (j - start)
                j += 1

        return must, mlen

    def isMatchSeg(self, s, p) :
        print(f"Entering isMatchSeg: s={s}, p={p}")
        if p == '$' or s == '': return True

        return True

    def translateS(self, s):
        snew = s[0].upper()
        for i in range(1, len(s)) :
            if s[i] != s[i-1] : snew += s[i].upper()

        return snew


    def isMatchSimple(self, s, p) :
        if s == '' :
            for pch in p :
                if pch.islower() or pch == '.' : return False
            return True
        # s != '' :
        if not s.islower() : return False

        # s is a good string:
        must, leastlen = self.findMustHave(p)
        print("s must have:", must, "least length", leastlen)

        plen = len(p)
        for i in range(-1, -plen, -1) :
            if p[i] == '$' :

        if p[-1] == '$' :
            suffix = len(must[-1])
            if must[-1].islower() :
                s = s[ : s.rfind(must[-1]) + suffix]
            else :

            p = p[:-1]

        if p[0] == '$' :
            suffix = len(must[0])
            if must[-1].islower() :
                s = s[ : s.rfind(must[-1]) + suffix]
            p = p[:-1]

        print("now s: ", s)

        slen = len(s)
        if slen < leastlen : return False

        segnum = len(must)

        s1, s2 = 0, 0
        p1, p2 = 0, 0
        ret = True

        for i in range(segnum) :
            print("must=",must[i])
            if must[i] != '.' :
                s1, p1 = s2, p2
                s2, p2 = s.find(must[i], s1), p.find(must[i], p1)
                print("s2, p2", s2, p2)
                print("left", slen, leastlen, slen-leastlen)
                if s2 == -1 or s2 > slen - leastlen :
                    print(f"can't find {must[i]} in s {s1} to end")
                    return False
                else :
                    ret = ret and self.isMatchSeg(s[s1:s2], p[p1:p2])
                lmust = len(must[i])
                leastlen -= lmust
                s2 += lmust
                p2 += lmust
            else :
                s1 += 1
                s2 += 1
                p1 = p2
                p2 = p.find(must[i], p1)
                ret = ret and self.isMatchSeg(s[s1:s2], p[p1:p2])
                p2 += 1
                leastlen -= 1
            if s2 > len(s) :
                print(f"s is too short: {s2}, ", len(s))
                return False
        #After all must, there may be other letters:
        if s2 == len(s) and p2 == len(p) : return ret

        return self.isMatchSeg(s[s2:] , p[p2:] )


        # must = self.findMustHave(s, p)
        #
        # print("s must have: " , must)
        #
        # pos = [[] for i in range(len(must))]
        # for i in range(len(must)) :
        #     if must[i].islower() :
        #         k = s.find(must[i])
        #         while k != -1 :
        #             pos[i].append( k )
        #             k = s.find(must[i], k + 1)
        #         else :
        #             if not pos[i] :
        #                 print("one 'must' is missing")
        #                 return False
        #     else :
        #         pos[i].append( -1 )
        #
        # print("here are they:", pos)


    def isMatch(self, s: str, p: str) -> bool:
        print(f"Entering isMatch: s = {s} , p = {p} : ")
        p = self.simplePattern(p)
        print("simplePattern : ", p)

        if p == '$' :
            return True
        if p == '' :
            return True if s == '' else False

        return self.isMatchSimple(s, p)



def process(args) :
    s = Solution()
    #print(s.isMatch('bbbbac', '.*a*a.'))  #True
    print(s.isMatch("bbcacbabbcbaaccabcgef","b*a*a*.c*bb*b*.*.*gef.*"))  #True
    #print(s.isMatch("mississippi", "mis*is*ip*.")) #True
    #print(s.isMatch("bccbbabcaccacbcacaa", ".*b.*c*.*.*.c*a*")) #False
    #print(s.isMatch("aaaaaaaaaaaaab","a*a*a*a*a*a*a*a*a*a*a*a*b")) #True
    # print(s.isMatch('mississippi', 'mis*is*p*'))  #False
    #print(s.isMatch('abcdecdefg', '.*cdef.*'))  #True

def main( argv = [__name__] ) :
    opt, args = getopt.getopt(argv[1:], "h", ["help"] )
    process(args)

if __name__ == "__main__" :
    sys.exit(main(sys.argv))
