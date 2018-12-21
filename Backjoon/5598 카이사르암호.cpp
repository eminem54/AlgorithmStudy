#include <iostream>
#include <string>

using namespace std;

int main() {
	string a;
	cin >> a;

	for (int i = 0; i < a.size(); i++) {
		if (a.at(i) >= 'X') {
			cout << (char)(a.at(i) - 26 + 3);
		}
		else {
			cout << (char)(a.at(i) - 3);
		}
	}
	return 0;
}