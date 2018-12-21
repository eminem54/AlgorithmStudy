#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
using namespace std;

int testcase;
vector<string> vocas1, vocas2;
void makeInput() {
	cin >> testcase;
	string voca1, voca2;
	for (int i = 0; i < testcase; i++) {
		cin >> voca1 >> voca2;
		vocas1.push_back(voca1);
		vocas2.push_back(voca2);
		voca1 = "";
		voca2 = "";
	}
}
int main() {
	makeInput();

	for (int i = 0; i < vocas1.size(); i++) {
		cout << "Distancec: " ;

		for (int j = 0; j < vocas1[i].size(); j++) {
			if (vocas2[i][j] >= vocas1[i][j]) {
				cout << (int)(vocas2[i][j] - vocas1[i][j]);
			}
			else {
				cout << (int)(vocas2[i][j] - vocas1[i][j]) + 26;
			}
			if (j != vocas1[i].size() - 1) {
				cout << " ";
			}
		}
	}
	return 0;
}