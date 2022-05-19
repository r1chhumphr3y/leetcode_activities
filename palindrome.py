# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: [ListNode]) -> bool:

        list_len = len(head)
        print(list_len)

        midpoint = int(list_len / 2)

        print("mid:", midpoint)
        if (midpoint % 2) == 0:
            # number is even
            print("even")

        check_against = list_len-1

        # assume true until proven false
        is_palindrome = True

        for i in range(midpoint):
            # debug: print("checking if:", head[i], "==", head[check_against])
            if (head[i]!=head[check_against]):
                is_palindrome = False
                break
            check_against -= 1

        return(is_palindrome)

if __name__ == '__main__':

    test_ll = ListNode
    test_ll = [1,1,1,1,1,2,6,2,1,1,1,1,1]

    print("Checking: ", test_ll)
    solution = Solution;
    print(solution.isPalindrome(solution, test_ll))
