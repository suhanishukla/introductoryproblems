#include <bits/stdc++.h> 
using namespace std; 
typedef long long ll; 

int main() {
    ll n; 
    cin >> n; 
    ll sum = 0.5*n*(n+1); 
    vector<int> a; 
    vector<int> b; 

    if (sum % 2 == 1) {
        cout << "NO" << endl; 
    } else {
        cout << "YES" << endl; 

        if (n % 2 == 0) {
            for (ll i = 1; i < n/2 + 1; i++) {
                if (i % 2 == 1) {
                    a.push_back(i); 
                    a.push_back(n+1- i); 
                } else {
                    b.push_back(i); 
                    b.push_back(n+1 - i); 
                }
            }
        } else {
            for (ll j = 1; j < (n-1)/2 + 1; j++) {
                if (j % 2 == 1) {
                    a.push_back(j); 
                    a.push_back(2*(sum-n)/(n-1) - j); 
                } else {
                    b.push_back(j); 
                    b.push_back(2*(sum-n)/(n-1) - j); 
                }
            }
            b.push_back(n); 
        }
        cout << a.size() << endl; 
        for (int x : a) {
            cout << x << " "; 
        }
        cout << "\n" << b.size() << endl; 
        for (int y : b) {
            cout << y << " "; 
        }
    }
}