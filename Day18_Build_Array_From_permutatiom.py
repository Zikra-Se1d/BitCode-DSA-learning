class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        
        # Look through every index in our list
        for i in range(len(nums)):
            # Target the secret index value
            secret_index = nums[i]
            # Grab the value from that secret index and add it to our answers
            ans.append(nums[secret_index])
            
        return ans
