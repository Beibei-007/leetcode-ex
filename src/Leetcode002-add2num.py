import sys
import getopt
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def traverse(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next

class Solution:
    #84 ms
    def addTwoNumbers(self, l1, l2):
        head = sum = ListNode(0)
        while (l1.next != None or l2.next != None) :
            sum.val = sum.val + l1.val + l2.val
            sum.next = ListNode(0)
            if (10 <= sum.val):
                sum.val = sum.val - 10
                sum.next = ListNode(1)
            l1 = l1.next if l1.next != None else ListNode(0)
            l2 = l2.next if l2.next != None else ListNode(0)
            sum = sum.next
        else:  #l1, l2 has only one node
            sum.val = sum.val + l1.val + l2.val
            if (10 <= sum.val):
                sum.val = sum.val - 10
                sum.next = ListNode(1)
        return head
    # 72 ms, 13.2M
    def addTwoNumbers2(self, l1, l2):
        head = l1
        while (l1.next != None or l2.next != None) :
            exceed = 0
            l1.val = l1.val + l2.val
            if (10 <= l1.val):
                l1.val = l1.val - 10
                exceed = 1
            if l1.next != None:
                l1 = l1.next
                l1.val = l1.val + exceed
            else:
                l1.next = ListNode(exceed)
                l1 = l1.next
            l2 = l2.next if l2.next != None else ListNode(0)
        else:  #l1, l2 has only one node
            l1.val = l1.val + l2.val
            if (10 <= l1.val):
                l1.val = l1.val - 10
                l1.next = ListNode(1)
        return head

    def addTwoNumbers3(self, l1, l2):
        head = l1
        while (l1.next != None or l2.next != None) :
            exceed = 0
            l1.val = l1.val + l2.val
            if (10 <= l1.val):
                l1.val = l1.val - 10
                exceed = 1

            if l2.next == None:
                if l1.next.val < 9:
                    l1.next.val += exceed
                    break
                l2.next = ListNode(0)
            elif l1.next == None:
                if l2.next.val < 9:
                    l2.next.val += exceed
                    l1.next = l2.next
                    break
                l1.next = ListNode(exceed)
                l1 = l1.next
            else:
                l1 = l1.next
                l1.val += exceed
                l2 = l2.next
        else:  #l1, l2 has only one node
            l1.val = l1.val + l2.val
            if (10 <= l1.val):
                l1.val = l1.val - 10
                l1.next = ListNode(1)
        return head

    #64 ms
    def addTwoNumbers4(self, l1, l2):
        head = l1
        while ( l1.next and l2.next) :
            exceed = 0
            l1.val = l1.val + l2.val
            if (10 <= l1.val):
                l1.val = l1.val - 10
                exceed = 1
            l1 = l1.next
            l1.val += exceed
            l2 = l2.next
        else:  #l1.next == None or l2.next == None
            l1.val = l1.val + l2.val
            exceed = 0
            if( l1.next == None and l2.next == None):  #finish, just add two end nodes
                if (10 <= l1.val):
                    l1.val = l1.val - 10
                    l1.next = ListNode(1)
                return head
            elif ( l1.next == None ):   #l1.next == None, l2.next != None
                if (10 <= l1.val):
                    l1.val = l1.val - 10
                    exceed = 1
                l1.next = l2.next
                l1 = l1.next
                l1.val += exceed
            while ( l1.next != None):
                exceed = 0
                if (10 <= l1.val):
                    l1.val = l1.val - 10
                    exceed = 1
                l1 = l1.next
                l1.val += exceed
            else:
                if (10 <= l1.val):
                    l1.val = l1.val - 10
                    l1.next = ListNode(1)

        return head

    #64 ms
    def addTwoNumbers5(self, l1, l2):
        head = l1
        exceed = 0
        l1.val = l1.val + l2.val + exceed
        while ( l1.next and l2.next) :
            exceed = 0
            if (10 <= l1.val):
                l1.val = l1.val - 10
                exceed = 1
            l1 = l1.next
            l2 = l2.next
            l1.val = l1.val + l2.val + exceed
        else:
            if (10 <= l1.val):
                l1.val = l1.val - 10
                exceed = 1
            else:
                exceed = 0

            if( l1.next == None and l2.next == None):  #finish, just add two end nodes
                if (exceed):
                    l1.next = ListNode(exceed)
                return head

            if ( l1.next == None ):   #l1.next == None, l2.next != None
                l1.next = l2.next

            l1 = l1.next
            l1.val += exceed

            while ( l1.next != None):
                exceed = 0
                if (10 <= l1.val):
                    l1.val = l1.val - 10
                    exceed = 1
                l1 = l1.next
                l1.val += exceed
            else:
                if (10 <= l1.val):
                    l1.val = l1.val - 10
                    l1.next = ListNode(1)

        return head

    #60 ms
    def addTwoNumbers6(self, l1, l2):
        if (l1 == None and l2 == None):
            return None;

        i1 = 0 if l1==None else l1.val
        i2 = 0 if l2==None else l2.val

        sum = i1 + i2
        head = s = ListNode( sum % 10 )
        exceed =  sum // 10

        l1 = None if l1 == None else l1.next
        l2 = None if l2 == None else l2.next

        while (l1  or l2 ) :
            i1 = 0 if l1==None else l1.val
            i2 = 0 if l2==None else l2.val

            sum = i1 + i2 + exceed
            s.next = ListNode( sum % 10 )
            exceed =  sum // 10

            l1 = None if l1 == None else l1.next
            l2 = None if l2 == None else l2.next

            s = s.next
        else:
            if (exceed):
                s.next = ListNode(exceed)

        return head

    def addTwoNumbers_short(self, l1, l2):
        result = pointer = ListNode(0)
        acc = 0

        while l1 or l2 or acc:
            v1, l1 = (l1.val, l1.next) if l1 else (0,  None)
            v2, l2 = (l2.val, l2.next) if l2 else (0,  None)
            acc, n = divmod(v1 + v2 + acc, 10)

            pointer.next = ListNode(n)
            pointer = pointer.next

        return result.next

def process(args):
    s = Solution()
    for arg in args:
        if "2" == arg:
            l1 = ListNode(5)
            l2 = ListNode(5)
            p = s.addTwoNumbers6(l1, l2)
            if p != None:
                p.traverse()

#def main1(argv=None): # Take an optional 'argv' argument
#    if argv is None:
#        argv = sys.argv
def main(argv=[__name__]):
    opts, args = getopt.getopt(argv[1:], "h", ["help"])
    process(args) # process() is defined elsewhere

if __name__ == "__main__":
    sys.exit(main(sys.argv))
