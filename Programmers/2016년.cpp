#include <string>
#include <vector>
#include <iostream>
using namespace std;

string solution(int a, int b) {
    string weekend[7] = {"FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"};
    int days[12] = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    int total = 0;
    if(a>1){
        for(int i=0; i<a-1; i++){
            total += days[i];
        }   
    }

    string answer = weekend[(total+b-1)%7];


    return answer;
}

int main(){

    cout<< solution(1, 1)<<endl;
    cout<< solution(2, 1)<<endl;

    return 0;
}