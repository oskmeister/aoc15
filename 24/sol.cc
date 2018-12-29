#include <iostream>
#include <vector>
#include <map>

using namespace std;

int num[28];
int target;

typedef unsigned long long ull;

map<pair<int,pair<int,int>>, pair<int, ull>> cache;

pair<int, ull> dp(int sum1, int sum2, int at) {
    if (at == 28) {
        return sum1 == target && sum2 == target ? make_pair(0, 1ULL) : make_pair(1<<30, 1ULL);
    }
    if (sum1 > target || sum2 > target) return make_pair(1<<30, 1ULL);
    auto c = make_pair(sum1, make_pair(sum2,at));
    if (cache.count(c)) {
        return cache[c];
    }
    auto ans = make_pair(1<<30, 1ULL);
    auto try_first = dp(sum1+num[at], sum2, at+1);
    try_first.first += 1; try_first.second *= num[at];
    if (try_first < ans) ans = try_first;
    auto try_second = dp(sum1, sum2 + num[at], at+1);
    if (try_second < ans) ans = try_second;
    auto try_third =  dp(sum1, sum2, at+1);
    if (try_third < ans) ans = try_third;
    cache[c] = ans;
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
    sort(num, num+28);
    target = sum/3;
    cout << "Target is " << target << endl;
    cout << dp(0, 0, 0).second << endl;
}
