class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_list = []

        for i, v in enumerate(nums):
            if not(len(nums) >= i):
                break
            else:
                if i == len(nums) - 1:
                    my_list.append(i)
                    return my_list
                else:
                    for key, value in enumerate(nums):
                        if v + value == target and i != key:
                                my_list.append(i),
                                my_list.append(key)
                                return my_list