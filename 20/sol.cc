#include <iostream>

using namespace std;


typedef long long ll;

const int ng = 50000000;
int gen[ng];

int main() {
    for (int i = 1; i < ng; ++i) {
        ll t = 0;
        int k = 1;
        int num = 0;
        while (i * k < ng) {
            if (num == 50) break;
            gen[i*k] += i * 11;
            ++k;
            ++num;
        }
    }
    for (int i = 0; i < ng; ++i) {
        int t = gen[i];
        if (t >= 29000000) {
            cout << i << endl;
            break;
        }
    }
}
