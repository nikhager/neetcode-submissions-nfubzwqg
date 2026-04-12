class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        vector<int> seen;
        for (int i = 0; i < size(nums); ++i){
            for (int j = 0; j < size(seen); ++j){
                if (nums[i] == seen[j]){
                    return true;
                }
            }
            seen.push_back(nums[i]);
        }
        return false;
    }
};