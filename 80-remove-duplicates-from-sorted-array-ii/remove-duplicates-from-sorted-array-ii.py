class Solution(object):
    def removeDuplicates(self, nums):
        # If there are 2 or fewer elements,
        # all elements can remain.
        if len(nums) <= 2:
            return len(nums)

        # write points to the position where
        # the next valid number will be placed.
        write = 2

        # Start from index 2 because the first
        # two elements are always allowed.
        for read in range(2, len(nums)):

            # Keep nums[read] only if it is different
            # from the element two positions before it.
            if nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1

        return write