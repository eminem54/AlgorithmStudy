#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        stack<int> stack, stack2;
        int l = nums.size(), r = 0;
        for (int i = 0; i < nums.size(); i++) {
            while (!stack.empty() && nums[stack.top()] > nums[i]){
                l = min(l, stack.top());
                stack.pop();
            }
            stack.push(i);
        }

        for (int i = nums.size() - 1; i >= 0; i--) {
            while (!stack2.empty() && nums[stack2.top()] < nums[i]){
                r = max(r, stack2.top());
                stack2.pop();
            }
            stack2.push(i);
        }
        return r - l > 0 ? r - l + 1 : 0;
    }
};

int main(){
    Solution sol = Solution();
    vector<int> vec = {1,3,2,2,2};
    cout<< sol.findUnsortedSubarray(vec)<<endl;

    return 0;
}