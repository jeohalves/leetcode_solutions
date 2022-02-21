#include <math.h> 

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        
        short left = 0;
        short right = nums.size()-1;
        
        short idx = nums.size() / 2;
        
        if (target <= nums[left]) {
            return left;
        }
        
        if (target > nums[right]) {
            return right+1;
        }
        
        while(right - left > 1) {
            if(nums[idx] == target) {
                return idx;
            } else if(nums[idx] < target) {
                left = idx;
            } else {
                right = idx;
            }

            idx = round((right - left) / 2) + left;
            
        }      
        
        
        return right;
        
    }
};

