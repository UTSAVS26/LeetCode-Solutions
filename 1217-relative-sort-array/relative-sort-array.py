from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Frequency array to count occurrences of each element in arr1 (range 0-1000)
        frequency = [0] * 1001
        result_index = 0
        max_element = 0

        # Count the frequencies of each element in arr1 and track the maximum element
        for num in arr1:
            frequency[num] += 1
            max_element = max(num, max_element)

        # Result list to store the sorted elements
        sorted_array = []

        # Add elements of arr2 to result in the order they appear in arr2
        for num in arr2:
            while frequency[num] > 0:
                sorted_array.append(num)
                frequency[num] -= 1

        # Add remaining elements not in arr2 to result in ascending order
        for num in range(max_element + 1):
            while frequency[num] > 0:
                sorted_array.append(num)
                frequency[num] -= 1

        return sorted_array