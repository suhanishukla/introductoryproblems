#include <bits/stdc++.h> 
using namespace std; 
typedef long long ll; 
typedef long long int lli; 

int main() {
    ll n; 
    ll a; 
    cin >> n; 
    cout.precision(0); 
    for (ll k=1; k<=n; k++) {
        a = 0.5*k*k*(k*k-1) - 4*(k-1)*(k-2); 
        cout << fixed << floor(0.5*k*k*(k*k-1) - 4*(k-1)*(k-2))<< endl; 
    }
}
