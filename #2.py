class LinkedList:
    def __init__(self):
        self.head = None  

    def append(self, data):
        new_node = ListNode(data) 
        
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            nxt = curr.next  
            curr.next = prev  
            prev = curr      
            curr = nxt       
        self.head = prev 
        return prev

class Solution(object):
    def getList(self, l):
        new_list = []
        current = l
        e = False
        while e == False and current != None:
            new_list.append(current.val)
            try:
                current = current.next
            except:
                e = True
                break
        return new_list
    def addTwoNumbers(self, l1, l2):
        a = self.getList(l1)
        b = self.getList(l2)

        a.reverse()
        b.reverse()

        a_n = ""
        b_n = ""

        for n in a:
            a_n += str(n)
        for n in b:
            b_n += str(n)
        
        r = str(int(a_n) + int(b_n))
        
        result = LinkedList()
        for n in r:
            result.append(int(n))
        
        result.reverse()

        return result.head