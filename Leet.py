"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice."""
class Solution:
    def twoSum(self, nums, target):
        for i, h in enumerate(nums):
            for j in range(i+1, len(nums)):
                if h + nums[j] == target:
                    return [i, j]
                   

"""Given an integer x, return true if x is palindrome integer. An integer is a palindrome when it reads the same backward as forward. 
For example, 121 is a palindrome while 123 is not."""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
    
        # WHY store the number in a variable?
        number = x
        # This will store the reverse of the number
        reverse = 0
        while number:
            reverse = reverse * 10 + number % 10
            number //= 10
        return x == reverse

                    
                
