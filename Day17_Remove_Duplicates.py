class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # pointer tracks where to overwrite the next unique number
        write = 1
        
        # loop  that scans through the static array
        for i in range(1, len(nums)):
            # If the current number is new (different from the last one)
            if nums[i] != nums[i - 1]:
                # Overwrite the duplicate value at our 'write' position
                nums[write] = nums[i]
                write += 1
                
        # Return the count of unique elements
        return write
