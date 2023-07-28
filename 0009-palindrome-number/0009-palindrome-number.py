class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums = [num for num in str(x)]
        return nums == nums[::-1]