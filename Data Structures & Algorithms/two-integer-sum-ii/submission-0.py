class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        first,last = 1,len(numbers)
        while first < last:
            if numbers[first-1] + numbers[last-1] == target:
                return [first,last]
            elif numbers[first-1] + numbers[last-1] > target:
                last-=1
            elif numbers[first-1] + numbers[last-1] < target:
                first+=1

        return result