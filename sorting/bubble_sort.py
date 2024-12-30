
# O(N^2)

class BubbleSort:
    def __init__(self):
        pass
    
    def sort(self, nums):
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    tmp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j]=tmp