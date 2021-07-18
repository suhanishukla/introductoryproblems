#include <bits/stdc++.h> 
using namespace std; 
typedef long long ll; 

int main() {
    ll t, y, x; 
    cin >> t; 
    while(t--) {
        cin >> y >> x; 
        if (x <= y) {
            if (y%2 == 1) {
                cout << y*y - 2*y + 1 + x << endl; 
            } else {
                cout << y*y - x + 1 << endl; 
            }
        } else {
            if (x%2==1) {
                cout << x*x - y + 1 << endl; 
            } else {
                cout << x*x - 2*x + 1 + y << endl; 
            }
        }
    } 
}
