class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int majority = nums[0];
        int count = 0;
        for (int i: nums){
            if (i == majority){
                count++;
            } else if (count == 0){
                majority = i;
                count = 1;
            } else {
                count--;
            }
        }

        return majority;
    }
};