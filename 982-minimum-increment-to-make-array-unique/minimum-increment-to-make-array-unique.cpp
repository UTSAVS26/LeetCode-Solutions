class Solution {
public:
    int minIncrementForUnique(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());

        int numTracker = 0;
        int minIncrement = 0;

        for (int num : nums) {
            numTracker = std::max(numTracker, num);
            minIncrement += numTracker - num;
            numTracker += 1;
        }

        return minIncrement;
    }
};