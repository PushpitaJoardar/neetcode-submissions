class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for item in range(1,n):
            key = nums[item]
            j = item - 1

            while( j >= 0 and nums[j] > key):
                nums[j+1] = nums[j]
                j = j -  1
            nums[j+1] = key

        for item in range(n):
            j = item + 1
            if(j<n):
                if(nums[item] == nums[j]):
                    return True
        return False


         