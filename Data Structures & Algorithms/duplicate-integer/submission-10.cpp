class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // return true if any value appears more than once in the array, 
        unordered_set<int> seen;

        for (int num : nums) {
            if (seen.count(num)) { return true; }
            seen.insert(num);
        }
        // otherwise return false.
        return false;
    }
};