#include <vector>
#include <math.h>
#include <iostream>
using namespace std;

long long solution(int N) {
    long long answer = 0;
    
    long long *prime = new long long[N+1];
    
    for(int i=2; i<=N; i++){
        if (prime[i] == 0){
            answer += i;
            for(int j=i+i; j<=N; j+=i){
                prime[j] = 1;
            }
        }
    } 
    return answer;
}

int main(){

    cout<<solution(2)<<endl;

    return 0;
}