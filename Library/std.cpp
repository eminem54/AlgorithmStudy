#include <math.h>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <set>
using namespace std;

vector<int> randVec(int num, int until){
    srand((unsigned int)time(NULL));
    vector<int> ret;
    for(int i=0; i<num; i++){
        ret.push_back(rand()%until);
    }
    return ret;
}

vector<int> randVecDup(int num, int until){
    srand((unsigned int)time(NULL));
    vector<int> ret;
    while(ret.size() < num){
        int a = rand()%until;
        if(find(ret.begin(), ret.end(), a) == ret.end()){
            ret.push_back(a);
        }
    }
    return ret;
}

void print(vector<int> a){
    for(int i=0; i<a.size(); i++){
        cout<<a[i]<<" ";
    }
}


