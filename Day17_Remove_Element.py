class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Tracks where to overwrite the next non-target number
        write = 0
        
        # Scan through the array
        for i in range(len(nums)):
            # If the current number is not equal to val
            if nums[i] != val:
                # Overwrite the element at the write position
                nums[write] = nums[i]
                # Move our tracker forward
                write += 1
        return write
