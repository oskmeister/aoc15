#include <iostream>
#include <string>

using namespace std;

int main() {
    string str;
    cin >> str;
    {
        int ans = 0;
        int pos = 1;
        for (char c : str) {
            if (c == '(') ++ans;
            else if (c == ')') --ans;
        }
        cout << ans << endl;
    }
    {
        int ans = 0;
        int pos = 1;
        for (char c : str) {
            if (c == '(') ++ans;
            else if (c == ')') --ans;
            if (ans == -1) {
                cout << pos << endl;
                break;
            }
            ++pos;
        }
    }
}
