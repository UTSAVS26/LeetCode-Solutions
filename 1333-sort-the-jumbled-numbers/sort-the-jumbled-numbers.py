class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        # Step 1: Create a list to store original nums and their mapped values
        mapped_list = []
        for i, num in enumerate(nums):
            s = str(num)
            n = ''.join(str(mapping[int(ch)]) for ch in s)
            mapped_list.append((num, int(n), i))

        # Step 2: Sort the list based on the mapped values and original indices for stability
        mapped_list.sort(key=lambda x: (x[1], x[2]))

        # Step 3: Create a result list and fill it with the sorted original nums
        sorted_nums = [t[0] for t in mapped_list]

        return sorted_nums

# Example usage
sol = Solution()
mapping = [2, 1, 4, 8, 6, 3, 0, 9, 7, 5]
nums = [990, 332, 981, 330]
sorted_nums = sol.sortJumbled(mapping, nums)
print(sorted_nums)  # Output should be sorted based on mapped values, preserving order for duplicates