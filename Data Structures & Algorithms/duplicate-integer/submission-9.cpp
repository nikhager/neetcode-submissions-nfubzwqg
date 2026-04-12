class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // return true if any value appears more than once in the array, 
        vector<int> seen;

        for (int i = 0; i < size(nums); ++i) {
            if (find(seen.begin(), seen.end(), nums[i]) != seen.end()) { return true; }
            seen.push_back(nums[i]);
        }
        // otherwise return false.
        return false;
    }
};