#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int main() {
    int op;
    int x1, x2, y1, y2;
    vector<vector<int>> b(1000, vector<int>(1000, false));

    while (cin >> op >> x1 >> y1 >> x2 >> y2) {
        for (int i = x1; i <= x2; ++i) {
            for (int j = y1; j <= y2; ++j) {
                if (op == 0)
                    b[i][j] = max(0, b[i][j] - 1);
                if (op == 1)
                    b[i][j]++;
                if (op == 2)
                    b[i][j] += 2;
            }
        }
    }

    int ans = 0;
    for (int i = 0; i < 1000; ++i) {
        for (int j = 0; j < 1000; ++j) {
            ans += b[i][j];
        }
    }
    cout << ans << endl;
}
