#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
using namespace std;


int main() {
	int testcase;
	cin >> testcase;


	for (int i = 0; i < testcase; i++) {
		string voca1, voca2;
		cin >> voca1 >> voca2;

		cout << "Distances: " ;

		int length = voca1.size();

		for (int j = 0; j < length; j++) {
			if ((int)voca2[j] >= (int)voca1[j]) {
				cout << (int)(voca2[j] - voca1[j]) << " ";
			}
			else {
				cout << ((int)(voca2[j] + 26 -voca1[j])) << " ";
			}
		}
		cout << endl;
	}
	return 0;
}


