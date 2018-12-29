#include <iostream>

using namespace std;

int sizes[20];

int count(int at, int cur, int n) {
    if (cur > 150) return 0;
    if (at == 20) {
        return cur == 150 && n == 4;
    }
    return count(at+1, cur, n) + count(at+1, cur + sizes[at], n+1);
}

int main() {
    {
        int cur;
        int at = 0;
        while (cin >> cur) {
            sizes[at++] = cur;
        }
    }


    cout << count(0, 0, 0) << endl;
}
