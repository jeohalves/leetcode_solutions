using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        
        /* "The majority element is the element that appears more than ⌊n / 2⌋ times"
        
        The code below assumes that the above statement is false. So, return the "most frequent" element.        
        */

        
        int16_t major;
        uint16_t major_count = 1;  
        
        sort(nums.begin(), nums.end());  
        
        if (nums.size() == 1) {
            return nums[0];
        } else {
            major = nums[0];            
        }
        
        int16_t cur = major;
        uint16_t cur_count = 0;
        
        for (auto num = nums.begin(); num != nums.end(); num++) {
            
            if (*num != cur) {
                
                if (cur_count > major_count) {
                    major = cur;
                    major_count = cur_count;
                }                
                
                cur = *num;
                cur_count = 1;
                
            } else {
                cur_count++;
            }
        }
        
        if (cur_count > major_count) {
            major = cur;
            } 
        
        
        return major;
    }
};


