#include <iostream>
#include <vector>
#include <map>

using namespace std;

int num[28];
int target;

typedef unsigned long long ull;

pair<int, ull> cache[388][388][388][30];

pair<int, ull> dp(int sum1, int sum2, int sum3, int at) {
    if (at == 28) {
        return sum1 == target && sum2 == target && sum3 == target ? make_pair(0, 1ULL) : make_pair(1<<30, 1ULL);
    }
    if (sum1 > target || sum2 > target || sum3 > target) return make_pair(1<<30, 1ULL);
    auto &cached = cache[sum1][sum2][sum3][at];
    if (cached.first != -1) {
        return cached;
    }
    auto ans = make_pair(1<<30, 1ULL);
    auto try_first = dp(sum1+num[at], sum2, sum3, at+1);
    try_first.first += 1; try_first.second *= num[at];
    if (try_first < ans) ans = try_first;
    auto try_second = dp(sum1, sum2 + num[at], sum3, at+1);
    if (try_second < ans) ans = try_second;
    auto try_third =  dp(sum1, sum2, sum3 + num[at], at+1);
    if (try_third < ans) ans = try_third;
    auto try_fourth =  dp(sum1, sum2, sum3, at+1);
    if (try_fourth < ans) ans = try_fourth;
    cached = ans;
    return ans;
}

int main() {
    int cur;
    int at = 0;
    int sum = 0;
    while (cin >> cur) {
        num[at++] = cur;
        sum += cur;
    }
    cout << "Resetting dp table..." << endl;
    for (int i = 0; i < 388; ++i) {
        for (int j = 0; j < 388; ++j) {
            for (int k = 0; k < 388; ++k) {
                for (int l = 0; l < 30; ++l) {
                    cache[i][j][k][l] = make_pair(-1, 0);
                }
            }
        }
    }
    sort(num, num+28);
    target = sum/4;
    cout << "Target is " << target << endl;
    cout << dp(0, 0, 0,0 ).second << endl;
}
