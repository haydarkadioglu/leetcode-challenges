class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x < 10: return True

        reversed=0
        original=x

        while (x > 0):
            digit = x%10
            reversed = reversed * 10 + digit
            x //= 10

        return reversed == original


        