#include <bits/stdc++.h> 
using namespace std; 
typedef long long ll; 

int main() {
    ll n; 
    cin >> n; 
    vector<int> evens; 
    vector<int> odds; 

    if (n == 1) {
        cout << n << endl; 
    } else if (n==2 || n==3) {
        cout << "NO SOLUTION" << endl; 
    } else {
        for (ll i=1; i<n+1; i++) {
            if (i%2 == 0) {
                evens.push_back(i); 
            } else {
                odds.push_back(i); 
            }
        }
        for (int x : evens) {
            cout << x << " "; 
        }
        for (int y : odds) {
            cout << y << " ";  
        }

    } 
}
