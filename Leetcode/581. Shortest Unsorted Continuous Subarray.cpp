#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int reverse = nums.size()-1;
        int sameCount1 = 0;
        int location1 = 0;
        for(int i=0; i<reverse-1; i++){
            if(nums[i+1] < nums[i]){
                location1 = i;
                break;
            }
            else if(nums[i+1] == nums[i]){
                sameCount1++;
            }
        }
        int sameCount2 = -1;
        int location2 = -1;
        for(int i=reverse; i>0; i--){
            if(nums[i] < nums[i-1]){
                location2 = i;
                break;
            }
            else if(nums[i]==nums[i-1]){
                sameCount2++;
            }
        }
        cout<<location1<<" "<<location2<<" "<<sameCount1<<" "<<sameCount2 << endl;

        return location2 - location1 + (location1==-1 || location2==-1 ? 0 : 1);
    }
};

int main(){
    Solution sol = Solution();
    vector<int> vec = {1,3,2,2,2};
    cout<< sol.findUnsortedSubarray(vec)<<endl;

    return 0;
}