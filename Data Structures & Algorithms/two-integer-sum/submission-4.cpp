class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> nummap;
        vector<int> ret;
        int diff;

        for(size_t num = 0; num < nums.size(); num++) {
            diff = target - nums[num];
            if(nummap.contains(diff)) {
                ret.push_back(nummap[diff]);
                ret.push_back(num);
            }
            nummap[nums[num]] = num;
        }
        return ret;
    }
};
