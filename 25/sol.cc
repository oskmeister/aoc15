#include <iostream>
#include <vector>

using namespace std;

typedef long long LL;

int target_r = 2978;
int target_c = 3083;

int main() {
    int r = 2;
    int c = 1;
    int next_r = 3;
    LL prev = 20151125LL;
    for (;;) {
        LL cur = (252533LL * prev) % 33554393LL;
        if (r == target_r && c == target_c) { cout << cur << endl; break; }
        prev = cur;
        r -= 1;
        c += 1;
        if (r <= 0) {
            r = next_r;
            c = 1;
            next_r = next_r + 1;
        }
    }
}
