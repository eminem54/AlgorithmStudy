#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if(nums.size()==1){
            return nums[0];
        }
        int maxv = -987654321;
        int cur = 0;
        for(int i=1; i<=nums.size(); i++){
            cur = max(nums[i], cur + nums[i]);
            maxv = max(maxv, cur);
        }
        return maxv;
    }
};

int main(){
    Solution sol = Solution();
    vector<int> a = {-2,1,-3,4,-1,2,1,-5,4};
    cout<< sol.maxSubArray(a);

    return 0;
}