'''
Difficulty: Easy
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, and return the reversed list.

'''



class Solution:


    # iteratively
    def reverseList(self, head):
        
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        
    # Recursively
    def reverseList_recusive(self,head):

        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList_recusive(head.next)
            head.next.next = head

        head.next = None    


        return newHead