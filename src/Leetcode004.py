import sys
import getopt

class Solution:
    def findKth(self, A, B, k):
        lenA, lenB = len(A), len(B)

        if lenA > lenB :
            return self.findKth(B, A, k)

        if lenA == 0 :
            return B[k-1]

        if k == 1 :
            return min(A[0], B[0])

        pa = min( k // 2, lenA)
        pb = k - pa

        if A[pa-1] <= B[pb-1] :
            return self.findKth(A[pa:], B, pb)
        else:
            return self.findKth(A, B[:pb], pa)

    def findMedianSortedArrays1(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        mid = ( m + n ) // 2

        if ( m + n ) % 2 :
            return findKth(nums1, nums2, mid + 1)
        else:
            return (findKth(nums1, nums2, mid) + findKth(nums1, nums2, mid + 1 )) / 2.0

    def findMedianSortedArrays(self, nums1, nums2):
        A, B, m, n = nums1, nums2, len(nums1), len(nums2)

        #let B be the longer list, length is n
        if m > n :
            A, B, m, n = B, A, n, m

        if n == 0 :
            raise ValueError

        median = [0, 0]
        middle = ( m + n + 1) // 2   # 中位数是第middle个数，或者middle, middle+1的平均

        left, right = 0, m
        while ( left <= right ) :
            i = (left + right) // 2
            edge = middle - i
            # 说明A[i]开始都比B[edge]还大，应该舍弃右边，到左边去查找
            if i > 0 and A[i-1] > B[edge] :   #i>0时， edge <= (m+n+1)/2 - 1 <= (2n-1)/2 <= n
                right = i - 1
            # 说明A[i]开始都比B[edge-1]还小，应该舍弃左边，到右边查找
            elif i < m and A[i] < B[edge-1]: #i<m时， edge >= (m+n+1)/2 - (m-1) > (n-m+3)/2 >= 1
                left = i + 1
            else:
                #找到了一个A[i]，使得A[i-1], A[i], B[edge-1], B[edge]排在中间四个位置
                # 而且（A[i-1], B[edge-1]) 肯定是小于 (A[i], B[edge])
                if i == 0 : # 说明没有A[i-1]
                    median[0] = B[edge - 1]
                elif edge == 0 : #说明没有B[edge-1]
                    median[0] = A[i-1]
                else :
                    median[0] = max(B[edge-1], A[i-1])

                if ( m + n ) % 2 :
                    return median[0]/1.0

                if i == m :  # 不存在A[i]
                    median[1] = B[edge]
                elif edge == n :  # 不存在B[edge]
                    median[1] = A[i]
                else:
                    median[1] = min(B[edge], A[i])

                return ((median[0] + median[1])/2.0)
    def findMedianSortedArrays(self, nums1, nums2):
        A, B, m, n = nums1, nums2, len(nums1), len(nums2)

        #let B be the longer list, length is n
        if m > n :
            A, B, m, n = B, A, n, m

        if n == 0 :
            raise ValueError

        median = [0, 0]
        middle = ( m + n + 1) // 2   # 中位数是第middle个数，或者middle, middle+1的平均

        left, right = 0, m
        while ( left <= right ) :
            i = (left + right) // 2
            edge = middle - i
            # 说明A[i]开始都比B[edge]还大，应该舍弃右边，到左边去查找
            if i > 0 and A[i-1] > B[edge] :   #i>0时， edge <= (m+n+1)/2 - 1 <= (2n-1)/2 <= n
                right = i - 1
            # 说明A[i]开始都比B[edge-1]还小，应该舍弃左边，到右边查找
            elif i < m and A[i] < B[edge-1]: #i<m时， edge >= (m+n+1)/2 - (m-1) > (n-m+3)/2 >= 1
                left = i + 1
            else:
                #找到了一个A[i]，使得A[i-1], A[i], B[edge-1], B[edge]排在中间四个位置
                # 而且（A[i-1], B[edge-1]) 肯定是小于 (A[i], B[edge])
                if i == 0 : # 说明没有A[i-1]
                    median[0] = B[edge - 1]
                elif edge == 0 : #说明没有B[edge-1]
                    median[0] = A[i-1]
                else :
                    median[0] = max(B[edge-1], A[i-1])

                if ( m + n ) % 2 :
                    return median[0]/1.0

                if i == m :  # 不存在A[i]
                    median[1] = B[edge]
                elif edge == n :  # 不存在B[edge]
                    median[1] = A[i]
                else:
                    median[1] = min(B[edge], A[i])

                return ((median[0] + median[1])/2.0)

def process(args):
    s = Solution()
    print(s.findMedianSortedArrays0([1,2],[3,4]))
    print(s.findMedianSortedArrays([1,2],[3,4]))

def main(argv = [__name__]):
    opts, args = getopt.getopt( argv[1:], "h", ["help"])
    process(args)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
