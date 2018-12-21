#include <iostream>
#include <map>
#include <unordered_map>
#include <string>
#include <vector>
using namespace std;

int alphabet[26] = { 0 };
int main() {
	string temp;
	while (cin>>temp) {
		for (int j = 0; j < temp.length(); j++) {
			if(temp[j] >= 'a' && temp[j] <='z')
				alphabet[temp[j] - 'a']++;
		}
		temp.clear();
	}

	int max = alphabet[0];
	int maxindex = 0;
	for (int i = 1; i < 26; i++) {
		if (alphabet[i] > max) {
			maxindex = i;
			max = alphabet[i];
		}
	}
	for (int i = 0; i < 26; i++) {
		if (alphabet[i] == max) {
			maxindex = i;
		}
	}


	cout << (char)(maxindex + 'a') << endl;

	return 0;
}



//#include <iostream>
//#include <algorithm>
//#include <string>
//#include <cstring>
//using namespace std;
//
//int alphabet[26];
//int main(void)
//{
//	ios_base::sync_with_stdio(0);
//	cin.tie(0);
//	string s;
//	while (cin >> s)
//	{
//		for (int i = 0; i < s.length(); i++)
//			if (s[i] >= 'a' && s[i] <= 'z')
//				alphabet[s[i] - 'a']++;
//		s.clear();
//	}
//	int temp = alphabet[0];
//	for (int i = 1; i < 26; i++)
//		temp = max(alphabet[i], temp);
//	for (int i = 0; i < 26; i++)
//		if (alphabet[i] == temp)
//			cout << (char)(i + 'a');
//	cout << "\n";
//	return 0;
//}