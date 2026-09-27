class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        longest=0
        for num in nums:
            if num-1 not in nums:
                lenght=1
                while num+lenght in nums:
                    lenght+=1

                longest=max(longest,lenght)
        return longest