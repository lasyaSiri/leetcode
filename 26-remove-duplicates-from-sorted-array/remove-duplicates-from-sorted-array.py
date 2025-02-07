class Solution(object):
    def removeDuplicates(self, nums):
        lastNumber = nums[0]
        newNums = [lastNumber]

        for i in range(1, len(nums)):
            if nums[i] != lastNumber:
                newNums.append(nums[i])
            lastNumber = nums[i]

        nums[:] = newNums
        return len(newNums)


        