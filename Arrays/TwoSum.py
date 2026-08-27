
class TwoSum:
    def twoSumHashMap(self, nums: list[int], target: int) -> list[int]:
        seen:list[int]=list()
        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen.index(complement), i]

            seen.append(num)

        return []
    




nums = [2, 7, 11, 15]
target = 17

obj = TwoSum()

print(obj.twoSumHashMap(nums, target))