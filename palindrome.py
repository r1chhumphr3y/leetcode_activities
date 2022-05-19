# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: [ListNode]) -> bool:

        list_len = 0
        mylist = []

        while (head):
            list_len += 1
            mylist.append(head.val)
            head = head.next

        midpoint = int(list_len / 2)

        check_against = list_len - 1

        # assume true until proven false
        is_palindrome = True

        for i in range(midpoint):
            if (mylist[i] != mylist[check_against]):
                is_palindrome = False
                break
            check_against -= 1

        return (is_palindrome)
if __name__ == '__main__':

    test_ll = ListNode

    print("Checking: ", test_ll)
    solution = Solution;
    print(solution.isPalindrome(solution, test_ll))
