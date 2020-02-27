#include <iostream>

#include <algorithm>

using namespace std;

 

const int MAX = 200000;

 

int N, C;

int house[MAX];

 

bool possible(int dist)

{

        int cnt = 1;
        int prev = house[0];
        //조건 충족하는지 확인
        cout << "dist: " << dist << endl;
        for(int i=1; i<N; i++){
            cout << "house: " << house[i]  << "   prev:  " << prev << endl;
            if (house[i] - prev >= dist){
                cout<< "i: " << i <<endl; 
                cnt++;
                prev = house[i];
            }
        }

        //조건 충족
        cout << "cnt: " << cnt << " C: "<< C << endl;

        if (cnt >= C)
            return true;
        return false;

}

int main(void)
{
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cin >> N >> C;
        for (int i = 0; i < N; i++)
            cin >> house[i];
        sort(house, house + N);

        for (int i=0; i< N; i++)
            cout << house[i] << endl;
        //최소거리, 최대 거리
        int low = 1, high = house[N - 1] - house[0];
        int result = 0;
        while (low <= high)
        {
            int mid = (low + high) / 2;
            if (possible(mid))
            {
                result = max(result, mid);
                low = mid + 1;
            }
            else
                high = mid - 1;
            cout<< "high: " << high << "  low: " << low << endl;
        }

        cout << result << "\n";

        return 0;

}