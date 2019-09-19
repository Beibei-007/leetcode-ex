import sys
import getopt

class Solution:
    #784 ms
    def twoSum(self, nums, target):
        for item in nums:
            otherItem = target - item
            if otherItem == item:
                result = [i for i,x in enumerate(nums) if x==item]
                if len(result) > 1:
                    return result[0:2]
            elif (otherItem in nums):
                return [nums.index(item), nums.index(otherItem)]
        return [-1,-1]

    #36 ms
    def twoSumFaster(self, nums, target):
        numberpairs = {}
        for index, value in enumerate(nums):
            if value in numberpairs:     #note that value is the KEY of the dictionary
                return [numberpairs[value], index]
            numberpairs[target - value]=index
        return [-1,-1]

def process(args):
    s = Solution()
    for arg in args:
        if "2" == arg:
            print(s.twoSum([2,7,11,15], 13))

#def main1(argv=None): # Take an optional 'argv' argument
#    if argv is None:
#        argv = sys.argv
def main(argv=[__name__]):
    opts, args = getopt.getopt(argv[1:], "h", ["help"])
    process(args) # process() is defined elsewhere

if __name__ == "__main__":
    sys.exit(main(sys.argv))
